#!/usr/bin/env python3
"""
RAGDaily — 每日 RAG 论文发现核心脚本
从 arxiv 拉取最近36小时内发布的 RAG 相关顶级机构论文，
为每篇论文生成结构化摘要概括，
输出：
  daily/YYYY-MM-DD.md  — 当日详细报告
  README.md            — 仓库首页，展示最新论文目录与概要
"""

import os
import re
import sys
import json
import time
import random
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ═══════════════════════════════════════════════════════════
#  配置区域
# ═══════════════════════════════════════════════════════════

MAX_PAPERS  = 20    # 每天最多输出论文数
FETCH_MAX   = 300   # 从 arxiv 拉取的最大候选数
HOURS_RANGE = 36    # 向前追溯小时数（略大于24h，应对 arxiv 处理延迟）
OUTPUT_DIR  = Path("daily")
README_PATH = Path("README.md")
INDEX_PATH  = Path("index.json")   # 用于追踪历史，方便首页展示

CATEGORIES = ["cs.AI", "cs.LG"]

# 顶级 AI 研究机构 / 大学关键词（大小写不敏感匹配）
TOP_INSTITUTIONS: list[str] = [
    # ── 科技公司 ──
    "Microsoft Research", "Microsoft",
    "Google DeepMind", "Google Brain", "Google Research", "Google",
    "DeepMind",
    "OpenAI",
    "Anthropic",
    "Meta AI", "Meta FAIR", "FAIR",
    "Amazon AWS", "Amazon",
    "Apple",
    "NVIDIA Research", "NVIDIA",
    "Samsung AI",
    "IBM Research",
    "Salesforce Research",
    "Adobe Research",
    "Baidu Research", "Baidu",
    "Alibaba DAMO", "Alibaba",
    "Tencent AI Lab", "Tencent",
    "Huawei Noah's Ark", "Huawei",
    "ByteDance Research", "ByteDance",
    "Meituan",
    # ── 北美顶级大学 ──
    "MIT", "Massachusetts Institute of Technology",
    "Stanford University", "Stanford",
    "Carnegie Mellon University", "CMU",
    "UC Berkeley", "University of California, Berkeley",
    "Harvard University", "Harvard",
    "Princeton University", "Princeton",
    "Yale University",
    "Columbia University",
    "University of Washington",
    "University of Michigan",
    "New York University", "NYU",
    "UCLA", "University of California, Los Angeles",
    "UCSD", "University of California, San Diego",
    "University of Illinois", "UIUC",
    "Cornell University", "Cornell",
    "Caltech", "California Institute of Technology",
    "Georgia Tech", "Georgia Institute of Technology",
    # ── 中国顶级大学 / 机构 ──
    "Tsinghua University", "Tsinghua",
    "Peking University", "PKU",
    "Zhejiang University", "ZJU",
    "Shanghai Jiao Tong University", "SJTU",
    "Fudan University",
    "University of Science and Technology of China", "USTC",
    "Renmin University",
    "Beihang University",
    "Harbin Institute of Technology", "HIT",
    "Nanjing University",
    "Chinese Academy of Sciences", "CAS",
    "Microsoft Research Asia", "MSRA",
    # ── 欧洲 / 其他 ──
    "University of Oxford", "Oxford",
    "University of Cambridge", "Cambridge",
    "ETH Zurich", "ETH Zürich", "ETHZ",
    "University of Toronto",
    "Mila", "Vector Institute",
    "INRIA",
    "Max Planck Institute",
    "National University of Singapore", "NUS",
    "Nanyang Technological University", "NTU",
    "Seoul National University", "SNU",
    "KAIST",
    "Allen Institute for AI", "AI2", "AllenAI",
    "Toyota Research Institute", "TRI",
    "JPMorgan AI Research",
]

# ═══════════════════════════════════════════════════════════
#  arxiv 查询
# ═══════════════════════════════════════════════════════════

