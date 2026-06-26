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

## 📅 今日论文 — 2026-06-26　　[→ 查看完整报告](daily/2026-06-26.md)

> 共筛选出 **4** 篇论文 | 更新于 2026-06-26 06:41 UTC

### 论文目录与概要

| # | 论文标题 | 核心概要 | 来源机构 | 第一作者 |
|---|---------|---------|---------|--------|
| 1 | [MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming f…](http://arxiv.org/abs/2606.26793v1) | 多模式代理检索增强生成（ RAG ）系统将攻击面扩展到提示注入之外，包括文本中毒、图像注入、直接查询攻击和编排器级工具操作。现有的红队方法通常是特定于表面的，并且经常回收已知的攻击模板；在文本中毒基准… | — | Inderjeet Singh |
| 2 | [Temporal Validity in Retrieval Memory: Eliminating Stale-Fac…](http://arxiv.org/abs/2606.26511v1) | 检索增强生成（ RAG ）使客服代表能够访问积累的知识，但没有时间模型。当事实发生变化（例如，函数被重命名或API重构）时， RAG会检索具有几乎相同嵌入相似性的过时值和当前值。然后，代理人要么弃权，… | — | Neeraj Yadav |
| 3 | [MKG-RAG-Bench: Benchmarking Retrieval in Multimodal Knowledg…](http://arxiv.org/abs/2606.26458v1) | 基于知识图的检索增强生成（ RAG ）已成为一种有前途的大型语言模型基础方法，但现有的基准在很大程度上忽略了多模态知识图RAG （ MKG-RAG ）中检索的挑战。在实践中，检索是一个关键的瓶颈：多模… | — | Xiaochen Wang |
| 4 | [How Do Tool-Augmented LLM Agents Perform on Real-World Energ…](http://arxiv.org/abs/2606.26346v1) | 代理基准已经出现在通用和特定领域的设置中，包括金融、编码、法律和药物发现，但能源领域评估在很大程度上仍然局限于静态知识召回。对于一个需要实时数据检索、专业监管和市场知识以及现实世界约束下的多步定量推理… | — | David Akinpelu |

### 论文详情

<details>
<summary><b>1. MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Inderjeet Singh、Andrés Murillo、Motoyoshi Sekiya、Yuki Unno、Junichi Suga |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-06-25T09:26:49Z |
| **关键词** | `Agentic RAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26793v1](http://arxiv.org/abs/2606.26793v1) |

**📝 摘要概括：**

> 多模式代理检索增强生成（ RAG ）系统将攻击面扩展到提示注入之外，包括文本中毒、图像注入、直接查询攻击和编排器级工具操作。现有的红队方法通常是特定于表面的，并且经常回收已知的攻击模板；在文本中毒基准上，我们测量了73-84%的精确重复。我们呈现了镜子，这是一个统一的跨表面框架……

</details>

<details>
<summary><b>2. Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Neeraj Yadav |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-06-25T01:31:53Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26511v1](http://arxiv.org/abs/2606.26511v1) |

**📝 摘要概括：**

> 检索增强生成（ RAG ）使客服代表能够访问积累的知识，但没有时间模型。当事实发生变化（例如，函数被重命名或API重构）时， RAG会检索具有几乎相同嵌入相似性的过时值和当前值。然后，代理人要么弃权，要么提供被取代的事实。我们表明这是一个结构性问题：在校准数据集上，余弦相似性将矛盾的事实与……区分开来

</details>

<details>
<summary><b>3. MKG-RAG-Bench: Benchmarking Retrieval in Multimodal Knowledge Graph-Augmented Generation</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Xiaochen Wang、Bao Hoang、Han Liu、Ting Wang、Fenglong Ma |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-06-24T23:38:42Z |
| **关键词** | `Graph RAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26458v1](http://arxiv.org/abs/2606.26458v1) |

**📝 摘要概括：**

> 基于知识图的检索增强生成（ RAG ）已成为一种有前途的大型语言模型基础方法，但现有的基准在很大程度上忽略了多模态知识图RAG （ MKG-RAG ）中检索的挑战。在实践中，检索是一个关键的瓶颈：多模态知识是异构的，难以跨模态对齐，并且通常由专为非结构化语料库设计的检索器提供很少的服务。

</details>

<details>
<summary><b>4. How Do Tool-Augmented LLM Agents Perform on Real-World Energy Analytics Tasks?</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | David Akinpelu、Akintonde Abbas、Rereloluwa Alimi、Ayodeji Lana |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-06-24T19:38:21Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26346v1](http://arxiv.org/abs/2606.26346v1) |

**📝 摘要概括：**

> 代理基准已经出现在通用和特定领域的设置中，包括金融、编码、法律和药物发现，但能源领域评估在很大程度上仍然局限于静态知识召回。对于一个需要实时数据检索、专业监管和市场知识以及现实世界约束下的多步定量推理的行业来说，这是一个关键的差距。我们提出了一个工具增强的实证研究……

</details>

## 🗄️ 历史归档

| 日期 | 论文数 | 报告链接 |
|------|--------|----------|
| 2026-06-26 | 4 篇 | [2026-06-26.md](daily/2026-06-26.md) |

## 🏛️ 顶级机构覆盖范围

覆盖超过 **70 个**顶级 AI 机构，包括：

- **科技公司：** Microsoft、Google DeepMind、OpenAI、Anthropic、Meta AI、NVIDIA、Baidu、Alibaba、ByteDance 等
- **北美顶级大学：** MIT、Stanford、CMU、UC Berkeley、Harvard、Princeton、Cornell、Caltech 等
- **中国顶级大学/机构：** 清华大学、北京大学、浙大、上交大、复旦、中科院、MSRA 等
- **欧洲/其他：** Oxford、Cambridge、ETH Zurich、Mila、NUS、KAIST 等

---

*由 [clawBot RAGDaily](https://github.com/Jacob-biu/clawBot) 自动维护 | 最后更新：2026-06-26 06:41 UTC*
