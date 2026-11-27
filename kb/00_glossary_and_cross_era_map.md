# 机器人装配知识库：统一缩略词表与跨时代技术演进映射（1985–2025）

> **来源书目**
> - **Book2025**：Jing Xu, Hao Su, Rui Chen, Zhimin Hou, *Robotic Intelligent Assembly*, Springer & Huazhong University of Science and Technology Press, 2025, 246 pp., ISBN 978-981-96-2656-4 / 978-981-96-2657-1 (eBook), DOI: `https://doi.org/10.1007/978-981-96-2657-1`.
> - **Book1985**：Keith Rathmill (Ed.), *Robotic Assembly*, IFS (Publications) Ltd & Springer-Verlag, 1985, 390 pp., ISBN 0-903-608-71-5 / 3-540-15483-3 / 0-387-15483-3.

---

## 1. 跨 40 年核心技术演进映射表（1985 → 2025）

| 技术领域 | 1985 经典工业装配（Book1985） | 2025 智能自主装配（Book2025） | 演进逻辑与知识关联 |
| :--- | :--- | :--- | :--- |
| **柔顺与接触控制** | 机械被动柔顺 **RCC（Remote Center Compliance）**、主动顺应（Active Accommodation）、自适应被动顺应（Adaptive Passive Accommodation）、Type I/II 力控方案 [Book1985 Part 5] | **阻抗条件动作空间**（Impedance-Conditioned Action Space）、分层柔顺控制策略搜索（**HC-CPS**）、可变阻抗学习 [Book2025 Ch.10] | 从固定物理刚度/手调增益演进为策略网络动态调节刚度与阻尼参数 |
| **轴孔装配机理（PiH）** | 倒角设计规则（Chamfer）、间隙配合分析、机械导向与振动辅助插入 [Book1985 Part 3 & Part 5] | 单轴孔螺旋插入（间隙配合与过盈配合卡滞相图）、双轴孔柔性连接板大/小变形阶段卡滞分析 [Book2025 Ch.4 & Ch.5] | 从经验几何公差演进为多接触状态力学建模与卡滞边界解析 |
| **视觉与触觉感知** | 早期 2D/3D 工业视觉（Hitachi 3-D 视觉+力觉、Delft FLAIR、Hull 视觉引导功率二极管装配）与六维腕力传感器 [Book1985 Part 5] | **VA-Point-MVSNet** 多视角立体视觉、**PointFlow**、基于 FEM/IPC 的标记点视触觉仿真（**GelSight** 标记流 + PointNet 自编码器 + 物理/光学/任务域随机化 Sim2Real） [Book2025 Ch.2 & Ch.3] | 从结构光/二值视觉与单点力觉演进为稠密 3D 点云重建与高分辨率视触觉融合 |
| **编程与技能获取** | 显式机器人编程语言：**VAL-II**、**RAIL**、**SRL**、**ARL**、**FA-BASIC**、**MCP** 及关系型世界模型 **RODABAS** [Book1985 Part 4] | 示教学习 **LFD**（3D 视觉 + 高斯过程回归 **GPR** 变形补偿）与经验学习 **LFE**（**MDDPG**、**GVFs/VTSP**、**HRL**、**HC-CPS**） [Book2025 Ch.6–Ch.10] | 从人工硬编码轨迹与状态机演进为基于演示与强化学习的自主策略泛化 |
| **装配系统与本体** | 专用与通用装配本体：**PRAGMA A3000**、**SCARA** 家族、Hitachi 6-DOF 双连杆、**YESMAN** 协作机器人、**ASEA** 摆式机器人；IBM RS 7565、Flymo、Saab-Scania 产线 [Book1985 Part 1 & Part 2] | 面向非结构化/易变形/难测量精密部件的多传感闭环智能装配单元 [Book2025 Ch.1 & Ch.6] | 从高刚度重复定位产线演进为面向柔性、小批量、高不确定性任务的智能装配系统 |
| **面向装配的设计（DFA）与经济性** | 面向机器人装配的零件设计准则（小零件 DFA、IBM 分层装配/卡扣/倒角规范、IPA 面向装配连接目录）；**Miller 盈亏平衡资本成本 $Q$**、**Boothroyd** 通用机器人经济模型、**Redford/Lo/Killeen** 多臂供料成本模型 [Book1985 Part 3 & Part 6] | Sim2Real 迁移降低真机试错成本、少量交互样本高效的基于模型强化学习（MBRL）与分层策略复用 [Book2025 Ch.3, Ch.8–Ch.10] | 从硬件/工装与节拍经济性优化延伸至算法数据效率与跨任务迁移成本优化 |

---

## 2. 现代智能装配缩略词表（Book2025 pp. xv–xvi）