ARXIV_NS = {
    "atom":       "http://www.w3.org/2005/Atom",
    "arxiv":      "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}


def build_query() -> str:
    """构建 arxiv API 搜索查询字符串，修复拼写错误，收紧匹配"""
    cat_q = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    # 修正 AAgentic 拼写错误，增加强约束，区分纯检索增强生成
    kw_pairs = [
        # 核心精确短语
        'ti:"Retrieval-Augmented Generation"', 'abs:"Retrieval-Augmented Generation"',
        'ti:"Retrieval Augmented Generation"', 'abs:"Retrieval Augmented Generation"',
        'ti:RAG', 'abs:RAG',
        'ti:"GraphRAG"', 'abs:"GraphRAG"',
        'ti:"Graph RAG"', 'abs:"Graph RAG"',
        'ti:"Agentic RAG"', 'abs:"Agentic RAG"',
        'ti:"AgenticRAG"', 'abs:"AgenticRAG"',
    ]
    kw_q = " OR ".join(kw_pairs)
    return f"({cat_q}) AND ({kw_q})"


def fetch_arxiv_papers(query: str, max_results: int = FETCH_MAX) -> list[dict]:
    """
    调用 arxiv API，返回解析后的论文列表
    带分页、请求间隔、指数退避重试，严格符合arxiv限流规则
    """
    all_papers = []
    per_page = 10  # 每次请求50篇，更小的请求避免触发限流
    user_agent = "clawBot-RAGDaily/1.0"  # 请替换为你的邮箱

    for start in range(0, max_results, per_page):
        current_max = min(per_page, max_results - start)
        params = {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": str(current_max),
            "start": str(start),
        }
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
        print(f"[INFO] 请求 arxiv API 分页：start={start}, max={current_max}")
        
        # 指数退避重试，最多5次，初始等待3秒
        papers = None
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": user_agent})
                with urllib.request.urlopen(req, timeout=90) as resp:
                    # 正常响应，解析结果
                    xml_bytes = resp.read()
                    papers = _parse_atom(xml_bytes)
                    break
            except urllib.error.HTTPError as e:
                # 处理HTTP错误，尤其是429/503
                code = e.code
                if code in (429, 503):
                    # 优先读取服务器返回的Retry-After头
                    retry_after = e.headers.get('Retry-After')
                    if retry_after:
                        try:
                            wait_time = int(retry_after)
                            print(f"[WARN] 服务器要求等待 {wait_time} 秒后重试...")
                        except:
                            # 解析失败，使用指数退避+抖动
                            wait_time = 3 * (2 ** attempt) + random.randint(0, 3)
                    else:
                        wait_time = 3 * (2 ** attempt) + random.randint(0, 3)
                    
                    print(f"[WARN] 收到 {code} 限流错误，第{attempt+1}次重试，等待 {wait_time} 秒...")
                    time.sleep(wait_time)
                else:
                    # 其他错误，直接抛出
                    raise e
            except Exception as exc:
                # 网络错误等其他异常，使用指数退避重试
                wait_time = 3 * (2 ** attempt) + random.randint(0, 3)
                print(f"[WARN] 请求失败：{str(exc)[:100]}，第{attempt+1}次重试，等待 {wait_time}s...")
                time.sleep(wait_time)
        
        if papers is None:
            print(f"[ERROR] 本页请求全部失败，终止拉取，已获取 {len(all_papers)} 篇")
            break
        
        all_papers.extend(papers)
        # 如果返回结果少于请求数，说明已经到最后一页
        if len(papers) < current_max:
            break
        
        # 分页请求间隔，严格遵守arxiv的限流要求，5秒间隔
        print(f"[INFO] 分页间隔，等待5秒...")
        time.sleep(5)
    
    return all_papers


def _parse_atom(xml_bytes: bytes) -> list[dict]:
    """解析 arxiv Atom XML，提取论文字段"""
    root = ET.fromstring(xml_bytes)
    ns = ARXIV_NS
    papers: list[dict] = []

    for entry in root.findall("atom:entry", ns):
        p: dict = {}

        t = entry.find("atom:title", ns)
        p["title"] = (t.text or "").strip().replace("\n", " ") if t is not None else ""

        id_el = entry.find("atom:id", ns)
        p["url"] = (id_el.text or "").strip() if id_el is not None else ""

        pub_el = entry.find("atom:published", ns)
        p["published"] = (pub_el.text or "").strip() if pub_el is not None else ""

        sum_el = entry.find("atom:summary", ns)
        raw_abs = (sum_el.text or "").strip() if sum_el is not None else ""
        # 规范化空白
        p["abstract"] = re.sub(r"\s+", " ", raw_abs)

        authors, affiliations = [], []
        for au in entry.findall("atom:author", ns):
            name_el = au.find("atom:name", ns)
            aff_el  = au.find("arxiv:affiliation", ns)
            if name_el is not None:
                authors.append((name_el.text or "").strip())
            if aff_el is not None and aff_el.text:
                aff = aff_el.text.strip()
                if aff and aff not in affiliations:
                    affiliations.append(aff)
        p["authors"]      = authors
        p["affiliations"] = affiliations

        cats = [c.get("term", "") for c in entry.findall("atom:category", ns)]
        p["categories"] = [c for c in cats if c]

        papers.append(p)

    return papers


# ═══════════════════════════════════════════════════════════
#  过滤逻辑
# ═══════════════════════════════════════════════════════════

def _within_hours(published: str, hours: int = HOURS_RANGE) -> bool:
    try:
        pub_dt = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - pub_dt) <= timedelta(hours=hours)
    except Exception:
        return False


