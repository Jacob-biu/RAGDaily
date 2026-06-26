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

> 共筛选出 **5** 篇论文 | 更新于 2026-06-26 06:08 UTC

### 论文目录与概要

| # | 论文标题 | 核心概要 | 来源机构 | 第一作者 |
|---|---------|---------|---------|--------|
| 1 | [LCAi: Life Cycle Assessment with big data fusion and retriev…](http://arxiv.org/abs/2606.26857v1) | 生命周期评估的解释阶段通常缺乏结构化机制，无法在技术、社会和政策不确定性下将解决环境热点的量化改进机会转化为可操作的战略路径。为了克服这一局限性，本研究引入了用于LCA解释的透视条件检索增强生成框架，… | Apple、MIT | Georgios Tsironis |
| 2 | [MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming f…](http://arxiv.org/abs/2606.26793v1) | 多模式代理检索增强生成（ RAG ）系统将攻击面扩展到提示注入之外，包括文本中毒、图像注入、直接查询攻击和编排器级工具操作。现有的红队方法通常是特定于表面的，并且经常回收已知的攻击模板；在文本中毒基准… | TRI | Inderjeet Singh |
| 3 | [Temporal Validity in Retrieval Memory: Eliminating Stale-Fac…](http://arxiv.org/abs/2606.26511v1) | 检索增强生成（ RAG ）使客服代表能够访问积累的知识，但没有时间模型。当事实发生变化（例如，函数被重命名或API重构）时， RAG会检索具有几乎相同嵌入相似性的过时值和当前值。我们发布了知识进化下的… | Mila、TRI | Neeraj Yadav |
| 4 | [Retrieval-Warmed Energy-Based Reasoning: A Five-Arm Ablation…](http://arxiv.org/abs/2606.26476v1) | 热启动的扩散采样器加速了迭代推理，但很少清楚流水线的哪一部分承载了增益。我们研究\ textbf {基于检索加热能量的推理（ RW-EBR ）} -一种基于IRED能量的扩散模型\ cite {du2… | TRI | Libo Sun |
| 5 | [MKG-RAG-Bench: Benchmarking Retrieval in Multimodal Knowledg…](http://arxiv.org/abs/2606.26458v1) | 基于知识图的检索增强生成（ RAG ）已成为一种有前途的大型语言模型基础方法，但现有的基准在很大程度上忽略了多模态知识图RAG （ MKG-RAG ）中检索的挑战。在实践中，检索是一个关键的瓶颈：多模… | MIT、TRI | Xiaochen Wang |

### 论文详情

<details>
<summary><b>1. LCAi: Life Cycle Assessment with big data fusion and retrieval-augmented generation-assisted interpretation</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Georgios Tsironis、Juan D. Medrano-Garcia、Gonzalo Guillen-Gosalbez |
| **所属机构** | （详见原文） |
| **顶级机构标签** | Apple、MIT、HIT |
| **发布时间** | 2026-06-25T10:41:48Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26857v1](http://arxiv.org/abs/2606.26857v1) |

**📝 摘要概括：**

> 生命周期评估的解释阶段通常缺乏结构化机制，无法在技术、社会和政策不确定性下将解决环境热点的量化改进机会转化为可操作的战略路径。为了克服这一局限性，本研究引入了用于LCA解释的透视条件检索增强生成框架，其中多视角检索和控制…

</details>

<details>
<summary><b>2. MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Inderjeet Singh、Andrés Murillo、Motoyoshi Sekiya、Yuki Unno、Junichi Suga |
| **所属机构** | （详见原文） |
| **顶级机构标签** | TRI |
| **发布时间** | 2026-06-25T09:26:49Z |
| **关键词** | `Agentic RAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26793v1](http://arxiv.org/abs/2606.26793v1) |

**📝 摘要概括：**

> 多模式代理检索增强生成（ RAG ）系统将攻击面扩展到提示注入之外，包括文本中毒、图像注入、直接查询攻击和编排器级工具操作。现有的红队方法通常是特定于表面的，并且经常回收已知的攻击模板；在文本中毒基准上，我们测量了73-84%的精确重复。我们发布了ART-SafeBench ，其中包含41,815条包内记录……

</details>

<details>
<summary><b>3. Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Neeraj Yadav |
| **所属机构** | （详见原文） |
| **顶级机构标签** | Mila、TRI |
| **发布时间** | 2026-06-25T01:31:53Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26511v1](http://arxiv.org/abs/2606.26511v1) |

**📝 摘要概括：**

> 检索增强生成（ RAG ）使客服代表能够访问积累的知识，但没有时间模型。当事实发生变化（例如，函数被重命名或API重构）时， RAG会检索具有几乎相同嵌入相似性的过时值和当前值。我们发布了知识进化下的记忆线束、数据集和无标记评估协议。

</details>

<details>
<summary><b>4. Retrieval-Warmed Energy-Based Reasoning: A Five-Arm Ablation Methodology for Diffusion-as-Inference on Structured Reasoning Tasks</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Libo Sun、Po-Wei Harn、Zewei Zhang、Peixiong He、Xiao Qin |
| **所属机构** | （详见原文） |
| **顶级机构标签** | TRI |
| **发布时间** | 2026-06-25T00:28:08Z |
| **关键词** | `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26476v1](http://arxiv.org/abs/2606.26476v1) |

**📝 摘要概括：**

> 热启动的扩散采样器加速了迭代推理，但很少清楚流水线的哪一部分承载了增益。我们研究\ textbf {基于检索加热能量的推理（ RW-EBR ）} -一种基于IRED能量的扩散模型\ cite {du2024ired} ，增强了现代霍普菲尔德轨迹记忆-并提供了一种\ textbf {五臂消融方法} （甲骨文，最佳常数，每查询随机，洗牌，对齐） ，将三个c…

</details>

<details>
<summary><b>5. MKG-RAG-Bench: Benchmarking Retrieval in Multimodal Knowledge Graph-Augmented Generation</b></summary>

| 字段 | 内容 |
|------|------|
| **作者** | Xiaochen Wang、Bao Hoang、Han Liu、Ting Wang、Fenglong Ma |
| **所属机构** | （详见原文） |
| **顶级机构标签** | MIT、TRI |
| **发布时间** | 2026-06-24T23:38:42Z |
| **关键词** | `Graph RAG` · `RAG` |
| **原文链接** | [http://arxiv.org/abs/2606.26458v1](http://arxiv.org/abs/2606.26458v1) |

**📝 摘要概括：**

> 基于知识图的检索增强生成（ RAG ）已成为一种有前途的大型语言模型基础方法，但现有的基准在很大程度上忽略了多模态知识图RAG （ MKG-RAG ）中检索的挑战。在实践中，检索是一个关键的瓶颈：多模态知识是异构的，难以跨模态对齐，并且通常为非结构化语料库设计的检索器服务不佳。通过…

</details>

## 🗄️ 历史归档

| 日期 | 论文数 | 报告链接 |
|------|--------|----------|
| 2026-06-26 | 5 篇 | [2026-06-26.md](daily/2026-06-26.md) |

## 🏛️ 顶级机构覆盖范围

覆盖超过 **70 个**顶级 AI 机构，包括：

- **科技公司：** Microsoft、Google DeepMind、OpenAI、Anthropic、Meta AI、NVIDIA、Baidu、Alibaba、ByteDance 等
- **北美顶级大学：** MIT、Stanford、CMU、UC Berkeley、Harvard、Princeton、Cornell、Caltech 等
- **中国顶级大学/机构：** 清华大学、北京大学、浙大、上交大、复旦、中科院、MSRA 等
- **欧洲/其他：** Oxford、Cambridge、ETH Zurich、Mila、NUS、KAIST 等

---

*由 [clawBot RAGDaily](https://github.com/Jacob-biu/clawBot) 自动维护 | 最后更新：2026-06-26 06:08 UTC*
