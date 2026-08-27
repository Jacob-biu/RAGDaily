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

## 📅 今日论文 — 2026-08-27　　[→ 查看完整报告](daily/2026-08-27.md)

> 共筛选出 **5** 篇论文 | 更新于 2026-08-27 02:53 UTC

### 论文目录与概要

| # | 论文标题 | 核心概要 | 来源机构 | 第一作者 |
|---|---------|---------|---------|--------|
| 1 | [Multi-Granularity Context-Enhanced RAG over Multimodal Knowl…](http://arxiv.org/abs/2608.25986v1) | 检索增强生成（ RAG ）被广泛用于缓解大型语言模型（ LLM ）和多模态大型语言模型（ MLLM ）中的幻觉问题。特别是，基于知识图谱（ KG ）的RAG利用结构化知识为（ M ） LLM提供高质量… | — | Zongyu Wu |
| 2 | [LivingRAG: Augmenting Graph RAG with Experience](http://arxiv.org/abs/2608.25960v1) | 基于图形的RAG通过将证据组织为知识图来改进多跳问答。然而，大多数现有的RAG系统单独处理每个查询，并在推理后从LLM的响应中丢弃有用的推理。因此，以后的相关查询需要从头开始检索证据和原因。我们提出了… | — | Yuzhuo Cui |
| 3 | [PonsRAG: A Pons-Inspired RAG Bridging Cognitive Islands for …](http://arxiv.org/abs/2608.25486v1) | 长叙事推理是处理和推理复杂叙事的基本能力。虽然检索增强生成提供了一个有前途的框架，但现有方法仍然面临两个关键挑战：认知孤岛和跨层证据断开。为了解决这些问题，我们提出了PonsRAG ，这是一种受生物桥… | — | Rongchen Zhao |
| 4 | [SelfGraphRAG: Bridging the Supervision Gap in Graph-Based RA…](http://arxiv.org/abs/2608.25123v1) | 检索增强生成（ RAG ）通过合并外部知识而无需重新训练来改进大型语言模型，但现有方法通常未充分利用知识图形中编码的关系结构。基于图的RAG可以捕获实体关系，但监督式图检索通常需要标记的问答数据，这些… | — | Ben Lagnese |
| 5 | [Retrieved But Not Reliable: A Survey on Attacks, and Defense…](http://arxiv.org/abs/2608.24977v1) | 检索增强生成（ RAG ）通过将输出建立在外部知识的基础上，改善事实性并减少幻觉，从而增强大型语言模型。同时，检索增强管道引入了新的鲁棒性和安全风险，包括语料库中毒、后门攻击、隐私泄露和公平性违规。尽… | — | Minh Tran |

### 论文详情

<details>
<summary><b>1. Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Zongyu Wu、Yilong Wang、Xiaochen Wang、Minhua Lin、Zhichao Xu 等（共 8 人） |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-08-26T16:38:02Z |
| **关键词** | `Graph RAG` · `GraphRAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2608.25986v1](http://arxiv.org/abs/2608.25986v1) |

**📝 摘要概括：**

> 检索增强生成（ RAG ）被广泛用于缓解大型语言模型（ LLM ）和多模态大型语言模型（ MLLM ）中的幻觉问题。特别是，基于知识图谱（ KG ）的RAG利用结构化知识为（ M ） LLM提供高质量的外部信息。在这些工作的基础上，最近的研究探索了多模态知识图（ MMKG ）作为GraphRAG的知识库。这使Graph RAG能够在…

</details>

<details>
<summary><b>2. LivingRAG: Augmenting Graph RAG with Experience</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Yuzhuo Cui、Zongye Zhang、Qingjie Liu |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-08-26T16:21:06Z |
| **关键词** | `Graph RAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2608.25960v1](http://arxiv.org/abs/2608.25960v1) |

**📝 摘要概括：**

> 基于图形的RAG通过将证据组织为知识图来改进多跳问答。然而，大多数现有的RAG系统单独处理每个查询，并在推理后从LLM的响应中丢弃有用的推理。因此，以后的相关查询需要从头开始检索证据和原因。我们提出了LivingRAG ，这是一个具有可写和可重用推理经验的Graph RAG框架。LivingRAG增加了一种可写的体验……

</details>

<details>
<summary><b>3. PonsRAG: A Pons-Inspired RAG Bridging Cognitive Islands for Coordinated Long Narrative Reasoning</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Rongchen Zhao、Yu Chen、Juyuan Wang、Zhouting Mo、Jianxing Yu 等（共 7 人） |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-08-26T07:55:44Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2608.25486v1](http://arxiv.org/abs/2608.25486v1) |

**📝 摘要概括：**

> 长叙事推理是处理和推理复杂叙事的基本能力。虽然检索增强生成提供了一个有前途的框架，但现有方法仍然面临两个关键挑战：认知孤岛和跨层证据断开。为了解决这些问题，我们提出了PonsRAG ，这是一种受生物桥梁启发的协调RAG框架。PonsRAG由两个关键组成部分组成：三层工业……

</details>

<details>
<summary><b>4. SelfGraphRAG: Bridging the Supervision Gap in Graph-Based RAG with Synthetic QA Generation</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Ben Lagnese、Manas Gaur |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-08-25T20:18:05Z |
| **关键词** | `GraphRAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2608.25123v1](http://arxiv.org/abs/2608.25123v1) |

**📝 摘要概括：**

> 检索增强生成（ RAG ）通过合并外部知识而无需重新训练来改进大型语言模型，但现有方法通常未充分利用知识图形中编码的关系结构。基于图的RAG可以捕获实体关系，但监督式图检索通常需要标记的问答数据，这些数据可能不适用于新构建的图。我们通过SelfGraphRAG来解决这一局限性，这是一个分数……

</details>

<details>
<summary><b>5. Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Minh Tran、Cuong Dang、Tuc Nguyen、Khanh-Tung Tran、Minh Huynh Nguyen 等（共 12 人） |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-08-25T16:18:04Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2608.24977v1](http://arxiv.org/abs/2608.24977v1) |

**📝 摘要概括：**

> 检索增强生成（ RAG ）通过将输出建立在外部知识的基础上，改善事实性并减少幻觉，从而增强大型语言模型。同时，检索增强管道引入了新的鲁棒性和安全风险，包括语料库中毒、后门攻击、隐私泄露和公平性违规。尽管在这一领域取得了快速进展，但现有的调查在治疗攻击者目标方面仍然有限……

</details>

## 🗄️ 历史归档

| 日期 | 论文数 | 报告链接 |
|------|--------|----------|
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
| 2026-08-16 | 0 篇 | [2026-08-16.md](daily/2026-08-16.md) |
| 2026-08-15 | 0 篇 | [2026-08-15.md](daily/2026-08-15.md) |
| 2026-08-14 | 1 篇 | [2026-08-14.md](daily/2026-08-14.md) |
| 2026-08-13 | 1 篇 | [2026-08-13.md](daily/2026-08-13.md) |
| 2026-08-12 | 0 篇 | [2026-08-12.md](daily/2026-08-12.md) |
| 2026-08-11 | 0 篇 | [2026-08-11.md](daily/2026-08-11.md) |
| 2026-08-10 | 0 篇 | [2026-08-10.md](daily/2026-08-10.md) |
| 2026-08-09 | 0 篇 | [2026-08-09.md](daily/2026-08-09.md) |
| 2026-08-08 | 0 篇 | [2026-08-08.md](daily/2026-08-08.md) |
| 2026-08-07 | 1 篇 | [2026-08-07.md](daily/2026-08-07.md) |
| 2026-08-05 | 1 篇 | [2026-08-05.md](daily/2026-08-05.md) |
| 2026-08-04 | 0 篇 | [2026-08-04.md](daily/2026-08-04.md) |
| 2026-08-03 | 0 篇 | [2026-08-03.md](daily/2026-08-03.md) |
| 2026-08-02 | 0 篇 | [2026-08-02.md](daily/2026-08-02.md) |
| 2026-08-01 | 0 篇 | [2026-08-01.md](daily/2026-08-01.md) |
| 2026-07-31 | 0 篇 | [2026-07-31.md](daily/2026-07-31.md) |
| 2026-07-30 | 0 篇 | [2026-07-30.md](daily/2026-07-30.md) |
| 2026-07-29 | 0 篇 | [2026-07-29.md](daily/2026-07-29.md) |
| 2026-07-28 | 1 篇 | [2026-07-28.md](daily/2026-07-28.md) |
| 2026-07-27 | 0 篇 | [2026-07-27.md](daily/2026-07-27.md) |

## 🏛️ 顶级机构覆盖范围

覆盖超过 **70 个**顶级 AI 机构，包括：

- **科技公司：** Microsoft、Google DeepMind、OpenAI、Anthropic、Meta AI、NVIDIA、Baidu、Alibaba、ByteDance 等
- **北美顶级大学：** MIT、Stanford、CMU、UC Berkeley、Harvard、Princeton、Cornell、Caltech 等
- **中国顶级大学/机构：** 清华大学、北京大学、浙大、上交大、复旦、中科院、MSRA 等
- **欧洲/其他：** Oxford、Cambridge、ETH Zurich、Mila、NUS、KAIST 等

---

*由 [clawBot RAGDaily](https://github.com/Jacob-biu/clawBot) 自动维护 | 最后更新：2026-08-27 02:53 UTC*