def _match_institution(paper: dict) -> tuple[bool, list[str]]:
    aff_text  = " | ".join(paper.get("affiliations", []))
    author_text = " ".join(paper.get("authors", []))
    title_text = paper.get("title", "")
    abs_text = paper.get("abstract", "")
    # 全文检索，覆盖所有可能出现机构的位置
    search_in = f"{aff_text} {author_text} {title_text} {abs_text}"

    matched: list[str] = []
    lower_search = search_in.lower()
    for inst in TOP_INSTITUTIONS:
        inst_low = inst.lower()
        if inst_low in lower_search:
            if inst not in matched:
                matched.append(inst)

    return len(matched) > 0, matched


def filter_papers(papers: list[dict]) -> list[dict]:
    """过滤：最近36h + 顶级机构，最多 MAX_PAPERS 篇"""
    result: list[dict] = []
    seen_urls: set[str] = set()

    for p in papers:
        if p["url"] in seen_urls:
            continue
        # 只跳过当前超时论文，不break！
        if not _within_hours(p["published"]):
            continue
        # matched, insts = _match_institution(p)
        # if matched:
            # p["matched_institutions"] = insts
        result.append(p)
        seen_urls.add(p["url"])
        if len(result) >= MAX_PAPERS:
            break

    return result

def rag_core_check(paper: dict) -> bool:
    """二次校验：论文核心是RAG，而非仅提及RAG"""
    text = (paper["title"] + " " + paper["abstract"]).lower()
    # 核心RAG动作词，必须至少命中一个
    core_words = [
        "retrieval augmented", "graphrag", "graph rag", "agentic rag",
        "retrieve document", "knowledge retrieval", "external knowledge",
        "retrieval prompt", "rag framework", "rag benchmark"
    ]
    hit = any(word in text for word in core_words)
    return hit


# ═══════════════════════════════════════════════════════════
#  摘要提炼 + 中文翻译
# ═══════════════════════════════════════════════════════════

def _split_sentences(text: str) -> list[str]:
    """将英文文本按句号/感叹号/问号分割为句子列表"""
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in parts if s.strip()]


