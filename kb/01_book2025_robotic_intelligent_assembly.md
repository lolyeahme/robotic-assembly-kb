# 《Robotic Intelligent Assembly》(2025) 工程知识库

- **书名**：*Robotic Intelligent Assembly*
- **作者**：Jing Xu, Hao Su, Rui Chen, Zhimin Hou
- **出版社**：Springer / Huazhong University of Science and Technology Press（*Research on Intelligent Manufacturing* 丛书）
- **出版年份**：2025（共 246 PDF 页，11 章）
- **DOI**：`https://doi.org/10.1007/978-981-96-2657-1`

---

## Chapter 1: Introduction（绪论与轴孔装配系统综述） [Book2025 Ch.1]

### 核心问题与系统框架
本章以工业制造中最具代表性的**轴孔装配（Peg-in-Hole, PiH）**为核心基准任务，系统梳理了机器人智能装配从“感知—建模—学习—控制”的完整技术链条。传统工业机器人依赖高精度定位与专用夹具，难以应对零件公差波动、柔性形变、遮挡以及复杂接触非线性问题。

### 五大技术方向综述
1. **多视角立体视觉（MVS）感知**：在反光、弱纹理与遮挡工业场景中重建精密工件三维几何与位姿。
2. **视触觉感知与 Sim2Real 仿真**：通过高分辨率弹性体触觉传感器（如 GelSight）获取局部接触力场与微滑移，并借助高保真仿真解决真机数据采集昂贵问题。
3. **基于模型的装配策略（Model-Based）**：建立单轴孔与双轴孔装配的准静态/动力学接触力学模型，推导卡滞（Jamming）与楔紧（Wedging）边界条件。
4. **示教学习（LFD）**：通过人工示范轨迹结合视觉/力觉反馈与非参数回归（如 GPR）实现易变形、难测量工件的快速技能迁移。
5. **经验学习（LFE / 强化学习）**：利用无模型 RL、基于模型 RL、分层 RL 与分层柔顺策略搜索，在未知动力学环境中自主探索最优插入策略。

---

## Chapter 2: Multi-View Stereo Sensing Method（多视角立体视觉感知方法） [Book2025 Ch.2]

### 技术痛点
在精密装配场景中，金属零件常存在高反光、弱纹理与自遮挡，传统基于规则体素代价体（Cost Volume）的 MVS 方法显存开销大，且在遮挡区域易产生深度估计漂移。

### 核心方法：VA-Point-MVSNet 与 PointFlow
- **点云级联优化架构**：先通过低分辨率深度图初始化粗略三维点云，再在三维点空间中进行迭代细化，避免构建高分辨率 3D 规则体素网格带来的立方级显存爆炸。
- **可见性感知（Visibility-Aware, VA）机制**：在多视角特征聚合时引入视角可见性权重，自动抑制被遮挡视角或高光异常视角的特征贡献，提高金属与复杂结构装配体的深度估计鲁棒性。
- **PointFlow 模块**：沿每个点法向/深度方向动态预测残差位移流，实现亚毫米级三维几何重建，为下游精密对准与位姿估计提供稠密点云输入。

---

## Chapter 3: General-Purpose Sim2Real Protocol for Marker-Based Visuotactile Sensing（基于标记点的视触觉通用 Sim2Real 协议） [Book2025 Ch.3]

### 架构与物理仿真核心
面向 GelSight 类基于标记点（Marker-Based）的视触觉传感器，本章提出一套端到端的通用 Sim2Real 协议，打通“物理接触仿真 → 光学图像渲染 → 特征对齐 → 强化学习策略零样本迁移”全流程：
- **高精度接触力学仿真（FEM + IPC）**：采用**有限元法（FEM）**模拟硅胶弹性体的大变形，并结合**增量势能接触（Incremental Potential Contact, IPC）**保证在任意大步长与复杂接触几何下无网格穿透（Intersection-free），精确计算标记点三维位移流（Marker Flow）。
- **紧凑表征学习（PointNet Autoencoder）**：将高维标记点位移场输入基于 PointNet 的自编码器，提取对局部几何与切向/法向力分布敏感的低维隐向量，降低强化学习策略网络的输入维度。
- **三层域随机化（Domain Randomization）**：
  1. **物理域随机化**：随机化弹性体杨氏模量、泊松比、摩擦系数与接触刚度。
  2. **光学域随机化**：随机化光照方向、相机畸变、标记点检测噪声与背景扰动。
  3. **任务域随机化**：随机化零件尺寸公差、初始位姿误差与装配孔隙。
