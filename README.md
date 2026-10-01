# 📚 RAGDaily

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

## 📅 今日论文 — 2026-10-01　　[→ 查看完整报告](daily/2026-10-01.md)

> 共筛选出 **3** 篇论文 | 更新于 2026-10-01 01:08 UTC

### 论文目录与概要

| # | 论文标题 | 核心概要 | 来源机构 | 第一作者 |
|---|---------|---------|---------|--------|
| 1 | [Re-ranking and Late Interaction Drive Retrieval Quality: A C…](http://arxiv.org/abs/2609.38473v1) | 检索增强生成（ RAG ）现在是在外部知识中接地大型语言模型（ LLM ）的标准方法，但检索管道的设计空间很大，变体之间的权衡尚未得到很好的理解，特别是在现实规模的特定领域语料库上。在这项工作中，我们… | — | Bhagyesh Rathi |
| 2 | [BITEM at the NTCIR-19 R2C2 Task: Predicting Confidence from …](http://arxiv.org/abs/2609.37993v1) | BITEM团队通过单个代理管道进入了NTCIR-19 R2C2任务的两个子任务，其中模型在电影语料库上搜索、读取和记录证据，而编导则保留记录并规定可以提交的内容。只有当牵连级联根据其引用的段落对其进行… | — | Julien Knafou |
| 3 | [Retrieve, Reproduce, Reveal: Dissecting Retrieval-Augmented …](http://arxiv.org/abs/2609.37669v1) | 通过在检索到的漏洞知识（如漏洞报告）中进行预测，越来越多地使用检索增强生成（ RAG ）来增强基于大语言模型（ LLM ）的软件漏洞检测。然而，现有的基于RAG的软件漏洞检测（ RAG4SVD ）系统… | — | Sabrina Kaniewski |

### 论文详情

<details>
<summary><b>1. Re-ranking and Late Interaction Drive Retrieval Quality: A Controlled Comparison of RAG Strategies for Scientific Question Answering</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Bhagyesh Rathi、Eshan Chawla、William B. Andreopoulos |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-09-29T20:04:29Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2609.38473v1](http://arxiv.org/abs/2609.38473v1) |

**📝 摘要概括：**

> 检索增强生成（ RAG ）现在是在外部知识中接地大型语言模型（ LLM ）的标准方法，但检索管道的设计空间很大，变体之间的权衡尚未得到很好的理解，特别是在现实规模的特定领域语料库上。在这项工作中，我们提出了六种科学问答检索策略的对照比较： （ i ）经典的top-k密集检索， （ ii ） LLM…

</details>

<details>
<summary><b>2. BITEM at the NTCIR-19 R2C2 Task: Predicting Confidence from Agentic RAG Pipeline Signals</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Julien Knafou、Luc Mottin、Alexandre Flament、Paul van Rijen、Esteban Gaillac 等（共 6 人） |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-09-29T16:52:38Z |
| **关键词** | `Agentic RAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2609.37993v1](http://arxiv.org/abs/2609.37993v1) |

**📝 摘要概括：**

> BITEM团队通过单个代理管道进入了NTCIR-19 R2C2任务的两个子任务，其中模型在电影语料库上搜索、读取和记录证据，而编导则保留记录并规定可以提交的内容。只有当牵连级联根据其引用的段落对其进行检查时，才会承认索赔，并且只有当其背后有足够的经过检查的证据时，才会发布答案。每个问题运行三个或f...

</details>

<details>
<summary><b>3. Retrieve, Reproduce, Reveal: Dissecting Retrieval-Augmented Software Vulnerability Detection</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Sabrina Kaniewski、Tim Krämer、Julius Bächle、Markus Enzweiler、Michael Menth 等（共 6 人） |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-09-29T14:24:46Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2609.37669v1](http://arxiv.org/abs/2609.37669v1) |

**📝 摘要概括：**

> 通过在检索到的漏洞知识（如漏洞报告）中进行预测，越来越多地使用检索增强生成（ RAG ）来增强基于大语言模型（ LLM ）的软件漏洞检测。然而，现有的基于RAG的软件漏洞检测（ RAG4SVD ）系统通常使用专有模型进行评估，这对开放科学和可重复性提出了挑战。此外，研究使用不同的数据集，客户…

</details>

## 🗄️ 历史归档

| 日期 | 论文数 | 报告链接 |
|------|--------|----------|
| 2026-10-01 | 3 篇 | [2026-10-01.md](daily/2026-10-01.md) |
| 2026-09-30 | 0 篇 | [2026-09-30.md](daily/2026-09-30.md) |
| 2026-09-29 | 0 篇 | [2026-09-29.md](daily/2026-09-29.md) |
| 2026-09-15 | 0 篇 | [2026-09-15.md](daily/2026-09-15.md) |
| 2026-09-13 | 0 篇 | [2026-09-13.md](daily/2026-09-13.md) |
| 2026-09-12 | 0 篇 | [2026-09-12.md](daily/2026-09-12.md) |
| 2026-09-11 | 0 篇 | [2026-09-11.md](daily/2026-09-11.md) |
| 2026-09-10 | 1 篇 | [2026-09-10.md](daily/2026-09-10.md) |
| 2026-09-09 | 0 篇 | [2026-09-09.md](daily/2026-09-09.md) |
| 2026-09-08 | 0 篇 | [2026-09-08.md](daily/2026-09-08.md) |
| 2026-09-07 | 0 篇 | [2026-09-07.md](daily/2026-09-07.md) |
| 2026-09-06 | 0 篇 | [2026-09-06.md](daily/2026-09-06.md) |
| 2026-09-05 | 0 篇 | [2026-09-05.md](daily/2026-09-05.md) |
| 2026-09-04 | 1 篇 | [2026-09-04.md](daily/2026-09-04.md) |
| 2026-09-03 | 0 篇 | [2026-09-03.md](daily/2026-09-03.md) |
| 2026-09-02 | 0 篇 | [2026-09-02.md](daily/2026-09-02.md) |
| 2026-09-01 | 0 篇 | [2026-09-01.md](daily/2026-09-01.md) |
| 2026-08-31 | 0 篇 | [2026-08-31.md](daily/2026-08-31.md) |
| 2026-08-29 | 0 篇 | [2026-08-29.md](daily/2026-08-29.md) |
| 2026-08-28 | 0 篇 | [2026-08-28.md](daily/2026-08-28.md) |
| 2026-08-27 | 5 篇 | [2026-08-27.md](daily/2026-08-27.md) |
| 2026-08-25 | 0 篇 | [2026-08-25.md](daily/2026-08-25.md) |
| 2026-08-24 | 0 篇 | [2026-08-24.md](daily/2026-08-24.md) |
| 2026-08-23 | 0 篇 | [2026-08-23.md](daily/2026-08-23.md) |
| 2026-08-22 | 0 篇 | [2026-08-22.md](daily/2026-08-22.md) |
| 2026-08-21 | 0 篇 | [2026-08-21.md](daily/2026-08-21.md) |
| 2026-08-20 | 1 篇 | [2026-08-20.md](daily/2026-08-20.md) |
| 2026-08-19 | 0 篇 | [2026-08-19.md](daily/2026-08-19.md) |
| 2026-08-18 | 0 篇 | [2026-08-18.md](daily/2026-08-18.md) |
| 2026-08-17 | 0 篇 | [2026-08-17.md](daily/2026-08-17.md) |

## 🏛️ 顶级机构覆盖范围

覆盖超过 **70 个**顶级 AI 机构，包括：

- **科技公司：** Microsoft、Google DeepMind、OpenAI、Anthropic、Meta AI、NVIDIA、Baidu、Alibaba、ByteDance 等
- **北美顶级大学：** MIT、Stanford、CMU、UC Berkeley、Harvard、Princeton、Cornell、Caltech 等
- **中国顶级大学/机构：** 清华大学、北京大学、浙大、上交大、复旦、中科院、MSRA 等
- **欧洲/其他：** Oxford、Cambridge、ETH Zurich、Mila、NUS、KAIST 等

---

*由 [clawBot RAGDaily](https://github.com/Jacob-biu/clawBot) 自动维护 | 最后更新：2026-10-01 01:08 UTC*