def _translate_to_zh(text: str, retries: int = 2) -> str:
    """
    调用 MyMemory 免费翻译 API 将英文文本翻译为中文（简体）。
    无需 API Key，使用 urllib 标准库即可，每次请求限制约 500 字符。
    翻译失败时返回原英文，并附注（翻译服务暂不可用）。
    """
    # MyMemory 每次请求有字符限制，先截取
    if len(text) > 450:
        text = text[:450] + "…"

    params = urllib.parse.urlencode({
        "q":        text,
        "langpair": "en|zh-CN",
        "de":       "clawbot@noreply.github.com",  # 可选联系邮箱，提升配额
    })
    api_url = f"https://api.mymemory.translated.net/get?{params}"

    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                api_url,
                headers={"User-Agent": "clawBot-RAGDaily/1.0"},
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            # responseStatus 200 表示成功
            if data.get("responseStatus") == 200:
                translated = data.get("responseData", {}).get("translatedText", "").strip()
                if translated:
                    return translated

        except Exception as exc:
            wait_time = 2 ** attempt
            print(f"[WARN] 翻译 API 第{attempt+1}次尝试失败：{exc}，等待 {wait_time} 秒...")
            time.sleep(wait_time)

    # 全部重试失败，回退到原文
    return f"{text}（翻译服务暂不可用）"


# def summarize_paper(paper: dict) -> str:
#     """
#     为论文生成中文摘要概括。
#     策略：
#       1. 提取摘要的前2句（通常描述问题背景与方法）
#       2. 若总句数 >= 4，追加最后1句（通常是实验结论）
#       3. 调用 MyMemory API 将提取内容翻译为中文
#     返回: 中文概括字符串
#     """
#     abstract = paper.get("abstract", "").strip()
#     if not abstract:
#         return "（摘要不可用）"

#     sentences = _split_sentences(abstract)
#     if not sentences:
#         en_text = abstract[:400] + ("…" if len(abstract) > 400 else "")
#         return _translate_to_zh(en_text)

#     selected: list[str] = []

#     # 取前2句（背景/方法）
#     for s in sentences[:2]:
#         selected.append(s)

#     # 若总句数 >= 4，取最后1句（结论），避免重复
#     if len(sentences) >= 4 and sentences[-1] not in selected:
#         selected.append(sentences[-1])

#     en_summary = " ".join(selected)

#     # 翻译为中文
#     return _translate_to_zh(en_summary)

def summarize_paper(paper: dict) -> str:
    """
    为论文生成中文摘要概括。
    策略：直接翻译整篇完整英文摘要
    返回: 完整中文翻译摘要
    """
    abstract = paper.get("abstract", "").strip()
    if not abstract:
        return "（摘要不可用）"

    # 不再截取句子，直接全文翻译
    return _translate_to_zh(abstract)


def extract_keywords(paper: dict) -> list[str]:
    """从标题和摘要中提取 RAG 相关核心关键词"""
    text = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()

    kw_map = {
        "agenticrag": "AgenticRAG",
        "agentic rag": "Agentic RAG",
        "graph rag": "Graph RAG",
        "graphrag": "GraphRAG",
        "rag": "RAG",
        "retrieval-augmented generation": "RAG",
        "retrieval augmented generation": "RAG"
    }

    found: list[str] = []
    for pattern, label in kw_map.items():
        if pattern in text and label not in found:
            found.append(label)
        if len(found) >= 5:
            break

    return found


# ═══════════════════════════════════════════════════════════
#  Markdown 生成 — 每日详细报告
# ═══════════════════════════════════════════════════════════

