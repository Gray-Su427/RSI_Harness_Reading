---
id: arxiv-2606.09498
title: "Self-Harness: Harnesses That Improve Themselves"
authors: "Zhang, Zhang, Li, Zhang, Chen, Zhang, Bai, Hu"
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: false
org: "Shanghai Artificial Intelligence Laboratory"
role: harness-core
read_status: skim
read_date: 2026-10-13
---

**一句话**：提出 Self-Harness 范式，让固定模型的 agent 在无人类工程师、也不借助更强外部 agent 的条件下，按「弱点挖掘 → harness 提案 → 提案验证」三阶段循环自行修改自己所运行的 harness，并在 3 个模型 × 3 个 benchmark 的九种组合上全部提升 Pass。

**改进对象**：prompt、工具、记忆/状态、验证规则、权限策略、middleware 等多值。作者把 harness 定义为「instructions, the available tools, memory and state」等可配置面，主张每次只做 *bounded edits*、不替换整体控制架构；但保留的编辑里包含 subagent 分解与 middleware 创建等结构性机制。（主要贡献落在 harness 可配置面的整体，本篇自身不设单一轴值。泛读初步判断，待精读确认）

**改进信号**：失败轨迹（聚类失败 execution traces 得出模型特有失败模式）＋外部验证（benchmark 官方 verifier + held-out 上的 non-regression 接受门控）。（泛读初步判断，待精读确认）

**搜索算子**：refine（多样性候选提案 + 显式接受/拒绝门控，无种群、无遗传算子、无树搜索）。（泛读初步判断，待精读确认）

**递归深度**：**iterative**。作者逐字原话（§2 末与 §3 首段）：

> "Self-Harness studies a middle ground in which a fixed model iteratively improves the harness around itself through an explicit self-improvement loop driven by execution evidence."

> "whether the same fixed model, operating under the current harness, can propose a bounded candidate change to the harness that governs its own future behavior."

作者同时自设边界（§5 Conclusion）：

> "It studies bounded harness edits under fixed benchmarks, not open-ended self-improvement. Accepted edits may still reflect benchmark-specific failure patterns, and the protocol depends on the quality of verifier outcomes and trace records."

**主要实验**：benchmark：Terminal-Bench-2.0（主评测集 64 case）、SWE-bench Verified（固定 100 子集，67 held-in / 33 held-out）、AppWorld（180 例，90/90）；后端 MiniMax M2.5、Qwen3.5-35B-A3B、GLM-5。主指标 Pass（%），每个候选跑 2 次重复。结果：TB2.0 held-in 43.0→50.0 / 15.1→36.0 / 47.7→57.0，held-out 40.5→61.9 / 23.8→38.1 / 42.9→57.1；SWE-bench Verified +3.5–22.0 pt；AppWorld +10.3–40.6 pt；最大相对增益 132%，最大绝对增益 40.6 pt（GLM-5，44.4→85.0）。基线：仅 minimal DeepAgent-based 初始 harness 的前后自身对比（原文自述 "comparisons are therefore within-model comparisons"），**无外部强基线**。算力开销：未报告（附录只给部署细节：两个模型走托管 API，Qwen3.5-35B-A3B 本地 4×H200）。

**可复现性**：代码开源？原文未见说明（未见代码链接或开源声明）。archive 公开？未见说明，但附录给了较细的复现配置（Harbor 环境、2 MB/s 带宽上限、3600 s case / 120 s tool timeout、50 turns、每评测 2 次重复、固定数据划分）。

**是否入选精读**：是——本组 A/B/D 三轴的主证据候选：改进对象横跨多值但作者有明确的自定 harness 定义，且有 held-out non-regression 门控可直接回应争议 Q1（测量效度）。

**可疑之处**：
1. 无强基线，增益只与自身初始 harness 比；未做「多试几次总会挑出更好的」对照实验，直接落在 Q1 的质疑路径上。
2. 作者自称 "not open-ended self-improvement"，且改动被限制为 bounded edits——E 轴若按 `iterative` 记，需在精读时明确作者未主张 `full-rsi`。
3. Terminal-Bench-2.0 主评测集剔除了依赖不可靠外部资源、以及需要初始 harness 不支持的多模态输入的任务，即评测子集经过裁剪；跨 benchmark 数字不可直接比较。
4. 代码与 evolution archive 均未见公开声明，Q5 可复现性存疑。
5. `venue` 为 arXiv preprint；作者单位为 Shanghai AI Laboratory（含通讯作者 Lei Bai、Shuyue Hu），是否已有同行评审版本 ⚠️ 未核实。
