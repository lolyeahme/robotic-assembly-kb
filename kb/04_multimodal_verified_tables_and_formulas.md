# 多模态视觉高精度精修：疑难横排表格、核心公式与算法基准（Book1985 + Book2025）

本文件由多模态视觉直接审阅原书高清扫描页与排版页精修而成，专门修复常规 OCR 无法识别的 **90° 旋转横排宽表、竖排表头矩阵、复杂 LaTeX 数学公式与关键实验数据表**。

---

## 1. Book1985 PDF 第 53 页（书 p.35）Table 1: Outline of Program Grammar (ARL)

> 原页为 90° 逆时针旋转横排宽表，传统 OCR 输出完全乱码。以下为视觉转正后逐行还原的 Hitachi **ARL（Assembly Robot Language）** 核心语法表（注：位置常量在示教阶段替换为实际坐标值）。

| Category | Instruction | Format |
| :--- | :--- | :--- |
| **Motion instruction** | move | `MOVE interpolation_method { [midpoint,...] / point_group } target_point [, option]` |
| **Motion instruction** | drive on joint | `DRIV joint_no., { absolute_angle / relative_angle }` |
| **End-effector instruction** | change | `CHG end_effector_no.` |
| **End-effector instruction** | definition | `HAND end_effector_no. [, parameter]` |
| **Program flow control** | Repetition | `FOR variable = { variable / constant }, { variable / constant }` ... `END` |
| **Program flow control** | conditional branch | `IF { variable / I/O_variable } [ { comparative_operator / logic_operator } { variable / I/O_variable } ] THEN ~ ELSE ~` |
| **Program flow control** | repetition with conditional branch | `WHILE { variable / I/O_variable } [ { comparative_operator / logic_operator } { variable / I/O_variable } ]` ... `END` |
| **Program flow control** | simple branch | `GOTO label` |
| **Program flow control** | conditional wait | `WAIT I/O_variable [ { comparative_operator / logic_operator } { variable / I/O_variable } ]` |
| **Program flow control** | subroutine branch | `CALL name [(parameter [, parameter, ...])]` |
| **Others** | timer wait | `DELAY { Variable / Constant }` |
| **Others** | substitution | `{ variable / I/O_variable } = { variable / I/O_variable / constant } [ { arithmetic_operator / logic_operator } { variable / I/O_variable / constant } ]` |
| **Others** | position definition | `position_variable = { position_variable / position_constant } + (DX, DY, DZ)` |

---

## 2. Book1985 PDF 第 199 页（书 p.181）Table 2: Technical/Economic Comparison of Joining Techniques (IPA)

> 原页列标题为 90° 竖排文字，传统 OCR 丢失全部列头。评分说明：`1 = most favourable（最有利）`，`2 = favourable（有利）`，`3 = good（良好）`。

| Joining techniques | Strength | Assembly cost | Design | Reliability | Visual inspection | Ease of maintenance | Alignment accuracy | Flexible alignment | Small parts | Large parts |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Screwing** | 1 | 3 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 1 |
| **Resistance welding** | 1 | 1 | 2 | 3 | 3 | 3 | 3 | 1 | 1 | 1 |
| **Arc welding** | 1 | 2 | 2 | 1 | 2 | 2 | 3 | 1 | 3 | 1 |
| **Hard soldering** | 1 | 3 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 1 |
| **Rivetting** | 1 | 2 | 2 | 1 | 1 | 3 | 1 | 3 | 3 | 1 |
| **Notching** | 3 | 1 | 3 | 2 | 1 | 3 | 1 | 3 | 2 | 3 |
| **Overlapping** | 2 | 1 | 1 | 1 | 1 | 3 | 3 | 2 | 1 | 3 |
| **Bonding by adhesives** | 3 | 2 | 1 | 2 | 3 | 3 | 3 | 1 | 1 | 2 |
| **Special joining elements** | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 3 | 1 |

---

## 3. Book1985 核心力控与装配经济学精准公式集

### 3.1 Simons & Van Brussel 端阻抗与柔顺控制方程 [Book1985 pp.258–261 / PDF pp.276–279]
- 机械结构阻抗：$F = Z_R (X_R - X_C)$
- 伺服控制器阻抗：$F = Z_S (X_C - X_S)$
- 主动控制反馈阻抗：$F = Z_A (X_S - X_P)$
- 总端阻抗串联关系：
  $$Z_E^{-1} = Z_A^{-1} + Z_S^{-1} + Z_R^{-1}$$