- **策略训练与迁移**：在仿真中采用 **TD3（Twin Delayed DDPG）** 算法结合触觉隐特征训练插孔/对准策略，并直接零样本（Zero-shot）迁移至真实机器人与真实 GelSight 传感器。

---

## Chapter 4: Model-Based Strategies — Screw Insertion for Single PiH Assembly（基于模型的单轴孔螺旋插入策略） [Book2025 Ch.4]

### 力学建模与装配模式
针对单轴孔精密装配中的**间隙配合（Clearance-fit）**与**过盈配合（Interference-fit）**两种工况，本章分析螺旋插入（轴向推进与绕轴旋转耦合）对降低插入力和规避卡滞的机理：
- **接触状态划分**：涵盖单点接触、两点接触以及插入深度递增过程中的力/力矩平衡方程。
- **卡滞相图（Jamming Diagrams）**：在广义力比空间（如侧向力/轴向力 $F_x / F_z$ 与倾覆力矩/轴向力 $M_y / (r F_z)$）中解析刻画**无卡滞安全区**与**卡滞边界**。
- **螺旋插入减阻机制**：施加绕轴旋转角速度使接触点相对运动方向由纯轴向转为螺旋切向，从而将部分摩擦力分量转移至切向，显著降低沿轴向的有效摩擦阻力分量，扩大无卡滞可行域，尤其对高摩擦或微过盈装配效果显著。

---

## Chapter 5: Model-Based Strategies — Jamming Analysis for Dual PiH Assembly（基于模型的双轴孔卡滞分析） [Book2025 Ch.5]

### 结构特征与多阶段变形建模
工业装配中大量存在带**柔性连接板（Flexible Connecting Plate）**的双轴孔（Dual PiH）组件。与刚性单轴孔相比，双轴之间存在几何耦合与结构弹性变形：
- **双阶段变形分析**：
  - **大变形阶段（Large Deformation Stage）**：连接板受初始偏心与倾角影响产生显著弯曲/扭转弹性形变，需采用非线性弹性力学描述两轴的相对位姿耦合。
  - **小变形阶段（Small Deformation Stage）**：双轴进入孔内较深位置后，几何约束收紧，系统进入线性小变形主导阶段。
- **多接触组合卡滞判据**：系统枚举双轴在各自孔内的多点接触组合状态，推导联立静力平衡与库仑摩擦不等式约束，给出双轴孔的全局卡滞条件与柔顺补偿方向，为机械臂末端力控调节提供解析依据。

---

## Chapter 6: LFD for Hard-Measuring Easy-Deformation PiH Assembly（面向难测量易变形轴孔装配的示教学习） [Book2025 Ch.6]

### 问题特征
对于柔性电缆插头、薄壁或弹性体连接件等**难测量（Hard-Measuring）且易变形（Easy-Deformation）**工件，装配过程中零件自身发生未知弯曲或扭转，导致仅靠刚体运动学无法准确对齐。

### 方法流程
1. **3D 视觉粗定位与引导**：利用三维视觉传感器获取柔性件与目标孔的初始相对位姿，完成接近阶段的粗对准。
2. **基于高斯过程回归（GPR）的变形补偿**：在人工示教采集的力/位姿/视觉历史数据上训练 **GPR** 非参数模型，学习接触力与柔性体端部位移偏差之间的非线性映射，并利用 GPR 输出的后验均值进行在线位姿补偿、利用后验方差量化不确定性。
3. **卡滞检测与恢复（Jam Handling）**：结合末端六维力/力矩阈值与方向特征在线识别异常卡滞状态，触发局部回退与微调恢复动作，确保易变形件在不损伤的前提下完成装配。

---

## Chapter 7: LFE — Model-Free RL Method for PiH Assembly（基于无模型强化学习的轴孔装配） [Book2025 Ch.7]

### 核心挑战
在真实机器人上进行无模型强化学习（Model-Free RL）面临三大瓶颈：稀疏奖励导致探索效率低、连续动作空间随机探索易引发过大接触力损坏工件、状态-动作维度耦合导致收敛慢。