def _fmt_paper_detail(paper: dict, idx: int) -> str:
    """将单篇论文渲染为详细 Markdown 块（用于 daily/ 报告）"""
    title    = paper.get("title", "无标题")
    authors  = paper.get("authors", [])
    affs     = paper.get("affiliations", [])
    # matched  = paper.get("matched_institutions", [])
    # matched  = []
    abstract = paper.get("abstract", "")
    url      = paper.get("url", "")
    pub      = paper.get("published", "")
    cats     = paper.get("categories", [])
    summary  = paper.get("summary", "")
    keywords = paper.get("keywords", [])

    authors_str = "、".join(authors[:6])
    if len(authors) > 6:
        authors_str += f" 等（共 {len(authors)} 位作者）"

    lead_authors = authors[:3]
    lead_str     = "、".join(lead_authors)
    if len(authors) > 3:
        lead_str += f" 等"

    affs_str    = "；".join(affs) if affs else "（详见原文）"
    # matched_str = "、".join(matched[:4])
    cats_str    = " | ".join(cats[:3])
    kw_str      = " · ".join(f"`{k}`" for k in keywords) if keywords else "—"

    # 完整摘要（不截断）
    full_abstract = abstract if abstract else "（摘要不可用）"

    return f"""### {idx}. {title}

<table>
<tr><td><b>通讯作者</b></td><td>{lead_str}</td></tr>
<tr><td><b>全部作者</b></td><td>{authors_str}</td></tr>
<tr><td><b>作者机构</b></td><td>{affs_str}</td></tr>
<tr><td><b>arxiv 分类</b></td><td>{cats_str}</td></tr>
<tr><td><b>发布时间</b></td><td>{pub}</td></tr>
<tr><td><b>关键词</b></td><td>{kw_str}</td></tr>
<tr><td><b>原文链接</b></td><td><a href="{url}">{url}</a></td></tr>
</table>

#### 📝 摘要概括

> {summary}

#### 📄 原始摘要（英文）

<details>
<summary>展开查看完整摘要</summary>

{full_abstract}

</details>

---
"""


def generate_daily_markdown(papers: list[dict], date_str: str) -> str:
    """生成当日详细论文报告（存入 daily/YYYY-MM-DD.md）"""
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    if not papers:
        return (
            f"# RAGDaily — {date_str}\n\n"
            f"> 今日（{date_str}）暂无符合条件的论文：最近36小时内、来自顶级机构、"
            f"RAG 相关。\n\n"
            f"*由 clawBot RAGDaily skill 自动生成 | {now_str}*\n"
        )

    # 目录
    toc_lines = [
        f"# RAGDaily — {date_str}\n",
        f"> 自动筛选自 arxiv | 来自顶级 AI 机构 | 最近36小时内发布 | **共 {len(papers)} 篇**\n",
        f"> 关键词：RAG · GraphRAG · Graph RAG · Agentic RAG · AgenticRAG\n",
        f"> 生成时间：{now_str}\n",
        "\n---\n",
        "## 📋 本日论文目录\n",
    ]
    for i, p in enumerate(papers):
        title = p.get("title", "无标题")
        insts = "、".join(p.get("matched_institutions", [])[:2])
        first_author = p.get("authors", ["—"])[0]
        toc_lines.append(f"{i+1}. [{title}](#{i+1}-{_slugify(title)}) — {first_author} | {insts}")

    toc_lines.append("\n---\n")
    toc_lines.append("## 📚 论文详情\n")

    header = "\n".join(toc_lines) + "\n"
    body   = "\n".join(_fmt_paper_detail(p, i + 1) for i, p in enumerate(papers))
    footer = f"\n*由 [clawBot RAGDaily](https://github.com/Jacob-biu/RAGDaily) 自动生成 | {now_str}*\n"

    return header + body + footer


def _slugify(text: str) -> str:
    """生成 GitHub Markdown anchor 用的 slug"""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


# ═══════════════════════════════════════════════════════════
#  README 生成 — 仓库首页（每日自动更新）
# ═══════════════════════════════════════════════════════════

def _load_index() -> list[dict]:
    """加载历史索引（index.json）"""
    if INDEX_PATH.exists():
        try:
            return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return []