- 实阻抗下真实位置与编程位置关系：$X_R = X_P + C F$（$C$ 为末端柔顺矩阵）
- 自适应被动顺应（Adaptable Passive Accommodation）关节刚度矩阵映射：
  $$K_J = J^\top K_E J$$

### 3.2 Miller 盈亏平衡资本成本 $Q$ 表 [Book1985 p.320 / PDF p.338, Table 1]
| 参数 / 运行年限 | Case A | Case B | Case C | Case D |
| :--- | :---: | :---: | :---: | :---: |
| Discount rate (%) | 10 | 10 | 15 | 15 |
| Annual wage inflation (%) | 5 | 5 | 15 | 15 |
| Capital writing down period (years) | 8 | 4 | 8 | 4 |
| **1 年运行 Multiplier $Q$** | 1.58 | 1.44 | 1.50 | 1.38 |
| **2 年运行 Multiplier $Q$** | 2.69 | 2.34 | 2.58 | 2.27 |
| **3 年运行 Multiplier $Q$** | 3.55 | 2.99 | 3.47 | 3.00 |
| **4 年运行 Multiplier $Q$** | 4.25 | 3.53 | 4.26 | 3.65 |

### 3.3 Boothroyd 通用装配机器人经济模型核心方程 [Book1985 pp.336–343 / PDF pp.354–361]
- 自动供料单件成本（Eq. 1–3）：
  $$CSA = CF \times CR \times TAT = 0.014 \times CF \times TAT / PS, \quad CR = 0.014 / PS \text{ (cents/k\$s)}$$
- 人工装料料仓成本（Eq. 4–5）：
  $$CSM = CM \times CR \times TAT + TM \times OP = 0.014 \times CM \times TAT / PS + 0.7 \text{ (cents)}$$
- 单工位单臂与双臂系统设备总成本（Eq. 6–7，单位 k\$）：
  $$CET(1) = 110 + 5.07 \times NP, \quad CET(2) = 165 + 5.97 \times NP$$
- 不良件停机时间与基础装配成本方程（Eq. 8–9）：
  $$TDA = XP \times NP \times TD, \quad CST = (TAT + TDA) \times CET \times CR + (TOT + TDA) \times OP$$
- 单臂与双臂单工位单件装配成本（Eq. 10–11，单位 cents/part）：
  $$CST(1)/NP = (8.84 + 0.41 \times NP)/PS + 0.48$$
  $$CST(2)/NP = (8.99 + 0.32 \times NP)/PS + 0.48$$
- 多工位自由传送系统设备总成本与单件成本（Eq. 14 & Eq. 17）：
  $$CET(T) = (11.4 + 78.5 \times VS) \times NP$$
  $$CST(T)/NP = (6.13 + 0.89/VS)/PS + 0.23/(NP \times VS) + 0.24$$
- 核心决策阈值：在回收期 $PS = 6$ 班年下，单班年产量低于约 40,000 件时机器人装配通常不经济；单工位系统零件数超过约 22 个时经济性劣于人工；年产 160,000–500,000 件时多工位自由传送系统最经济。

---

## 4. Book2025 核心数学公式与关键实验基准精修

### 4.1 Ch.2 VA-Point-MVSNet（Book2025 pp.31–42）
- 可见性感知方差聚合（`vis-var`, Eq. 2.2）：
  $$\mathbf{C} = \frac{\sum_{i=0}^N (\omega_i \cdot \mathbf{F}_i^2)}{\sum_{i=0}^N \omega_i} - \left(\frac{\sum_{i=0}^N (\omega_i \cdot \mathbf{F}_i)}{\sum_{i=0}^N \omega_i}\right)^2$$
- PointFlow 深度残差期望（Eq. 2.7）：$\Delta d_p = \mathbf{E}(ks) = \sum_{k=-m}^{m} ks \times \mathrm{Prob}(\tilde{\mathbf{p}}_k)$
- DTU 评估集最优结果（Table 2.4）：`Ours-"vis-max"` 达到 **Acc = 0.359 mm, Comp = 0.358 mm, Overall = 0.359 mm**，全面优于 MVSNet（Overall 0.462 mm）和 R-MVSNet（Overall 0.417 mm）。