### 关键技术：MDDPG + 双层模糊奖励 + 反馈探索
- **MDDPG 算法**：基于深度确定性策略梯度（DDPG）改进的连续控制架构，输入机器人末端位姿与六维力/力矩状态，输出末端增量位移/柔顺控制指令。
- **双层模糊奖励系统（Two-Layer Fuzzy Reward System）**：替代生硬的手工分段线性奖励，利用模糊规则将“插入深度进度、接触力/力矩安全性、偏心误差”融合为平滑稠密奖励信号，兼顾装配成功率与接触力柔顺性。
- **反馈探索策略（Feedback Exploration）**：在探索噪声中引入接触力安全反馈约束，当接触力趋近安全上限时抑制危险方向的随机探索，提升真机训练安全性与样本效率。

---

## Chapter 8: LFE — Model-Based RL for PiH Assembly（基于模型的强化学习轴孔装配） [Book2025 Ch.8]

### 核心思想
为了显著减少真实机器人与环境的物理交互次数，本章构建基于模型的强化学习（Model-Based RL）框架，通过学习环境状态转移与预测值函数来指导策略优化。

### 核心组件与算法（Algorithms 8.1 & 8.2）
- **通用价值函数（General Value Functions, GVFs）**：不仅预测单一标量累积奖励，还并行预测多维物理观测量（如未来时刻的接触力、力矩与深度变化趋势），构成丰富的预测性状态表征。
- **VTSP 与 FLDVTSP-DQN / DDPG**：结合模糊逻辑与 VTSP 状态预测框架，分别在离散动作空间（DQN 变体，Algorithm 8.1）和连续动作空间（DDPG 变体，Algorithm 8.2）中实现高样本效率的轴孔插入学习，在少量真机回合内即可收敛至稳定插入策略。

---

## Chapter 9: LFE — Hierarchical RL Method for PiH Assembly（基于分层强化学习的轴孔装配） [Book2025 Ch.9]

### 分层分解动机
复杂轴孔装配包含多个物理特性迥异的子阶段（如自由空间接近、表面搜孔、倒角对准、孔内柔顺插入），单一扁平策略网络难以同时兼顾粗定位与精密力控。

### 双增广 MDP 与 Softmax 门控策略（Algorithm 9.1）
- **两层增广 MDP（Two Augmented MDPs）**：
  - **底层策略（Sub-policies / Skills）**：针对特定接触子任务学习专门化的运动/力控原语。
  - **高层策略（Gating Policy）**：基于当前全局状态与接触特征，通过 **Softmax 门控机制（Softmax Gating Policy）** 动态计算各底层子策略的激活权重，实现子阶段间的平滑切换与组合。
- **工程优势**：在跨孔径、跨间隙或不同初始偏差条件下，分层架构比单层 RL 具有更强的泛化能力和可解释性（Algorithm 9.1 给出完整交替训练伪代码）。

---

## Chapter 10: LFE — Hierarchical Compliance Control for PiH Assembly（分层柔顺控制策略搜索 HC-CPS） [Book2025 Ch.10]

### 核心框架：HC-CPS（Algorithm 1）
传统力/位混合控制或固定参数阻抗控制难以适应装配全过程刚度需求的剧烈变化。本章提出**分层柔顺控制策略搜索（Hierarchical Compliance Control via Policy Search, HC-CPS）**：
- **阻抗条件动作空间（Impedance-Conditioned Action Space）**：策略不仅输出目标轨迹增量，还同步输出阻抗控制器的刚度（Stiffness）与阻尼（Damping）参数，使机器人在自由接近阶段保持较高刚度、在强接触阶段自动柔顺化。
- **VAE 隐空间压缩**：利用变分自编码器（VAE）对高维多模态感知序列（位姿 + 力/力矩）进行降维与去噪编码。
- **GMR-GP 复合前向动力学模型**：结合高斯混合回归（GMR）的全局多模态拟合能力与高斯过程（GP）的局部非线性残差建模及不确定性估计，构建高精度接触动力学前向模型，在模型内部进行策略评估与优化，极大降低真实硬件交互次数与碰撞风险。

---

## Chapter 11: Concluding Remarks（总结与展望） [Book2025 Ch.11]

### 核心结论与未来方向
全书从感知（MVS + 视触觉 Sim2Real）、机理（单/双轴孔力学与卡滞分析）到智能学习控制（LFD + Model-Free/Model-Based/Hierarchical RL + HC-CPS）构成了机器人智能装配闭环体系。未来关键挑战包括：
- 面向复杂异形/多部件长时序装配的通用基础模型与技能组合；
- 高保真多物理场仿真（刚柔耦合 + 光学触觉）与更低成本的 Sim2Real 迁移；
- 面向工业产线部署的安全性验证、实时性与跨产线零样本泛化。