def _save_index(index: list[dict]) -> None:
    """保存历史索引，最多保留最近60天"""
    index = sorted(index, key=lambda x: x.get("date", ""), reverse=True)[:60]
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def generate_readme(papers: list[dict], date_str: str) -> str:
    """
    生成仓库首页 README.md：
    - 项目介绍
    - 今日论文目录（含概要、来源机构、作者信息）
    - 历史归档链接
    """
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # ── 项目介绍 ──
    intro = f"""# 📚 RAGDaily

> **每日 RAG 论文自动发现** · 由 [clawBot](https://github.com/Jacob-biu/clawBot) 驱动

自动从 [arxiv](https://arxiv.org/) 筛选来自**顶级 AI 机构**的最新 RAG 相关论文，  
每天北京时间 **08:00**（UTC 00:00）自动更新，包含结构化摘要概括与作者信息。

| 特性 | 说明 |
|------|------|
| 📡 数据来源 | arxiv API（cs.AI / cs.LG） |
| 🏛️ 机构筛选 | 70+ 顶级 AI 机构（MIT、Stanford、CMU、清华、OpenAI 等） |
| 🔍 关键词 | RAG, GraphRAG, Graph RAG, Agentic RAG, AgenticRAG |
| 📄 每日上限 | 最多 20 篇 |
| ⏰ 更新时间 | 每天 UTC 00:05（北京时间 08:05） |
| 📬 通知方式 | GitHub Issue @Jacob-biu |

---

"""

    # ── 今日论文 ──
    if not papers:
        today_section = (
            f"## 📅 今日论文 — {date_str}\n\n"
            f"> ⚠️ 今日暂无符合条件的论文（来自顶级机构的最近36小时内 RAG 相关论文）。\n\n"
        )
    else:
        daily_url = f"daily/{date_str}.md"
        today_section = (
            f"## 📅 今日论文 — {date_str}　　"
            f"[→ 查看完整报告]({daily_url})\n\n"
            f"> 共筛选出 **{len(papers)}** 篇论文 | 更新于 {now_str}\n\n"
        )

        # 论文概览表
        today_section += "### 论文目录与概要\n\n"
        today_section += "| # | 论文标题 | 核心概要 | 来源机构 | 第一作者 |\n"
        today_section += "|---|---------|---------|---------|--------|\n"

        for i, p in enumerate(papers):
            title   = p.get("title", "无标题")
            url     = p.get("url", "")
            summary = p.get("summary", "")
            insts = p.get("affiliations", [])
            authors = p.get("authors", [])

            # 截短以适配表格
            short_title   = title[:60] + ("…" if len(title) > 60 else "")
            short_summary = summary[:100] + ("…" if len(summary) > 100 else "")
            # 去掉 summary 中的换行
            short_summary = short_summary.replace("\n", " ").replace("|", "｜")
            short_title   = short_title.replace("|", "｜")

            inst_str   = "、".join(insts[:2]) if insts else "—"
            author_str = authors[0] if authors else "—"

            title_link = f"[{short_title}]({url})" if url else short_title

            today_section += f"| {i+1} | {title_link} | {short_summary} | {inst_str} | {author_str} |\n"

        today_section += "\n"

        # 每篇详细卡片（展开式）
        today_section += "### 论文详情\n\n"
        for i, p in enumerate(papers):
            title    = p.get("title", "无标题")
            url      = p.get("url", "")
            authors  = p.get("authors", [])
            affs     = p.get("affiliations", [])
            # matched  = p.get("matched_institutions", [])
            # matched  = []
            summary  = p.get("summary", "")
            keywords = p.get("keywords", [])
            pub      = p.get("published", "")

            authors_disp = "、".join(authors[:5])
            if len(authors) > 5:
                authors_disp += f" 等（共 {len(authors)} 人）"
            affs_disp    = "；".join(affs[:3]) if affs else "（详见原文）"
            # matched_disp = "、".join(matched[:3])
            kw_disp      = " · ".join(f"`{k}`" for k in keywords) if keywords else "—"

            today_section += f"""<details>
<summary><b>{i+1}. {title}</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | {authors_disp} |
| **所属机构** | {affs_disp} |
| **发布时间** | {pub} |
| **关键词** | {kw_disp} |
| **原文链接** | [{url}]({url}) |

**📝 摘要概括：**

> {summary}

</details>

"""

    # ── 历史归档 ──
    index = _load_index()
    archive_section = "## 🗄️ 历史归档\n\n"
    if not index:
        archive_section += "_暂无历史记录。_\n\n"
    else:
        archive_section += "| 日期 | 论文数 | 报告链接 |\n"
        archive_section += "|------|--------|----------|\n"
        for entry in index[:30]:
            d     = entry.get("date", "")
            cnt   = entry.get("count", 0)
            fpath = f"daily/{d}.md"
            archive_section += f"| {d} | {cnt} 篇 | [{d}.md]({fpath}) |\n"
        archive_section += "\n"

    # ── 机构列表 ──
    inst_section = """## 🏛️ 顶级机构覆盖范围

覆盖超过 **70 个**顶级 AI 机构，包括：

- **科技公司：** Microsoft、Google DeepMind、OpenAI、Anthropic、Meta AI、NVIDIA、Baidu、Alibaba、ByteDance 等
- **北美顶级大学：** MIT、Stanford、CMU、UC Berkeley、Harvard、Princeton、Cornell、Caltech 等
- **中国顶级大学/机构：** 清华大学、北京大学、浙大、上交大、复旦、中科院、MSRA 等
- **欧洲/其他：** Oxford、Cambridge、ETH Zurich、Mila、NUS、KAIST 等

---

*由 [clawBot RAGDaily](https://github.com/Jacob-biu/clawBot) 自动维护 | 最后更新：{now_str}*
""".format(now_str=now_str)

    return intro + today_section + archive_section + inst_section