### 4.2 Ch.3 视触觉 Sim2Real（Book2025 pp.55–70）
- 针孔相机投影（Eq. 3.4）：$[u_i', v_i', 1]^\top = \frac{1}{z_i'} \mathbf{K} [x_i', y_i', z_i']^\top$
- 单调插入（Monotone Insertion）Sim2Real 对比（Table 3.2）：
  - **Sim2Real (Ours, FEM+IPC+PointNet+TD3+DR)**：成功率 **$95.08 \pm 2.70\%$**，尝试次数 **$3.55 \pm 0.19$**（Sim2Sim 为 $94.50 \pm 3.20\%$，Sim2Real 鸿沟极小）。
  - **Sim2Real (Rigid-body baseline [20])**：成功率仅 **$46.33 \pm 4.96\%$**，尝试次数 $4.09 \pm 0.26$。
- 域随机化消融（Table 3.4）：全三域随机化 $95.08\%$；去物理域降至 $80.70\%$；去任务域降至 $61.57\%$；去光学域（未对齐）骤降至 $10.01\%$。

### 4.3 Ch.4 单轴孔螺旋插入与减阻公式（Book2025 pp.80–104）
- 螺旋节距与等效轴向/切向摩擦系数（Eqs. 4.1, 4.9, 4.10）：
  $$h = \frac{v_a}{w}, \quad \mu_a = \frac{h}{\sqrt{h^2 + r^2}}\mu, \quad \mu_t = \frac{r}{\sqrt{h^2 + r^2}}\mu$$
- 卡滞四边形可行域面积（Eq. 4.24）：$S = \frac{4\lambda}{\mu}$；因 $\mu_a < \mu$ 且 $\lambda_a > \lambda$，故 $S_{\text{screw}} > S_{\text{linear}}$，显著降低卡滞概率。
- 往复螺旋插入三大工程约束（Eqs. 4.29, 4.30, 4.32）：
  $$\theta_{\text{screw}} \le k_m \frac{\delta}{d}, \quad f_{\text{screw}} = \frac{w}{\theta_{\text{screw}}} \le k_i f_r, \quad \frac{r}{h} \ge \sqrt{\frac{1 - k_f^2}{k_f^2}}$$
- 过盈配合（弹性轴+刚性孔）摩擦扳手节距（Eq. 4.39）：$h_w = \frac{m_t}{f_a} = \frac{r_h^2}{h}$。

### 4.4 Ch.5 双轴孔柔性板卡滞分析（Book2025 pp.105–120）
- 几何变形角约束（Eq. 5.4）：$\theta_{c1} = \arccos(d/D)$，$\theta_{c2} \approx \arcsin((D-d)/2h)$。
- 卡滞因子动态调节律（p.114）：当处于卡滞区且 $l_2 > l_1$ 时，$J_f = J_{f\min} + (1 - J_{f\min})(l_1/l_2)$，用 $J_f K_{pz}$ 减缓 $z$ 向推进并用 $K_{pxy}/J_f$ 加速 $x,y$ 向脱困；50 次真机实验成功率 **100%**（间隙 0.04 mm）。

### 4.5 Ch.6–Ch.10 学习控制核心公式（Book2025 pp.123–227）
- **Ch.6 LFD 最优孔轴闭式解（Eq. 6.5）**：$\mathbf{v}_h = (\mathbf{V}_p^\top \mathbf{V}_p)^{-1}\mathbf{V}_p^\top \cos\phi$；GPR 真机位置补偿误差 10–20 $\mu$m，满足 40 $\mu$m 间隙装配。
- **Ch.7 MDDPG 动作修正（Eq. 7.5–7.6）**：$u_t^e = \mathbf{K}_p \circ (\mathcal{F}_t - \mathcal{F}_r)$，$u_t = u_t^e \circ a_t + u_t^e$；双层模糊奖励将 625 条规则压缩至 75 条。
- **Ch.8 GVFs 与 FLDVTSP（Eq. 8.3 & 8.16）**：$v_\pi^G(s_t) = \mathbb{E}_\pi\left[\sum_{k=t}^T C_{t+1} \prod_{i=t+1}^k \gamma(s_i) \mid s_t, C_t, \gamma\right]$；FLDVTSP-DQN 较普通 DQN 减少装配时间约 44%，FLDVTSP-DDPG 较普通 DDPG 减少约 24%。
- **Ch.9 HRL Softmax 门控（Eq. 9.4）**：$\pi_O(o \mid s) = \frac{\exp(Q_O^\pi(s, o))}{\sum_{o' \in O}\exp(Q_O^\pi(s, o'))}$，双增广 MDP 离线同源采样（Algorithm 9.1）。
- **Ch.10 HC-CPS（Eq. 10.5 & 10.17–10.21）**：VAE 隐空间约束降低离线外推误差，GMR-GP 复合前向模型（分离位姿模型与接触力模型）使力预测 RMSE 较端到端 GP 降低约 **30%**（Table 10.1）。
