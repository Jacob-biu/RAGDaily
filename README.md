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

## 📅 今日论文 — 2026-10-08　　[→ 查看完整报告](daily/2026-10-08.md)

> 共筛选出 **5** 篇论文 | 更新于 2026-10-08 01:34 UTC

### 论文目录与概要

| # | 论文标题 | 核心概要 | 来源机构 | 第一作者 |
|---|---------|---------|---------|--------|
| 1 | [From Retrieval to Customer Context: Evaluating Frontier-Mode…](http://arxiv.org/abs/2610.09375v1) | 组织越来越多地使用前沿语言模型来分析客户反馈，但回答质量也取决于如何组织和提供反馈。我们将\ emph {customer context graph}定义为客户和业务环境的统一模型。类型化的关系将客… | — | Raviraja G |
| 2 | [TopoGraphRAG-Bench: Evaluating Multimodal GraphRAG on Layout…](http://arxiv.org/abs/2610.09360v1) | 真实世界的文档在复杂的页面布局中跨文本、表格、图形和标题分发证据。因此，回答此类文档的复杂问题不仅仅需要检索相关段落：系统必须恢复连接异构证据单元的证据拓扑。现有的GraphRAG评估仍然主要以文本为… | — | Ruochi Li |
| 3 | [BEACON-SP: Ontology-Grounded GraphRAG Framework for Clinical…](http://arxiv.org/abs/2610.09026v1) | 我们提出了BEACON-SP ，这是一个基于本体的图检索增强生成（ GraphRAG ）框架，用于在自杀预防等行为健康环境中面向临床医生的决策支持，其中有效的评估需要整合异构临床，行为，社会和时间证据… | — | Kemal Davaslioglu |
| 4 | [Trustworthy Domain-Specific AI for Structured Knowledge Retr…](http://arxiv.org/abs/2610.08894v1) | 本文提出了一种可扩展的架构，用于将非结构化、特定领域的文本转换为结构化知识，以进行检索和推理。它将半自动语料库管理、语义结构、检索和推理集成到一个可解释的管道中。该研究引入了Binary Bleed … | — | Ryan C. Barron |
| 5 | [Agentic AutoRAG: RAG Pipeline Optimization through Reasoning…](http://arxiv.org/abs/2610.08452v1) | 检索增强生成（ RAG ）是一种广泛使用的方法，用于在外部知识中建立大型语言模型（ LLM ）。然而，在从分块和嵌入模型到重新排序和生成等许多相互作用的选择上，配置流水线是一个昂贵的超参数优化问题。现… | — | Lasse B. Strand |

### 论文详情

<details>
<summary><b>1. From Retrieval to Customer Context: Evaluating Frontier-Model Systems for Voice-of-Customer Analysis</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Raviraja G、Viraj Bagal、Prabhath Chellingi |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-10-07T03:30:22Z |
| **关键词** | `Agentic RAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2610.09375v1](http://arxiv.org/abs/2610.09375v1) |

**📝 摘要概括：**

> 组织越来越多地使用前沿语言模型来分析客户反馈，但回答质量也取决于如何组织和提供反馈。我们将\ emph {customer context graph}定义为客户和业务环境的统一模型。类型化的关系将客户对象（反馈、对话、用户和账号）、运营对象（工单、客服代表、机会和竞争对手）和分析联系起来……

</details>

<details>
<summary><b>2. TopoGraphRAG-Bench: Evaluating Multimodal GraphRAG on Layout-Grounded Evidence Reasoning</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Ruochi Li、Jianzhe Lin、Haoxuan Zhang、Haihua Chen、Junhua Ding 等（共 7 人） |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-10-07T03:15:31Z |
| **关键词** | `GraphRAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2610.09360v1](http://arxiv.org/abs/2610.09360v1) |

**📝 摘要概括：**

> 真实世界的文档在复杂的页面布局中跨文本、表格、图形和标题分发证据。因此，回答此类文档的复杂问题不仅仅需要检索相关段落：系统必须恢复连接异构证据单元的证据拓扑。现有的GraphRAG评估仍然主要以文本为中心，而多模态文档RAG基准评估跨模态检索和生成……

</details>

<details>
<summary><b>3. BEACON-SP: Ontology-Grounded GraphRAG Framework for Clinical Suicide Risk Assessment</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Kemal Davaslioglu、Nathan Conger、Sastry Kompella、Yalin E. Sagduyu、Nathaniel D. Bastian |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-10-06T19:23:51Z |
| **关键词** | `GraphRAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2610.09026v1](http://arxiv.org/abs/2610.09026v1) |

**📝 摘要概括：**

> 我们提出了BEACON-SP ，这是一个基于本体的图检索增强生成（ GraphRAG ）框架，用于在自杀预防等行为健康环境中面向临床医生的决策支持，其中有效的评估需要整合异构临床，行为，社会和时间证据。BEACON-SP将患者知识图与本体引导的检索相结合，以支持跨诊断、药物、R的多跳推理……

</details>

<details>
<summary><b>4. Trustworthy Domain-Specific AI for Structured Knowledge Retrieval and Reasoning</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Ryan C. Barron |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-10-06T16:35:41Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2610.08894v1](http://arxiv.org/abs/2610.08894v1) |

**📝 摘要概括：**

> 本文提出了一种可扩展的架构，用于将非结构化、特定领域的文本转换为结构化知识，以进行检索和推理。它将半自动语料库管理、语义结构、检索和推理集成到一个可解释的管道中。该研究引入了Binary Bleed ，这是一种自适应的二进制搜索方法，可降低非负矩阵分解（ NMF ）的低秩搜索复杂性，以及Hierarch...

</details>

<details>
<summary><b>5. Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Lasse B. Strand、Robert Jakob、Kevin O'Sullivan、Markus Kreft |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-10-06T14:38:15Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2610.08452v1](http://arxiv.org/abs/2610.08452v1) |

**📝 摘要概括：**

> 检索增强生成（ RAG ）是一种广泛使用的方法，用于在外部知识中建立大型语言模型（ LLM ）。然而，在从分块和嵌入模型到重新排序和生成等许多相互作用的选择上，配置流水线是一个昂贵的超参数优化问题。现有的优化器，从贪婪搜索到贝叶斯优化，将每次试验简化为总分，无需模拟为什么……

</details>

## 🗄️ 历史归档

| 日期 | 论文数 | 报告链接 |
|------|--------|----------|
| 2026-10-08 | 5 篇 | [2026-10-08.md](daily/2026-10-08.md) |
| 2026-10-07 | 1 篇 | [2026-10-07.md](daily/2026-10-07.md) |
| 2026-10-06 | 0 篇 | [2026-10-06.md](daily/2026-10-06.md) |
| 2026-10-05 | 0 篇 | [2026-10-05.md](daily/2026-10-05.md) |
| 2026-10-04 | 0 篇 | [2026-10-04.md](daily/2026-10-04.md) |
| 2026-10-03 | 2 篇 | [2026-10-03.md](daily/2026-10-03.md) |
| 2026-10-02 | 0 篇 | [2026-10-02.md](daily/2026-10-02.md) |
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

## 🏛️ 顶级机构覆盖范围

覆盖超过 **70 个**顶级 AI 机构，包括：

- **科技公司：** Microsoft、Google DeepMind、OpenAI、Anthropic、Meta AI、NVIDIA、Baidu、Alibaba、ByteDance 等
- **北美顶级大学：** MIT、Stanford、CMU、UC Berkeley、Harvard、Princeton、Cornell、Caltech 等
- **中国顶级大学/机构：** 清华大学、北京大学、浙大、上交大、复旦、中科院、MSRA 等
- **欧洲/其他：** Oxford、Cambridge、ETH Zurich、Mila、NUS、KAIST 等

---

*由 [clawBot RAGDaily](https://github.com/Jacob-biu/clawBot) 自动维护 | 最后更新：2026-10-08 01:34 UTC*