# ═══════════════════════════════════════════════════════════
#  入口
# ═══════════════════════════════════════════════════════════

def main() -> int:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"[INFO] RAGDaily 开始拉取论文，日期：{today}")

    query = build_query()
    print(f"[INFO] 查询语句：{query[:120]} …")

    papers_raw = fetch_arxiv_papers(query)
    print(f"[INFO] 拉取候选论文：{len(papers_raw)} 篇")

    papers = filter_papers(papers_raw)
    # 新增：过滤仅顺带提及RAG的无关论文
    papers = [p for p in papers if rag_core_check(p)]
    print(f"[INFO] 二次RAG核心校验后剩余：{len(papers)} 篇")

    # 为每篇论文生成摘要概括和关键词
    for p in papers:
        p["summary"]  = summarize_paper(p)
        p["keywords"] = extract_keywords(p)

    # 写入每日报告
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    daily_file = OUTPUT_DIR / f"{today}.md"
    daily_file.write_text(generate_daily_markdown(papers, today), encoding="utf-8")
    print(f"[INFO] 已写入每日报告 → {daily_file}")

    # 更新历史索引
    index = _load_index()
    # 移除同一天的旧记录（幂等）
    index = [e for e in index if e.get("date") != today]
    index.insert(0, {"date": today, "count": len(papers)})
    _save_index(index)

    # 更新仓库首页 README
    README_PATH.write_text(generate_readme(papers, today), encoding="utf-8")
    print(f"[INFO] 已更新首页 README → {README_PATH}")

    # 向 GitHub Actions 传递输出变量
    gh_output = os.environ.get("GITHUB_OUTPUT", "")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"paper_count={len(papers)}\n")
            f.write(f"date={today}\n")

    return len(papers)


if __name__ == "__main__":
    sys.exit(0 if main() >= 0 else 1)