| 缩略词 | 英文全称 | 中文释义 | 对应章节 |
| :--- | :--- | :--- | :--- |
| **PiH** | Peg-in-Hole | 轴孔装配（典型精密接触装配基准任务） | 全书（Ch.1–Ch.11） |
| **MVS** | Multi-View Stereo | 多视角立体视觉 | Ch.1, Ch.2 |
| **VA-Point-MVSNet** | Visibility-Aware Point-based Multi-View Stereo Network | 可见性感知点云多视角立体网络 | Ch.2 |
| **FEM** | Finite Element Method | 有限元法（用于弹性体接触变形仿真） | Ch.3 |
| **IPC** | Incremental Potential Contact | 增量势能接触（无穿透高精度接触力学仿真框架） | Ch.3 |
| **Sim2Real** | Simulation-to-Reality | 仿真到现实迁移 | Ch.3 |
| **TD3** | Twin Delayed Deep Deterministic Policy Gradient | 双延迟深度确定性策略梯度 | Ch.3 |
| **LFD** | Learning from Demonstration | 示教学习 / 从演示中学习 | Ch.1, Ch.6 |
| **LFE** | Learning from Experience | 经验学习 / 从交互经验中学习（强化学习范式） | Ch.1, Ch.7–Ch.10 |
| **GPR** | Gaussian Process Regression | 高斯过程回归（用于易变形件位移/形变补偿） | Ch.6 |
| **RL** | Reinforcement Learning | 强化学习 | Ch.7–Ch.10 |
| **MDDPG** | Multi-step / Modified Deep Deterministic Policy Gradient | 面向轴孔装配的改进深度确定性策略梯度方法 | Ch.7 |
| **DDPG** | Deep Deterministic Policy Gradient | 深度确定性策略梯度 | Ch.7, Ch.8 |
| **DQN** | Deep Q-Network | 深度 Q 网络 | Ch.8 |
| **GVFs** | General Value Functions | 通用价值函数 | Ch.8 |
| **VTSP** | Value-based / Vision-Tactile State Prediction（模型预测状态表示） | 基于通用价值函数的状态预测框架 | Ch.8 |
| **FLDVTSP** | Fuzzy-Logic Driven VTSP | 模糊逻辑驱动的 VTSP 强化学习方法 | Ch.8 |
| **HRL** | Hierarchical Reinforcement Learning | 分层强化学习 | Ch.9 |
| **MDP** | Markov Decision Process | 马尔可夫决策过程 | Ch.7–Ch.10 |
| **HC-CPS** | Hierarchical Compliance Control via Policy Search | 基于策略搜索的分层柔顺控制 | Ch.10 |
| **VAE** | Variational Autoencoder | 变分自编码器（用于隐空间特征提取） | Ch.10 |
| **GMR-GP** | Gaussian Mixture Regression – Gaussian Process | 高斯混合回归与高斯过程复合前向动力学模型 | Ch.10 |

---

## 3. 经典工业装配核心术语与系统词典（Book1985）

| 术语 / 缩写 | 全称或来源 | 核心定义与工程意义 | 对应位置 |
| :--- | :--- | :--- | :--- |
| **SCARA** | Selective Compliance Assembly Robot Arm | 选择顺应性装配机械臂：水平面柔顺、垂直方向高刚度，由山梨大学牧野洋团队提出，适合垂直插入类装配 | Book1985 Part 1 |
| **PRAGMA A3000** | DEA (Digital Electronic Automation) 装配机器人 | 早期典型直角坐标多臂协同精密装配机器人系统 | Book1985 Part 1 |
| **YESMAN** | 协作型双臂装配机器人 | 日本早期面向复杂协同装配的双臂机器人系统 | Book1985 Part 1 |
| **DFA** | Design for Assembly | 面向装配的设计：通过减少零件数量、对称设计、防缠绕、分层自上而下装配、卡扣与倒角降低自动化装配难度 | Book1985 Part 3 |
| **IPA** | Fraunhofer IPA (Stuttgart) | 德国弗劳恩霍夫制造工程与自动化研究所，提出面向机器人装配的设计指南与连接方式目录 | Book1985 Part 3 |
| **VAL-II** | Unimation / PUMA 机器人编程语言 | 第二代结构化机器人语言，支持实时路径修正、传感器通信与并发监控 | Book1985 Part 4 |
| **RAIL** | Robot Automatix Incorporated Language | Automatix 推出的类 Pascal 高级机器人与视觉集成编程语言 | Book1985 Part 4 |
| **SRL** | Structured Robot Language | 卡尔斯鲁厄大学提出的结构化机器人语言，与关系数据库世界模型 RODABAS 配合使用 | Book1985 Part 4 |
| **RODABAS** | Robot Database System | 基于关系模型的机器人装配环境与工件几何/状态数据库 | Book1985 Part 4 |
| **ARL** | Assembly Robot Language | 装配机器人专用语言（Book1985 PDF p.53 / 书 p.35 包含完整横排语法定义表 Table 1） | Book1985 Part 1/4 |
| **RCC** | Remote Center Compliance | 远心柔顺装置：通过弹性连杆机构将柔顺中心投影到轴端，使侧向力只产生平移、力矩只产生旋转，消除卡滞 | Book1985 Part 5 |
| **FLAIR** | Flexible Assembly Industrial Robot Cell (Delft) | 荷兰代尔夫特理工大学研发的多传感柔性装配工作站 | Book1985 Part 5 |
| **Breakeven Capital Cost ($Q$)** | Miller 装配经济模型 | 自动化装配系统在给定投资回收期、班次、人工成本与年产量下所能承受的盈亏平衡资本投入上限 | Book1985 Part 6 |
