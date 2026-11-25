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

## 📅 今日论文 — 2026-11-25　　[→ 查看完整报告](daily/2026-11-25.md)

> 共筛选出 **3** 篇论文 | 更新于 2026-11-25 04:47 UTC

### 论文目录与概要

| # | 论文标题 | 核心概要 | 来源机构 | 第一作者 |
|---|---------|---------|---------|--------|
| 1 | [Efficient Video Retrieval Augmented Generation via Token All…](http://arxiv.org/abs/2611.32938v1) | 要高效理解长视频，需要识别相关证据，同时最大限度地减少视觉-语言模型（VLM）处理的token数量。现有的视频检索增强生成（RAG）方法依赖于帧选择和令牌压缩，但忽视了每个额外令牌的价值。我们推出了L… | — | Ayush Barik |
| 2 | [SPARQL-Planned Single-Hop Traversal over a Live Knowledge Gr…](http://arxiv.org/abs/2611.31771v1) | 语义检索在召回率和准确率方面都难以应对多跳问答：黄金段落被埋没在干扰项中，这些干扰项会降低阅读器的答案质量，检索这些段落需要对查询进行推理，而不是简单地进行匹配。GraphRAG 技术通过将段落与图节… | — | Priyesh Vakharia |
| 3 | [BRAG: Bayesian Retrieval Augmented Generation](http://arxiv.org/abs/2611.31656v1) | 检索增强生成（RAG）根据与查询的语义相似性对记忆块进行排序。许多方法通过从检索结果的反馈中学习来改进这一点，但每种方法都是一种独立的启发式方法，并没有考虑何时是正确的选择。我们推出了BRAG，这是一… | — | Javier Movellan |

### 论文详情

<details>
<summary><b>1. Efficient Video Retrieval Augmented Generation via Token Allocation</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Ayush Barik、Fan Lai、Francis Y. Yan |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-11-24T16:43:31Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2611.32938v1](http://arxiv.org/abs/2611.32938v1) |

**📝 摘要概括：**

> 要高效理解长视频，需要识别相关证据，同时最大限度地减少视觉-语言模型（VLM）处理的token数量。现有的视频检索增强生成（RAG）方法依赖于帧选择和令牌压缩，但忽视了每个额外令牌的价值。我们推出了Lembas，这是一个即插即用的框架，将视频RAG表述为在共享……下对帧和字幕的token分配问题。

</details>

<details>
<summary><b>2. SPARQL-Planned Single-Hop Traversal over a Live Knowledge Graph for Multi-Hop Question Answering</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Priyesh Vakharia、Masud Moshtaghi、Pratyay Banerjee、Nicholas Jedema、Amita Misra 等（共 6 人） |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-11-24T01:24:00Z |
| **关键词** | `GraphRAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2611.31771v1](http://arxiv.org/abs/2611.31771v1) |

**📝 摘要概括：**

> 语义检索在召回率和准确率方面都难以应对多跳问答：黄金段落被埋没在干扰项中，这些干扰项会降低阅读器的答案质量，检索这些段落需要对查询进行推理，而不是简单地进行匹配。GraphRAG 技术通过将段落与图节点相连，并在初始检索后执行一次或多次跳跃式扩展，从而扩展语义检索。这提高了召回率，但多跳扩展……

</details>

<details>
<summary><b>3. BRAG: Bayesian Retrieval Augmented Generation</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Javier Movellan、Manjot Bilkhu、Young-mok Jung、Sirajul Salekin、Henry Tran 等（共 6 人） |
| **所属机构** | （详见原文） |
| **发布时间** | 2026-11-23T22:41:00Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2611.31656v1](http://arxiv.org/abs/2611.31656v1) |

**📝 摘要概括：**

> 检索增强生成（RAG）根据与查询的语义相似性对记忆块进行排序。许多方法通过从检索结果的反馈中学习来改进这一点，但每种方法都是一种独立的启发式方法，并没有考虑何时是正确的选择。我们推出了BRAG，这是一种带有使用功能的检索生成模型。每个片段从锚定在其原始嵌入的冯·米塞斯-费舍尔分量混合中生成其所回答的查询，并且每个……

</details>

## 🗄️ 历史归档

| 日期 | 论文数 | 报告链接 |
|------|--------|----------|
| 2026-11-25 | 3 篇 | [2026-11-25.md](daily/2026-11-25.md) |
| 2026-11-24 | 0 篇 | [2026-11-24.md](daily/2026-11-24.md) |
| 2026-11-23 | 0 篇 | [2026-11-23.md](daily/2026-11-23.md) |
| 2026-11-22 | 0 篇 | [2026-11-22.md](daily/2026-11-22.md) |
| 2026-11-21 | 0 篇 | [2026-11-21.md](daily/2026-11-21.md) |
| 2026-11-20 | 1 篇 | [2026-11-20.md](daily/2026-11-20.md) |
| 2026-11-05 | 0 篇 | [2026-11-05.md](daily/2026-11-05.md) |
| 2026-11-04 | 0 篇 | [2026-11-04.md](daily/2026-11-04.md) |
| 2026-11-03 | 0 篇 | [2026-11-03.md](daily/2026-11-03.md) |
| 2026-11-02 | 0 篇 | [2026-11-02.md](daily/2026-11-02.md) |
| 2026-11-01 | 0 篇 | [2026-11-01.md](daily/2026-11-01.md) |
| 2026-10-31 | 0 篇 | [2026-10-31.md](daily/2026-10-31.md) |
| 2026-10-30 | 0 篇 | [2026-10-30.md](daily/2026-10-30.md) |
| 2026-10-29 | 1 篇 | [2026-10-29.md](daily/2026-10-29.md) |
| 2026-10-28 | 0 篇 | [2026-10-28.md](daily/2026-10-28.md) |
| 2026-10-27 | 0 篇 | [2026-10-27.md](daily/2026-10-27.md) |
| 2026-10-25 | 0 篇 | [2026-10-25.md](daily/2026-10-25.md) |
| 2026-10-24 | 0 篇 | [2026-10-24.md](daily/2026-10-24.md) |
| 2026-10-23 | 2 篇 | [2026-10-23.md](daily/2026-10-23.md) |
| 2026-10-22 | 1 篇 | [2026-10-22.md](daily/2026-10-22.md) |
| 2026-10-21 | 0 篇 | [2026-10-21.md](daily/2026-10-21.md) |
| 2026-10-20 | 0 篇 | [2026-10-20.md](daily/2026-10-20.md) |
| 2026-10-18 | 0 篇 | [2026-10-18.md](daily/2026-10-18.md) |
| 2026-10-17 | 0 篇 | [2026-10-17.md](daily/2026-10-17.md) |
| 2026-10-16 | 1 篇 | [2026-10-16.md](daily/2026-10-16.md) |
| 2026-10-15 | 0 篇 | [2026-10-15.md](daily/2026-10-15.md) |
| 2026-10-14 | 0 篇 | [2026-10-14.md](daily/2026-10-14.md) |
| 2026-10-13 | 0 篇 | [2026-10-13.md](daily/2026-10-13.md) |
| 2026-10-12 | 0 篇 | [2026-10-12.md](daily/2026-10-12.md) |
| 2026-10-11 | 0 篇 | [2026-10-11.md](daily/2026-10-11.md) |

## 🏛️ 顶级机构覆盖范围

覆盖超过 **70 个**顶级 AI 机构，包括：

- **科技公司：** Microsoft、Google DeepMind、OpenAI、Anthropic、Meta AI、NVIDIA、Baidu、Alibaba、ByteDance 等
- **北美顶级大学：** MIT、Stanford、CMU、UC Berkeley、Harvard、Princeton、Cornell、Caltech 等
- **中国顶级大学/机构：** 清华大学、北京大学、浙大、上交大、复旦、中科院、MSRA 等
- **欧洲/其他：** Oxford、Cambridge、ETH Zurich、Mila、NUS、KAIST 等

---

*由 [clawBot RAGDaily](https://github.com/Jacob-biu/clawBot) 自动维护 | 最后更新：2026-11-25 04:47 UTC*
