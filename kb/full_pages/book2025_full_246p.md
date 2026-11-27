# Robotic Intelligent Assembly (2025) — Full Page-by-Page Text Corpus

> Source PDF: `Robotic Intelligent Assembly (Jing Xu, Hao Su, Rui Chen, Zhimin Hou) (z-library.sk, 1lib.sk, z-lib.sk).pdf` | Total PDF pages: 246

> Extraction track: Poppler `pdftotext` UTF-8 verbatim page-indexed extraction paired with multimodal visual overrides in `04_multimodal_verified_tables_and_formulas.md`.

## [Book2025 PDF p.1] Page 1

Research on Intelligent Manufacturing

Jing Xu · Hao Su ·
Rui Chen · Zhimin Hou

Robotic Intelligent
Assembly

## [Book2025 PDF p.2] Page 2

Research on Intelligent Manufacturing
Editors-in-Chief
Han Ding, Huazhong University of Science and Technology, Wuhan, China
Ronglei Sun, Huazhong University of Science and Technology, Wuhan, China
Series Editors
Kok-Meng Lee, Georgia Institute of Technology, Atlanta, USA
Cheng’en Wang, School of Mechanical Engineering, Shanghai Jiao Tong
University, Shanghai, China
Yongchun Fang, College of Computer and Control Engineering, Nankai University,
Tianjin, China
Yusheng Shi, School of Materials Science and Engineering, Huazhong University
of Science and Technology, Wuhan, China
Hong Qiao, Institute of Automation, Chinese Academy of Sciences, Beijing, China
Shudong Sun, School of Mechanical Engineering, Northwestern Polytechnical
University, Xi’an, China
Zhijiang Du, State Key Laboratory of Robotics and System, Harbin Institute of
Technology, Harbin, China
Dinghua Zhang, School of Mechanical Engineering, Northwestern Polytechnical
University, Xi’an, China
Xianming Zhang, School of Mechanical and Automotive Engineering, South China
University of Technology, Guangzhou, China
Dapeng Fan, College of Mechatronic Engineering and Automation, National
University of Defense Technology, Changsha, China
Xinjian Gu, School of Mechanical Engineering, Zhejiang University, Hangzhou,
China
Bo Tao, School of Mechanical Science and Engineering, Huazhong University of
Science and Technology, Wuhan, China
Jianda Han, College of Artificial Intelligence, Nankai University, Tianjin, China
Yongcheng Lin, College of Mechanical and Electrical Engineering, Central South
University, Changsha, China
Zhenhua Xiong, School of Mechanical Engineering, Shanghai Jiao Tong
University, Shanghai, China

## [Book2025 PDF p.3] Page 3

Research on Intelligent Manufacturing (RIM) publishes the latest developments
and applications of research in intelligent manufacturing—rapidly, informally and
in high quality. It combines theory and practice to analyse related cases in fields
including but not limited to:
Intelligent design theory and technologies
Intelligent manufacturing equipment and technologies
Intelligent sensing and control technologies
Intelligent manufacturing systems and services
This book series aims to address hot technological spots and solve challenging problems in the field of intelligent manufacturing. It brings together scientists and engineers working in all related branches from both East and West, under the support of
national strategies like Industry 4.0 and Made in China 2025. With its wide coverage
in all related branches, such as Industrial Internet of Things (IoT), Cloud Computing,
3D Printing and Virtual Reality Technology, we hope this book series can provide
the researchers with a scientific platform to exchange and share the latest findings,
ideas, and advances, and to chart the frontiers of intelligent manufacturing.
The series’ scope includes monographs, professional books and graduate textbooks, edited volumes, and reference works intended to support education in related
areas at the graduate and post-graduate levels.

## [Book2025 PDF p.4] Page 4

Jing Xu · Hao Su · Rui Chen · Zhimin Hou

Robotic Intelligent Assembly

## [Book2025 PDF p.5] Page 5

Jing Xu
Department of Mechanical Engineering
Tsinghua University
Beijing, China
Rui Chen
Department of Mechanical Engineering
Tsinghua University
Beijing, China

Hao Su
Department of Computer Science
and Engineering
University of California
San Diego, CA, USA
Zhimin Hou
Mechanical and Aerospace Engineering
North Carolina State University
Raleigh, NC, USA

ISSN 2523-3386
ISSN 2523-3394 (electronic)
Research on Intelligent Manufacturing
ISBN 978-981-96-2656-4
ISBN 978-981-96-2657-1 (eBook)
https://doi.org/10.1007/978-981-96-2657-1
Jointly published with Huazhong University of Science and Technology Press
The print edition is not for sale in China (Mainland). Customers from China (Mainland) please order the
print book from: Huazhong University of Science and Technology Press.
© Huazhong University of Science and Technology Press 2025
This work is subject to copyright. All rights are solely and exclusively licensed by the Publisher, whether
the whole or part of the material is concerned, specifically the rights of reprinting, reuse of illustrations,
recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or
information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar
methodology now known or hereafter developed.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication
does not imply, even in the absence of a specific statement, that such names are exempt from the relevant
protective laws and regulations and therefore free for general use.
The publishers, the authors, and the editors are safe to assume that the advice and information in this book
are believed to be true and accurate at the date of publication. Neither the publishers nor the authors or
the editors give a warranty, express or implied, with respect to the material contained herein or for any
errors or omissions that may have been made. The publishers remain neutral with regard to jurisdictional
claims in published maps and institutional affiliations.
This Springer imprint is published by the registered company Springer Nature Singapore Pte Ltd.
The registered company address is: 152 Beach Road, #21-01/04 Gateway East, Singapore 189721,
Singapore
If disposing of this product, please recycle the paper.

## [Book2025 PDF p.6] Page 6

Foreword

Robotic assembly is a fundamental technique in a wide range of manufacturing
processes. While the classical rule-based robotic assembly methods have reached
an elevated level of maturity, they have limitations when it comes to handling
complex tasks with a large variety of components, which significantly restricts their
applications.
Fortunately, in the past decade, deep learning and artificial intelligence have undergone transformative breakthroughs, showcasing remarkable success across various
domains such as computer vision and natural language processing. These data-driven
approaches have demonstrated great generalizability and have paved the way for
significant advancements in robotic assembly by improving the robot capability of
perception, planning and control to meet the requirement of increasing complexity
and variety of assembly tasks.
This book is devoted to presenting the latest advances in robotic intelligent
assembly strategies, with a focus on pig-in-hole tasks. The book covers a range
of perspectives related to robotic PiH assembly strategies, including perception,
model-based control, and learning-based control. The authors have put great effort
into organizing previous research works in a systematic manner, offering readers a
comprehensive understanding of the field.
The first part of the book introduces the background and drawbacks of existing
approaches. The second part delves into improving the accuracy and computational
efficiency of learning-based multi-view stereo and narrowing the simulation-toreality domain gap for depth sensors. These techniques improve the robot’s ability
to perceive the geometry information of the assembly environment. The third part
describes the model-based strategies. And the fourth part presents state-of-the-art
learning-based strategies for general PiH tasks. These approaches enhance the generalizability of robot assembly by utilizing learning-based algorithms. By leveraging
the power of deep learning, robots can adapt to new assembly scenarios and handle
a wider range of components efficiently. The authors also explore techniques for
accelerating the training process of existing learning algorithms, enabling faster
deployment and improved performance.

v

## [Book2025 PDF p.7] Page 7

vi

Foreword

The outcome of this book is a comprehensive treatise that establishes significant advances in the theoretical formulation and experimental validation of robotic
assembly techniques. By leveraging the power of deep learning and artificial intelligence, the authors have made substantial contributions to the field. This book serves as
a vivid signature, showcasing the remarkable progress in robotic intelligent assembly
and inspiring future advancements in the field.
Hong Kong, China

Ning Xi

## [Book2025 PDF p.8] Page 8

Preface

Over a decade ago, we embarked on tackling one of the most fundamental yet challenging tasks in manufacturing—the robot assembly at a time when reinforcement
learning (RL) methods were not yet well-developed or widely adopted.
Our initial efforts focused on developing models to accurately represent the intricate contact status between the peg and the hole during insertion. We reasoned that
by precisely capturing and recognizing this critical contact status, we could adjust the
peg’s movements accordingly and accomplish the assembly task. The model-based
approaches offered the advantages of efficiency and explainability.
However, as our research progressed, we gradually uncovered the limitations of
this methodology. Complex contact scenarios involving multiple points of interaction and substantial variability in real-world conditions posed significant challenges
that our models struggled to accommodate. It became evident that a paradigm shift
was necessary to overcome these bottlenecks and achieve robust, adaptive assembly
capabilities.
Consequently, we pivoted our focus towards learning-based strategies, embracing
the power of reinforcement learning to derive optimal policies from data and experience. Unlike the vast body of work on RL in simulation environments or video
games, two critical factors emerged as paramount for the successful adoption of RL
in PiH tasks on physical robots: safety and sample efficiency. Any learning algorithm
deployed in a real manufacturing setting must ensure the safety of the equipment and
components, while also minimizing the need for costly trial-and-error during the
training phase.
To address these challenges, we delved into the study of impedance-conditioned
actions and hierarchical RL techniques. By incorporating compliant control and
hierarchies of low-level policies, our methods demonstrated the ability to learn
intricate insertion strategies that could successfully handle complex contact situations. Experimental validations on real PiH tasks verified the efficacy of our
approaches, accomplishing these intricate assembly tasks with remarkable efficiency
and reliability.
Despite these promising results, we recognize that there remain opportunities for
further advancement. Aspects such as the autonomous discovery and definition of
vii

## [Book2025 PDF p.9] Page 9

viii

Preface

low-level policies, seamless integration with higher-level task planners, and generalization to diverse manufacturing scenarios warrant continued investigation. Our
team remains committed to exploring these fundamental scientific problems, driven
by the ambition to push the boundaries of intelligent robotic systems.
Beijing, China
June 2024

Jing Xu
Rui Chen

## [Book2025 PDF p.10] Page 10

Contents

1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Robotic Peg-in-Hole Assembly System . . . . . . . . . . . . . . . . . . . . . .
1.2.1 Manipulators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.2 Mating Parts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.3 Sensing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.4 Assembly Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.1 Multi-view Stereo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.2 Tactile Sensor Simulation . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.3 Model-Based Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.4 Learning from Demonstrations . . . . . . . . . . . . . . . . . . . . .
1.3.5 Learning From Environments . . . . . . . . . . . . . . . . . . . . . . .
1.4 Scientific Goals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.5 Book Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

1
1
2
3
3
3
4
4
5
6
7
10
14
17
17
18

2

Multi-view Stereo Sensing Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1 Visibility-Aware Feature Aggregation . . . . . . . . . . . . . . . .
2.2.2 Coarse Depth Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.3 2D-3D Feature Lifting . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.4 PointFlow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.5 Training Loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.1 Experiments on Synthetic Data . . . . . . . . . . . . . . . . . . . . .
2.3.2 Experiments on DTU Benchmark . . . . . . . . . . . . . . . . . . .

27
27
29
29
32
33
34
36
36
37
40

ix

## [Book2025 PDF p.11] Page 11

x

Contents

2.3.3 Network Design Analysis . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.4 Generalizability of the PointFlow Module . . . . . . . . . . . .
2.4 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3

4

General-Purpose Sim2Real Protocol for Marker-Based
Visuotactile Sensing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.1 Tactile Sensing Principle . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.2 General-Purpose FEM-Based Physics Simulation . . . . . .
3.2.3 Synthesis of Tactile Sensor Signals . . . . . . . . . . . . . . . . . .
3.2.4 Tactile Feature Extraction and Pre-Training . . . . . . . . . . .
3.2.5 Reinforcement Learning Policy . . . . . . . . . . . . . . . . . . . . .
3.2.6 Domain Randomization . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Experiment: Data Collection, Training, and Performance
of Autoencoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.1 Autoencoder Data Collection . . . . . . . . . . . . . . . . . . . . . . .
3.3.2 Autoencoder Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.3 Autoencoder Performance on Unseen Data . . . . . . . . . . .
3.4 Experiment: Peg-in-Hole Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.1 Definition of Monotone Insertion . . . . . . . . . . . . . . . . . . .
3.4.2 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.3 Details of RL Policy Training . . . . . . . . . . . . . . . . . . . . . . .
3.4.4 Advantage of FEM Simulation over Rigid-Body
Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.5 Simulation Speed . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.6 Ablation Study for Domain Randomization . . . . . . . . . . .
3.4.7 Generalizable Peg-in-Hole Policy for Arbitrary
Shapes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.8 Advantage of the Proposed Tactile Representation . . . . .
3.4.9 Advantage of the Pre-Trained Tactile Encoder . . . . . . . . .
3.4.10 Comparison in the Original Version of the Insertion
Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.11 Generalizability to Different Sensor Instances . . . . . . . . .
3.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Model-Based Strategies: Screw Insertion for Single PiH
Assembly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Axial Friction Reduction Analysis . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.1 Axial Friction Reduction of Point Contact . . . . . . . . . . . .
4.2.2 Axial Friction Reduction of Face Contact . . . . . . . . . . . .
4.2.3 Screw Insertion with Axial Friction Reduction . . . . . . . .

41
48
49
49
51
51
52
53
54
55
56
58
59
60
61
62
63
63
63
64
66
67
69
69
70
72
73
73
75
76
77
79
79
79
80
82
84

## [Book2025 PDF p.12] Page 12

Contents

xi

4.3

Screw Insertion for Clearance-Fit Assembly . . . . . . . . . . . . . . . . . . 84
4.3.1 Jamming Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
4.3.2 Jamming Diagram for XOZ and XOY Planes . . . . . . . . . 87
4.3.3 Robotic Screw Insertion in Peg-In-Hole Assembly
with Axis Offset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
4.4 Screw Insertion for Interference-Fit Assembly . . . . . . . . . . . . . . . . 92
4.4.1 Interference Fit of Metal Parts . . . . . . . . . . . . . . . . . . . . . . 93
4.4.2 Interference Fit of Elastic Peg and Inelastic Hole . . . . . . 93
4.5 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
4.5.1 Experiment of Screw Motion with Point Contact . . . . . . 94
4.5.2 Experiment of Screw Insertion in Interference-Fit
Peg-In-Hole Assembly . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
4.5.3 Experiment of Screw Insertion in Clearance-Fit
Peg-In-Hole Assembly . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
4.6 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
5

6

Model-Based Strategies: Jamming Analysis for Dual PiH
Assembly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1 Theoretical Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.1 Model Simplification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.2 Deformation Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.3 Contact State Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.4 Contact Force Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.5 Jamming Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.6 Vertical Assembly Strategy Analysis . . . . . . . . . . . . . . . . .
5.2 Experimental Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.1 Experiment Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.2 Experimental Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
LFD for Hard-Measuring Easy-Deformation PiH Assembly . . . . . . .
6.1 Working Principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.1 The Assembly Robot System . . . . . . . . . . . . . . . . . . . . . . .
6.1.2 LFD-Based Optimal Path Planning Method . . . . . . . . . . .
6.1.3 GPR-Based Deformation Prediction
and Compensation Method . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.4 GPR Model Establishment . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.5 Training of GPR Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.6 Online GPR-Based Deformation Compensation
Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.7 Jam Handling Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

105
105
105
105
107
108
112
112
115
115
116
120
120
121
121
121
122
126
126
127
128
129

## [Book2025 PDF p.13] Page 13

xii

Contents

6.2

Simulation Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.1 Cantilever Beam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2 Assembly Robot System . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3 Realistic Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

131
131
132
135
137

7

LFE: Model-Free RL Method for PiH Assembly . . . . . . . . . . . . . . . . .
7.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2 Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2.1 Problem Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2.2 Network Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2.3 Network Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3 Fuzzy Reward System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4 Feedback Exploration Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4.1 Action Space Noise Exploration . . . . . . . . . . . . . . . . . . . .
7.4.2 Parameter Space Noise Exploration . . . . . . . . . . . . . . . . .
7.5 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5.2 Experimental Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.6 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

139
139
140
141
141
143
144
146
147
147
148
149
150
153
154

8

LFE: Model-Based RL for PiH Assembly . . . . . . . . . . . . . . . . . . . . . . . .
8.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.2 Variable Time-Scale Prediction Learning . . . . . . . . . . . . . . . . . . . .
8.2.1 Problem Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.2.2 Variable Time-Scale Prediction Definition . . . . . . . . . . . .
8.2.3 Variable Time-Scale Prediction Learning . . . . . . . . . . . . .
8.3 Variable Time-Scale Prediction-Based RL Policy Learning . . . . .
8.3.1 Preliminary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.3.2 FLS Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.3.3 FLDVTSP-DQN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.3.4 FLDVTSP-DDPG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.4 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.4.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.4.2 VTSP Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.4.3 Control Performance and Analysis . . . . . . . . . . . . . . . . . .
8.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

155
155
157
157
158
160
161
161
163
165
166
167
167
167
173
180
180

9

LFE: Hierarchical RL Method for PiH Assembly . . . . . . . . . . . . . . . .
9.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.1.1 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.2 Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.2.1 Foundations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.2.2 Two Augmented MDPs . . . . . . . . . . . . . . . . . . . . . . . . . . . .

183
183
184
184
184
185

## [Book2025 PDF p.14] Page 14

Contents

xiii

9.2.3 Higher-Level Policy Learning . . . . . . . . . . . . . . . . . . . . . .
9.2.4 Lower-Level Policies Learning . . . . . . . . . . . . . . . . . . . . .
9.2.5 Convergence Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.3 Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.3.1 MuJoCo Continuous Control Tasks . . . . . . . . . . . . . . . . . .
9.3.2 Multiple PiH Assembly . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.4 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.4.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.4.2 Comparison 1: Data Efficiency . . . . . . . . . . . . . . . . . . . . .
9.4.3 Comparison 2: Generalization Performance . . . . . . . . . . .
9.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

189
190
190
191
191
194
196
196
197
201
203
203

10 LFE: Hierarchical Compliance Control for PiH Assembly . . . . . . . .
10.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.1.1 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.2 Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.2.1 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.2.2 Lower-Level Impedance-Conditioned RL Policy
Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.2.3 Higher-Level Contextual Policy Learning . . . . . . . . . . . .
10.3 Impedance-Conditioned Action Space . . . . . . . . . . . . . . . . . . . . . . .
10.3.1 Torque-Controlled Robots . . . . . . . . . . . . . . . . . . . . . . . . . .
10.3.2 Position-Controlled Robots . . . . . . . . . . . . . . . . . . . . . . . . .
10.4 Composite Forward Model Learning . . . . . . . . . . . . . . . . . . . . . . . .
10.4.1 Composite Forward Model . . . . . . . . . . . . . . . . . . . . . . . . .
10.4.2 GMR-GP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.5 Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.6 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.6.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.6.2 Performance of Composite Forward Model . . . . . . . . . . .
10.6.3 Performance of HC-CPS . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

205
205
207
208
208
210
212
214
214
215
217
218
219
220
222
222
222
224
227
227

11 Concluding Remarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233

## [Book2025 PDF p.15] Page 15

Acronyms

ABS
AI
ARIE
BC
BSDF
CPS
CSCT
DDPG
DMP
DRL
EM
F/T
FC
FEM
FLDVTSP
FLS
FOV
FPS
GAN
GMM
GMR
GPR
GPS
GS
GVF
HC-CPS
HMM
HRL
iLQG
IPC
IR

Acrylonitrile Butadiene Styren
Artificial Intelligence
Attractive Region in Environment
Behavior Cloning
Bidirectional Scattering Distribution Function
Contextual Policy Search
Center-Symmetric Census Transform
Deep Deterministic Policy Gradient
Dynamic Movement Primitive
Deep Reinforcement Learning
Expectation Maximization
Force-Torque
Fuzzy Classifier
Finite Element Method
Fuzzy Logic-Driven Variable Time-Scale Prediction
Fuzzy Logic System
Field of View
Frame Per Second
Generative Adversarial Network
Gaussian Mixture Model
Gaussian Mixture Regression
Gaussian Process Regression
Guided Policy Search
Gravitational Search
General Value Function
Hierarchical Compliance-based Contextual Policy Search
Hidden Markov Model
Hierarchical Reinforcement Learning
Iterative Linear-Quadratic-Gaussian
Incremental Potential Contact
Infrared
xv

## [Book2025 PDF p.16] Page 16

xvi

kNN
LFD
LFE
MDDPG
MDP
MSD
MVS
OC
PBR
PiH
PTFE
REPS
RF
RL
RMSE
ROI
SAC
SGBM
SGM
SPP
SVM
TD
TD3
ToF
VAE

Acronyms

k Nearest Neighbor
Learning From Demonstrations
Learning From Environments
Model-driven Deep Deterministic Policy Gradient
Markov Decision Process
Mean Standard Deviation
Multi-View Stereo
Option Critic
Physically Based Rendering
Peg-in-Hole
Polytetrafluoroethylene
Relative Entropy Policy Search
Random Forest
Reinforcement Learning
Root Mean Square Error
Region of Interest
Soft Actor-Critic
Semi-Global Block Matching
Semi-Global Matchin
Samples Per Pixel
Support Vector Machine
Temporal Difference
Twin-Delayed-DDPG
Time-of-Flight
Variational Auto-Encoder

## [Book2025 PDF p.17] Page 17

Chapter 1

Introduction

1.1 Background
ASSEMBLY is a capstone stage in the manufacturing process, which directly affects
the quality of the final product [154]. Statistical evidence indicates that the time spent
on assembly typically accounts for 20–50% of the total production time, while the
associated costs constitute approximately 20–30% of the overall cost of a given product [160]. With the development and advancement of automation technologies, robots
have been widely used in assembly tasks to overcome the inherent challenges associated with manual assembly, such as low efficiency, high cost, and increased accident
rate [166]. Nevertheless, the escalating complexity and specialization of assembly
tasks necessitate the deployment of an increasing number of assembly robots within
unstructured and dynamic environments, thereby presenting substantial challenges
such as inadequate adaptability to assembly processes, limited sensing capabilities,
and demanding assembly environment prerequisites [61, 62]. Consequently, robotic
assembly necessitates a transition towards enhanced intelligence to address these
challenges.
The rapid advancement of Artificial Intelligence (AI) technology has promoted the
advancement of intelligent robotic assembly system. When combined with advanced
sensing system and control strategy, AI can significantly augment the capabilities
of assembly robots in all the phases, including perception, decision-making, and
control [20].
Peg-in-Hole (PiH) assembly is a fundamental and widely employed technique in
industrial manufacturing [99, 154]. It accounts for approximately 40% of the overall assembly workload [61]. PiH has been extensively investigated across various
domains, ranging from large-scale aviation component assembly [149] to smallscale component assembly in automotive production lines [133] and mold casting
manufacturing [95]. Furthermore, it extends to the assembly of electronic components [60] and even micro-product assembly [83]. Notably, there has been a recent
surge in research on PiH assembly for household tasks in human environments [6],
© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_1

1

## [Book2025 PDF p.18] Page 18

2

1 Introduction

e.g., chair assembly [136]. Due to its prominent status in assembly processes, the
study of PiH assembly is of importance for the advancement of robotic intelligent
assembly technology. Consequently, this monograph focuses explicitly on robotic
PiH assembly.

1.2 Robotic Peg-in-Hole Assembly System
We first introduce a typical robotic PiH system. As shown in Fig. 1.1a, the holes
are fixed, while manipulators grasp pegs to complete part mating based on feedback
from the sensing system. Therefore, the sensing system is crucial for acquiring the
feedback for successful assembly.

Fig. 1.1 Robotic PiH
assembly system.
a Framework.
b Cylinder [115],
square [67], and
complex-shaped
cases [131]. c Single [57],
dual [166], and multiple PiH
assemblies [120]

## [Book2025 PDF p.19] Page 19

1.2 Robotic Peg-in-Hole Assembly System

3

1.2.1 Manipulators
Manipulators have evolved significantly to meet the diverse requirements of assembly
tasks. Industrial robots excel in large-scale and heavy component assembly and
possess advanced position and velocity control for high-precision tasks. In contrast,
collaborative robots find extensive application in the assembly of small products and
deformable parts due to their ability to achieve compliant behaviors through precise
force and torque control.

1.2.2 Mating Parts
Mating parts consist of a peg and a corresponding hole (Fig. 1.1a). While cylindrical
PiH assemblies serve as the foundation, other geometries, including square pegs [67,
107], pegs with key slots, and complex shapes like gear assemblies [85], are employed
in special cases. Besides single PiH [57], dual PiH [166], multiple PiH [120, 148]
are also necessary for certain industrial applications, like electronics industry (see
Fig. 1.1b).
The scale of mating parts varies significantly depending on the application. It
ranges from macro-assembly, involving large aviation parts [149], to micro-assembly,
focused on electronic components in circuit boards [83]. Certain assembly tasks
require high precision, with clearances smaller than the resolution and accuracy of
robots, often ranging from 0.02 mm to 0.2 mm [49]. Additionally, in addition to
common rigid parts with high stiffness properties, other tasks necessitate flexible
components made of materials such as plastics and wood [57, 85]. The clearance
and surface characteristics of mating parts contribute to the complexity of assembly
tasks, resulting in varying degrees of difficulty. While this monograph aims to provide
an in-depth analysis of robotic PiH systems, the examination of clearance and surface
characteristics falls outside its scope.

1.2.3 Sensing
Similar to human tactile and vision sensing, the sensing in PiH includes force and
vision.
Force feedback is commonly used to monitor contact force and recognize environmental uncertainties. As shown in Fig. 1.1a, an external Force-Torque (F/T) sensor is amounted to the industrial robot wrist to obtain wrench signals (forces and
torques) [158]. Wrench signals can also be estimated based on joint currents [108].
For compliant robots, joint torque sensors have been utilized to calculate wrench
signals at the end-effector [74, 115]. Some researchers have embedded force sensors

## [Book2025 PDF p.20] Page 20

4

1 Introduction

in grippers or dexterous hands [9, 14, 109]. A table force sensor has been applied to
guide PiH insertion [101, 161].
Vision is commonly used to capture the pose (position and orientation) of holes
and pegs (see Fig. 1.1a). 2D cameras are widely utilized for coarse localization of
holes by extracting their boundaries from images [92]. Marker points captured by
2D cameras are used to calculate the pose of pegs [149]. Image-based visual servo
systems have been designed to track the relationship between pegs and holes [82,
110]. Position-based visual servo systems have been improved to enable high-speed
microscale PiH assembly [48].
In contrast to 2D cameras, depth sensors [2, 108, 151] have been applied to
capture the 3D geometry information. The obtained depth information is advantageous for estimating the spatial relationship between mating parts. In recent years,
the cost reduction of 3D measurement systems and the rapid development of 3D
vision and deep learning have significantly improved the efficiency and robustness
of robotic assembly based on 3D vision, making it a new mainstream solution. In this
monograph, we mainly focus on multi-view stereo (MVS) in general environment.

1.2.4 Assembly Strategies
Assembly trajectories are generally generated by a high-level planning module,
which takes into account task specifications and assembly knowledge. Subsequently,
low-level controllers are employed to track the planned trajectories and compensate
for uncertainties arising from the environment or the robot. Since these low-level
controllers have matured in implementing accurate motion and force tracking. The
assembly strategies for PiH tasks can be categorized based on the high-level planning
module.
With advancements in robotic techniques and task specifications, the strategies
for robotic PiH assembly can be broadly classified into three types: model-based
strategies, learning from demonstrations (LFD) [119], and learning from environments (LFE) [70]. It should be noted that the term “model” within the context
of model-based strategies pertains to the process of modeling the contact status
between the peg and the hole. In the subsequent chapters of this monograph, we will
explore these assembly strategies in detail, focusing on their application to various
PiH tasks.

1.3 Literature Review
In this section, we present a literature overview of MVS, tactile sensor simulation,
model-based strategies, LFD and LFE. We organize the review in the aforementioned
order to provide a coherent and structured presentation of these topics.

## [Book2025 PDF p.21] Page 21

1.3 Literature Review

5

1.3.1 Multi-view Stereo
The geometry information of the peg and the hole is critical for assembly strategy.
MVS aims to reconstruct the dense geometry of the 3D object from a sequence of
images and corresponding camera poses and intrinsic parameters. MVS is a classical
problem that had been extensively studied before the rise of deep learning. A number
of 3D representations were adopted, including volumes [23, 44, 45], deformation
models [25, 127, 165], and patches [8, 31, 39], which were iteratively updated
through multi-view photo-consistency and regularization optimization.

Learning-Based Multi-view Stereo
Inspired by the success of deep learning in image recognition tasks, researchers
began to apply learning techniques to stereo reconstruction tasks for better patch
representation and matching [37, 69, 122]. Although these methods, in which only
2D networks were used, had made a great improvement on stereo tasks, it was difficult
to extend them to MVS tasks, and their performance was limited in challenging scenes
due to the lack of contextual geometry knowledge. Concurrently, 3D cost volume
regularization approaches were proposed [59, 64, 65], where a 3D cost volume was
built either in the camera frustum or the scene. Next, the multi-view 2D image features
were warped into the cost volume, so that 3D CNNs could be applied to it. The key
advantage of 3D cost volume is that the 3D geometry of the scene can be captured by
the network explicitly, and the photo-metric matching can be performed in 3D space,
alleviating the influence of image distortion caused by perspective transformation,
which makes these methods achieve better results than 2D learning-based methods.
More recently, Luo et al. [86] proposed to use a learnable patchwise aggregation
function and apply isotropic and anisotropic 3D convolutions on the 3D cost volume to improve the matching accuracy and robustness. Xue et al. [163] proposed
Multi-view StereoCRF, where Multi-Scale Conditional Random Fields are adopted
to constraint the smoothness of depth prediction explicitly.

High-Resolution and Hierarchical Multi-View Stereo
High-resolution MVS is critical to PiH assembly. Traditional methods [31, 77, 104]
generated dense 3D patches by expanding from confident matching key points repeatedly, which was potentially time-consuming. These methods were also sensitive to
noise and change of viewpoint owing to the usage of hand-crafted features. Recent
learning methods tried to ease memory consumption by advanced space partitioning [116, 142, 150] or by replacing 3D CNNs with RNN [164]. However, most of
these methods constructed a fixed cost volume representation for the whole scene,
lacking flexibility.

## [Book2025 PDF p.22] Page 22

6

1 Introduction

Hierarchical MVS generates high-resolution depth maps in a coarse-to-fine manner, which reduces unnecessary computation and leads to improved efficiency. For
classic methods, hierarchical Mutual Information computation was utilized to initialize and refine disparity maps [41, 117]. Learning-based methods were proposed
to predict the residual of the depth map from warped images [105] or by constructing
cascade narrow cost volume [33, 169].

1.3.2 Tactile Sensor Simulation
The simulation process of tactile sensors is typically divided into two phases. The
first phase involves the simulation of the sensor’s deformation caused by contact.
The second phase involves the simulation of the transduction of physical quantities
from the deformation. For marker-based visuotactile sensors, the first phase is a fundamental step for the second phase. This subsection primarily summarizes methods
related to the first phase. Tactile sensors that operate on other principles, such as
BioTac [30], share a similar first phase as marker-based visuotactile sensors and are
also included in this subsection.
In [32, 168], a Gazebo-based GelSight simulator was proposed, where the deformation was simulated from the contact geometry using Gaussian filtering followed
by difference of Gaussian. In [18, 81, 152], PyBullet was used to simulate the contact between the object and the sensor, and the deformation was approximated by
calculating the penetration of the object into the sensor. A similar method is also
reported in [3]. The focus of these works is the simulation of sensors’ optical properties. Despite their computational efficiency, these geometry-based methods cannot
model the sensor’s tangential deformation, which is crucial for many robot applications such as slip detection and peg-in-hole insertion. Xu et al. [159] proposed a
penalty-based tactile model upon rigid body dynamics, which is able to simulate both
normal and shear tactile force fields at high speed. While the penalty-based simulation can approximate the sensor deformation in manipulation, it cannot simulate the
elastic behavior of the elastomer accurately, especially the contact force caused by
the tangential deformation. Therefore, its Sim2Real transferability is limited, which
has been demonstrated by our experimental results.
Compared with rigid-body-based simulation, Finite Element Methods (FEM) can
model the deformation of the sensor’s elastomer more accurately. Bi et al. [5] developed a FEM-based tactile sensor simulator and achieved zero-shot Sim2Real transfer of RL policies for aggressive swing-up manipulation. However, they utilized the
cylindrical geometry of the poles to simplify the simulation, and constrained the
motion of the pole in the x-y plane, rendering it inapplicable to objects with various
geometries. Si and Yuan [124] proposed a superposition method to approximate the
FEM dynamics and successfully simulate the sensor’s tangential deformation, but no
manipulation tasks were demonstrated. Narang et al. built a linear-FEM-based tactile
simulator for BioTac with Isaac Gym [96], achieving faster speeds than the commercial FEM software (ANSYS) [97]. Recently, Luu et al. employed SOFA [28] to build

## [Book2025 PDF p.23] Page 23

1.3 Literature Review

7

a simulator for large-scale marker-cum-vision-based-tactile sensor [87]. However,
both [87, 96] primarily used their simulators to collect supervised datasets for interpreting tactile signals, leaving the potential of using simulation to train manipulation
policies unexplored.

1.3.3 Model-Based Strategies
Model-based strategies employ contact state recognition to generate assembly motion
trajectories. Hence, constructing an accurate contact state model becomes crucial.
In the 1990s, several analytical models were proposed for contact state recognition.
However, with the growing amount of data and task complexity, statistical approaches
have been researched to identify contact states from assembly data.

Analytical Contact Model
Contact states can be recognized relying on the analysis of the geometrical and
environmental constraints [153]. It can be implemented via two stages: contact state
modeling and contact state determining [157].
Firstly, contact states can be modeled according to the mating features. Commonly
used features include geometrical information and topology information [121]. Desai
et al. [22] classified the contact states as the set of Elemental Contacts with same
topology information. Xiao et al. [138, 156] introduced the concept of Principal
Contacts for topological representation of contact states and generated the graph to
represent the transition of contact states. Bruyninckx et al. [11, 12] built the kinematic
models based on the constraints analysis for compliant motion in the presence of
uncertainties [89]. Ohwovoriole et al. [103] defined three screw pairs to represent
the contact constraints based on the screw theory. Hirai and Asada [40] extended
the theory of polyhedral convex cones to solve manipulation problems governed by
unidirectional constraints.
Secondly, the contact states can be determined or verified depending on the
force/torque information [4]. McCarragher and Asada [91] developed a neural
network-based qualitative recognition method to identify the transition of contact
states quickly, where the dynamics effects were analyzed with the Petri Net. In an
edge mating task, the contact states were detected via a singular value decomposition technique depending on analyzing the force/moment signals, which has shown
better robustness to noise [68]. Geometric interpretation based on polyhedral convex
cones was utilized to determine the likelihood of each feasible contact formation even
without accurate contact force [27]. To reduce the redundancies to build the static
equilibrium equations, a part knowledge-based system was developed to identify the
contact states [144].

## [Book2025 PDF p.24] Page 24

8

1 Introduction

In summary, the contact constraints can be analyzed at a certain level [22]. However, the environmental uncertainties (e.g., part poses, rigidity or elasticity of the
assembly components, and friction model) always result in challenges to recognize
the contact state exactly. Additionally, the analytical analysis is sensitive to uncertainties, and it is impossible for any perfect model to account for all uncertainties.
Moreover, the analytical analysis relies solely on past contact states, which limits its
ability to generalize to new situations.

Statistical Contact Model
Statistical analysis methods often model the assembly trajectory as several segmented phases with different contact states [134]. Contact state recognition via
statistical analysis is often formulated as a classification problem given possible
contact states [93]. Statistical strategies can recognize the contact states from the
pattern of collected samples without any assumption [51]. Commonly used statistical techniques for contact states consist of non-parametric classification methods,
e.g., Fuzzy Classifier (FC) and Random Forest (RF); and parametric classification
methods, e.g., Neural Network, Support Vector Machine (SVM), Gaussian Mixture
Model (GMM), and Hidden Markov Model (HMM).
FC was applied in recognizing contact states via accommodating the uncertainties
based on task knowledge [111, 128]. To enhance the robustness of the fuzzy system,
the Gravitational Search (GS) was used to adjust the fuzzy rules [55]. GS-FC could
solve the simple classification with little computing time through giving more accurate logic rules. Additionally, RF [16] and binary Stochastic Gradient Boosting [15]
with strong classifier diversity were explored for multiple classification problems.
NN was researched to map the nonlinear relationship between the force information and contact states [10]. Two NN-based efficient classifiers combining with
FC had achieved better sample efficiency performance in terms of the environmental
noise [128, 130]. SVMs could reduce the risk and controlling the confidence interval
for correct classification. It was suitable and applicable to design a practical contact
states recognition method or real-world tasks [51, 53]. A Fuzzy Inference Mechanism with an adaptive classifier boundary was proposed to improve the robustness
of the contact states classification [52].
GMM was employed to encode the states of PiH assembly, and Expectation
Maximization (EM) had been demonstrated to optimize the parameters of GMMs.
Bayesian classification had been incorporated to estimate a binary classification of the
given GMMs [56, 58]. Jasim et al. [58] utilized the Distribution Similarity Measure
to determine the optimal number of GMM components. HMMs could recognize both
the contact states and state transitions via considering the temporal information [38].
It was suitable for dynamic assembly with sensor noise because the parameters of
HMMs can be learned from empirical data [46]. A practical contact states identification system based on HMMs was implemented via incorporating with the prior
spatial relationships of contact formations [21, 72].

## [Book2025 PDF p.25] Page 25

1.3 Literature Review

9

In addition, some researchers had done related analyses on real-world tasks. Comparison of FC and NNs was presented in [10, 129], which shows that FC is less sensitive to the overlap of input states. Jasim et al. [58] set up rubber-manipulated objects
assembly platform and compared the accuracy and computing time of several commonly used statistical classification methods. They also presented a comprehensive
summary of the strengths and limitations.

Assembly Trajectory Generation
To complete the assembly tasks based on the contact states analysis, the assembly trajectories can be designed as a sequence of contact states [135]. Mason et
al. [84] proposed an approach to integrate a class of fine-motion strategies, in which
each separate motion is specified to bound the motion error according to geometrical constraints. Asada et al. [90] proposed to model the assembly constraints as
discrete event dynamic systems by Petri Nets. The motion trajectory needs to follow the desired contact states and recover from the undesired contact states. The
velocity and applicable force of contact point under friction-less assumption could
be identified automatically by the geometric constraints analysis [42, 94]. In addition to the geometrical constraints [100, 108], Qiao et al. developed the Attractive
Region in Environment (ARIE) concept [113] to take into account the environmental
constraints. Therefore, the position uncertainties were eliminated by coarse wrench
signals. The constraint region in configuration space and physical space had been
discussed and the assembly trajectories can be formulated following the attractive
region as shown in Fig. 1.2a [79]. In [123] and [140], a hybrid motion trajectory was
generated by choosing the corresponding low-level controller based on the contact
states recognition.
Jamming and wedging are problematic contact states that should be avoided during
PiH assembly motion trajectories [126]. Whitney [153] constructed a quasi-static
model to clarify the relation between force and geometrical constraints for a single
PiH assembly. A jamming diagram was drawn to analyze the jamming conditions.
Based on the jamming diagram (see Fig. 1.2b), a single PiH assembly trajectory was
formulated as the transitions among no contact, one-point contact and two-point
contact [153]. [118] and [29] enumerated contact states and presented 3D analysis
of jamming conditions for complex multiple PiH assembly problem. In contrast
to the quasi-static model and rigid body assumptions, researchers also proposed
dynamical and flexible models, which are closer to real-world assembly tasks. Xia et
al. [155] presented a 3D jamming analysis for an elastic contact dynamic model and
designed several assembly strategies. Son [111, 130] utilized a NN to approximate the
nonlinear relationship between the jamming states and the insertion control strategy.
Xia et al. [155] proposed to design a no-jamming and no-wedging assembly strategy
via choosing the appropriate set of applied forces and moments.

## [Book2025 PDF p.26] Page 26

10

1 Introduction

Fig. 1.2 Geometrical
analysis motion trajectory
generation. a ARIE concept
for motion planning [113].
b Jamming diagram [153]

1.3.4 Learning from Demonstrations
As depicted in Fig. 1.3a, the implementation of LFDs involves two principal
stages: demonstration perception and assembly trajectory reproduction [170]. Firstly,
the demonstrations are collected and meaningful features are extracted. These
extracted features are then encoded to facilitate the learning of subsequent assembly
trajectories.

Demonstration Collection
For PiH assembly, human demonstrations involve capturing both motion trajectories and interaction forces. These demonstrations are typically gathered through
three methods: kinesthetic demonstration, motion capture systems, and teleoperated

## [Book2025 PDF p.27] Page 27

1.3 Literature Review

11

Fig. 1.3 LFD strategies.
a Framework of LFDs
strategies. b Example:
GMM-GMR

demonstration [114]. Motion trajectories of pegs can be obtained by recording robot
joint encoders or using visual techniques such as marker point matching [149] or 3D
point cloud processing [58]. The applied force during assembly is often measured
using F/T sensors or joint torque sensors [24, 141]. The execution commands usually include translation-rotation offsets or velocities, applied forces in task space, or
torque commands in joint space [141].

## [Book2025 PDF p.28] Page 28

12

1 Introduction

Feature Extraction
To handle the original demonstration data, various feature extraction techniques were
employed. These included Principal Component Analysis for dimension reduction
and Dynamic Time Warping to align data from different demonstrations [132]. NNs
had gained popularity for combining diverse demonstration types, such as motion
and wrench signals [19]. To mitigate noise and select important features, filtering
and feature selection modules were also incorporated. Three commonly used encoding approaches to represent collected demonstrations were Dynamic Movement
Primitive (DMP), GMM, and HMM [170].
DMPs were generally applied to represent a nonlinear dynamic system [1].
For instance, to model the discrete movements of the assembly trajectories, the
selected kinematic variables, including positions, velocities, and accelerations, were
used [145]. The complex motion trajectories for PiH assembly were often decomposed into five phases. Different DMPs encoded the corresponding phase with individual separate goal states [71, 98]. GMMs were commonly used for clustering
and feature classification, particularly for high-dimensional and noisy demonstration data [7]. GMMs were not only utilized for modeling human motions but also
the applied force [140, 141]. HMMs, on the other hand, wear robust probabilistic
models that integrate spatial and temporal variability. They had been extensively
researched for encoding and generalizing collected assembly trajectories [17, 50,
167]. HMMs, which can be considered as a type of dynamic Bayesian network, were
well-suited for handling partially observed data. They had been employed to model
state transitions in assembly procedures with missing data [162].
DMPs were effective in modeling the demonstrated assembly trajectories, as they
are less impacted by spatial perturbations. Complex tasks consisted of sequential
sub-tasks, and DMPs-based approaches could construct individual DMPs for each
subtask [2, 98]. GMMs and HMMs could model various types of demonstrations,
including motion and wrench signals. GMMs estimated the probability density function for clustering, offering better robustness against environmental noise and missing data [139, 141]. In contrast, HMMs excelled at handling temporal transition
information, encompassing both periodic and discrete movements [167]. They could
perform imitation learning with partial demonstrations by incorporating preceding
information, which is necessary for real-world tasks [47]. However, solving HMMs
could pose challenges, often requiring additional optimization algorithms or iterative
learning approaches [47]. Notably, different encoding methods had been explored to
combine these techniques. For example, GMMs were used to encode demonstrations
and provide a latent representation of motions, while HMMs employed the mixture
Gaussian to encapsulate transition probabilities [167].

## [Book2025 PDF p.29] Page 29

1.3 Literature Review

13

Assembly Trajectory Generation
The assembly trajectories for robots execution need to not only imitate human behaviors but also handle robustness against disturbance and generalization in new situations. DMP strategies can generate the desired assembly trajectories given the
start position and goal position. The differential variant of DMPs was proposed to
improve the adaptation against the uncertainties of the goal position and obstacle
avoidance [106]. Instead of the trajectory-level generation, a NN control policy was
trained to output the control command in terms of each state. A linear Gaussian
controller optimized by the demonstration trajectories was applied to guide the network training [75]. Gaussian Mixture Regression (GMR) is a real-time regression
solution to reproduce the trajectories modeled by GMMs, which can easily meet the
requirements of real-world robotic assembly tasks [54]. In [141] and [139], GMR was
employed to imitate the admittance behaviors from human to generate the potential
velocities based on wrench signals. HMM is a generative model to generate the new
assembly trajectories. Additionally, HMM also combining with GMR was developed to achieve robust performance through estimating the redundancies besides the
demonstrations [17]. Gaussian Process Regression (GPR) is a probabilistic model
to estimate the input-output relationship, where the desired assembly trajectories
can be reproduced by the predictions of Gaussian process [54, 149]. Recently, imitation learning has been explored to imitate the action-level behaviors from expert
demonstrations, which is formulated as a supervised learning problem to estimate
the sampled state-action pairs from demonstrations [43].
Robotic assembly trajectories need to not only imitate human behaviors but also
exhibit robustness against disturbances and generalizability to new situations. DMPs
offer strategies for generating desired assembly trajectories based on start and goal
positions. The differential variant of DMPs was proposed to enhance adaptability
by addressing uncertainties in goal positions and obstacle avoidance [106]. Instead
of trajectory-level generation, a NN control policy was trained to output the control command for each state, guided by an optimized linear Gaussian controller
using demonstration trajectories [75]. GMR is a real-time regression solution that
reproduces trajectories modeled by GMMs, making it well-suited for real-world
robotic assembly tasks [54]. GMR has been employed to imitate admittance behaviors from humans, generating potential velocities based on wrench signals [139,
141]. HMMs serve as generative models for generating new assembly trajectories.
Combining HMMs with GMR improved robust performance by estimating redundancies in addition to demonstrations [17]. GPR is a probabilistic model used to
estimate the input-output relationship, enabling the reproduction of desired assembly trajectories through Gaussian process predictions [54, 149]. Imitation learning
has been explored to imitate action-level behaviors from expert demonstrations, formulating it as a supervised learning problem to estimate sampled state-action pairs
from demonstrations [43].

## [Book2025 PDF p.30] Page 30

14

1 Introduction

1.3.5 Learning From Environments
Foundations
Compared to model-based strategies and LFDs, highly intelligent assembly motion
trajectories can be learned through interaction with the environment and sensing of
the environment’s dynamics. LFEs show promise in solving not only more complex
tasks but also in achieving better generalizability for a wide range of unseen tasks.
Among LFE techniques, Reinforcement Learning (RL) stands out as the most popular
approach. Therefore, our main focus is on RL-based techniques.
The control problem addressed by RL generally can be formulated as a Markov
Decision Process (MDP) .< S, A, T , R >, in which .S is the state space set, .A
is the action space set, .T is the state transition function: .S × A × S → [0, 1], .R
is the reward function .S × A → R. At each environment step .t, the agent selects
an action .at ∈ A from the policy .π(at |st ) according to the current state .st ∈ S.
The environment transits to the next state .st+1 with the probability . P(st+1 |st , at ) =
The return from a state is defined
T (st , at , st+1 ). A reward .rt = R(st , at ) is
received.
T
γ i−t ri . .γ ∈ [0, 1) is a discount factor.
as the sum of discounted reward .G t = i=t
. T is the length of one episode.
The policy is often parameterized by .θ as .πθ . The objective of RL is to optimize
the expected return from the start distribution:
J (θ) = Esi ∼ pπ ,ai ∼π [G 0 ]

.

(1.1)

For PiH assembly tasks, the action space .A, state space .S and reward function .R
should be formulated according to the task specifications. And the policy is defined
for continuous control, the policy parameter .θ will be updated by taking the gradient
of the expected return as.∇θ J (θ ). Particularly, the actor-critic methods are commonly
employed to update the policy parameters based on the estimated expected return
from critic network[80] as:
.

∇θ J (θ) = Es∼ pπ [∇a Q π (s, a)|a=π(s)∇θ πθ (s) ]

(1.2)

where . Q π (s, a) is state-action value function to represent the expected return when
executing the action .a in state .s following policy .π .
State representation: The state denotes observations via the sensing system (see
Sect. 1.2.3). As described in Sect. 1.2, the holes are typically fixed, and the pegs
are grasped or mounted on the robot end-effector. The state typically includes the
poses (positions/orientations) and corresponding velocities of pegs. The wrench can
be obtained from an F/T sensor or estimated from joint torques [49]. However, force
signals are often noisy and require preprocessing with suitable filters [85, 115].
In contrast, images and depth images are commonly used to represent the assembly
environment, enabling more efficient interpretation of the hole position and the peg’s
relative position [120].

## [Book2025 PDF p.31] Page 31

1.3 Literature Review

15

Recently, Deep Reinforcement Learning (DRL) has been increasingly studied,
where all the components are approximated by NN [137], which basically extract the
essential information from states. However, in real-world tasks, the states are usually
partially observable, necessitating the capture of historical information rather than
solely relying on the current time step. To address this, RNNs have been employed
to leverage the sequential observations of the assembly environment [49].
Reward Formulation: The reward function is a manually defined mapping that
assigns a scalar value to a state-action pair, based on task requirements and assembly
knowledge [137]. For example, a sparse reward function is often used to determine
if the assembly task is completed or not [75]. Additionally, the reward function can
also be designed to encourage faster assembly speed [49]. Sparse rewards typically
require a large amount of interaction in order to gather useful data. To reduce random exploration in real-world tasks, dense rewards are often used. This involves
applying a penalty term for factors such as the distance to the goal position and a
large contact force [115]. Reward formulation is a practical approach for efficient
learning that combines assembly knowledge. For instance, a fuzzy reward function
was proposed to incorporate human assembly experience [158]. Another approach
involves comparing reward functions with reference demonstrations [143].
Action Space Formulation: In the 1990s, RL was explored for learning reactive robotic skills, mapping sensing signals to control commands [34, 102]. These
works aimed to solve single PiH tasks despite sensor noise and control errors. The
action space involved velocity or position commands in task space, estimating the
admittance mapping from force signals to precomputed peg trajectories [35, 36].
With advancements in robots and GPU technology, more data can be collected and
complex policies, such as high-dimensional functions, can be estimated using deep
NNs [73]. DRL was proposed to learn manipulation skills [75, 76]. The action space
often involves torque commands [26] or desired angles/velocities in joint space and
end-effector pose/velocities [158]. A significant development was the Deterministic
Policy Gradient theorem, enabling direct estimation of continuous parameterized
policies [125]. Deep Deterministic Policy Gradient (DDPG) [80] is a popular DRL
approach for learning continuous high-dimensional assembly policies [78, 158].
In contrast to the aforementioned control command, the action space of DRL
was also reformulated according to the high-level planning module to generate the
reference for low-level controllers [85]. In a comparative study of four action spaces
(direct torque control, joint PD, inverse dynamics, and impedance controller) [146],
the task-space impedance controller demonstrates the most efficient performance in
terms of sample efficiency.

Assembly Trajectory Generation
End-to-End Learning: End-to-end learning DRL estimates a mapping function to
generate the motion assembly trajectories without any assumption of robot dynamics
and environmental dynamics. However, end-to-end learning DRL needs to compensate all the dynamics from interactions, which often results in poor sample efficiency.

## [Book2025 PDF p.32] Page 32

16

1 Introduction

It is easy to implement end-to-end learning but still challenging to solve a simple
PiH task in the real world. To improve the applicability of DRL, two main aspects
have been developed [158].
Firstly, for robotic PiH assembly tasks, some structures or partial model can be
addressed by hand-crafted model-based controllers. DRL can be applied to learn the
residual part involving environmental dynamics [63]. Therefore, a general framework
named residual policy learning is formulated as:
π (s) = π(s) + f θ (s)

. θ

(1.3)

where .π(s) denotes the initial policies, e.g., hand-designed policies or other efficient
Model-Predictive Controller, . f θ (s) denotes a residual differentiable policy updated
by DRL algorithms.
Model-based RL has been extensively studied for robotic assembly tasks, aiming
to minimize physical interactions by estimating a dynamic model [112]. A noteworthy framework in this area is Dyna-style, which combines planning with a dynamic
model and learning through environment interactions. It updates the policy using predicted and realistic interaction data. However, accurately estimating a dynamic model
remains challenging due to noisy force signals and inconsistencies in state transitions [26]. While most Dyna-style model-based RL algorithms are demonstrated in
simulations, Guided Policy Search (GPS) [75] exhibits superior sample efficiency
in various manipulation tasks. GPS employs a time-varying linear Gaussian model
to estimate local environment dynamics, with its performance heavily influenced by
the choice of trajectory optimization solver and the dynamic model. Fan et al. [26]
proposed a fusion actor-critic framework that combines the strengths of GPS and
DDPG. This integration allowed the trajectory optimization component of GPS to
guide the actor network, while the critic network of DDPG helped mitigate potential
inconsistencies and instabilities compared to using GPS alone.
Reference Generation: DRL plays a dual role in assembly tasks. Firstly, it can
enhance adaptability by integrating with original reference assembly trajectories.
DMPs have been widely employed for generating desired motion trajectories, and
various extensions of DMPs have been developed to improve adaptability. One such
extension is Policy Improvement with Path Integrals [13], which optimizes parameterized DMPs to generate assembly trajectories that adapt to different initial positions.
DRL also combines with imitation learning to refine reference assembly trajectories learned from human demonstrations. For example, DDPG guided from human
demonstrations [147, 148] was a common approach. Another approach involved utilizing geometric CAD data to plan desired assembly trajectories instead of relying
on demonstrations [143]. Additionally, a time-dependent NN policy could be trained
with augmented loss to track the expected trajectory, offering an alternative to the
imitation learning mechanism.
On the other hand, DRL is utilized to provide references for low-level controllers.
For instance, DRL using RNN-based state representation was employed to select
desired force/moment references for low-level hybrid motion-force controllers [49],
where the action space consists of six elementary desired forces/moments. Variable

## [Book2025 PDF p.33] Page 33

1.5 Book Organization

17

impedance controllers in joint space and task space have been extensively researched
for contact-rich assembly tasks [88]. In the case of impedance controllers, a NNbased global policy learned through iterative Linear-Quadratic-Gaussian (iLQG) was
applied to learn the desired force or impedance in task space [85]. This approach was
particularly useful for collaborative robots executing PiH assembly tasks. Many DRL
approaches focused on optimizing the parameters of low-level hybrid motion-force
controllers or generating impedance settings [13, 66]. While these approaches could
improve performance, they may also introduce instabilities as choosing the appropriate parameters is crucial. Consequently, successful simulations may not translate
well to physical systems due to time delays [146].

1.4 Scientific Goals
This book covers the following issues related to robotic PiH assembly strategies:
– Improve the accuracy and computational efficiency of learning-based MVS.
– Build general-purpose Sim2Real protocol of PiH with marker-based visuotactile
sensing.
– Develop the state of art assembly strategies for general PiH tasks within scope of
model-based strategies.
– Improve generalizability of robot assembly using learning-based strategies.
– Develop the state of art assembly strategies using LFDs for large-scale heavyweight component assembly tasks.
– Explore efficient techniques for accelerating the training process of existing LFE
algorithms.
According to different scopes of assembly strategies, these issues are divided into
three chapters and discussed to enhance the understanding of the user.

1.5 Book Organization
The structure of the book is as follows:
– This chapter presents a brief introduction of assembly and the reasons why PiH
assembly is chosen as the main topic in this monograph. This chapter also includes
preliminaries and foundations of PiH assembly and reviews existing model-based
and learning-based assembly methods.
– In Chap. 2, a Visibility-Aware Point-based MVS Network (VA-Point-MVSNet) is
presented, which improves the geometry reconstruction’s accuracy and resolution
by a large margin.

## [Book2025 PDF p.34] Page 34

18

1 Introduction

– In Chap. 3, a general-purpose Sim2Real protocol of PiH with marker-based
visuotactile sensing is presented, which achieves zero-shot Sim2Real of PiH
policies.
– In Chaps. 4 and 5, two model-based assembly strategies and their theoretical
analysis are proposed for reducing frictional force and performing flexible dual
PiH assembly tasks.
– In Chap. spsexrefCspsLFD, an LFD-based optimal method for optimizing assembly path planning, a learning-based online robot control method that utilizes GPR
and a deformation compensation strategy to model and compensate the robot
deformation are presented for hard-measuring easy-deformation PiH assembly.
– In Chaps. 7, 8, 9, and 10, four LFE-based methods and their theoretical analysis
are proposed to present to improve the data-efficiency and generalization of PiH
assembly policy learning.
– Chapter 11 concludes the monograph contribution and presents future research
directions.

References
1. F. Abu-Dakka, B. Nemec, A. Ude, Peg-in-hole using dynamic movement primitives, in Proceedings of RAAD, the 21th International Workshop on Robotics in Alpe-Adria-Danube
Region, Napoli, Italy (2012), pp. 143–149
2. F.J. Abu-Dakka, B. Nemec, A. Kramberger, A.G. Buch, N. Krüger, A. Ude, Solving peg-inhole tasks by human demonstration and exception strategies. Ind. Robot: Int. J. 41(6), 575–584
(2014)
3. A. Agarwal, T. Man, W. Yuan, Simulation of vision-based tactile sensors using physics based
rendering, in 2021 IEEE International Conference on Robotics and Automation (ICRA) (IEEE,
202)1, pp. 1–7
4. H. Asada, S. Hirai, Towards a symbolic-level force feedback: recognition of assembly process
states, in The Fifth International Symposium on Robotics Research (2021), pp. 341–346
5. T. Bi, C. Sferrazza, R. D’Andrea, Zero-shot sim-to-real transfer of tactile control policies for
aggressive swing-up manipulation. IEEE Robot. Autom. Lett. 6(3), 5761–5768 (2021)
6. A. Billard, D. Kragic Trends and challenges in robot manipulation. Science 364 (2019)
7. J.A. Bilmes et al., A gentle tutorial of the em algorithm and its application to parameter
estimation for gaussian mixture and hidden markov models. Int. Comput. Sci. Inst. 4(510),
126 (1998)
8. M. Bleyer, C. Rhemann, C. Rother, Patchmatch stereo-stereo matching with slanted support
windows. Bmvc 11, 1–11 (2011)
9. B. Borovac, D.J. Seslija, S. Stankovski, Soft sensored grippers in assembly process, in Proceedings 1992 IEEE International Conference on Robotics and Automation (IEEE Computer
Society, 1992), pp. 1283–1284
10. L. Brignone, M. Howarth A geometrically validated approach to autonomous robotic
assembly. IEEE/RSJ Int. Conf. Intell. Robots Syst. 2, 1626–1631 (2002)
11. H. Bruyninckx, J. De Schutter, Specification of force-controlled actions in the “task frame
formalism”-a synthesis. IEEE Trans. Robot. Autom. 12(4), 581–589 (1996)
12. H. Bruyninckx, J.D. Schutter, Kinematic models of rigid body interactions for compliant
motion tasks in the presence of uncertainties, in [1993] Proceedings IEEE International
Conference on Robotics and Automation, vol. 1 (1993), pp. 1007–1012

## [Book2025 PDF p.35] Page 35

References

19

13. J. Buchli, F. Stulp, E.A. Theodorou, S. Schaal, Learning variable impedance control. Int. J.
Robot. Res. 30, 820–833 (2011)
14. J. Butterfaß, M. Grebenstein, H. Liu, G. Hirzinger, Dlr-hand ii: next generation of a dextrous robot hand, in Proceedings 2001 ICRA IEEE International Conference on Robotics and
Automation (Cat No01CH37164), vol. 1 (2001), pp. 109–114
15. S. Cabras, M.E. Castellanos, E. Staffetti, Contact-state classification in human-demonstrated
robot compliant motion tasks using the boosting algorithm. IEEE Trans. Syst. Man Cybernet.
Part B (Cybernet.) 40, 1372–1386 (2010)
16. S. Cabras, M.E. Castellanos, E. Staffetti, A random forest application to contact-state classification for robot programming by human demonstration. Appl. Stoch. Model. Bus. Ind. 32,
209–227 (2016)
17. S. Calinon, F. D’halluin, E.L. Sauser, D.G. Caldwell, A.G. Billard, Learning and reproduction
of gestures by imitation. IEEE Robot. Autom. Mag. 17(2), 44–54 (2010)
18. A. Church, J. Lloyd, N.F. Lepora et al., Tactile sim-to-real policy transfer via real-to-sim
image translation, in Conference on Robot Learning, PMLR (2022), pp. 1645–1654
19. R.P.D. Cortesão, R. Koeppe, U. Nunes, G. Hirzinger, Data fusion for robotic assembly tasks
based on human skills. IEEE Trans. Rob. 20, 941–952 (2004)
20. S. Das, I. Das, R.N. Shaw, A. Ghosh, Chapter seven - advance machine learning and artificial
intelligence applications in service robot, in (eds) Artificial Intelligence for Future Generation
Robotics, ed. by R.N. Shaw, A. Ghosh, V.E. Balas, M. Bianchini (Elsevier, 2021), pp. 83–91.
https://doi.org/10.1016/B978-0-323-85498-6.00002-2
21. T. Debus, P.E. Dupont, R.D. Howe, Contact state estimation using multiple model estimation
and hidden Markov models. Int. J. Robot. Res. 23, 399–413 (2002)
22. R. Desai, J. Xiao, R.A. Volz, Contact formations and design constraints: A new basis for the
automatic generation of robot programs, in CAD Based Programming for Sensory Robots
(Springer, 1988), pp. 361–395
23. C.R. Dyer, Volumetric scene reconstruction from multiple views, in Foundations of Image
Understanding (Springer, 2001), pp. 469–489
24. D. Ehlers, M. Suomalainen, J. Lundell, V. Kyrki, Imitating human search strategies for assembly, in 2019 International Conference on Robotics and Automation (ICRA) (IEEE, 2019), pp.
7821–7827
25. C.H. Esteban, F. Schmitt, Silhouette and stereo fusion for 3d object modeling. Comput. Vis.
Image Underst. 96(3), 367–392 (2004)
26. Y. Fan, J. Luo, M. Tomizuka, A learning framework for high precision industrial assembly,
in 2019 International Conference on Robotics and Automation (ICRA) (IEEE, 2019), pp.
811–817
27. A. Farahat, B. Graves, J.C. Trinkle, Identifying contact formations in the presence of uncertainty, in Proceedings 1995 IEEE/RSJ International Conference on Intelligent Robots and
Systems. Human Robot Interaction and Cooperative Robots, vol. 3 (IEEE, 1995), pp. 59–64
28. F. Faure, C. Duriez, H. Delingette, J. Allard, B. Gilles, S. Marchesseau, H. Talbot, H. Courtecuisse, G. Bousquet, I. Peterlik, S. Cotin, SOFA: a multi-model framework for interactive
physical simulation, in Soft Tissue Biomechanical Modeling for Computer Assisted Surgery,
Studies in Mechanobiology, Tissue Engineering and Biomaterials, ed. by Y. Payan, vol. 11
(Springer, 2012), pp. 283–321. https://doi.org/10.1007/8415_2012_125, URL https://inria.
hal.science/hal-00681539
29. Y. qiong Fei, X. Zhao, An assembly process modeling and analysis for robotic multiple
peg-in-hole. J. Intell. Robot. Syst. 36, 175–189 (2003)
30. J.A. Fishel, G.E. Loeb, Sensing tactile microvibrations with the biotac–comparison with
human sensitivity, in 2012 4th IEEE RAS & EMBS International Conference on Biomedical
Robotics and Biomechatronics (BioRob) (IEEE, 2012), pp. 1122–1127
31. Y. Furukawa, J. Ponce, Accurate, Dense, and Robust Multiview Stereopsis. IEEE Trans.
Pattern Anal. Mach. Intell. 32(8), 1362–1376 (2010). https://doi.org/10.1109/TPAMI.2009.
161

## [Book2025 PDF p.36] Page 36

20

1 Introduction

32. D.F. Gomes, P. Paoletti, S. Luo, Generation of gelsight tactile images for sim2real learning.
IEEE Robot. Autom. Lett. 6(2), 4177–4184 (2021)
33. X. Gu, Z. Fan, S. Zhu, Z. Dai, F. Tan, P. Tan, Cascade cost volume for high-resolution
multi-view stereo and stereo matching (2019). arXiv:1912.06378
34. V. Gullapalli, R.A. Grupen, A.G. Barto, Learning reactive admittance control, in Proceedings
1992 IEEE International Conference on Robotics and Automation (IEEE, 1992), pp. 1475–
1480
35. V. Gullapalli, R.A. Grupen, A.G. Barto, Learning admittance mappings for force-guided
assembly, in Proceedings of the 1994 IEEE International Conference on Robotics and
Automation (IEEE, 1994), pp. 2633–2638
36. V. Gullapalli, J.A. Franklin, H. Benbrahim, Acquiring robot skills via reinforcement learning.
IEEE Control. Syst. 14, 13–24 (1994)
37. X. Han, T. Leung, Y. Jia, R. Sukthankar, A.C. Berg, Matchnet: unifying feature and metric
learning for patch-based matching, in Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition (2015), pp. 3279–3286
38. B. Hannaford, P. Lee, Hidden Markov model analysis of force/torque information in
telemanipulation. Int. J. Robot. Res. 10, 528–539 (1991)
39. P. Heise, S. Klose, B. Jensen, A. Knoll, Pm-huber: Patchmatch with huber regularization for
stereo matching, in Proceedings of the IEEE International Conference on Computer (2013),
pp 2360–2367
40. S. Hirai, H.H. Asada, Kinematics and statics of manipulation using the theory of polyhedral
convex cones. Int. J. Robot. Res. 12, 434–447 (1993)
41. H. Hirschmuller, Stereo processing by semiglobal matching and mutual information. IEEE
Trans. Pattern Anal. Mach. Intell. 30(2), 328–341 (2007)
42. H. Hirukawa, T. Matsui, K. Takase, Automatic determination of possible velocity and applicable force of frictionless objects in contact from a geometric model. IEEE Trans Robot.
Autom. 10, 309–322 (1994)
43. J. Ho, S. Ermon, Generative adversarial imitation learning. Advances in Neural Information
Processing Systems, vol. 29 (2016)
44. A. Hornung, L. Kobbelt, Hierarchical volumetric multi-view stereo reconstruction of manifold
surfaces based on dual graph embedding, in 2006 IEEE Computer Society Conference on
Computer Vision and Pattern Recognition (CVPR’06), vol. 1 (2006), pp. 503–510. https://
doi.org/10.1109/CVPR.2006.135
45. A. Hornung, L. Kobbelt, Robust and efficient photo-consistency estimation for volumetric 3d
reconstruction, in European Conference on Computer Vision (Springer, 2006), pp. 179–190
46. G. Hovland, B.J. McCarragher, Hidden Markov models as a process monitor in robotic
assembly. Int. J. Robot. Res. 17, 153–168 (1998)
47. G.E. Hovland, P. Sikka, B.J. McCarragher, Skill acquisition from human demonstration using
a hidden Markov model, in Proceedings of IEEE International Conference on Robotics and
Automation, vol. 3 (1996), pp. 2706–2711. https://doi.org/10.1109/ROBOT.1996.506571
48. S. Huang, Y. Yamakawa, T. Senoo, M. Ishikawa, Realizing peg-and-hole alignment with one
eye-in-hand high-speed camera, in 2013 IEEE/ASME International Conference on Advanced
Intelligent Mechatronics (2013), pp. 1127–1132
49. T. Inoue, G. De Magistris, A. Munawar, T. Yokoya, R. Tachibana, Deep reinforcement learning
for high precision assembly tasks, in 2017 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS) (IEEE, 2017), pp. 819–825
50. K. Itabashi, K. Hirana, T. Suzuki, S. Okuma, F. Fujiwara, Modelling and realization of the
peg-in-hole task based on hidden Markov model, in Proceedings. 1998 IEEE International
Conference on Robotics and Automation (Cat. No. 98CH36146), vol. 2 (IEEE, 1998), pp
1142–1147
51. Ž Jakovljević, P.B. Petrovic, J. Hodolic, Contact states recognition in robotic part mating
based on support vector machines. Int. J. Adv. Manuf. Technol. 59, 377–395 (2012)
52. Ž Jakovljević, P.B. Petrovic, V.D. Mikovic, M. Pajic, Fuzzy inference mechanism for
recognition of contact states in intelligent robotic assembly. J. Intell. Manuf. 25, 571–587
(2014)

## [Book2025 PDF p.37] Page 37

References

21

53. Z. Jakovljevic, P. Petrovic, Recognition of contact states in robotized assembly using qualitative wavelet based features and support vector machines, in Proceedings of the 36th
International MATADOR Conference (Springer, 2010), pp. 305–308
54. N. Jaquier, D. Ginsbourger, S. Calinon, Learning from demonstration with model-based gaussian process, in 3rd Annual Conference on Robot Learning, CoRL 2019, Osaka, Japan, October 30 - November 1, 2019, Proceedings, PMLR, PMLR, Proceedings of Machine Learning
Research, vol. 100 (2019), pp. 247–257
55. I.F. Jasim, P.W. Plapper, T-s fuzzy contact state recognition for compliant motion robotic tasks
using gravitational search-based clustering algorithm, in 2013 IEEE International Conference
on Fuzzy Systems (FUZZ-IEEE) pp. 1–8
56. I.F. Jasim, P.W. Plapper, Contact-state monitoring of force-guided robotic assembly tasks using
expectation maximization-based gaussian mixtures models. Int. J. Adv. Manuf. Techno. 73,
623–633 (2014)
57. I.F. Jasim, P.W. Plapper, H. Voos, Position identification in force-guided robotic peg-in-hole
assembly tasks. Proc. Cirp 23, 217–222 (2014)
58. I.F. Jasim, P.W. Plapper, H. Voos, Contact-state modelling in force-controlled robotic pegin-hole assembly processes of flexible objects using optimised gaussian mixtures. Proc. Inst.
Mech. Eng. Part B: J. Eng. Manuf. 231, 1448–1463 (2017)
59. M. Ji, J. Gall, H. Zheng, Y. Liu, L. Fang, Surfacenet: An end-to-end 3d neural network for
multiview stereopsis, in Proceedings of the IEEE International Conference on Computer
Vision (2017), pp. 2307–2315
60. Z. Jia, A. Bhatia, R.M. Aronson, D. Bourne, M.T. Mason, A survey of automated threaded
fastening. IEEE Trans. Autom. Sci. Eng. 16(1), 298–310 (2019). https://doi.org/10.1109/
TASE.2018.2835382
61. J. Jiang, Z. Huang, Z. Bi, X. Ma, G. Yu, State-of-the-art control strategies for robotic pih
assembly. Robot. Comput. Integr. Manuf. 65, 101894 (2020)
62. Y.L. Jiang, Z. Huang, B. Yang, W. Yang, A review of robotic assembly strategies for the full
operation procedure: planning, execution and evaluation. Robot. Comput. Integr Manuf. 78,
102366 (2022)
63. T. Johannink, S. Bahl, A. Nair, J. Luo, A. Kumar M. Loskyll, J.A. Ojea, E. Solowjow, S.
Levine, Residual reinforcement learning for robot control, in 2019 International Conference
on Robotics and Automation (ICRA) (IEEE, 2019), pp. 6023–6029
64. A. Kar, C. Häne, J. Malik, Learning a multi-view stereo machine. Advances in Neural
Information Processing Systems 30(2017)
65. A. Kendall, H. Martirosyan, S. Dasgupta, P. Henry, R. Kennedy, A. Bachrach, A. Bry, End-toend learning of geometry and context for deep stereo regression, in Proceedings of the IEEE
International Conference on Computer Vision (2017), pp. 66–75
66. B. Kim, J. Park, S. Park, S. Kang, Impedance learning for robotic contact tasks using natural
actor-critic algorithm. IEEE Trans. Syst. Man Cybernet. Part B (Cybernet.) 40, 433–443
(2010)
67. Y.L. Kim, H.C. Song, J.B. Song, Hole detection algorithm for chamferless square peg-in-hole
based on shape recognition using f/t sensor. Int. J. Precis. Eng. Manuf. 15, 425–432 (2014)
68. K. Kitagaki, T. Ogasawara, T. Suehiro, Methods to detect contact state by force sensing in
an edge mating task. in [1993] Proceedings IEEE International Conference on Robotics and
Automation (IEEE, 1993), pp. 701–706
69. P. Knobelreiter, C. Reinbacher, A. Shekhovtsov, T. Pock, End-to-end training of hybrid cnncrf models for stereo, in Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition (2017), pp. 2339–2348
70. J. Kober, J.A. Bagnell, J. Peters, Reinforcement learning in robotics: a survey. Int. J. Robot.
Res. 32(11), 1238–1274 (2013)
71. A. Kramberger, A. Gams, B. Nemec, C. Schou, D. Chrysostomou, O. Madsen, A. Ude, Transfer of contact skills to new environmental conditions, in 2016 IEEE-RAS 16th International
Conference on Humanoid Robots (Humanoids), pp. 668–675

## [Book2025 PDF p.38] Page 38

22

1 Introduction

72. H.Y.K. Lau, A hidden Markov model-based assembly contact recognition system. Mechatronics 13, 1001–1023 (2003)
73. Y. LeCun, Y. Bengio, G. Hinton, Deep learning. Nature 521(7553), 436 (2015)
74. H. Lee, J. Park, An active sensing strategy for contact location without tactile sensors using
robot geometry and kinematics. Auton. Robot. 36, 109–121 (2014)
75. S. Levine, N. Wagener, P. Abbeel, Learning contact-rich manipulation skills with guided
policy search, in 2015 IEEE International Conference on Robotics and Automation (ICRA)
(2015), pp. 156–163
76. S. Levine, P. Pastor, A. Krizhevsky, J. Ibarz, D. Quillen, Learning hand-eye coordination
for robotic grasping with deep learning and large-scale data collection. Int. J. Robot. Res.
37(4–5), 421–436 (2018)
77. M. Lhuillier, L. Quan, A quasi-dense approach to surface reconstruction from uncalibrated
images. IEEE Trans. Pattern Anal. Mach. Intell. 27(3), 418–433 (2005)
78. F. Li, Q. Jiang, S. Zhang, M. Wei, R. Song, Robot skill acquisition in assembly process using
deep reinforcement learning. Neurocomputing 345, 92–102 (2019)
79. R. Li, H. Qiao, Condition and strategy analysis for assembly based on attractive region in
environment. IEEE/ASME Trans. Mechatron. 22, 2218–2228 (2017)
80. T.P. Lillicrap, J.J. Hunt, A. Pritzel, N.M.O. Heess, T. Erez, Y. Tassa, D. Silver, D. Wierstr,
Continuous control with deep reinforcement learning. CoRR abs/1509.02971 (2016)
81. Y. Lin, J. Lloyd, A. Church, N.F. Lepora, Tactile gym 2.0: Sim-to-real deep reinforcement
learning for comparing low-cost high-resolution robot touch. IEEE Robot. Autom. Lett. 7(4),
10754–10761 (2022)
82. C. Liu, L. Song, K. Chen, J. Xu, Image-based visual servoing using a set for multiple pin-inhole assembly. Assembly Automation (2019)
83. S. Liu, Y.F. Li, D. Xing, Sensing and control for simultaneous precision peg-in-hole assembly
of multiple objects. IEEE Trans. Autom. Sci. Eng. 17, 310–324 (2020)
84. T. Lozano-Perez, M.T. Mason, R.H. Taylor, Automatic synthesis of fine-motion strategies for
robots. Int. J. Robot. Res. 3, 24–3 (1984)
85. J. Luo, E. Solowjow, C. Wen, J.A. Ojea, A.M. Agogino, A. Tamar, P. Abbeel, Reinforcement learning on variable impedance controller for high-precision robotic assembly, in 2019
International Conference on Robotics and Automation (ICRA) (IEEE, 2019), pp. 3080–3087
86. K. Luo, T. Guan, L. Ju, H. Huang, Y. Luo, P-mvsnet: Learning patch-wise matching confidence
aggregation for multi-view stereo, in The IEEE International Conference on Computer Vision
(ICCV) (2019)
87. Q.K. Luu, N.H. Nguyen et al., Simulation, learning, and application of vision-based tactile
sensing at large scale. IEEE Trans. Robot. (2023)
88. K.M. Lynch, F.C. Park, Modern Robotics (Cambridge University Press, 2017)
89. M.T. Mason, Compliance and force control for computer controlled manipulators. IEEE Trans.
Syst. Man Cybern. 11(6), 418–432 (1981)
90. B.J. McCarragher, H.H. Asada, A discrete event approach to the control of robotic assembly
tasks, in [1993] Proceedings IEEE International Conference on Robotics and Automation
vol. 1 (1993), pp. 331–336
91. B.J. McCarragher, H.H. Asada, Qualitative template matching using dynamic process models
for state transition recognition of robotic assembly. J. Dyn. Syst. Meas. Control-Trans. Asme
115, 261–269 (1993)
92. J. Miura, K. Ikeuchi, Task-oriented generation of visual sensing strategies in assembly tasks.
IEEE Trans. Pattern Anal. Mach. Intell. 20, 126–138 (1998)
93. H. Mosemann, A. Raue, F. Wahl, Classification and recognition of contact states for force
guided assembly, in SMC’98 Conference Proceedings. 1998 IEEE International Conference
on Systems, Man, and Cybernetics (Cat. No. 98CH36218), vol. 4 (IEEE, 1998), pp. 3400–3405
94. S. yo Muto, K. ichiro Shimokura, Accurate contact point detecting using force and velocity information complementarily, in [1993] Proceedings IEEE International Conference on
Robotics and Automation, vol. 1 (1993), pp. 738–744

## [Book2025 PDF p.39] Page 39

References

23

95. P. Nagarajan, S.S. Perumaal, B. Yogameena, Vision based pose estimation of multiple pegin-hole for robotic assembly, in International Conference on Computer Vision, Graphics, and
Image Processing (Springer, 2016), pp. 50–62
96. Y. Narang, B. Sundaralingam, M. Macklin, A. Mousavian, D. Fox, Sim-to-real for robotic
tactile sensing via physics-based simulation and learned latent projections, in 2021 IEEE
International Conference on Robotics and Automation (ICRA) (IEEE, 2021), pp. 6444–6451
97. Y.S. Narang, B. Sundaralingam, K. Van Wyk, A. Mousavian, D. Fox, Interpreting and predicting tactile signals for the syntouch biotac. Int. J. Robot. Res. 40(12–14), 1467–1487
(2021)
98. B. Nemec, F.J. Abu-Dakka, B. Ridge, A. Ude, J.A. Jørgensen, T.R. Savarimuthu, J. Jouffroy,
H.G. Petersen, N. Krüger, Transfer of assembly operations to new workpiece poses by adaptation to the desired force profile, in 2013 16th International Conference on Advanced Robotics
(ICAR) (2017), pp. 1–7
99. J.L. Nevins, D.E. Whitney, Assembly research. Automatica 16(6), 595–613 (1980)
100. W.S. Newman, Y. Zhao, Y.H. Pao, Interpretation of force and moment signals for compliant
peg-in-hole assembly, in Proceedings 2001 ICRA. IEEE International Conference on Robotics
and Automation (Cat. No. 01CH37164), vol. 1 (IEEE, 2001), pp. 571–576
101. P. Nguyen, F. Naghdy, Fuzzy control of automatic peg-in-hole insertion, in Proceedings of
Third Australian and New Zealand Conference on Intelligent Information Systems ANZIIS-95
(1995), pp 134–139
102. M. Nuttin, H. Van Brussel, Learning the peg-into-hole assembly operation with a connectionist
reinforcement technique. Comput. Ind. 33(1), 101–109 (1997)
103. M.S. Ohwovoriole, B. Roth, An extension of screw theory. J. Mech. Des. 103, 725–735 (1981)
104. A. Owens, J. Xiao, A. Torralba, W. Freeman, Shape anchors for data-driven multi-view reconstruction, in 2013 IEEE International Conference on Computer Vision (2013), pp. 33–40.
https://doi.org/10.1109/ICCV.2013.461
105. J. Pang, W. Sun, J.S. Ren, C. Yang, Q. Yan, Cascade residual learning: A two-stage convolutional neural network for stereo matching, in Proceedings of the IEEE International
Conference on Computer Vision (2017), pp. 887–895
106. D.H. Park, H. Hoffmann, P. Pastor, S. Schaal, Movement reproduction and obstacle avoidance with dynamic movement primitives and potential fields, in 8th IEEE-RAS International
Conference on Humanoid Robots, 2008. Humanoids 2008 (IEEE, 2008), pp. 91–98
107. H. Park, J.H. Bae, J.H. Park, M. Baeg, J. Park, Intuitive peg-in-hole assembly strategy with a
compliant manipulator. IEEE ISR 2013, 1–5 (2013)
108. H. Park, J. Park, D.H. Lee, J.H. Park, M.H. Baeg, J.H. Bae, Compliance-based robotic peg-inhole assembly strategy without force feedback. IEEE Trans. Ind. Electron. 64(8), 6299–6309
(2017)
109. Y. Park, S.C. Ryu, R.J. Black, K. Chau, B. Moslehi, M.R. Cutkosky, Exoskeletal forcesensing end-effectors with embedded optical fiber-bragg-grating sensors. IEEE Trans. Rob.
25, 1319–1331 (2009)
110. J. Pauli, A. Schmidt, G. Sommer, Vision-based integrated system for object inspection and
handling. Robot. Auton. Syst. 37, 297–309 (2001)
111. P.B. Petrovic, V.R. Milacic, A concept of an intelligent fuzzy control for assembly robot.
CIRP Ann. 47, 9–12 (1998)
112. A.S. Polydoros, L. Nalpantidis, Survey of model-based reinforcement learning: applications
on robotics. J. Intell. Robot. Syst. 86(2), 153–173 (2017)
113. H. Qiao, M. Wang, J. Su, li Jia S, Li R, The concept of “attractive region in environment”
and its application in high-precision tasks with low-precision systems. IEEE/ASME Trans.
Mechatron. 20, 2311–2327 (2015)
114. H. Ravichandar, A.S. Polydoros, S. Chernova, A. Billard, Recent advances in robot learning
from demonstration. Ann. Rev. Control Robot. Auton. Syst. 3, 297–330 (2020)
115. T. Ren, Y. Dong, D. Wu, K. Chen, Learning-based variable compliance control for robotic
assembly. J. Mech. Robot. 10(6), 061008 (2018)

## [Book2025 PDF p.40] Page 40

24

1 Introduction

116. G. Riegler, A. Osman Ulusoy, A. Geiger, Octnet: Learning deep 3d representations at high resolutions, in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition
(2017), pp. 3577–3586
117. M. Rothermel, K. Wenzel, D. Fritsch, N. Haala, Sure: Photogrammetric surface reconstruction
from imagery, in Proceedings LC3D Workshop, Berlin, vol 8 (2012), p. 2
118. K. Sathirakul, R.H. Sturges, Jamming conditions for multiple peg-in-hole assemblies.
Robotica 16, 329–345 (1998)
119. S. Schaal, Learning from demonstration, in Advances in Neural Information Processing
Systems (1997), pp. 1040–1046
120. G. Schoettler, A. Nair, J. Luo, S. Bahl, S. Levine, Deep reinforcement learning for industrial
insertion tasks with visual inputs and natural rewards, in IEEE/RSJ International Conference
on Intelligent Robots and Systems, IROS 2020, Las Vegas, NV, USA, October 24, 2020 January 24, 2021. (IEEE, 2020), pp. 5548–5555
121. J.D. Schutter, H. Bruyninckx, S. Dutré, J.D. Geeter, J. Katupitiya, S. Demey, T. Lefebvre,
Estimating first-order geometric parameters and monitoring contact transitions during forcecontrolled compliant motion. Int. J. Robot. Res. 18, 1161–1184 (1999)
122. A. Seki, M. Pollefeys, Sgm-nets: Semi-global matching with neural networks, in Proceedings
of the IEEE Conference on Computer Vision and Pattern Recognition (2017), pp. 231–240
123. B. Shirinzadeh, Y. Zhong, P.D.W. Tilakaratna, Y. Tian, M.M. Dalvand, A hybrid contact state
analysis methodology for robotic-based adjustment of cylindrical pair. Int. J. Adv. Manuf.
Technol. 52, 329–342 (2011)
124. Z. Si, W. Yuan, Taxim: an example-based simulation model for gelsight tactile sensors. IEEE
Robot. Autom. Lett. 7(2), 2361–2368 (2022)
125. D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, M. Riedmiller, Deterministic policy
gradient algorithms, in Proceedings of the 31st International Conference on International
Conference on Machine Learning - Volume 32, JMLR, ICML’14 (2014), pp. I–387–I–395
126. S. Simunovic, Force information in assembly processes, in 5th International Symposium on
Industrial Robots (1975), pp. 415–431
127. S.N. Sinha, P. Mordohai, M. Pollefeys, Multi-view stereo via graph cuts on the dual of an
adaptive tetrahedral mesh, in 2007 IEEE 11th International Conference on Computer Vision
(2007), pp. 1–8. https://doi.org/10.1109/ICCV.2007.4408997
128. M. Skubic, R.A. Volz, Identifying single-ended contact formations from force sensor patterns.
IEEE Trans. Robot. Autom. 16, 597–603 (2000)
129. M. Skubic, S.P. Castriannii, R.A. Volz, Identifying contact formations from force signals: a comparison of fuzzy and neural network classifiers, in Proceedings of International
Conference on Neural Networks (ICNN’97), vol. 3 (IEEE, 1997), pp. 1623–1628
130. C. Son, A neural/fuzzy optimal process model for robotic part assembly. Int. J. Mach. Tools
Manuf. 41, 1783–1794 (2001)
131. H.C. Song, Y.L. Kim, J.B. Song, Automated guidance of peg-in-hole assembly tasks for
complex-shaped parts, in 2014 IEEE/RSJ International Conference on Intelligent Robots and
Systems (2014), pp. 4517–4522
132. H.C. Song, Y.L. Kim, J.B. Song, Guidance algorithm for complex-shape peg-in-hole strategy
based on geometrical information and force control. Adv. Robot. 30, 552–563 (2016)
133. J. Su, H. Qiao, C. Liu, Z. Ou, A new insertion strategy for a peg in an unfixed hole of the
piston rod assembly. Int. J. Adv. Manuf. Technol. 59, 1211–1225 (2012)
134. R. Suarez, L. Basanez, M. Nuttin, H. Van Brussel, J. Rosell, Learning versus analytical
approach to contact estimation in assembly tasks with robots, in Proceedings of the 7th
International Conference on Advanced Robotics (1995), pp. 769–775
135. R. Suárez, L. Basañez, J. Rosell Using configuration and force sensing in assembly task
planning and execution, in Proceedings IEEE International Symposium on Assembly and
Task Planning (1995) pp. 273–279
136. F. Suarez-Ruiz, X. Zhou, Q.C. Pham, Can robots assemble an ikea chair? Sci. Robot. 3 (2018)
137. R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction (MIT Press, 2018)

## [Book2025 PDF p.41] Page 41

References

25

138. P. Tang, J. Xiao, Automatic generation of high-level contact state space between planar
curved objects, in Proceedings of the 2005 IEEE International Conference on Robotics and
Automation (2005), pp. 3601–3606
139. T. Tang, H.C. Lin, M. Tomizuka, A learning-based framework for robot peg-hole-insertion,
in ASME 2015 Dynamic Systems and Control Conference, American Society of Mechanical
Engineers, pp V002T27A002–V002T27A002 (2015)
140. T. Tang, H.C. Lin, Y. Zhao, Y. Fan, W. Chen, M. Tomizuka, Autonomous alignment of peg
and hole by force/torque measurement for robotic assembly, in 2016 IEEE International
Conference on Automation Science and Engineering (CASE) (IEEE, 2016), pp. 162–167
141. T. Tang, H.C. Lin, Y. Zhao, Y. Fan, W. Chen, M. Tomizuka, Teach industrial robots peg-holeinsertion by human demonstration, in 2016 IEEE International Conference on Advanced
Intelligent Mechatronics (AIM) (IEEE, 2016), pp. 488–494
142. M. Tatarchenko, A. Dosovitskiy, T. Brox, Octree generating networks: Efficient convolutional architectures for high-resolution 3d outputs, in Proceedings of the IEEE International
Conference on Computer Vision (2017), pp. 2088–2096
143. G. Thomas, M. Chien, A. Tamar, J.A. Ojea, P. Abbeel, Learning robotic assembly from cad,
in 2018 IEEE International Conference on Robotics and Automation (ICRA) (IEEE, 2018),
pp. 3524–3531
144. C. Tsaprounis, N. Aspragathos, Contact point identification in robot assembly strategies under
uncertainty. Robotica 16(6), 679–690 (1998)
145. A. Ude, A. Gams, T. Asfour, J. Morimoto, Task-specific generalization of discrete and periodic
dynamic movement primitives. IEEE Trans. Rob. 26(5), 800–815 (2010)
146. P. Varin, L. Grossman, S. Kuindersma, A comparison of action spaces for learning manipulation tasks, in 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems,
IROS 2019, Macau, SAR, China, November 3-8, 2019 (IEEE, 2019), pp. 6015–6021
147. M. Vecerík, T. Hester, J. Scholz, F. Wang, O. Pietquin, B. Piot, N.M.O. Heess, T. Rothörl,
T. Lampe, M.A. Riedmiller, Leveraging demonstrations for deep reinforcement learning on
robotics problems with sparse rewards (2017). ArXiv abs/1707.08817
148. M. Vecerík, O.O. Sushkov, D. Barker, T. Rothörl, T. Hester, J. Scholz, A practical approach
to insertion with variable socket position using deep reinforcement learning, in 2019
International Conference on Robotics and Automation (ICRA) (2019), pp. 754–760
149. A. Wan, J. Xu, H. Chen, S. Zhang, K. Chen, Optimal path planning and control of assembly robots for hard-measuring easy-deformation assemblies. IEEE/ASME Trans. Mechatron.
22(4), 1600–1609 (2017)
150. P.S. Wang, Y. Liu, Y.X. Guo, C.Y. Sun, X. Tong, O-CNN: octree-based convolutional neural
networks for 3D shape analysis. ACM Trans. Graph. (SIGGRAPH) 36(4) (2017)
151. S. Wang, S. Yang, Research of depth information acquisition with two stage structured light
method. IEEE Int. Conf. Prog. Inf. Comput. 2, 800–803 (2010)
152. S. Wang, M. Lambeta, P.W. Chou, R. Calandra, Tacto: a fast, flexible, and open-source simulator for high-resolution vision-based tactile sensors. IEEE Robot. Autom. Lett. 7(2), 3930–3937
(2022)
153. D.E. Whitney, Quasi-static assembly of compliantly supported rigid parts. J. Dyn. Syst. Meas.
Contr. 104(1), 65–77 (1982)
154. D.E. Whitney, Mechanical Assemblies: Their Design, Manufacture, and Role in Product
Development, vol. 1 (Oxford University Press, New York, 2004)
155. Y. Xia, Y. Yin, Z. Chen, Dynamic analysis for peg-in-hole assembly with contact deformation.
Int. J. Adv. Manuf. Technol. 30, 118–128 (2006)
156. J. Xiao, Automatic determination of topological contacts in the presence of sensing uncertainties, in [1993] Proceedings IEEE International Conference on Robotics and Automation,
vol. 1 (1993), pp. 65–70
157. J. Xiao, L. Liu, Contact states: representation and recognizability in the presence of uncertainties, in Proceedings 1998 IEEE/RSJ International Conference on Intelligent Robots and
Systems Innovations in Theory, Practice and Applications (Cat No98CH36190), vol. 2 (1998),
pp. 1151–1156

## [Book2025 PDF p.42] Page 42

26

1 Introduction

158. J. Xu, Z. Hou, W. Wang, B. Xu, K. Zhang, K. Chen, Feedback deep deterministic policy
gradient with fuzzy reward for robotic multiple peg-in-hole assembly tasks. IEEE Trans. Ind.
Inf. 15, 1658–1667 (2019)
159. J. Xu, S. Kim, T. Chen, A.R. Garcia, P. Agrawal, W. Matusik, S. Sueda, Efficient tactile
simulation with differentiability for robotic manipulation, in 6th Annual Conference on Robot
Learning (2022). https://openreview.net/forum?id=6BIffCl6gsM
160. L. Xu, C. Wang, Z. Bi, J. Yu, Autoassem: an automated assembly planning system for complex
products. IEEE Trans. Ind. Inf. 8, 669–678 (2012)
161. Y. Xu, R.P. Paul, A robot compliant wrist system for automated assembly, in Proceedings.,
IEEE International Conference on Robotics and Automation (IEEE, 1990), pp. 1750–1755
162. Y. Xu, J. Yang, Towards human-robot coordination: skill modeling and transferring via hidden
Markov model, in Proceedings of 1995 IEEE International Conference on Robotics and
Automation, vol. 2 (IEEE, 1995), pp. 1906–1911
163. Y. Xue, J. Chen, W. Wan, Y. Huang, C. Yu, T. Li, J. Bao, Mvscrf: Learning multi-view stereo
with conditional random fields, in The IEEE International Conference on Computer Vision
(ICCV) (2019)
164. Y. Yao, Z. Luo, S. Li, T. Shen, T. Fang, L. Quan, Recurrent mvsnet for high-resolution
multi-view stereo depth inference. Computer Vision and Pattern Recognition (CVPR) (2019)
165. A. Zaharescu, E. Boyer, R. Horaud, Transformesh: a topology-adaptive mesh-based approach
to surface evolution, in Asian Conference on Computer Vision (Springer, 2007), pp. 166–175
166. K. Zhang, J. Xu, H. Chen, J. Zhao, K. Chen, Jamming analysis and force control for flexible
dual peg-in-hole assembly. IEEE Trans. Ind. Electron. 66(3), 1930–1939 (2019). https://doi.
org/10.1109/TIE.2018.2838069
167. Y. Zhao, A. Al-Yacoub, Y.M. Goh, L. Justham, N. Lohse, M.R. Jackson, Human skill capture:
A hidden Markov model of force and torque data in peg-in-a-hole assembly process, in 2016
IEEE International Conference on Systems, Man, and Cybernetics (SMC) (IEEE, 2016), pp.
000655–000660
168. Y. Zhao, X. Jing, K. Qian, D.F. Gomes, S. Luo, Skill generalization of tubular object
manipulation with tactile sensing and sim2real learning. Robot. Auton. Syst. 160, 104321
(2023)
169. H. Zhou, B. Ummenhofer, T. Brox, Deeptam: Deep tracking and mapping, in Proceedings of
the European Conference on Computer Vision (ECCV) (2018), pp. 822–838
170. Z. Zhu, H. Hu, Robot learning from demonstration in robotic assembly: a survey. Robotics
7(2), 17 (2018)

## [Book2025 PDF p.43] Page 43

Chapter 2

Multi-view Stereo Sensing Method

2.1 Introduction
The geometry information of the peg and the hole is critical for PiH assembly. MVS
aims to reconstruct the dense geometry of a 3D object from a sequence of images and
corresponding camera poses and intrinsic parameters. Recent learning-based MVS
methods [9, 11, 21] have shown great success compared with their traditional counterparts as learning-based approaches are able to learn to take advantage of scene
global semantic information, including object materials, specularity, 3D geometry
priors, and environmental illumination, to get more robust matching and more complete reconstruction. Most of these approaches apply dense multi-scale 3D CNNs to
predict the depth map or voxel occupancy. However, 3D CNNs require memory cubic
to the model resolution, which can be potentially prohibitive to achieving optimal
performance. While Tatarchenko et al. [15] addressed this problem by progressively
generating an Octree structure, the quantization artifacts brought by grid partitioning
still remain, and errors may accumulate since the tree is generated layer by layer.
Moreover, MVS fundamentally relies on finding photo-consistency across the input
images. However, image appearance cues from invisible views, which include being
occluded and out of Field of View (FOV), are not consistent with those from visible
views, which is misguiding for accurate depth prediction and therefore needs robust
handling.
In this chapter, we propose a novel VA-Point-MVSNet, where the target scene is
directly processed as a point cloud, a more efficient representation, particularly when
the 3D resolution is high. Our framework is composed of two steps: first, in order to
carve out the approximate object surface from the whole scene, an initial coarse depth
map is generated by a relatively small 3D cost volume and then converted to a point
cloud. Subsequently, our novel PointFlow module is applied to iteratively regress
accurate and dense point clouds from the initial point cloud. Similar to ResNet [7],
we explicitly formulate the PointFlow to predict the residual between the depth of
the current iteration and that of the ground truth. The 3D flow is estimated based on
© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_2

27

## [Book2025 PDF p.44] Page 44

28

2 Multi-view Stereo Sensing Method

Fig. 2.1 VA-Point-MVSNet performs MVS reconstruction in a coarse-to-fine fashion, learning to
predict the 3D flow of each point to the ground truth surface based on geometry priors and 2D image
appearance cues dynamically fetched from multi-view images and regress accurate and dense point
clouds iteratively

geometry priors inferred from the predicted point cloud and the 2D image appearance
cues dynamically fetched from multi-view input images (Fig. 2.1). Moreover, in order
to take into account visibility, including occlusion and out of FOV, for accurate MVS
reconstruction, we propose a number of network structure alternatives that infer the
visibility of each view for the multi-view feature aggregation.
We find that our VA-Point-MVSNet framework enjoys advantages in accuracy,
efficiency, and flexibility when it is compared with previous MVS methods that
are built upon a predefined 3D cost volume with a fixed resolution to aggregate
information from views. Our method adaptively samples potential surface points
in the 3D space. It keeps the continuity of the surface structure naturally, which is
necessary for high precision reconstruction. Furthermore, because our network only
processes valid information near the object surface instead of the whole 3D space
as is the case in 3D CNNs, the computation is much more efficient. The adaptive
refinement scheme allows us to first peek at the scene at a coarse resolution and
then density the reconstructed point cloud only in the Region of Interest (ROI).
For scenarios such as interaction-oriented robot vision, this flexibility would result
in saving of computational power. Lastly, the visibility-aware multi-view feature
aggregation allows the network to aggregate multi-view appearance cues while taking
into account visibility, which excludes misguiding image information from invisible
views and leads to improved reconstruction quality.
Our method achieves state-of-the-art performance on standard MVS benchmarks
among learning-based methods, including DTU [1] and Tanks and Temples [12].
Compared with previous state-of-the-arts, our method produces better results in terms
of both completeness and overall quality.

## [Book2025 PDF p.45] Page 45

2.2 Method

29

2.2 Method
This section describes the detailed network architecture of VA-Point-MVSNet. Our
method can be divided into two steps, coarse depth prediction and iterative depth
refinement. First, we introduce the visibility-aware feature aggregation (Sect. 2.2.1),
which reasons about the visibility of source images from image appearance cues and
aggregates multi-view image information while considering visibility. The visibilityaware feature aggregation is utilized in both coarse depth prediction and iterative
depth refinement. Secondly, we describe the coarse depth map prediction. Let .I0
N
denote the reference image and .{Ii }i=1
denote a set of its neighboring source images.
Since the resolution is low, the existing volumetric MVS method has sufficient efficiency and can be used to predict a coarse depth map for .I0 (Sect. 2.2.2). Then
we describe the 2D-3D feature lifting (Sect. 2.2.3), which associates the 2D image
information with 3D geometry priors. Finally, we propose our novel PointFlow module (Sect. 2.2.4) to iteratively refine the input depth map to higher resolution with
improved accuracy.

2.2.1 Visibility-Aware Feature Aggregation
The main intuition for depth estimation is multi-view photo-consistency, that image
projections of the reconstructed shape should be consistent across visible images.
Thus, features of multiple input views are aggregated together for later depth prediction. Various methods for feature aggregation have been proposed, such as average [10] and variance [21]. However, previous methods are not able to handle invisible views and can lead to incorrect feature matching. So we design novel feature
aggregation structures that take visibility into consideration.
Let .F0 denote the reference view feature, .Fi (i = 1, . . . , N ) denote the source
view feature, and .C denote the generated feature. The multi-view feature aggregation
processes .{Fi } to generate .C:
C = f ({Fi }), i = 0, . . . , N .

.

(2.1)

We observe that effective multi-view feature aggregation structures should meet
the following properties:
• Arbitrary number of views. As the number of input views can be different for
training and evaluation, the feature aggregation should be generalizable to an
arbitrary number of views.
• Unordered. 3D reconstruction is irrelevant to the order of input views. Thus, our
feature aggregation module should be invariant to the permutation of source view
feeding order.

## [Book2025 PDF p.46] Page 46

30

2 Multi-view Stereo Sensing Method

Fig. 2.2 Overview of VA-Point-MVSNet architecture. The visibility-aware feature aggregation
module aggregates the multi-view image appearance cues to generate visibility-robust features for
coarse depth prediction and depth refinement separately. A coarse depth map is first predicted
with low GPU memory and computation cost and then unprojected to a point cloud along with
hypothesized points. For each point, the feature is fetched from the multi-view image feature
pyramid dynamically. The PointFlow module uses the feature-augmented point cloud for depth
residual prediction, and the depth map is refined iteratively along with up-sampling

• Differentiable. As shown in Fig. 2.2, the feature aggregation module serves as an
interface between image feature extraction and 3D geometry inference. It has to
be differentiable such that the whole framework can be trained end-to-end.
• Robust to invisibility. The invisible views will obstruct the photo-consistency
across views for ground truth surface. Under the multi-view photo-consistency
assumption, depth estimation can be wrong if we try to match the feature of
invisible views, including occlusion and out of FOV. In other words, the feature
aggregation process needs to take each input view visibility into consideration.
Following the above philosophy, we compare feature aggregation operations
applied in recent works [10, 21] and propose novel aggregation structures to address
the visibility issue. See Fig. 2.3 for visualization. The average operation (Fig. 2.3a)
applied in [10] meets some properties, but it expresses no information about photoconsistency across views and cannot handle the visibility problem. The element-wise
max-pooling operation (Fig. 2.3b) also does not take into account the relationship
of appearances between the reference view and source views. The variance operation (Fig. 2.3c) used in [21] measures the appearance difference across all views but
does not count for the visibility issue.
Vis-avg We first propose the visibility-aware average operation (Fig. 2.3d) by including a network to infer the visibility for each source view. Note that pixels are all visible
for the reference view .F0 . Each source view .Fi is concatenated with the reference
view .F0 to predict the relationship separately. The subsequent average operation
combines the learned relationship across all source views and generates .C.
Vis-max Similarly, a visibility-aware max-pooling operation (Fig. 2.3e) is designed
by replacing the average operation with max-pooling. From the relationship between

## [Book2025 PDF p.47] Page 47

2.2 Method

31

Fig. 2.3 Different structures of multi-view feature aggregation. a “avg”: average operation
applied in [10]; b “max”: element-wise max-pooling operation; c “var”: variance operation applied
in [21]; d“vis-avg”: our visibility-aware average operation; e “vis-max”: our visibility-aware maxpooling operation; f“vis-var”: our visibility-aware variance operation. “Shared MLP” stands for
multi-layer perceptron with shared weights for all input features. Batchnorm and ReLU are used
for all layers except the last layer

the reference view and each source view, the max-pooling operation is able to preserve the most significant one for further depth prediction while excluding others,
which improves the robustness to potential causes of mismatches like occlusion and
highlights.
Vis-var Furthermore, we propose a visibility-aware variance operation (Fig. 2.3f):
N
C=

.

i=0 (ωi · Fi
N
i=0 ωi

2

)


−

N
i=0 (ωi · Fi )
N
i=0 ωi

2
,

(2.2)

where .ωi ∈ [0, 1] is the visibility mask of view .i. Note that .ω0 = 1 as we predict
the depth map in the reference view. For source views, a NN module is applied for
visibility prediction. The visibility module architecture is explained in the paragraph
below. Our “vis-var” operation measures the appearance variance across all visible
views explicitly.
As demonstrated in [18], for visible views, the correlation between the reference
view and source view with regard to depth shows a significant local maximum at the

## [Book2025 PDF p.48] Page 48

32

2 Multi-view Stereo Sensing Method

Fig. 2.4 Network architecture of the visibility prediction module. The module takes as input the
feature map of reference view .F0 and that of source view .Fi , and outputs the visibility mask for
view .i. “Shared MLP” stands for multi-layer perceptron with shared weights across all pixels, such
that the visibility of each pixel is predicted independently. The element-wise sigmoid function is
applied on the last layer to constrain the output in the range of .[0, 1]. Normalized depth is computed


by .dk = d k − dmin /(dmax − dmin )

correct depth. To utilize this observation, our visibility prediction module (Fig. 2.4)
warps the source feature map into different depth planes at the reference camera.
The projected source view feature is concatenated with the reference view feature
and the normalized depth .dk . The visibility module takes the compromised feature
and aggregates processed depth plane features using max-pooling operation. Note
that max-pooling operation can handle an arbitrary number of depth planes during
training and evaluation. The visibility prediction module can be trained either in a
supervised fashion or an unsupervised fashion as in Sect. 2.3.1.

2.2.2 Coarse Depth Prediction
Recently, learning-based MVS [10, 11, 21] achieves state-of-the-art performance
using multi-scale 3D CNNs on cost volume regularization. However, this step could
be extremely memory expensive as the memory requirement is increasing cubically

## [Book2025 PDF p.49] Page 49

2.2 Method

33

as the cost volume resolution grows. Taking memory and time into consideration, we
use the recently proposed MVSNet [21] to predict a relatively low-resolution depth
map.
Given the images and corresponding camera parameters, MVSNet [21] builds a
3D cost volume upon the reference camera frustum. Then the initial depth map for the
reference view is regressed through multi-scale 3D CNNs and the soft argmin [12]
operation. In MVSNet, feature maps are downsampled to .1/4 of the original input
image in each dimension and the number of virtual depth planes is .256 for both
training and evaluation. On the other hand, in our coarse depth estimation network, the
cost volume is constructed with feature maps of .1/8 the size of the reference image,
containing .48 and .96 virtual depth planes for training and evaluation, respectively.
Therefore, our memory usage of this 3D feature volume is about .1/20 of that in
MVSNet. Moreover, the visibility-aware feature aggregation (Sect. 2.2.1) is adopted
for the cost volume construction, where MVSNet utilizes “var” which does not count
for the visibility issue.

2.2.3 2D-3D Feature Lifting
Image Feature Pyramid Learning-based image features have been demonstrated to
be critical to boosting up dense pixel correspondence quality [14, 21]. In order to
endow points with a larger receptive field of contextual information at multiple scales,
we construct a 3-scale feature pyramid. 2D convolutional networks with stride .2 are
applied to downsample the feature map, and each last layer before the downsampling
is extracted to construct the final feature pyramid .{Fi1 , Fi2 , Fi3 } for image .Ii . Similar
to common MVS methods [10, 21], feature pyramids are shared among all input
images.
Dynamic Feature Fetching The point feature used in our network is compromised
of the aggregated multi-view image feature .C p with the normalized 3D coordinates
in the world space .X p . We will introduce them separately.
Image appearance features for each 3D point can be fetched from the multiview feature maps using a differentiable unprojection given corresponding camera
parameters. Note that features .Fi1 , Fi2 , Fi3 are at different image resolutions, thus the
camera intrinsic matrix should be scaled at each level of the feature maps for correct
feature warping. The feature of view .i is generated using concatenation:
Fi = concat[Fi1 , Fi2 , Fi3 ].

.

(2.3)

To form the features residing at each 3D point, we aggregate the multi-view
features using the visibility-aware feature aggregation module (Sect. 2.2.1) and do a
concatenation of the aggregated feature and the normalized point coordinates:

## [Book2025 PDF p.50] Page 50

34

2 Multi-view Stereo Sensing Method

G p = concat[C p , X p ].

.

(2.4)

This feature-augmented point .G p is the input to our PointFlow module.
As shall be seen in the next section, since we are predicting the depth residual
iteratively, we update the point position .X p after each iteration and fetch the point
feature from the multi-view images, an operation we name as dynamic feature fetching. Note that this step is distinct from cost-volume-based methods, by which the
fetched features at each voxel are determined by the fixed space partition of the scene.
In contrast, our method can fetch features from different areas of images dynamically
according to the updated point position. Therefore, we can concentrate on the ROI
in the feature maps, instead of treating them uniformly.

2.2.4 PointFlow
Depth maps generated from Sect. 2.2.2 have limited accuracy due to the low spatial resolution of 3D cost volume. We propose PointFlow, our novel approach to
iteratively refine the depth map.
With known camera parameters, we first unproject the depth map to be a 3D point
cloud. For each point, we aim to estimate its displacement to the ground truth surface
along the reference camera direction by observing its neighboring points from all
views, so as to push the points to flow to the target surface. Next, we discuss the
components of our module in detail.
Point Hypothesis Generation It is non-trivial to regress the depth displacement of
each point from the extracted image feature maps. Due to perspective transformation,
the spatial context embedded in 2D feature maps cannot reflect the proximity in 3D
Euclidean space.
In order to facilitate the modeling of network, we propose to generate a sequence of
point hypotheses .{p̃k } with different displacements along the reference camera direction as shown in Fig. 2.5. Let .t denotes the normalized reference camera direction,
and.s denotes the displacement step size. For an unprojected point.p, its hypothesized
point set .{p̃k } is generated by
p̃ = p + kst, k = −m, . . . , m.

. k

(2.5)

These point hypotheses gather the necessary neighborhood image feature information at different depths, and combine the image information with spatial geometry
relationship, which helps the network to infer the displacement.
Edge Convolution Classical MVS methods have demonstrated that local neighborhood is important for robust depth prediction. Similarly, we take the strategy of recent
work DGCNN [19] to enrich feature propagation between neighboring points. As
shown in Fig. 2.5, a directed graph is constructed on the point set using .k nearest

## [Book2025 PDF p.51] Page 51

2.2 Method

35

Fig. 2.5 Illustration of point hypotheses generation and edge construction: For each unprojected
point .p, the .2m point hypotheses .{p̃k } are generated along the reference camera direction. Directed
edges are constructed between each hypothesized point and its kNN points for edge convolution.

neighbors (kNN), such that local geometric structure information could be used for
the feature propagation of points.
The edge convolution is defined as:
Gp =

.



q∈kNN(p)



h  G p , G p − Gq ,

(2.6)

where .G p , Gq are the input features of center point .p and neighbor point .q, .Gp is
the output feature of point .p, .h  is a learnable non-linear function parameterized
by ., and . is a channel-wise symmetric aggregation operation. There are multiple
options for the symmetry operation, including max-pooling, average pooling, and
weighted sum. We compare max-pooling and average pooling and observe similar
performance after tuning hyper-parameters carefully.
Flow Prediction The network architecture for flow prediction is shown in Fig. 2.6.
The input is a feature-augmented point cloud, and the output is a depth residual map.
We use three EdgeConv layers to aggregate point features at different scales of the
neighborhood. Shortcut connections are used to include all the EdgeConv outputs

Fig. 2.6 Network architecture of the proposed PointFlow module

## [Book2025 PDF p.52] Page 52

36

2 Multi-view Stereo Sensing Method

as local point features. Finally, a shared MLP is used to transform the point-wise
features, which outputs a probability scalar with softmax among hypothesized points
of each unprojected point. The displacement of the unprojected points is predicted
as the probabilistic weighted sum of the displacement among all point hypotheses:
m


d p = E(ks) =

.

ks × Prob(p̃k ).

(2.7)

k=−m

Note that this operation is differentiable. The output depth residual map is obtained
by projecting the displacement back, which will be added to the initial input depth
map for depth refinement.
Iterative Refinement with Upsampling Because of the flexibility of our point-based
network architecture, the flow prediction can be performed iteratively, which is much
harder for 3D cost-volume-based methods, because the space partitioning is fixed
after the construction of cost volume. For depth map .D(i) from coarse prediction or
former residual prediction, we can first upsample it using nearest neighbor to higher
spatial resolution and then perform the flow prediction to obtain.D(i+1) . Moreover, we
decrease the depth interval .s between the unprojected points and hypothesized points
at each iteration, so that more accurate displacement can be predicted by capturing
more detailed features from closer point hypotheses.

2.2.5 Training Loss
Similar to most deep MVS networks, we treat this problem as a regression task and
train the network with the . L 1 loss, which measures the absolute difference between
the predicted depth map and the ground truth depth map. Losses for the initial depth
map and iteratively refined ones are all considered:
l


⎛

(i) 
⎝λ
.Loss =
s (i) p∈P
i=0

⎞
DGT ( p) − D(i) ( p) 1 ⎠ ,

(2.8)

valid

where .Pvalid represents the valid ground truth pixel set and .l is the iteration number.
The weight .λ(i) is set to 1.0 in training for all the iterations.

2.3 Experiments
We now present an extensive and comprehensive evaluation on both synthetic and real
data. Due to the fact that the depth captured for real data is usually not complete and
accurate, which is indispensable for visibility mask computation, we first generate

## [Book2025 PDF p.53] Page 53

2.3 Experiments

37

a small synthetic dataset to justify the effectiveness of our visibility-aware multiview feature aggregation structures (Sect. 2.3.1). Secondly, we evaluate our VAPoint-MVSNet on the DTU benchmark [1] (Sect. 2.3.2). Then we provide detailed
experiments to analyze our network design (Sect. 2.3.3). At last, we show the generalizability of our network (Sect. 2.3.4).

2.3.1 Experiments on Synthetic Data
Dataset Generation
We generate a synthetic dataset as shown in Fig. 2.7 using the YCB object dataset [2].
We first generate physically-plausible densely cluttered layouts for multiple objects
using the physics simulator MuJoCo [16]. Then each scene is rendered with nine
given camera configurations. We use path tracing renderer for realistic looking. The
resolution of rendered images is .512 × 512. The intensities and positions of lights
are set randomly for each scene. We create 400 training scenes and 100 testing
scenes. The networks are trained with the three views with red or blue border in
Fig. 2.7 and tested with source views chosen from the eight views that can be novel
to the networks. Since the visibility only depends on the local photo-consistency,
we assume the networks are able to learn to infer the visibility from the local image
information even for views that are unseen in the training set.

Comparison of Multi-View Aggregation Structures
All the six structures in Sect. 2.2.1 are trained and evaluated on the synthetic dataset.
The coarse prediction network is trained alone for 40 epochs, and then, the model
is trained end-to-end for another 176 epochs. The batch size is set as 4. The number
of views is set as 3 and 7 for training and evaluation, respectively. Percentage of
inliers of depth map (.d < δ, d < 3δ) are used as evaluation metrics, and the
comparison result is shown in Table 2.1. .δc = 19.15mm, δf = 0.375 ∗ δc = 7.18mm
for coarse depth map and refined depth map respectively, which are the depth intervals
between virtual planes or point hypotheses. The hyper-parameter 0.375 is chosen
empirically based on the experiments on the synthetic dataset and DTU dataset.
Our visibility-aware multi-view feature aggregation module can improve the depth
prediction accuracy significantly, especially in areas that are invisible in source views,
because by taking into account the appearance difference between the reference
view and each source view, our module can aggregate visible multi-view appearance
effectively while excluding misguiding invisible views.

## [Book2025 PDF p.54] Page 54

38

2 Multi-view Stereo Sensing Method

Fig. 2.7 Illustration of our synthetic dataset: rendered images for nine known camera configurations, image with red border is the reference view, images with blue border are the source views
used for training

Supervised Learning Versus Unsupervised Learning
In our “vis-var” structure, we predict the visibility mask of each source view explicitly. Given the complete and accurate depth maps generated from the synthetic data,
we obtain the ground truth visibility masks through cross-check (Fig. 2.8). Our visibility prediction is supervised by the ground truth mask. An. L 1 loss term for visibility
prediction is added to our depth prediction loss (Eq. 2.8) as

VGT ( p) − Vpred ( p) 1 ,
. L vis = λvis
(2.9)
p∈Pvalid

where .VGT is the ground truth visibility mask which equals 1 at visible pixels and 0
at invisible ones. The weight .λvis is set to 0.01 in training.

## [Book2025 PDF p.55] Page 55

2.3 Experiments

39

Table 2.1 Comparison results of predicted depth accuracy for different multi-view feature aggregation structures. Inlier ratios are used as metrics. “Invis” stands for areas in the reference view
that are invisible in at least one source view, and “Fully-vis” stands for areas that are visible in all
source views. .δc = 19.15mm, δf = 7.18mm
Coarse depth map
Structure
.< δc
.< 3δc
Invis .< δc
Invis .< 3δc Fully-vis
Fully-vis
.< δc
.< 3δc
avg
0.8931
max
0.9347
var
0.9187
vis-avg
0.9478
vis-max
0.9462
vis-var
0.9242
Refined depth map
Structure
.< δ f

0.9842
0.9887
0.9862
0.9917
0.9908
0.9878

0.8226
0.8744
0.8099
0.9032
0.9016
0.8315

0.9652
0.9725
0.9507
0.9817
0.9806
0.9577

.< 3δ f

Invis .< δ f

Invis .< 3δ f

avg
max
var
vis-avg
vis-max
vis-var

0.9485
0.9652
0.9636
0.9706
0.9721
0.9665

0.8107
0.8396
0.8054
0.8636
0.8643
0.8407

0.9353
0.9443
0.9384
0.9518
0.9493
0.9391

0.7847
0.8863
0.8679
0.9035
0.8982
0.8899

0.9170
0.9552
0.9499
0.9630
0.9615
0.9510

0.9907
0.9943
0.9964
0.9951
0.9943
0.9965

Fully-vis

Fully-vis

.< δ f

.< 3δ f

0.9130
0.9553
0.9524
0.9581
0.9602
0.9529

0.9866
0.9913
0.9926
0.9902
0.9902
0.9908

Fig. 2.8 Ground truth visibility mask: a reference view; b source view; c ground truth visibility
mask computed by checking depth consistency between a and b, green represents visible and red
represents occluded

Table 2.2 compares the predicted depth accuracy of supervised learning with unsupervised learning. Furthermore, we add the result using ground truth visibility masks
for training and evaluation to validate the effectiveness of visibility masks. Although
unsupervised learning achieves better overall prediction accuracy, supervision on
visibility mask improves the prediction accuracy in invisible areas. Moreover, the

## [Book2025 PDF p.56] Page 56

40

2 Multi-view Stereo Sensing Method

Table 2.2 Comparison results of supervised learning and unsupervised learning of our “vis-var”
structure. .δ = 7.18mm
.< δ
.< 3δ
Invis .< δ
Invis .< 3δ Fully-vis
Fully-vis
.< δ
.< 3δ
Supervised
0.8899
Unsupervised 0.8930
Ground truth 0.9037

0.9665
0.9661
0.9738

0.8407
0.8397
0.8560

0.9391
0.9378
0.9471

0.9529
0.9534
0.9604

0.9908
0.9901
0.9924

Table 2.3 Ablation study on introduction of normalized depth in our visibility prediction module.
.δ = 7.18mm

w/ depth
w/o depth

.< δ

.< 3δ

Invis .< δ

Invis .< 3δ

0.8899
0.8856

0.9665
0.9628

0.8407
0.8307

0.9391
0.9333

Fully-vis

Fully-vis

.< δ

.< 3δ

0.9529
0.9488

0.9908
0.9901

result of ground truth masks achieves the best accuracy for invisible regions, which
demonstrates accurate visibility masks are crucial for MVS reconstruction.

Ablation Study on Visibility Prediction Module
In order to help the network distinguish the spatial order of virtual planes before maxpooling, we concatenate the normalized depth of each plane with warped features.
Table 2.3 shows the ablation study result, which demonstrates the effectiveness of
introducing depth information for visibility prediction.

2.3.2 Experiments on DTU Benchmark
Dataset Introduction
The DTU dataset [1] is a large-scale MVS dataset, which consists of 124 different
scenes scanned in 7 different lighting conditions at 49 or 64 positions. The data for
each scan are composed of an RGB image and corresponding camera parameters. The
dataset is split into training, validation, and evaluation sets following MVSNet [21]1 .

1 Validation set: 18 scans {3, 5, 17, 21, 28, 35, 37, 38, 40, 43, 56, 59, 66, 67, 82, 86, 106, 117}.

Evaluation set: 22 scans {1, 4, 9, 10, 11, 12, 13, 15, 23, 24, 29, 32, 33, 34, 48, 49, 62, 75, 77, 110,
114, 118}. Training set: the other 79 scans.

## [Book2025 PDF p.57] Page 57

2.3 Experiments

41

Implementation Details
Training We train VA-Point-MVSNet on the DTU training dataset. For data preprocessing, we follow MVSNet [21] to generate depth maps from the given ground
truth point clouds. During training, we set input image resolution to .640 × 512, and
number of views to . N = 3. The input view set is chosen with the same view selection
strategy as in MVSNet. For coarse prediction, we construct a 3D cost volume with
. D = 48 virtual depth planes, which are uniformly sampled from .425 mm to .921
mm. For the depth refinement step, we set flow iteration number .l = 2, with depth
intervals being .8 mm and .4 mm, respectively. The number of nearest neighbor points
is .16. We use RMSProp [8] of initial learning rate .0.0005 which is decreased by 0.9
for every 2 epochs. The coarse prediction network is trained alone for 4 epochs, and
then, the model is trained end-to-end for another 20 epochs. Batch size is set to 4 on
4 NVIDIA GTX 1080Ti graphics cards.
Evaluation We use . D = 96 depth layers for initial depth prediction and set flow
iterations .l = 3 for depth refinement. We predict the reference view depth map for
each . N = 5 view set. Then we fuse all depth maps to point clouds using the same
post-processing provided by [21]. The image resolution for evaluation is.1280 × 960.
Implementation of kNN Naïve kNN of point cloud of . N points can be memoryconsuming with . O(N 2 ) complexity. However, we notice the kNN of a point tends to
come from its nearby 2D pixels in the depth map. By leveraging this fact and taking
the hypothesized points into consideration, we restrict the kNN search of each point
from the whole point cloud to its .k × k × (2m + 1) neighborhood. Furthermore, we
parallel the distance computation by using a fixed weight 3D kernel.
Post-processing Similar to MVSNet [21], our post-processing is composed of three
steps: photo-metric filtering, geometric consistency filtering, and depth fusion. For
photo-metric filtering, we use the predicted probability of the most likely depth layer
as the confidence metric and filter out points whose confidence is below a threshold.
The filtering threshold is set to 0.2 and 0.1 for coarse and our PointFlow stage, respectively. For geometric consistency, we calculate the discrepancy of predicted depths
among multi-view predictions through reverse projection. Points with discrepancy
larger than 0.12 mm are discarded. For depth fusion, we take the average value of
all reprojected depths of each point in visible views as the final depth prediction and
produce the 3D point cloud.

2.3.3 Network Design Analysis
Benchmarking
We evaluate the proposed method on the DTU evaluation dataset. Quantitative results
are shown in Table 2.4 and Fig. 2.9, where the accuracy and completeness are computed using the official code from the DTU dataset, and the f-score is calculated as

## [Book2025 PDF p.58] Page 58

42

2 Multi-view Stereo Sensing Method

Table 2.4 Quantitative results of reconstruction quality on the DTU evaluation dataset (lower is
better)
Acc. (mm)
Comp. (mm)
Overall (mm)
Camp [3]
Furu [5]
Tola [17]
Gipuma [6]
SurfaceNet [11]
MVSNet [21]
R-MVSNet [22]
Ours-“var”
Ours-“vis-var”
Ours-“vis-avg”
Ours-“vis-max”

0.835
0.613
0.342
0.283
0.450
0.396
0.383
0.361
0.379
0.475
0.359

0.554
0.941
1.190
0.873
1.040
0.527
0.452
0.421
0.374
0.467
0.358

0.695
0.777
0.766
0.578
0.745
0.462
0.417
0.391
0.377
0.471
0.359

Fig. 2.9 F-score, accuracy, and completeness of different distance thresholds on the DTU evaluation
dataset (higher is better). For a fair comparison, we upsample the depth map predicted by MVSNet to
the same resolution as our method before depth fusion (.288 × 216 to.640 × 480). The reconstruction
results of Gipuma [6] and SurfaceNet [11] are not publicly available

mentioned in [12] as the measure of the overall performance of accuracy and completeness. While Gipuma [6] performs the best in terms of accuracy, our VA-PointMVSNet outperforms start-of-the-art in both completeness and overall quality, and
our visibility-aware feature aggregation can improve the reconstruction completeness
significantly. Qualitative results are shown in Fig. 2.10. VA-Point-MVSNet generates

## [Book2025 PDF p.59] Page 59

2.3 Experiments

43

Fig. 2.10 Qualitative results of Scan 9 of DTU dataset. Top: Whole point cloud. Bottom: Visualization of normals in zoomed local area. Our VA-Point-MVSNet generates detailed point clouds with
more high-frequency components than MVSNet. For a fair comparison, the depth maps predicted
by MVSNet are interpolated to the same resolution as our method

a more detailed point cloud compared with MVSNet. Especially in those edgy areas,
our method can capture high-frequency geometric features.

PointFlow Iteration
Because of the continuity and flexibility of point representation, the refinement and
densification can be performed iteratively on former predictions to give denser and
more accurate predictions. While the model is trained using .l = 2 iterations, we
test the model using iteration ranging from 0 to 3. For each iteration, we upsample
the point cloud and decrease the depth interval of point hypotheses simultaneously,
enabling the network to capture more detailed features. We compare the reconstruction quality, depth map resolution, GPU memory consumption and runtime at
different iterations, along with performance reported by state-of-the-art methods in
Table 2.5. We use “var” feature aggregation structure for the comparison. The reconstruction quality improves significantly with multiple iterations, which verifies the
effectiveness of our method. Note that our method already outperforms the state-ofthe-art after the second iteration. Qualitative results are shown in Fig. 2.11.

Feature Aggregation Structure
In this section, we validate the effectiveness of different multi-view feature aggregation structures with regard to the number of views. All the structures can process
an arbitrary number of input views. Although the model is trained using . N = 3,

## [Book2025 PDF p.60] Page 60

44

2 Multi-view Stereo Sensing Method

Table 2.5 Comparison result at different flow iterations measured by reconstruction quality and
depth map resolution on the DTU evaluation set. Due to the GPU memory limitation, we decrease
the resolution of MVSNet [21] to 1152.×864.×192
Iter.

Acc.
(mm)

Comp.
(mm)

Overall
(mm)

0.5 mm
f-score

Depth
Map Res.

Depth
Interval
(mm)

GPU
Mem.
(MB)

Runtime
(s)

-

0.693

0.758

0.726

47.95

160.×120

5.30

7219

0.34

1

0.674

0.750

0.712

48.63

160.×120

5.30

7221

0.61

2

0.448

0.487

0.468

76.08

320.×240

4.00

7235

1.14

3

0.361

0.421

0.391

84.27

640.× 480

0.80

8731

3.35

MVSNet [21]

0.456

0.646

0.551

71.60

288.×216

2.65

10805

1.05

Fig. 2.11 Qualitative results at different flow iterations. Top: Whole point cloud. Bottom: Zoomed
local area. The generated point cloud becomes denser after each iteration, and more geometry details
can be captured

we can evaluate the model using either . N = 2, 3, 5, 7 on the DTU evaluation set
as shown in Fig. 2.12. When the number of input views increases from 2 to 5, the
reconstruction qualities of all the structures improve, which is consistent with common knowledge of MVS reconstruction. However, when the number of input views
increases from 5 to 7, the qualities of “var” and “vis-var” drop, which demonstrates
that image information from unideal views may lead to corrupted reconstruction if
the visibility issue is not considered. The qualities of “vis-avg” and “vis-max” keep
improving for . N = 7, validating the effectiveness of our visibility-aware multi-view
feature aggregation structures.

## [Book2025 PDF p.61] Page 61

2.3 Experiments

45

Fig. 2.12 Influence of
number of input views on
reconstruction quality on the
DTU evaluation set for
different multi-view
aggregation structures.
“vis-avg” and “vis-max” fail
to predict reasonable depth
when . N = 2

Ablation Study
In this section, we provide ablation experiments and quantitative analysis to evaluate
the strengths and limitations of the key components in our framework. For all the
following studies, experiments are performed and evaluated on the DTU dataset, and
both accuracy and completeness are used to measure the reconstruction quality. We
set the iteration number to .l = 2, use “var” feature aggregation structure, and all
other experiment settings are the same as Sect. 2.3.3.
Edge Convolution By replacing the edge convolution in Eq. 2.6 with geometryunaware feature aggregation:
Gp =

.



q∈kNN(p)

 
h  Gq ,

(2.10)

where the features of neighbor points are treated equally with no regard to their
geometric relationship to the centroid point, the reconstruction quality drops significantly as shown in Table 2.6, which illustrates the importance of local neighborhood
relationship information (captured by .G p − Gq ) for feature aggregation.
Euclidean Nearest Neighbor In this part, we construct the directed graph using
points belonging to adjacent pixels in the reference image, instead of searching the
kNN points, which leads to decreased reconstruction quality. The reason is that,
for images of 3D scenes, near-by pixels may correspond to distant objects due to
occlusion. Therefore, using neighboring points in the image space may aggregate
irrelevant features for depth residual prediction, leading to descending performance.
Feature Pyramid In this part, the point cloud only fetches features from the last
layer of the feature map, instead of from the whole feature pyramid. As shown in
Table 2.6, in contrast to the relatively stable performance for changing edge convolution strategies as discussed above, the drop will be significant in the absence of
the other two components, which demonstrates the effectiveness of the leveraging
context information at different scales for feature fetching.

## [Book2025 PDF p.62] Page 62

46

2 Multi-view Stereo Sensing Method

Table 2.6 Ablation study on network architectures on the DTU evaluation dataset, which demonstrates the effectiveness of different components. EDGE denotes edge convolution, EUCNN denotes
grouping by nearest neighbor points in Euclidean distance, and PYR denotes the usage of image
feature pyramid
EDGE
EUCNN
PYR
Acc. (mm)
Comp. (mm)
.

.

.

.

.

.

✕
.
✕
.
✕

✕
.
.
✕
✕
.

✕
.

✕
✕

0.448
0.455
0.455
0.501
0.475
0.574
0.529

0.487
0.489
0.492
0.518
0.504
0.565
0.532

Table 2.7 Ablation study of different number of point hypotheses .m on the DTU evaluation set [1]
(The model is trained with .m = 2 except the last one)
Point hypotheses
Acc. (mm)
Comp. (mm)
Overall (mm)
1
2
3
3 (.m = 3)

0.442
0.448
0.468
0.453

0.515
0.487
0.499
0.497

0.479
0.468
0.484
0.475

Table 2.8 Comparison result of direct regression and point hypotheses on the DTU evaluation
set [1]
Overall error (mm)
Direct regression
Ours
Iter0
Iter1
Iter2
Iter3

0.751
0.756
0.501
0.464

0.726
0.712
0.468
0.391

Point Hypotheses We choose .m = 2, 3 for the training and .m = 1, 2, 3 for the
test, and conduct the evaluation on the DTU evaluation set [1]. Table 2.7 shows the
comparison result. Our proposed algorithm achieves the best reconstruction quality
in terms of completeness and overall quality when the number of point hypotheses
is the same as training.
We also directly regress the depth residual without the facilitation of point
hypotheses and the comparison result is shown in Table 2.8. Although the direct
regression is also able to improve the reconstruction quality after each iteration, it is
still worse than the flow prediction facilitated by point hypotheses, which shows the
necessity of neighborhood image feature information to accurate flow prediction.

## [Book2025 PDF p.63] Page 63

2.3 Experiments

47

Reliance on Initial Depth Maps
Our method uses state-of-the-art approaches to get a coarse depth map prediction,
which is then iteratively refined by predicting depth residuals. We find that our
approach is robust to noisy initial depth estimation in a certain range through the
following experiments. We add Gaussian noise of different scales to the initial depth
map and evaluate the reconstruction error. Figure 2.13 shows that the error increases
slowly and is smaller than MVSNet within 6 mm noise.

Comparison to Point Cloud Upsampling
Our work can also be considered as a data-driven point cloud upsampling method with
assisting information from multi-view images. Therefore, we compare our method
with PU-Net [23], where multi-level features are extracted from the coarse point
cloud to reconstruct an upsampled point cloud.
We use the same coarse depth prediction network as in our model and train PUNet to upsample the coarse point cloud. We use the same joint loss as mentioned
in their paper, which consists of two losses—the Earth Mover’s Distance[4] loss
between the predicted point cloud and the reference ground truth point cloud and a
repulsion loss. For evaluation, the PU-Net is applied on the coarse predicted point
cloud twice to generate a denser point cloud with .16 times more points. Quantitative

Fig. 2.13 Reconstruction error w.r.t. initial depth map noise. AVG denotes average pooling in
EdgeConv, MAX denotes max-pooling in EdgeConv.

## [Book2025 PDF p.64] Page 64

48

2 Multi-view Stereo Sensing Method

Table 2.9 Comparison of reconstruction quality on the DTU evaluation dataset with PU-Net [23]
Acc. (mm)
Comp. (mm)
Overall (mm)
PU-Net [23]
Ours

1.220
0.361

0.667
0.421

0.943
0.391

Table 2.10 Quantitative results of published learning-based methods on Tanks and Temples benchmark [12]
Method

Rank

Mean

Family Francis Horse

Lighthouse

M60

Panther

Playground

Train

P-MVSNet [13] 12.38

55.62

70.04

44.64

40.22

65.20

55.08

55.17

60.37

54.29

VA-Point32.25
MVSNet (Ours)

48.70

61.95

43.73

34.45

50.01

52.67

49.71

52.29

44.75

R-MVSNet [22] 36.00

48.40

69.96

46.65

32.59

42.95

51.88

48.80

52.00

42.38

MVSCRF [20]

37.12

45.73

59.83

30.60

29.93

51.15

50.61

51.45

52.60

39.68

MVSNet [21]

45.75

43.48

55.99

28.55

25.07

50.79

53.96

50.86

47.90

34.69

result is shown in Table 2.9. Our VA-Point-MVSNet can generate a more accurate
point cloud from the coarse one by inducing flow for each point from observation of
context information in multi-view images.

2.3.4 Generalizability of the PointFlow Module
In order to evaluate the generalizability of our PointFlow module, we test it on
the Tanks and Temples intermediate dataset [12], which is a large outdoor dataset
captured in complex environments. We first generate coarse depth maps using MVSNet [21], and then apply our PointFlow module to refine them. The f-score increases

Fig. 2.14 Reconstruction results on the intermediate set of Tanks and Temples [12]

## [Book2025 PDF p.65] Page 65

References

49

from .43.48 to .48.70 and the rank rises from .45.75 to .32.25. Table 2.10 shows
the results of published learning-based approaches. Reconstructed point clouds are
shown in Fig. 2.14.

2.4 Conclusion
Accurate reconstruction of the shapes and poses of pegs and holes is critical for
assembly strategy. We present a novel visibility-aware point-based architecture for
high-resolution MVS reconstruction. Instead of building a high-resolution cost volume, our proposed VA-Point-MVSNet processes the scene as a point cloud directly.
The PointFlow module concentrates on the neighborhood of the target surface and
refines the predicted depth map iteratively, which therefore achieves improved time
and memory efficiency. Experiments on synthetic data and real data demonstrate that
the visibility-aware multi-view feature aggregation module can improve the reconstruction quality significantly by considering visibility, and VA-Point-MVSNet is
able to produce high-quality reconstruction point clouds on benchmarks.

References
1. H. Aanæs, R.R. Jensen, G. Vogiatzis, E. Tola, A.B. Dahl, Large-Scale Data for Multiple-View
Stereopsis. Int J Comput Vision 120(2), 153–168 (2016). https://doi.org/10.1007/s11263-0160902-9
2. Calli B, Singh A, Walsman A, Srinivasa S, Abbeel P, Dollar AM (2015) The ycb object and
model set: Towards common benchmarks for manipulation research. In: 2015 international
conference on advanced robotics (ICAR), IEEE, pp 510–517
3. Campbell NDF, Vogiatzis G, Hernández C, Cipolla R (2008) Using Multiple Hypotheses to
Improve Depth-Maps for Multi-View Stereo. In: Forsyth D, Torr P, Zisserman A (eds) Computer
Vision – ECCV 2008, vol 5302, pp 766–779, DOI https://doi.org/10.1007/978-3-540-886822_58
4. Fan H, Su H, Guibas LJ (2017) A point set generation network for 3d object reconstruction
from a single image. In: Proceedings of the IEEE conference on computer vision and pattern
recognition, pp 605–613
5. Y. Furukawa, J. Ponce, Accurate, Dense, and Robust Multiview Stereopsis. IEEE Transactions
on Pattern Analysis and Machine Intelligence 32(8), 1362–1376 (2010). https://doi.org/10.
1109/TPAMI.2009.161
6. Galliani S, Lasinger K, Schindler K (2015) Massively parallel multiview stereopsis by surface
normal diffusion. In: Proceedings of the IEEE International Conference on Computer Vision,
pp 873–881
7. He K, Zhang X, Ren S, Sun J (2016) Deep residual learning for image recognition. In: Proceedings of the IEEE conference on computer vision and pattern recognition, pp 770–778
8. G. Hinton, N. Srivastava, K. Swersky, Lecture 6a overview of mini–batch gradient descent
(2012). Coursera Lecture slides https://class.coursera.org/neuralnets-2012-001/lecture
9. P.H. Huang, K. Matzen, J. Kopf, N. Ahuja, J.B. Huang, Deepmvs: learning multi-view stereopsis, in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition
(2018), pp. 2821–2830

## [Book2025 PDF p.66] Page 66

50

2 Multi-view Stereo Sensing Method

10. S. Im, H.G. Jeon, S. Lin, I.S. Kweon, DPSNet: end-to-end deep plane sweep stereo, in
International Conference on Learning Representations (2019). https://openreview.net/forum?
id=ryeYHi0ctQ
11. M. Ji, J. Gall, H. Zheng, Y. Liu, L. Fang, Surfacenet: an end-to-end 3d neural network for
multiview stereopsis, in Proceedings of the IEEE International Conference on Computer Vision
(2017), pp 2307–2315
12. A. Knapitsch, J. Park, Q.Y. Zhou, V. Koltun, Tanks and temples: benchmarking large-scale
scene reconstruction. ACM Trans Graph 36(4), 78:1–78:13 (2017). https://doi.org/10.1145/
3072959.3073599
13. K. Luo, T. Guan, L. Ju, H. Huang, Y. Luo, P-mvsnet: learning patch-wise matching confidence
aggregation for multi-view stereo, in The IEEE International Conference on Computer Vision
(ICCV) (2019)
14. C. Tang, P. Tan, BA-net: Dense bundle adjustment network, in International Conference on
Learning Representations (2018). https://openreview.net/forum?id=B1gabhRcYX
15. M. Tatarchenko, A. Dosovitskiy, T. Brox, Octree generating networks: efficient convolutional
architectures for high-resolution 3d outputs, in Proceedings of the IEEE International Conference on Computer Vision (2017), pp. 2088–2096
16. E. Todorov, T. Erez, Y. Tassa, Mujoco: a physics engine for model-based control, in 2012
IEEE/RSJ International Conference on Intelligent Robots and Systems (IEEE, 2012), pp. 5026–
5033
17. E. Tola, C. Strecha, P. Fua, Efficient large-scale multi-view stereo for ultra high-resolution
image sets. Mach Vis. Appl. 23(5), 903–920 (2012). https://doi.org/10.1007/s00138-0110346-8
18. G. Vogiatzis, C.H. Esteban, P.H. Torr, R. Cipolla, Multiview stereo via volumetric graph-cuts
and occlusion robust photo-consistency. IEEE Trans. Pattern Anal. Mach. Intell. 29(12), 2241–
2246 (2007)
19. Y. Wang, Y. Sun, Z. Liu, S.E. Sarma, M.M. Bronstein, J.M. Solomon, Dynamic graph CNN
for learning on point clouds. ACM Trans. Graphics (TOG) (2019)
20. Y. Xue, J. Chen, W. Wan, Y. Huang, C. Yu, T. Li, J. Bao, Mvscrf: Learning multi-view stereo
with conditional random fields, in The IEEE International Conference on Computer Vision
(ICCV) (2019)
21. Y. Yao, Z. Luo, S. Li, T. Shen, T. Fang, L. Quan, Mvsnet: depth inference for unstructured
multi-view stereo, in Proceedings of the European Conference on Computer Vision (ECCV)
(2018), pp. 767–783
22. Y. Yao, Z. Luo, S. Li, T. Shen, T. Fang, L. Quan, Recurrent mvsnet for high-resolution multiview stereo depth inference. Computer Vision and Pattern Recognition (CVPR) (2019)
23. L. Yu, X. Li, C.W. Fu, D. Cohen-Or, P.A. Heng, Pu-net: Point cloud upsampling network, in
Proceedings of IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2018)

## [Book2025 PDF p.67] Page 67

Chapter 3

General-Purpose Sim2Real Protocol
for Marker-Based Visuotactile Sensing

3.1 Introduction
Tactile sensing can provide rich information about contacts between the robot and
the environment, including local geometry and force. This information is crucial
for contact-rich assembly tasks, and cannot be obtained from visual signals [10].
Therefore, tactile sensing is drawing increasing attention in robot applications, such
as object manipulation and assembly [4, 7, 16]. However, tactile sensor signals,
particularly those from visuotactile sensors, are high-dimensional, which poses a
significant challenge to manually designing rules for robust and generalizable control
policies.
To develop control policies that can utilize high-dimensional input data, robotics
researchers have employed deep RL to autonomously extract features and learn
complex control policies without manual design [1, 8]. However, the integration of
tactile sensing into RL policies remains under-explored currently. A major obstacle is
the high demand for massive amounts of interaction data, which are costly and timeconsuming to collect in reality. Sim2Real addresses this problem by enabling robots
to be trained in simulation and transferring the learned policies to real robots with
minimal or zero real-world data [11, 22, 23]. Furthermore, the access to ground-truth
environment states in simulation accelerates the policy learning process.
Most existing tactile sensor simulation methods are based on rigid-bod physics
simulation [2, 6, 17, 20, 24]. While the penalty-based contact model can approximate
the deformation of the tactile sensor, it cannot capture the elastic dynamics of the tactile sensor accurately. These methods trade off realism for computational efficiency,
resulting in a large Sim2Real gap that hinders the transferability of manipulation
policies learned in simulation.
In this work, we explore how to build an efficient, general, and effective tactile
Sim2Real protocol for robot manipulation with marker-based visuotactile sensors.
The protocol comprises four essential components, each of which significantly contributes to the final Sim2Real performance. Firstly, we employ a state-of-the-art Finite
© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_3

51

## [Book2025 PDF p.68] Page 68

52

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

Element Method (FEM)-based physics simulation to model the elastic dynamics of
the tactile sensor and the contacts between sensors and objects more precisely than
rigid body-based physics simulation. Secondly, through experiments, we discover
that it is better to use a point-based representation for tactile feature extraction and
policy learning, where the input points come from the set of pixel coordinates of
tactile sensor markers. Compared with CNNs that process the tactile sensor image,
our proposed network can achieve higher learning efficiency and better generalizability to unseen objects. Thirdly, while the raw signal from the marker-based tactile
sensor is high-dimensional, the feature related to the manipulation tasks is usually
low-dimensional. Therefore, to further improve learning efficiency, we propose to
leverage self-supervised representation learning to obtain general tactile representation that can be applied to various manipulation tasks. Finally, after systemically
analyzing the sources of Sim2Real discrepancy, we employ domain randomization
techniques in the physical, optical, and task domains to improve the Sim2Real transferability of the learned policy.
For PiH environments, our simulation achieves a speed of two orders of magnitude
faster than reality on a desktop CPU. We conduct extensive Sim2Real experiments
on the PiH task and compare our method against state-of-the-art tactile simulation
and feature extraction methods. We also propose an arbitrary-shape training scheme
for generalizable PiH policy learning.
In summary, the contributions of this work are as follows:
1. We present a general-purpose Sim2Real protocol for marker-based visuotactile
sensor that has been validated effective for Sim2Real of PiH policies.
2. We introduce point cloud learning architecture for tactile feature extraction that
directly processes the set of pixel coordinates of tactile sensor markers.
3. We introduce a self-supervised pre-training framework to improve the sample
efficiency of tactile-based robot learning.
The remainder of this chapter is structured as follows. Section 3.2 outlines the
proposed methodology, including the simulation method, tactile feature extraction,
and policy training scheme. The subsequent three sections present the experiments.
Section 3.3 focuses on the self-supervised tactile representation learning. Section 3.4
discusses the Sim2Real experiments for the PiH. Finally, Sect. 3.5 presents the conclusion.

3.2 Methodology
This section presents the simulation and policy learning pipeline for marker-based
visuotactile sensors. The tactile sensing principle is first introduced in Sect. 3.2.1.
The FEM-based physics simulation of the tactile sensor’s elastomer is described in
Sect. 3.2.2. The pixel coordinates of markers are used as the tactile signal, and the synthesis method is shown in Sect. 3.2.3. To efficiently process raw tactile observations in
policy training, we propose a tactile feature extractor network and the corresponding

## [Book2025 PDF p.69] Page 69

3.2 Methodology

53

pre-training method in Sect. 3.2.4. The tactile feature extractor is further utilized in
RL policies as introduced in Sect. 3.2.5. Finally, Sect. 3.2.6 summarizes the domain
randomization techniques that facilitate Sim2Real transfer.

3.2.1 Tactile Sensing Principle
Figure 3.1 shows the schematic of the marker-based visuotactile sensor used in our
work, which consists of an RGB camera, LEDs, an acrylic support, and a transparent
elastomer covered with a reflective surface. A 2D array of markers are distributed on
the elastomer surface. When the elastomer deforms due to contacts, the normal deformation can be computed from the image captured by the camera using photometric
stereo, and the tangential deformation can be measured by tracking the markers as
shown in Fig. 3.1.
For most contact-rich manipulation tasks, the tangential deformation of the elastomer is more informative than the normal deformation as it corresponds to the object
displacement during manipulation and can indicate the contact force and torque. It
is pointed out in [21] that using marker flow, a sensor can achieve equal or better
performance in terms of force sensing, compared with surface map measurement.
Therefore, the marker flow is usually used as the tactile signal in manipulation tasks
and we aim to simulate the marker flow accurately in this work.

Fig. 3.1 (a) The schematic of the marker-based visuotactile sensor used in our work, which is
based on GelSight [21]; (b) One example of real tactile image with marker tracking. The marker
flow in contact area is shown by yellow arrows.

## [Book2025 PDF p.70] Page 70

54

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

3.2.2 General-Purpose FEM-Based Physics Simulation
Marker-based visuotactile sensors typically employ silicone rubber as the elastomer,
which exhibits hyperelasticity and allows for large deformation. In order to achieve
successful transfer of RL policies trained in simulation for versatile manipulation
skills, the physics simulation needs to satisfy the following three requirements:
(1) it can support physics simulation of arbitrary 3D geometries;
(2) it can accurately capture the dynamic and elastic properties of the elastomer;
(3) it can simulate the large deformation of the elastomer during RL training stably.
Therefore, we use Incremental Potential Contact (IPC) [9] as the physics simulation in this work. IPC is based on FEM and supports elastomers with hyperelastic
material models such as the widely-adopted Neo-Hookean model. The major difference between IPC and other FEM simulators such as SOFA [5] is the contact
solver. Traditional contact solvers can introduce intersections and put the simulator
into an invalid state. Such artifact is typically mitigated by using very small time
steps, which significantly degrades simulation speed. On the other hand, IPC model
contacts with barrier energy and integrates continuous collision detection into its
solver to guarantee that the simulation is intersection-free and inversion-free. Thus
IPC enables robust FEM simulation at large time steps and improves the simulation
speed, which is desired for the RL training process.
For tactile-based manipulation tasks, the motion of the elastomer is induced by
the action executed on the robot end effector. We model the robot action as Dirichlet
boundary conditions on the elastomer mesh by setting the position and velocity of
boundary vertices. The shape of the tactile sensor’s elastomer is shown in Fig. 3.2.
The markers are distributed on the top surface of the elastomer, which can deform
freely due to contact with the object during manipulation, while the surfaces in purple

Fig. 3.2 (a) In our tactile sensor, the markers are distributed on the top surface. The surfaces in
purple are constrained by the shell. The elastomer frame is fixed on the constrained surfaces of the
elastomer. After transforming the marker point into the camera frame, one can calculate its pixel
coordinate using the pinhole model. (b) Illustration of interpolation using adjacent FEM vertices.
.pi denotes the .ith marker, and the facet it belongs to has three vertices: .xsi1 , .xsi2 , and .xsi3 .

## [Book2025 PDF p.71] Page 71

3.2 Methodology

55

are constrained by the sensor’s shell. In robotic manipulation tasks, the constrained
surfaces of the sensor’s elastomer are actuated by the robot to which the sensor is
attached to.
In IPC, the sensor’s elastomer is discretized as a tetrahedral mesh. We denote the
vertices of the mesh as .{xi }; for vertex coordinates in the world frame, we add a
superscript to distinguish, i.e., .{xiW }. The vertices on the aforementioned constrained
surfaces form a set .S. In the simulation, we enforce the positions and velocities of
the vertices in .S as the boundary constraint.
For one step in the simulation, suppose the rigid shell to which the sensor is
attached is moving at a linear velocity .v and an angular speed .ω around an instantaneous axis, defined by its direction .d and a point .xpivot , then the position at the next
step .xi , and the velocity .vi of each boundary point is given by
xi = vt + R(d, ωt)(xi − xpivot ) + xpivot ,
.

xi − xi
,
t
i ∈ {i|xi ∈ S}

vi =

(3.1)

where .t is the timestep of the simulation and .R(d, ωt) is the rotation matrix
defined by axis .d and rotation angle .ωt.
At each step, the simulated robot motion is converted to the boundary condition
given in Eq. 3.1. Then, IPC’s FEM solver will solve all the vertex positions at the
next step. In this way, the deformation of the sensor’s elastomer and the interactions
between the sensor and objects are obtained.

3.2.3 Synthesis of Tactile Sensor Signals
In this work, we use the marker flow as the tactile sensor signals. Given the vertices
of the elastomer mesh in the elastomer frame .{xiE } and the marker coordinates in the
elastomer frame .{piE }, we first determine the facet that each marker belongs to, and
compute the weight of each vertex:
p E = ki1 xsEi1 + ki2 xsEi2 + ki3 xsEi3

. i

(3.2)

where .ki1 , .ki2 and .ki3 are the triangular barycentric weights which satisfy.k1 , k2 , k3 ≥
0, k1 + k2 + k3 = 1. Note that .{(ki1 , ki2 , ki3 )} and .{(si1 , si2 , si3 )} are computed
before the physics simulation.
The transformation from the elastomer frame to the world frame is set at the
initialization of the simulation according to the sensor positions. For each time
step in the simulation of manipulation, the vertices of the deformed elastomer in

## [Book2025 PDF p.72] Page 72

56

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

the world frame .{xiW } are computed by the solver, and then the displaced marker
coordinates .{p iW } in the world frame can be computed using .{xiW }, .{(ki1 , ki2 , ki3 )},
and .{(si1 , si2 , si3 )}.
In order to generate the marker flow in the image, we first compute the marker
coordinate in the camera frame .piC = [xi , yi , z i ] as:
C W
C
pC = RW
pi + tW

. i

(3.3)

C
C
where .RW
and .tW
are the rotation matrix and the translation vector of the world
frame relative to the camera frame. Then the corresponding pixel coordinate .(u i , vi )
is computed using the camera pinhole model as:

⎡

⎡
⎤
⎤⎡ ⎤
u i
f x 0 cx
xi
1 ⎣

⎦
⎣
0
f
c
yi ⎦
. ⎣ vi ⎦ =
y y

z
i
1
0 0 1
z i

(3.4)

where . f x , f y , cx , c y are the camera intrinsic parameters. The marker’s initial pixel
coordinate before contact .(u i , vi ) can be computed similarly.
To ensure that the 3D vertex positions {.piC } and projected pixel coordinates
{.(u i , vi )} are within certain bounds, we impose constraints in both the simulation
and the reality:
• In simulation, the episode terminates immediately and is considered failure if
either the pose error exceeds the limit or the simulation step fails to converge due
to excessive contact force.
• In reality, the episode terminates immediately and is considered failure if either
the pose error exceeds the limit or the average marker displacement in the contact
area is larger than the threshold.

3.2.4 Tactile Feature Extraction and Pre-Training
For real tactile sensors, the correspondence between the initial and displaced markers is computed by detecting and tracking the markers in the camera stream, which
may fail when the sensor’s elastomer undergoes large or rapid deformation. It poses
difficulties in designing the tactile feature extractor, that the network should be able
to deal with a marker displacement set that is orderless and has a variable cardinality. Moreover, the marker displacements are high-dimensional, which limits the RL
sampling efficiency. Therefore, we propose an autoencoder structure as the tactile
feature extractor based on PointNet [13], and pre-train the network on a large amount
of simulated data to extract a low-dimensional and task-agnostic feature from the
marker displacements.

## [Book2025 PDF p.73] Page 73

3.2 Methodology

57

Tactile Feature Extraction
The structure of the proposed tactile feature extractor is shown in Fig. 3.3. The input of
the network is the concatenation of the original marker positions and the displaced
ones. If the number of detected and tracked markers is less than .n, padding by
replicating will be used. Then, a shared multi-layer perceptron (MLP) and a maxpooling layer will function as an approximation of a symmetrical function over the
input, to deal with the orderless input. The extracted 512-dim global feature is further
encoded by another MLP to be a .k-dim encoded tactile feature.
It should be noted that we do not use the difference between the original and
displaced marker positions as the network input, because the raw marker positions
contain spatial information of the tactile signals, which is crucial for inferring the
contact status.

Autoencoder Pre-Training
To pre-train the encoder for use in various tactile manipulation tasks, we design a
corresponding decoder to reconstruct the marker positions. Since the ideal extracted
feature should be an overall feature extracted from all marker points and independent
of the specific marker distribution, we design the proposed decoder to reconstruct
all the marker positions from the original marker positions and the latent feature. As
shown in Fig. 3.3, the encoded .k-dim feature is repeated and concatenated with the
original marker positions, and then fed into a shared MLP to reconstruct the displaced
marker positions. We use . L2 loss between the reconstructed marker positions and
the ground truth for training.

Fig. 3.3 Overview of the autoencoder structure. To deal with marker permutations and loss of
tracking, the PointNet [13] structure is utilized. The encoder takes in concatenated marker positions
as input and extracts the .k-dim marker flow feature. To reconstruct the deformed marker position,
the decoder concatenates the original marker positions with the .k-dim feature, and outputs the
reconstructed marker positions.

## [Book2025 PDF p.74] Page 74

58

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

3.2.5 Reinforcement Learning Policy
Training a one-step manipulation policy with supervised learning is feasible in simulation, where the ground truth state is accessible. However, we find that it suffers
from inferior generalizability and Sim2Real transferability, which is consistent as the
finding in [4]. A possible explanation is that the tactile observations are insufficient
to capture the full manipulation state. In contrast, RL can optimize the action policy
based on the estimated long-term reward and learn better decisions with partial tactile
observations. Therefore in this work, we utilize RL to train the contact-rich manipulation policy. We adopt an off-policy RL method, Twin-Delayed-DDPG (TD3) [3],
as the RL algorithm due to its sample efficiency.

RL Network Structure
The actor network in TD3 maps the observation to the action, and the critic network
evaluates the Q value of the action. Figure 3.4 illustrates the structure of the actor
network. We use two tactile sensors in all the manipulation experiments in this paper,
so the observation consists of left and right marker displacements. The shared feature
extractor transforms the two marker displacements into two latent .k-dim features.
Then, the MLP policy network concatenates and processes the two features to predict
actions. The critic network, on the other hand, uses privileged ground-truth states
from simulation instead of raw tactile observations to accelerate training [12].
The definition of actions and ground-truth states may vary for different tasks, while
the structures of the actor and critic network remain the same. The task-specified
parameters will be introduced in the experiment section.

Fig. 3.4 Structure of the actor network in the reinforcement learning policy. Considering two-finger
manipulation, the actor network takes in both sensor’s tactile signals. After the shared encoder, the
two .k-dim features are concatenated and put into the MLP policy network.

## [Book2025 PDF p.75] Page 75

3.2 Methodology

59

Feature Extractor Fine-Tuning
In Sect. 3.2.4, we propose to pre-train the tactile feature extractor before training
the RL policy to improve the sample efficiency and training stability. However,
because the tactile interactions in the pre-training dataset may differ from those in
the specific task, we introduce a short self-supervised fine-tune stage of the tactile
feature extractor when training the RL policy.
We modify the TD3 algorithm, such that after sampling from the replay buffer,
we first compute the reconstruction loss in Sect. 3.2.4, and then update the feature
extractor and the decoder parameters. Next, we freeze the tactile feature extractor
and update the critic network and the MLP part in the actor network following the
TD3 algorithm. The feature extractor fine-tuning stage continues until a maximum
number of updates is reached, or until the reconstruction loss is smaller than a preset
threshold.

3.2.6 Domain Randomization
Marker-based visuotactile sensors have inherent challenges for Sim2Real transfer
due to the discrepancy between simulation and reality. The discrepancy arises from
three main sources: (1) the large deformation and aging effects of the elastomer
that serves as the sensing surface, which make it difficult to model its physics and
identify its material parameters accurately; (2) the camera-imaging process that converts tactile interactions to tactile signals, which depends on various factors such
as marker distributions and camera parameters; and (3) the motion errors, uncertainties or latencies that may occur for real robots, such as the mismatch between
commanded and actual robot velocities. To address these challenges, we employ
domain randomization techniques in the Sim2Real learning process. We categorize
the domain randomization into three sub-domains: physical domain, optical domain,
and task domain.

Physical Domain
The behavior of the tactile sensor, including sensitivity, contact forces and deformation states, depends on the elastic modulus, Poisson’s ratio and friction coefficient.
However, due to the age-dependent properties of the elastomer, the actual elastic
modulus of the real sensor can hardly be obtained. Moreover, friction in the real
world is a complex interaction between the object and the sensor that is difficult to
model accurately. Therefore, to improve the Sim2Real transferability, we randomize
the elastic modulus, Poisson’s ratio and friction coefficient within an heuristically
determined range.

## [Book2025 PDF p.76] Page 76

60

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

Optical Domain
Due to the low elastic modulus of the tactile sensor elastomer, fabrication-induced
deformations may result in variations in the marker distribution. However, since the
markers merely serve as a medium to transform the tactile interaction into image
features, the exact marker distribution should not influence the underlying tactile
perception. To this end, we introduce random perturbations to marker positions.
We assume that the markers form a uniform grid and the randomization includes
grid spacing, global translation, global rotation, local perturbation, random noise
and loss of tracking. Grid spacing changes the distance between adjacent markers
that forms a uniform grid. Global translation and global rotation are applied to the
whole marker grid. Local perturbation allows a marker to deviate from its ideal
position as a grid point. These aforementioned four parameters can emulate the
fabrication variances of the sensor elastomer. On the contrary, random noise and
loss of tracking are related to the post-processing process using computer-vision
algorithms, that random noise affects the extracted marker positions in each frame and
loss of tracking allows a marker to disappear at a given probability. The combination
of these parameters provides enough degrees of freedom to cover all possible cases
for real sensors, promoting the Sim2Real transfer. For camera parameters, we do not
apply randomization because camera parameters will have a small variation range if
mass production is realized; the randomization on markers is sufficient to deal with
small camera parameter variations.

Task Domain
This domain mainly includes motion errors, uncertainties, or latencies that may occur
for real robots. For example, when tactile feedback serves as a stopping signal, the
actual position where the robot stops is affected by the robot’s speed, acceleration
and latencies, etc.; when a gripper grasps an object, the object may deviate from the
ideal grasping position. We randomize the parameters in this domain according to
the specific task settings, which will be introduced in the experiment section.

3.3 Experiment: Data Collection, Training,
and Performance of Autoencoder
In Sect. 3.2.4, we have proposed a tactile feature autoencoder to extract lowdimensional and task-agnostic features for tasks. In this section, the data collection,
training of the autoencoder are presented in detail. The performance of the autoencoder is validated on several datasets from simulated manipulation tasks.

## [Book2025 PDF p.77] Page 77

3.3 Experiment: Data Collection, Training, and Performance of Autoencoder

61

Fig. 3.5 Data collection of the proposed tactile autoencoder. (a) The simulation scene for collecting
autoencoder pre-training data. (b) Some samples of the collected marker flow training data. Markers
in red are the displaced ones.

3.3.1 Autoencoder Data Collection
To make the tactile encoder more generalizable, a diverse dataset for pre-training
should be collected. We design an independent simulation scene to collect the possible interactions between the sensor and objects. As shown in Fig. 3.5, a simple scene
is created where a cuboid object is interacting with the sensor elastomer. Despite
the scene’s simplicity, there are a number of parameters to be randomized. Firstly,
the size, position and orientation of the cuboid object are randomized. Secondly, in
the first stage of interaction, the indentation depth is randomized. Thirdly, after the
indentation is finished, the sensor will make a relative movement to the object and
the translational and rotational component of the movement are randomized. For
parameters in physics domain and optical domain, the randomization techniques in
Sect. 3.2.6 are used.
From each run of the aforementioned simulation, we extract three keyframes: the
initial tactile reading, the one after indentation and the final one. From these three
keyframes, six pairs of tactile readings can be combined as the training data for the
autoencoder. Some samples of the collected training data are shown in Fig. 3.5. In
total, 400K pairs of original-displaced markers are collected, among which 70% are
used for training, 15% for validation, and 15% for testing.

## [Book2025 PDF p.78] Page 78

62

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

3.3.2 Autoencoder Training
Training Details
We use . L2 loss between the ground-truth displaced marker positions and the reconstructed ones to train the tactile encoder and decoder simultaneously:
1  
[(u − û i )2 + (vi − v̂i )2 ]
2n i=0 i
n−1

.

L=

(3.5)

where .û i , v̂i are the reconstructed marker positions. For our sensor, in the region of
interest, there are approximately 100 markers so we select .n = 128 as the input size
of points. We use Adam optimizer and set the learning rate as 2e-4, with a batch size
of 128. The training lasts for 2000 epochs to ensure convergence.

Determination of Latent Feature Dimension
The dimension .k of the extracted latent feature is a hyperparameter that needs to
be determined in advance. We compare different latent dimensions, .k, from 4 to
256, to find an appropriate value that has both sufficient representative capability
and compactness. In Fig. 3.6, we present the smoothed validation loss over training
epochs. It shows that when the latent dimension .k is low, i.e., .k = 4, 8, 16, the
reconstruction loss is obviously higher than other cases, which means the encoder
does not have enough representative capability. When .k = 32, the reconstruction
loss is also higher than those when .k = 64, 128, 256, but the difference is minor.
Therefore, we choose .k = 32 to balance representative capability and compactness.

Fig. 3.6 Reconstruction loss
in validation during
autoencoder training, where
the latent feature has
different dimensions. The
loss is in log scale and is
smoothed using 10-element
moving average. .k = 32 is
chosen as the latent feature
dimension because it has
both compactness and
sufficient representative
capability

## [Book2025 PDF p.79] Page 79

3.4 Experiment: Peg-in-Hole Task
Table 3.1 Reconstruction
loss of the autoencoder on
seen and unseen datasets

63
Dataset

Reconstruction loss

Pre-training dataset (seen)
Dataset from PiH task

0.410
0.597

3.3.3 Autoencoder Performance on Unseen Data
We test the pre-trained autoencoder on the datasets collected in the PiH insertion
task. The datasets are from the replay buffer collected during the RL training process
and each contains 400K test samples.
Table 3.1 summarizes the average reconstruction loss of the autoencoder on seen
and unseen datasets. In the pre-training dataset, the reconstruction loss is 0.410,
which
√ means the reconstructed marker positions have a root-mean-squared distance
of . 2 × 0.410 ≈ 0.9 pixel from the ground-truth ones (see (3.5)). Considering that
the markers have random noises in simulation, this proves that the trained autoencoder
has sufficient capability of extracting compact and representative tactile features.
Table 3.1 also shows that in unseen datasets, the reconstruction losses are less than
1, proving that the trained autoencoder is generalizable.

3.4 Experiment: Peg-in-Hole Task
3.4.1 Definition of Monotone Insertion
The original version of the tactile-RL insertion task is proposed in [4]. In this task,
a gripper with tactile sensors is controlled to insert an object into a rectangle-shaped
hole with a random initial pose misalignment (Fig. 3.7). The random pose misalignment is 3-DoF, consisting of the 2-DoF .x − y plane translation and the rotation
around .z−axis (Fig. 3.7). Each insertion attempt is a downward motion along the .−z
direction. If getting blocked, the gripper will retreat to the initial height and adjust
the pose according to the trained policy, followed by another insertion attempt. This
task is later completed in a Sim2Real way in [20].
As discussed in [4, 20], this task is difficult in that the hole is unchamfered, and
thus the robot must recognize nuances in the tactile readings to decide the insertion
pose adjustment, in the case where the object hits the hole at four corners.
We introduce a novel variant of the tactile insertion task, which we call monotone
insertion. Unlike the original task, our variant does not allow the gripper to retract
during the insertion process. Instead, the gripper descends by a fixed distance at
each step. Thus, the gripper motion is monotone along the .z-axis. This modification
makes the task more realistic, intuitive, and efficient. However, it also poses higher
demands on the simulator, which has to capture the continuous deformation of the
elastomer under insertion. We evaluate our method on the monotone insertion task

## [Book2025 PDF p.80] Page 80

64

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

Fig. 3.7 a Our simulation environment of the PiH insertion task. Visualization is realized by
SAPIEN [18]. b Top view of the task. The initial pose error has 3 degrees of freedom

variant in Sects. 3.4.4, 3.4.7, 3.4.8, 3.4.9 and 3.4.11. For a fair comparison, we also
report our method’s performance on the original version of the task in Sect. 3.4.10.

3.4.2 Experimental Setup
In [4], there are cuboid, hexagonal, cylindrical, elliptical objects, while the holes are
all rectangular. In this work, the task is stricter, that the holes have the same shape as
the objects (pegs). Three representative shapes we choose to test in reality are shown
in Fig. 3.8b. The object to insert is grasped by a parallel gripper (Robotiq HandE), and the object width is unified to be 30 mm. The clearance between the object
and the hole is 2 mm, which is about 6.7% of the object width, similar to [4, 20].
Correspondingly, the initial error range is set to [.±5 mm, .±5 mm, .±10.◦ ]. In our
monotone insertion task, the gripper will move down 0.125 mm at each step; the
maximum number of allowed pose corrections is 8. Note that the maximum attempt
number in [4, 20] is 15, showing that our monotone task is more difficult and efficient.
The 4-axis motion (3-axis translation, 1-axis rotation) is provided by a translation
stage with orthogonal axes and a rotary stage (see Fig. 3.8).
To better facilitate the evaluation of the trained RL policies in reality, we design
an auto-resetting mechanism as shown in Fig. 3.8d. When insertion fails, the pose of
the peg may change largely because of the large contact force caused by incorrect
actions, which will impair the performance of the following episodes. Therefore, to
autonomously reset the pose, we use a “garage” with large chamfers for the peg. We

## [Book2025 PDF p.81] Page 81

3.4 Experiment: Peg-in-Hole Task

65

Fig. 3.8 The devices for the PiH experiment. a Our self-made GelSight-type tactile sensor. b These
three shapes, namely Cuboid, Concave and Trapezoid, are used to test the trained policy in reality.
The magnets are used for pose resetting. c We use a combined motorized stage and a parallel gripper
to execute the tasks. d The mechanism for auto-resetting the pose. The garage has large chamfers
to tolerate possible peg pose errors. There are also magnets at the bottom of the garage for pose
resetting

glue Nd-Fe-B magnets at the bottom of the garage and the peg to provide enough
attractive forces for resetting the peg’s pose. It should be noted that the magnets will
not interfere with the PiH insertion process because the screws to fasten the hole are
made of 304 stainless steel and thus will not be attracted by the magnets. Whether to
do pose resetting is determined by the average marker displacements in both sensors’
contact area.
Each test in reality contains 57 episodes starting with a series of pre-defined
initial errors. The pre-defined initial errors are uniformly sampled within the range
[.±5 mm, .±5 mm, .±10.◦ ], ensuring fair comparison across different tests. The metrics
summarized after each test are the success rate and the average number of pose
correction attempts in all successful episodes. Note that when success rate is high,
the average number of attempts may be also large because more challenging cases

## [Book2025 PDF p.82] Page 82

66

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

are taken into calculation. So the success rate should be the first to compare; when
the success rates of two policies are similar, the average number of attempts can be
compared to reveal their optimality.

3.4.3 Details of RL Policy Training
At the beginning of each episode, the original marker positions of each tactile sensor
are stored before any insertion attempt. At each step, the sensor’s displaced marker
positions corresponding to the original ones are recorded through a marker-tracking
algorithm. Then the original marker positions and displaced ones are concatenated
to form the observation. Observations from the two sensors are fed into the actor
network. The output action is a 3-dim vector .[ax , a y , aθz ]. Note that the action is
defined relative to the peg (or equivalently the gripper), not to the hole. The state
input for the critic network is the peg’s ground-truth offset .[ex , e y , eθz ].
One episode terminates under three conditions: (1) the insertion succeeds, (2)
the pose error is larger than a threshold in any axis, or (3) the number of insertion
attempts is over a limit. We set the max error in .x and . y axis to be 12mm, and 15.◦
in .θz . The maximum number of attempts is 8 for our monotone insertion task and 15
for the original version of the task.
The reward function at each step is shown in (3.6). It consists of 4 parts: the
decrease in error .et−1 − et , the constant penalty at each step . P = 1, the final success
reward . Rfinal and the penalty for too large error . Rfail . .et is calculated from the error
in each axis, where .ex and .e y are in mm and .eθz is in degrees. To prevent the policy
from quick failure, the penalty for large error is used where .tmax is the maximum
allowed number of attempts.
Rt = et−1 − et − P + Rfinal + Rfail

et = ex2 + e2y + eθ2z

10,
if success
R
=
. final
0,
otherwise
⎧
⎪
⎨ − 2(tmax − t)P, if ex,y ≥ 12
Rfail =
or eθz ≥ 15
⎪
⎩
0,
otherwise

(3.6)

The domain randomization method is mainly introduced in Sect. 3.2.6. For randomization in the task domain, the indentation depth into each sensor’s surface varies
from 0.5 to 1.25 mm, and the peg’s relative position to the sensors varies from -1 to
1 mm in .x direction and from -5 to 5 mm in .z direction.
As mentioned in Sect. 3.2.5, we adopt TD3 as the RL algorithm. For unmodified
TD3, we use Stable-Baselines3 [14] as a default implementation. For the proposed

## [Book2025 PDF p.83] Page 83

3.4 Experiment: Peg-in-Hole Task

67

fine-tuning method of tactile feature extractor, we make some modifications on it as
introduced in Sect. 3.2.5. To efficiently train the RL policy, we use 20 parallel environments with 500K environment steps in total. We note here for comparison that,
[4] uses startup bootstrap and a carefully designed curriculum learning scheme to
efficiently train the policy in reality (therefore no randomization) with 3K steps; [20]
uses PPO algorithm in simulation and the policy is trained for 5M steps. Considering
that zero-shot Sim2Real policies usually have large variance, in the following experiments, we train and test the policy several times to provide more reliable results.

3.4.4 Advantage of FEM Simulation over Rigid-Body
Simulation
We first compare our FEM-based simulator with the state-of-the-art work [20] on
tactile Sim2Real in the monotone PiH insertion task. Based on their open-source
code1 , we implement the monotone insertion task using our experimental settings.
We modify the object size, the hole size, the tactile readings according to our real
devices. The domain randomization parameters are unchanged. The level of noise
added to tactile readings is adjusted to be of a similar ratio to the noiseless value
as in the original code. To keep most of [20]’s implementation, we do not change
the RL algorithm PPO, the convolutional RNN policy and the reward function. For
Sim2Real transfer, we also apply the normalization technique proposed in [20].
It should be noted that the open-source simulator DiffHand [19] used in [20]
currently only supports the collisions where one object must be a primitive shape2
(e.g., cube, sphere, etc.). Therefore, only the cuboid object is considered in this
comparison.
For comparison, we train our proposed method using the proposed RL scheme
(without pre-training, for fairness) in Sect. 3.2.5. With the tactile encoder and the
randomization in optical domain, the trained policy can be directly transferred to
reality without any normalization. This advantage can be attributed to the following
two reasons. First, in our simulation, the synthesized marker displacement is the same
as the real tactile readings, so there is no need to do conversion or normalization as
[20] does. Second, with the domain randomization technique, the proposed tactile
encoder can extract features from raw tactile readings, regardless of the specific
marker distribution.
We train [20]’s policy and our method 10 times with different random seeds and
evaluate the trained policy in our real environment. The success rate and number of
pose correction attempts in each test are presented in Fig. 3.9, while each group’s
average number and standard deviation are summarized in Table 3.2. To compare the
Sim2Real gap of the two simulators, we also show the evaluation results in simulation
1 https://github.com/eanswer/TactileSimulation.
2 https://github.com/eanswer/TactileSimulation/issues/3.

## [Book2025 PDF p.84] Page 84

68

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

Fig. 3.9 Distribution of all the Sim2Sim and Sim2Real results of our method and [20]’s method on
the monotone PiH insertion task. The metrics are the success rate (higher is better) and the number
of attempts (lower is better). Our method has a higher success rate and a smaller Sim2Real gap
Table 3.2 Sim2Sim and Sim2Real comparison between our method and [20] on the Monotone
Peg-in-Hole insertion task
Success rate (%) .↑
Number of attempts .↓
Sim2Sim, [20]
Sim2Sim, ours
Sim2Real, [20]
Sim2Real, ours

92.50 .± 4.09
94.50 .± 3.20
46.33 .± 4.96
95.08 .± 2.70

3.26 .± 0.11
3.63 .± 0.10
4.09 .± 0.26
3.55 .± 0.19

in Fig. 3.9. Although the two methods have similar success rate in simulation, our
method performs significantly better in the real environment. The difference between
our simulation and reality is small, in terms of both success rate (94.5% in Sim, 95.1%
in Real) and attempt number (3.63 in Sim, 3.55 in Real). This proves our method has
a smaller Sim2Real gap in the monotone PiH insertion task. The reason is that, in
the monotone insertion task, the peg and the hole keep contacting until a successful
insertion, so the tangential deformation and the relative displacement of the peg to the
sensors always exist in the elastomer during insertion. Our FEM-based simulation
method is able to capture the complex and continuous deformation, thus achieving
a smaller Sim2Real gap. In rigid-body-based simulation proposed by [20], however, the penalty-based tactile model cannot account for the tangential deformation
because their tangential forces are approximated by friction. Therefore, during the
sequence of movements in the monotone insertion task, the tactile forces, especially
the tangential restoration forces by the elastomer, cannot maintain, which differs
largely from the reality. In conclusion, [20]’s method sacrifices physical accuracy
for efficiency, which is the reason why our method performs better in this task.

## [Book2025 PDF p.85] Page 85

3.4 Experiment: Peg-in-Hole Task

69

3.4.5 Simulation Speed
We conduct a comparison of the simulation speed of our method and that of [20] on
the monotone PiH insertion task. For our method, the tetrahedral mesh of the sensor
elastomer comprises 129 vertices and 412 elements. In the simulation scene, there are
878 elements in total. We set the simulation timestep.t as 0.1 s and each environment
step typically contains approximately 5 timesteps. The simulation is run on a PC
with Intel Core i7-13700K CPU3 and 64 GB memory using 8 parallel environments,
achieving a speed of 43 environment steps per second. For comparison, [20]’s rigid
body-based method reaches 151 steps per second in the same conditions. Our single
real experimental device can reach approximately 0.23 steps per second. The speed
of the real-world pipeline is mainly limited by the acceleration and deacceleration
of the stage because we implemented a conservative acceleration strategy to ensure
operational stability. These results demonstrate that while our FEM-based simulation
is less efficient than rigid-body-based simulation, the difference between the two
methods does not reach an order of magnitude. More importantly, our simulation
method is two orders of magnitude faster than reality, which can greatly accelerate
the policy training.

3.4.6 Ablation Study for Domain Randomization
In this subsection, an ablation study is conducted to validate the domain randomization techniques. In Sect. 3.2.6, the parameters are classified into three sub-domains:
physical domain, optical domain, and task domain. We therefore design three experiments, each of which has non-randomized parameters in one sub-domain respectively. The randomization range of the parameters and the non-randomized values
for ablation study are summarized in Table 3.3. Other conditions of training are kept
the same as in Sect. 3.4.4. In the experiments, training and test are repeated 10 times
for each condition, and the results are summarized in Table 3.4.
Table 3.4 shows that the randomization in the optical domain has the largest influence. This is because without optical domain randomization, the tactile feature extractor is unable to correctly interpret the tactile readings from a different marker distribution. We note here that, the default marker distributions used in the simulation are
different from those in reality, which leads to a significant performance degradation.
Once the simulated markers are aligned with the real two sensors used in test, the
Sim2Real success rate rises to 56.84%, which is better than [20] (46.33%). Furthermore, the Sim2Real performance deteriorates in the absence of the randomization in
the other two domains, as indicated by the decline in success rate and the increase in
the number of attempts. This proves that the randomization in the physical and task
domain plays a crucial role in enhancing the robustness and optimality of the trained
policy.
3 The actual frequency when running simulation is about 5 GHz.

## [Book2025 PDF p.86] Page 86

70

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

Table 3.3 Simulation parameters with and without domain randomization (DR)
Sub-domain
Parameter Name
w/DR
w/o DR
Physical

Optical

Task

Elastic modulus (MPa)
Poisson’s ratio
Friction coefficient
Grid spacing (mm)
Global translation.∗ (mm)
Global rotation (rad)
Local perturbation.∗ (mm)
Random noise.∗∗ (pixel)
Lose-tracking probability
Indentation depth (mm)
Peg offset .x (mm)
Peg offset .z (mm)

[0.3, 1]
[0.3, 0.47]
[0.5, 1]
[1.95, 2.05]
[0, 1]
[.−0.1, 0.1]
[0, 0.1]
0.5
0.01
[0.5 1.25]
[.−1 1]
[.−5 5]

0.65
0.4
0.75
2
0
0
0
0
0
0.8
0
0

* Global translation and local perturbation are applied in both directions.
** Random noise is Gaussian, in both directions.
Table 3.4 Ablation study results for domain randomization
Success Rate (%) .↑
w/ all domains
w/o physical domain
w/o optical domain*
w/o optical domain**
w/o task domain

95.08 .± 2.70
80.70 .± 10.44
10.01 .± 4.71
56.84 .± 12.87
61.57 .± 13.64

Number of Attempts .↓
3.55 .± 0.19
3.90 .± 0.67
3.34 .± 0.87
3.61 .± 0.38
4.35 .± 0.45

* The simulated marker positions are NOT aligned with real sensors.
** The simulated marker positions ARE aligned with real sensors.

3.4.7 Generalizable Peg-in-Hole Policy for Arbitrary Shapes
For real PiH applications, the shapes of pegs and holes are widely distributed and
the precise geometry information is usually unavailable. Therefore, we aim to train
a PiH policy that is generalizable to arbitrary shapes. In order to achieve this goal,
we randomize the shapes of pegs and holes during RL training, which is costly in
the real world but requires minimal effort in simulation.
We randomly generate 10000 polygons as the shape of the peg and the hole, as
shown in Fig. 3.10. Note that we do not assume the shape’s symmetry or convexity.
In training of the RL policy, a shape will be randomly selected when the environment
resets. To validate the generalizability of the trained policy, we test the policy in reality
using three pre-defined shapes, namely Cuboid, Concave, and Trapezoid (Fig. 3.8b).
These three shapes are chosen because the cuboid shape is more difficult to insert
compared with hexagonal or circular shapes [4]; the concave shape and the trapezoid
shape represent the objects with concavity and non-symmetry, respectively.

## [Book2025 PDF p.87] Page 87

3.4 Experiment: Peg-in-Hole Task

71

Fig. 3.10 Three examples of randomly generated shapes. We do not necessarily assume symmetry
or convexity of the shape. These arbitrary shapes used in simulation result in a generalizable PiH
insertion policy
Fig. 3.11 Ablation study of
the proposed arbitrary-shape
training scheme. Comparison
is done among training with
arbitrary shapes, training
with the exact three shapes
and training with only one
shape. The policy trained
with arbitrary shapes has the
best overall performance.
This proves that a
“generalist” policy performs
better in unknown
environments and in
Sim2Real

We evaluate the arbitrary-shape training scheme through an ablation study. RL
policies are trained in three training conditions: 1) train on cuboid shape only, 2)
train on the exact three test shapes, and 3) train on the proposed arbitrary shapes.
The trained policies are tested on the 3 selected shapes in Fig. 3.8b. The training
and test in each condition are repeated 10 times to get more reliable results. The
experimental results are summarized in Fig. 3.11. From the results, we draw the
following conclusions:
1. By training on cuboid only, we obtain a “specialist” policy that performs best and
most stably on the cuboid shape among the three groups. It reaches the highest
success rate and the lowest standard deviation in Sim2Real test of the cuboid
shape. It can also generalize to the concave and trapezoid shape, but the success
rates are lower than the two counterparts.

## [Book2025 PDF p.88] Page 88

72

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

2. A “generalist” policy is advantageous in unknown environments and is beneficial
for Sim2Real. We notice that the policy trained with arbitrary shapes can reach
similar success rates as the “specialist” policy on the cuboid shape; on the concave
and trapezoid shape, it performs better than the “specialist” policy. We surprisedly
find that the “generalist” policy performs better than the policy trained on the
exact three shapes. It may be because the real environment exhibits unavoidable
deviations from the ideal simulation and therefore the policy trained with the
exact three shapes has inferior performance.

3.4.8 Advantage of the Proposed Tactile Representation
In this subsection, we design an ablation study to compare the proposed marker-based
tactile representation with image-based tactile representation. In [4], the researchers
have found that binary marker images perform better than raw RGB images captured
with the sensor. Therefore, in this section, we adopt the binary marker image as
the image-based tactile representation. In simulation, the marker image is generated
using OpenCV from the calculated marker pixel coordinates. The image resolution
is 320.×320 and then binarized and downsampled to 256.×256 before being fed
into CNNs. Like the marker-based representation, the image-based representation
also contains two frames, and they are stacked to be a 2-channel binary image. The
corresponding actor network contains a shared CNN feature extractor for both left and
right sensor images. The dimension of the extracted latent feature and the following
MLP network is 32, the same as the marker-based one. Other conditions, such as
the randomization parameters, remain the same in this comparison. To implement
the randomization of the marker images, the marker positions are randomized first,
and then the marker image is generated based on the randomized markers. The pretraining uses the reconstructed displaced markers for self-supervision, and different
representations require different decoder networks and different loss functions. In
order to eliminate the potential influence of the pre-training, we do not apply it for
both representations. Both policies are trained with the proposed arbitrary shapes for
500K environment steps and the best weights are used for testing in reality.
Figure 3.12 shows the comparison result of the tactile representations. It shows
that although the randomization parameters are the same, using the proposed markerbased representation is advantageous over the image-based representation. The possible reason is that the convolutional operator in CNN has a translation-invariant
property, which makes it difficult for CNN to globally extract spatial features from
the tactile observations. Moreover, the randomization in marker distributions impedes
the CNN’s convergence. On the contrary, with the design of the symmetrical function approximation, the marker-based tactile representation and point cloud learning
architecture can inherently deal with the marker position input and extract both global
and local tactile features. The randomization enhances its generalizability and further
improves Sim2Real performance.

## [Book2025 PDF p.89] Page 89

3.4 Experiment: Peg-in-Hole Task

73

Fig. 3.12 Ablation study of
the proposed tactile
representation. Comparison
is done between the
proposed marker-based
tactile representation and the
image-based presentation.
The success rates are
compared over three test
shapes. The average success
rate and standard deviation
are calculated from 10
independently trained
weights for each
representation

3.4.9 Advantage of the Pre-Trained Tactile Encoder
We follow Sect. 3.2.5 to validate the effectiveness of the proposed pre-training and
fine-tuning method. In this experiment, we show that with the pre-trained tactile
encoder, the policy can achieve considerably high Sim2Real success rate even at
very early steps. We test the real success rate on the aforementioned 3 preset shapes
using the trained weight at different RL steps, from 4K to 500K. The experiments
with and without pre-training are repeated 3 times using different random seeds. The
Sim2Real results are presented in Fig. 3.13. As shown in the figure, at very early
steps (i.e., before 10K), the policy with pre-training shows a large advantage over
the one without pre-training. At 8K steps, the policies with pre-training can achieve
the success rates of 77.2 %, 64.3%, and 85.4% for the three shapes respectively,
comparable to those of the policies without pre-training at 40K steps.

3.4.10 Comparison in the Original Version of the Insertion
Task
In the original version of the PiH insertion task proposed by [4, 20], if an insertion attempt fails, the gripper will retreat to the initial height, canceling the contact
between the peg and the hole. Although we conduct most of the zero-shot Sim2Real
experiments on the proposed monotone insertion task, we also provide our method’s
results on the original version of the task. We repeat the training and testing process
10 times to get more reliable results, as shown in Fig. 3.14. The average success rate
and number of attempts are summarized in Table 3.5.
Despite the fact that our sensors, robots and objects are different from [4, 20], we
have tried our best to reproduce their results on our own hardware. The success rate
of [20] that we reproduce is 85.95.±14.97%, slightly higher than what [20] reported

## [Book2025 PDF p.90] Page 90

74

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

Fig. 3.13 Comparison
between the policy with
pre-training and without
pre-training. Sim2Real
success rates at different RL
steps on three preset peg
shapes are reported and each
line is averaged over three
weights trained with
different random seeds. The
horizontal axes are in log
scale

(83%). The average attempt number (3.98.±0.49) is also smaller than what [20]
reported (4.81). From these statistics, we believe that our reproduction is reasonable
and reliable. The difference may be attributed to the hardware differences, e.g., our
tactile sensor, the object width and peg-hole clearance are different; our motion stage
may have higher positioning accuracy; our objects and holes are 3D-printed using
stereo-lithography, instead of fused deposition modeling.
For our method, we achieve a similar Sim2Real success rate as [20] (86.48% compared to 85.95%). While the success rates are similar, our average attempt number is
significantly smaller (3.56 compared to 3.98). What’s more, as can be noticed, [20]’s
method has very few attempts in simulation (2.29) while having more attempts in
reality (3.98). On the contrary, our method has fewer attempts in reality (3.56) than
in simulation (4.05), which is reasonable because the success rate in simulation is

## [Book2025 PDF p.91] Page 91

3.4 Experiment: Peg-in-Hole Task

75

Fig. 3.14 Comparison of the Sim2Sim and Sim2Real results of our method and [20]’s method on
the original PiH insertion task. The metrics are the success rate (higher is better) and the number
of attempts (lower is better)
Table 3.5 Sim2Sim and Sim2Real comparison between our method and [20] on the original Pegin-Hole insertion task
Success Rate (%) .↑
Number of Attempts .↓
Sim2Sim, [20]
Sim2Sim, ours
Sim2Real, [20]
Sim2Real, ours

98.10 .± 0.88
93.40 .± 2.84
85.95 .± 14.97
86.48 .± 9.09

2.29 .± 0.20
4.05 .± 0.26
3.98 .± 0.49
3.56 .± 0.55

also higher, leading to more challenging cases to be counted when calculating the
average attempt number. These results prove that with FEM as the physics simulation
method, our simulator has a smaller Sim2Real gap and thus the optimal actions in
simulation are closer to those in reality than [20].

3.4.11 Generalizability to Different Sensor Instances
The modulus of the sensor’s elastomer varies over time due to degradation of its
molecular structure [15]. As a result, sensors produced using the same manufacturing
process yet at different dates will have different properties. Additionally, it should be
noted that there are slight variations in the marker spatial arrangement and camera
parameters among different sensor instances. Therefore, the policy’s generalizability
to different sensor instances is critical for real applications. However, it will be highly
costly, if possible, to train a generalizable policy using real sensors with different

## [Book2025 PDF p.92] Page 92

76

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

Table 3.6 Sim2Real comparison between different sensor instances
Sim2Real condition
Success rate (%) .↑
Number of attempts .↓
Sensor Pair 1
Sensor Pair 2

91.75 .± 7.48
87.37 .± 11.81

3.75 .± 0.17
3.66 .± 0.28

Table 3.7 Sim2Sim comparison in case of elastic modulus mismatch
Sim2Sim condition
Success rate (%) .↑
Number of attempts .↓
No mismatch in . E ∗
. E left = 0.7E right

90.20 .± 3.46
87.60 .± 4.57

3.84 .± 0.10
3.95 .± 0.15

* . E stands for elastic modulus

properties. In this subsection, we demonstrate that the policy learned by our Sim2Real
method has good generalizability to different real sensor instances.
Table 3.6 shows the results on two sensor pairs. The policies are trained on arbitrary shapes as described in Sect. 3.4.7. 10 policies trained with different random
seeds are tested on the two pairs. Only the cuboid shape is tested in reality. The
Sensor Pair 1 consists of two sensors that are manufactured in a same batch and
have similar properties. The Sensor Pair 2 consists of two sensors, where the elastic
modulus of the left sensor is different from that of the right sensor. The mismatch violates the common assumption that both sensors in a pair have similar properties and
poses additional challenge for control policies, which is again validated by Sim2Sim
experiments at the end of this subsection.
The experimental results show that the learned policies have good performance
on the two pairs, demonstrating the effective generalizability of our approach to
different sensor instances. This achievement can be attributed to the physics, optical
domain randomization, which effectively captures the variations among different
sensor instances.
We further replicate the performance decline phenomenon caused by the mismatch
in simulation. As shown in Table 3.7, the success rate decreases from 90.2% to 87.6%
when the elastic modulus of the left sensor is 70% of the right sensor. The result
demonstrates that our simulation method has a small Sim2Real gap.

3.5 Conclusion
In this chapter, we present a general-purpose Sim2Real protocol for learning contactrich assembly with marker-based visuotactile sensors. Our FEM-based simulation
method generates high-fidelity tactile observations and exhibits sufficient robustness for long-term RL training. We propose the use of marker flow as the tactile
representation and introduce a point cloud learning architecture for tactile feature
extraction. A tailored pre-training and fine-tuning method is employed to achieve

## [Book2025 PDF p.93] Page 93

References

77

high sample efficiency in tactile-based robot learning. Additionally, we summarize
a reasonable and diverse domain randomization technique that has been validated
for use with our proposed simulation and learning pipeline. The combination of
these techniques enables the successful completion of three contact-rich manipulation tasks in a zero-shot Sim2Real manner. The small Sim2Real gap observed in our
experiments demonstrates the effectiveness of our method.
Despite the promising results, several limitations remain to be addressed. Firstly,
the simulation engine currently employed only supports deformable bodies, resulting in slow performance when complex rigid bodies are present. Additionally, the
process of adding constraints in our FEM-based simulation is less convenient than
in other popular robot simulation environments. Secondly, while our pipeline can
theoretically generalize to other marker-based visuotactile sensors, this has not been
validated due to the limited availability of such sensors. Thirdly, the effectiveness of
our proposed learning scheme in more complex tasks remains unknown.

References
1. I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas et al., Solving rubik’s cube with a robot hand (2019). arXiv:1910.07113
2. A. Church, J. Lloyd, N.F. Lepora et al., Tactile sim-to-real policy transfer via real-to-sim image
translation, in Conference on Robot Learning, PMLR (2022), pp. 1645–1654
3. S. Dankwa, W. Zheng, Twin-delayed ddpg: a deep reinforcement learning technique to model
a continuous movement of an intelligent robot agent, in Proceedings of the 3rd International
Conference on Vision, Image and Signal Processing (2019), pp. 1–5
4. S. Dong, D.K. Jha, D. Romeres, S. Kim, D. Nikovski, A. Rodriguez, Tactile-rl for insertion:
generalization to objects of unknown geometry, in 2021 IEEE International Conference on
Robotics and Automation (ICRA) (IEEE, 2021), pp. 6437–6443
5. F. Faure, C. Duriez, H. Delingette, J. Allard, B. Gilles, S. Marchesseau, H. Talbot, H.
Courtecuisse, G. Bousquet, I. Peterlik, S. Cotin, SOFA: a multi-model framework for interactive physical simulation, in Soft Tissue Biomechanical Modeling for Computer Assisted
Surgery, Studies in Mechanobiology, Tissue Engineering and Biomaterials, ed. by Y. Payan,
vol. 11. (Springer, 2012), pp. 283–321. https://doi.org/10.1007/8415_2012_125, https://inria.
hal.science/hal-00681539
6. D.F. Gomes, P. Paoletti, S. Luo, Generation of gelsight tactile images for sim2real learning.
IEEE Robot. Autom. Lett. 6(2), 4177–4184 (2021)
7. F.R. Hogan, J. Ballester, S. Dong, A. Rodriguez, Tactile dexterity: Manipulation primitives with
tactile feedback, in 2020 IEEE international conference on robotics and automation (ICRA)
(IEEE, 2020), pp. 8863–8869
8. J. Hwangbo, J. Lee, A. Dosovitskiy, D. Bellicoso, V. Tsounis, V. Koltun, M. Hutter, Learning
agile and dynamic motor skills for legged robots. Sci. Robot. 4(26), eaau5872 (2019)
9. M. Li, Z. Ferguson, T. Schneider, T.R. Langlois, D. Zorin, D. Panozzo, C. Jiang, D.M. Kaufman,
Incremental potential contact: intersection-and inversion-free, large-deformation dynamics.
ACM Trans. Graph 39(4), 49 (2020)
10. Q. Li, O. Kroemer, Z. Su, F.F. Veiga, M. Kaboli, H.J. Ritter, A review of tactile information:
perception and action through touch. IEEE Trans. Robot. 36(6), 1619–1634 (2020)
11. X.B. Peng, M. Andrychowicz, W. Zaremba, P. Abbeel, Sim-to-real transfer of robotic control with dynamics randomization, in 2018 IEEE International Conference on Robotics and
Automation (ICRA) (IEEE, 2018), pp. 3803–3810

## [Book2025 PDF p.94] Page 94

78

3 General-Purpose Sim2Real Protocol for Marker-Based Visuotactile …

12. L. Pinto, M. Andrychowicz, P. Welinder, W. Zaremba, P. Abbeel, Asymmetric actor critic for
image-based robot learning, in 14th Robotics: Science and Systems, RSS 2018 (MIT Press
Journals, 2018)
13. C.R. Qi, H. Su, K. Mo, L.J. Guibas, Pointnet: deep learning on point sets for 3d classification
and segmentation, in Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition (2017), pp. 652–660
14. A. Raffin, A. Hill, A. Gleave, A. Kanervisto, M. Ernestus, N. Dormann, Stable-baselines3:
Reliable reinforcement learning implementations. J. Mach. Learn. Res. 22(268), 1–8 (2021).
http://jmlr.org/papers/v22/20-1364.html
15. C. Sferrazza, A. Wahlsten, C. Trueeb, R. D’Andrea, Ground truth force distribution for learningbased tactile sensing: a finite element approach. IEEE Access 7, 173438–173449 (2019)
16. C. Wang, S. Wang, B. Romero, F. Veiga, E. Adelson, Swingbot: learning physical features from
in-hand tactile exploration for dynamic swing-up manipulation. In: 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), (IEEE, 2020), pp. 5633–5640
17. S. Wang, M. Lambeta, P.W. Chou, R. Calandra, Tacto: a fast, flexible, and open-source simulator
for high-resolution vision-based tactile sensors. IEEE Robot. Autom. Lett. 7(2), 3930–3937
(2022)
18. F. Xiang, Y. Qin, K. Mo, Y. Xia, H. Zhu, F. Liu, M. Liu, H. Jiang, Y. Yuan, H. Wang et al., Sapien:
A simulated part-based interactive environment, in Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition (CVPR) (2020), pp. 11097–11107 Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2020), pp.
11097–11107 Proceedings of the IEEE<error l="306" c="Undefined command " />Conference
on Computer Vision and Pattern Recognition (CVPR) (2020), pp. 11097–11107
19. J. Xu, T. Chen, L. Zlokapa, M. Foshey, W. Matusik, S. Sueda, P. Agrawal, An end-to-end
differentiable framework for contact-aware robot design. In: Proceedings of Robotics: Science
and Systems, Virtual (2021). https://doi.org/10.15607/RSS.2021.XVII.008
20. J. Xu, S. Kim, T. Chen, A.R. Garcia, P. Agrawal, W. Matusik, S. Sueda, Efficient tactile
simulation with differentiability for robotic manipulation, in 6th Annual Conference on Robot
Learning (2022). https://openreview.net/forum?id=6BIffCl6gsM
21. W. Yuan, S. Dong, E.H. Adelson, Gelsight: high-resolution robot tactile sensors for estimating
geometry and force. Sensors 17(12), 2762 (2017)
22. X. Zhang, R. Chen, A. Li, F. Xiang, Y. Qin, J. Gu, Z. Ling, M. Liu, P. Zeng, S. Han, Z.
Huang, T. Mu, J. Xu, H. Su, Close the optical sensing domain gap by physics-grounded active
stereo sensor simulation. IEEE Trans. Robot. 1–19 (2023). https://doi.org/10.1109/TRO.2023.
3235591
23. W. Zhao, J.P. Queralta, T. Westerlund, Sim-to-real transfer in deep reinforcement learning
for robotics: a survey, in 2020 IEEE Symposium Series on Computational Intelligence (SSCI)
(IEEE, 2020), pp. 737–744
24. Y. Zhao, X. Jing, K. Qian, D.F. Gomes, S. Luo, Skill generalization of tubular object manipulation with tactile sensing and sim2real learning. Robot. Auton. Syst. 160, 104321 (2023)

## [Book2025 PDF p.95] Page 95

Chapter 4

Model-Based Strategies: Screw Insertion
for Single PiH Assembly

4.1 Introduction
This chapter presents a screw insertion method for PiH assembly, which combines
the screw motion strategy with the conventional motion control approaches to reduce
the axial frictional force, resulting in an increased area of jamming quadrangle and
decreased jamming possibility. The principle of axial friction reduction and applications for both interference-fit and clearance-fit peg-hole assembly are analyzed, and
comparative experiments for linear and screw motion strategy are implemented for
interference-fit assembly based on position control and clearance-fit assembly based
on impedance control.

4.2 Axial Friction Reduction Analysis
In the conventional PiH assembly controlled by passive compliance or the active
compliance approach, the actual trajectory of the manipulated workpiece is nearly
a 5-DOF (.x, y, z, θx , θ y ) motion, as shown in Fig. 4.1, and the rotation around the
axial (insertion) direction is almost stationary, this motion strategy is called linear
insertion in this chapter. In contrast, the screw motion strategy utilizes the 6th DOF
.θz to obtain axial friction reduction by imposing an additional axial rotation on the
conventional linear insertion along the peg axis.
The principle of axial friction reduction will be derived for both point contact and
face contact situations between a screw moving cylinder and the contacted geometry.

© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_4

79

## [Book2025 PDF p.96] Page 96

80

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Fig. 4.1 a Conventional linear insertion, b proposed screw insertion, c screw motion of points on
the peg

4.2.1 Axial Friction Reduction of Point Contact
Without loss of generality, we consider two situations of point contact between a
rigid cylinder and a stationary rigid geometry.
Figure 4.2a shows contact at the side surface, where the side surface of the cylinder
is tangent to the geometry at point C. The cylinder takes a screw motion that combines
a rotation around the cylindrical axis and a translation along the cylindrical axis. The
motion of a point fixed on the cylinder can be described with twist .ξ = (v, w), where
.w is the angular velocity and .v is linear component of screw motion. The pitch of
screw motion can be expressed as:
.

h=

w·v
va
=
w
w2

(4.1)

where .va is the axial linear velocity of the screw motion along the cylindrical axis.
Build coordinate frame .O − XYZ with the .YOZ plane crossing contact point C
and the cylindrical axis. The . Z -axis is parallel to cylindrical axis, and then, the relationship of instantaneous tangential velocity .vt , axial linear velocity .va and resultant
velocity .vC of point C can be expressed as:
. a

v = vC cos φ

(4.2)

v = vC sin φ

(4.3)

. t

where .φ is the angle between .vt and .va .
There are frictions from two directions at the contact point: axial frictional force
. f a , generated by relative translation along the axis between parts, and tangential

## [Book2025 PDF p.97] Page 97

4.2 Axial Friction Reduction Analysis

81

Fig. 4.2 Point contact of
cylinder and geometry: a
contact at side surface of
cylinder, b contact at the
edge of side surface of
cylinder

frictional force. f t , generated by relative rotation around the axis. The resultant friction
f follows the Coulomb’s friction law as . f C = μN , where . N is the normal force;
then, we can obtain:
. f a = μN cos φ
(4.4)

. C

f = μN sin φ.

. t

(4.5)

Combining Eqs. 4.1–4.5, we obtain the relationship of frictions and the screw
pitch .h and cylinder radius .r as:
.

h
fa
va
= .
=
ft
wr
r

(4.6)

Define .μa = μ cos φ and .μt = μ sin φ, called the equivalent tangential friction
coefficient and equivalent axial friction coefficient, respectively, in this chapter. Then,
Eqs. 4.4 and 4.5 can be simplified as:

## [Book2025 PDF p.98] Page 98

82

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly
. a

f = μa N

(4.7)

f = μt N .

(4.8)

. t

Additionally, .μa , .μt can be calculated by:
μa = √

.

μt = √

.

h

μ

(4.9)

μ.

(4.10)

h2 + r 2
r

h2 + r 2

Figure 4.2b shows contact point C at the bottom edge of the side surface of the
cylinder. The angle between the cylindrical axis and tangent plane is constant as .α.
The cylinder takes the composite motion of rotation around the cylindrical axis and
translation along the projection of the cylindrical axis on the tangent plane, which
can also be seen as a composite motion of the screw motion around the cylindrical
axis and translation along the normal of the tangent plane.
Build coordinate frame .O − XYZ with the .YOZ plane crossing C and cylindrical
axis. The . Z -axis is parallel to the projected line on the tangent plane. Then, the linear
velocity along the projected line .v A and axial linear velocity .va are related by:
v = va cos α.

. A

(4.11)

Similarly, the axial frictional force . f a and tangential frictional force . f t can be
expressed by:
⎧ f
vA
= hr cos α
⎪ fat = wr
⎨
f a = μa N
.
(4.12)
⎪
⎩ μa = √ h cos α2 μ.
2
(h cos α) +r

Equations 4.6, 4.7, 4.9, and 4.12 show that when the cylinder takes a screw motion
with point contacts with a stationary geometry, the resultant friction is reallocated by
the screw motion, where the ratio of axial frictional force . f a and tangential frictional
force . f t is proportional to the pitch .h and in inverse ratio to radius .r .

4.2.2 Axial Friction Reduction of Face Contact
Next, we extend the axial friction reduction of screw motion with point contact to
face contact.
Without loss of generality, we consider the situation shown in Fig. 4.3. The cylinder makes face contact with the stationary coaxial cylinder hole, and the cylinder

## [Book2025 PDF p.99] Page 99

4.2 Axial Friction Reduction Analysis

83

Fig. 4.3 Face contact of
cylinder and geometry

takes downward screw motion around its own axis. We assume that the cylinder peg
and hole are both rigid bodies.
In the case of face contact, axial frictional force and tangential frictional force are
distributed among the entire contact surface, resulting in a friction wrench .w that is
composed of a resultant axial friction . f a and a resultant tangential friction torque
. M t . Wrench describes a force along an axis in space and simultaneously applying a
torque about the same axis, denoted as .w = ( f a , M t ), and the pitch of wrench .h w
can be expressed as:
f · Mt
mt
h = a 2 =
.
 f a
fa

. w

(4.13)

By introducing the cylindrical coordinates (.ρ,.θ ,.z) fixed on the cylinder peg, the
pressure distributed on contact surface can be represented as . p(r, θ, z). Considering
a differential contact surface C, the corresponding differential axial frictional force
d. f a and differential tangential frictional torque d.m t can be obtained according to
Eqs. 4.7 and 4.8:
.d f a = μa p(r, θ, s)r dθ dz
(4.14)
dm t = r 2 μt p(r, θ, s)dθ dz.

.

as:

(4.15)

Hence, the resultant axial friction and tangential friction torque can be expressed
 
. fa =
μa p(r, θ, z)r dθ dz
(4.16)
 
mt =

.

r 2 μt p(r, θ, s)dθ dz.

(4.17)

## [Book2025 PDF p.100] Page 100

84

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Combining Eqs. 4.9, 4.10, 4.16, and 4.17, we can obtain:

μa p(r, θ, s)r dθ dz
μa h
fa
=
.
=  2
= .
mt
r μt r 2
r μt p(r, θ, s)dθ dz

(4.18)

Substituting Eqs. 4.13 in 4.18, we obtain the following:
h =

. w

mt r 2
= .
fa h

(4.19)

Equations 4.16, 4.18, and 4.19 show that when the cylinder takes screw motion
with face contact with geometry, the friction wrench is introduced, and the pitch of
friction wrench .h w is proportional to the square of cylinder radius .r 2 and in inverse
ratio to the pitch of screw motion .h.

4.2.3 Screw Insertion with Axial Friction Reduction
The previous subsections elaborate on the effect of screw motion on axial friction
reduction for situations of both point contact and face contact. With these analysis results, we can obtain the following conclusions for a screw insertion in PiH
assembly:
1. Axial frictional force . f a is equal to the product of normal force . N and equivalent
friction coefficient .μa ;
2. During screw insertion, keeping a constant axial linear velocity .va , the axial
frictional force . f a can be reduced by decreasing screw pitch .h, which means
larger angular velocity .w;
3. With the same screw pitch .h, a larger axial friction reduction can be obtained for
the larger dimension of mating peg.
To sum up, for a screw insertion in PiH assembly, we can control the axial friction
force by adjusting the screw parameter. In the next two sections, we will discuss the
applications of the screw insertion method to clearance-fit and interference-fit PiH
assembly.

4.3 Screw Insertion for Clearance-Fit Assembly
To verify the influence of the screw insertion method on contact situations of
clearance-fit PiH assembly, we will analyze the jamming conditions of both twopoint contact and one-point contact states with the quasi-static model. Then the
application of robotic PiH assembly with screw insertion will be discussed.

## [Book2025 PDF p.101] Page 101

4.3 Screw Insertion for Clearance-Fit Assembly

85

4.3.1 Jamming Conditions
Two-Point Contact
Figure 4.4 represents one type of two-point contact during screw insertion, and the
peg contacts with the hole at two points simultaneously.
In contrast to the situation of conventional linear insertion, additional tangential friction is introduced during screw insertion and the forces on the peg include
insertion forces .(Fx , Fy , Fz , Mx , M y , Mz ) and contact forces .(N1 , f t1 , f a1 ) and
.(N2 , f t2 , f a2 ). Considering the low-velocity nature of assembly process, the equilibrium relationships of forces and moments can be derived under quasi-static
assumption with equation:
⎧
Fx = N1 cos β − f a1 sin β − N2
⎪
⎪
⎪
⎪
⎨ Fy = f t1 − f t2
Fz = N1 sin β + f a1 cos β + f a2
.
⎪
⎪
M
⎪
y = f a2 r + N2 l − N1 r sin β − f a1 r cos β
⎪
⎩
Mz = r f t1 + r f t2

(4.20)

where .l is the insertion depth, .β is the tilt angle, and . D is the diameter of hole.
The contacts for peg screw insertion include both situations, as shown in Fig. 4.2a
and b. Denote the equivalent axial and tangential friction coefficients at two contact
points as .μa1 , .μt1 and .μa2 , .μt2 respectively. The clearance ratio (the ratio of clearance
to diameter) between parts is generally quite small, resulting in tilt angel .β → 0,

Fig. 4.4 Two-point contact
state: a 3D view, b .XOY
plane, c .XOZ plane

## [Book2025 PDF p.102] Page 102

86

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Fig. 4.5 Two different situations for one-point contact

where .sin β ≈ 0, .cos β ≈ 1; thus, .μa1 ≈ μa2 = μa and .μt1 ≈ μt2 = μt . Substituting
this into Eq. 4.20, the jamming condition for two-point contact state can be obtained:
⎧ Fx
N1 −N2
⎪
⎨ Fz = μa (N1 +N2 )
My
= m a FFxz + λa
.
r Fz
⎪
⎩ Mz = N1 +N2
r Fy
N1 −N2

(4.21)

ar
where .m a = − l+2μ
,.λa = 2μl a r .
2r

One-Point Contact
Figure 4.5 represents two different situations for one-point contact during PiH screw
insertion, in which the peg makes contact with the hole in the inner side surface and
the edge of the top surface. During screw insertion, the forces on the peg include
insertion forces .(Fx , Fy , Fz , Mx , M y , Mz ) and contact forces .(N , f t , f a ).
For the situation shown in Fig. 4.5a, the jamming condition can be derived as:
⎧ Fx
1
⎪
⎨ Fz = μa
My
= −1
.
r Fz
⎪
⎩ Mz = 1.
r Fy

(4.22)

For the situation shown in Fig. 4.5b, the jamming condition can be derived as:
⎧ Fx
1
⎪
⎨ Fz = − μa
My
μa r +l
= μa r
.
r Fz
⎪
⎩ Mz = −1.
r Fy

(4.23)

## [Book2025 PDF p.103] Page 103

4.3 Screw Insertion for Clearance-Fit Assembly

87

In contrast to conventional linear insertion, in the .XOY plane, force equilibrium
relations are added for screw insertion, where applied force . Fy and torque . Mz need to
keep balance with the tangential friction . f t . In the .XOZ plane the friction coefficient
.μ is replaced with the equivalent friction coefficient .μa in Eqs. 4.21–4.23 for screw
insertion, resulting in a changed jamming condition.

4.3.2 Jamming Diagram for XOZ and XOY Planes
With jamming conditions Eqs. 4.21, 4.22, and 4.23, jamming diagram of screw
insertion for the .XOZ plane and .XOY plane can be obtained.

Jamming Diagram for XOZ Plane
Figure 4.6 shows the jamming diagram of conventional linear insertion (black solid
line) and the jamming diagram of screw insertion (red dashed line).
The jamming diagram takes the ratio of forces . Fx /Fz to . M y /(r Fz ) as coordinate
axes, forming a close region of quadrangle, and four vertices that represent force
equilibrium conditions for one-point contact state, and the top and bottom lines
represent the equilibrium conditions for two-point contact state. When the proportion
of forces and moments is located in the jamming quadrangle, the peg will slip into
the hole; otherwise, the peg will be stuck on the hole.

Fig. 4.6 Jamming diagram
of screw insertion

## [Book2025 PDF p.104] Page 104

88

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

The jamming diagram describes the feasible region of proportions of forces and
moments, and the area of feasible region determines the jamming possibility, which
can be calculated by the following equation:
.

S=

4λ
.
μ

(4.24)

Combining Eq. 4.21, the relationship of parameters (. μ1 , λ) for conventional linear
insertion and parameters (. μ1a , λa ) for the proposed screw insertion is:
.

1
> μ1
μa

λa > λ.

(4.25)

Hence, we have . Sscrew > Slinear , that is, the area of jamming quadrangles of the
proposed screw insertion is larger than that of conventional linear insertion, suggesting that the proposed screw insertion method for PiH assembly has lower possibility
of jamming than that of conventional linear insertion in the .XOZ plane.

Feasible Region for . M z and . Fy in XOY Plane
Figure 4.7 shows the feasible regions in the .XOY plane, describing the constraints
for the relationship of torque . Mz and force . Fy to prevent jamming.

Fig. 4.7 Feasible regions (in dark color) for . Mz and . Fy in .XOY plane: a one-point contact state,
b two-point contact state

## [Book2025 PDF p.105] Page 105

4.3 Screw Insertion for Clearance-Fit Assembly

89

For one-point contact shown in Fig. 4.7a, the feasible regions to prevent jamming
are divided into four sections (R+, R-, L+, and L-) according to position of contact
points and rotary direction of peg. “R” represents the right side contact, and “L”
represents the left side contact; “+” represents the peg rotating in positive direction
of the . Z -axis, and “-” represents the peg rotating in negative direction of the . Z -axis.
For two-point contact shown in Fig. 4.7b, the feasible regions are divided into
four sections (R+, R-, L+, and L-) according to the value of normal forces and
rotary direction of peg. “R” represents the peg contacts with right normal force . N1
larger than left normal force . N2 , and “L” represents the peg contacts with condition
. N1 < N2 ; “+” represents the peg rotating in positive direction of the . Z -axis, and “-”
represents the peg rotating in negative direction of the . Z -axis. It should be noted
z
2
= NN11 +N
is dependent on the variations of normal forces
that, the curve shape of . M
Fy
−N2
. N1 and . N2 .
When . Mz and . Fy fall in the feasible regions in dark color, the peg can avoid
jamming in the .XOY plane. It can be seen that the feasible regions for one-point
contact and two-point contact are both open regions, which means the area of the
feasible region is infinity. The peg will not be stuck in the .XOY plane with large
enough applied torque . Mz , which is generally satisfied for automatic equipment.
Therefore, there is no need to consider the jamming problem in the .XOY plane for
PiH assembly.
In summary, the jamming analysis for the .XOZ and .XOY planes proves that the
proposed screw insertion method for PiH assembly has lower possibility of jamming
than that of conventional linear insertion.

4.3.3 Robotic Screw Insertion in Peg-In-Hole Assembly
with Axis Offset
Next, we focus on the application of robotic screw insertion to clearance-fit PiH
assembly.
During the robotic assembly process, points on peg could not rotate around the
nominal axis due to geometrical errors of the workpiece and kinematic errors of the
robots. Therefore, the influence of axis offset on screw insertion should be analyzed.
Consider the situation (see Fig. 4.8) in which the peg rotates around the axis with
geometric deviation to the nominal cylindrical axis. The actual rotary axis intersects
the top and bottom face at point . A and . A. When the peg rotates angle .θr around the
actual axis, circle . O on the bottom surface moves to circle . O  . Make a line through
point . A at angle .βr from . X -axis, intersecting the circles at points . B and . B  .
For the sake of simplification, neglect the orientation error between the actual and
nominal axis. Assume that the largest offset from points on the actual axis to the
nominal axis is .d, and it is obtained at point . A with angle .αr from . X -axis, and then,
the radial variations from points on the peg to actual axis in the direction with angle
.βr from . X -axis after rotation can be expressed by:

## [Book2025 PDF p.106] Page 106

90

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Fig. 4.8 Radial variation
after rotation with axis offset

B B  = AB  − AB
. = d cos ϕr +
r 2 − d 2 + d 2 cos2 ϕr
−d cos(ϕr + θr ) − r 2 − d 2 + d 2 cos2 (ϕr + θr )

(4.26)

where .ϕr = π − βr − θr , .αr , βr ∈ [−π, π ].
When condition .βr = π2 + αr − θr is satisfied, . B B  obtain the maximum value
as:
θr
.
.
= Max BB = 2d sin
(4.27)
2
Equation 4.27 shows that when the peg rotates with axis offset, the maximum
variation for points on the peg . has positive correlation with maximum axis offset
.d and rotation angle .θr . If the peg takes continuous screw insertion with .θr > π ,
maximum radial variation . is equal to .2d. For high-precision PiH assembly, the
tight clearance between the peg and hole is generally smaller than .2d. To maintain
screw insertion, the rotation angle .αr must be restricted. A feasible motion strategy
is reciprocate screw insertion with rotation frequency . f screw and amplitude .θscrew (see
Fig. 4.9).
The reciprocate screw insertion needs to meet the following constraints:
1. Mating precision requirement. The maximum radial variation .
the clearance .δ of the mating peg and hole with equation:
2d sin

.

θscrew
≤ km δ
2

is restricted by

(4.28)

where.km is the mating factor defined in this chapter, generally choosing.km < 0.3.
When .θscrew → 0 , Eq. 4.29 can be simplified as:
θ

. screw

δ
≤ km .
d

(4.29)

## [Book2025 PDF p.107] Page 107

4.3 Screw Insertion for Clearance-Fit Assembly

91

Fig. 4.9 Reciprocate screw insertion: a PiH assembly, b variations of .θ over time

2. Inertia matching requirement. The high frequency of reciprocate motion may
arouse the mechanical resonance of automation equipment, especially for heavyweight equipment whose resonance frequency could be tens of Hz. Therefore, the
frequency of reciprocate motion . f screw needs to be restricted as follows:
f

. screw

=

w
≤ ki f r
θscrew

(4.30)

where .ki is the inertia matching factor, generally choosing .ki < 0.3.
3. Friction reduction requirement. Equations 4.9 and 4.12 show that the axial friction
reduction is related to screw pitch. To maintain proper axial friction, the screw
insertion parameter needs to satisfy condition:
μa = √

.

h
h2 + r 2

μ ≤ kf μ

(4.31)

where .kf is friction reduction factor with .kf < 1. Then, the screw parameter .r/ h
needs to satisfy:

.

r
≥
h

1 − kf2
.
kf2

(4.32)

Equations 4.29, 4.30, and 4.32 provide the constraints for the reciprocate screw
insertion that can be used to choose the proper reciprocate screw insertion parameters
to reduce the influence of axis offset.

## [Book2025 PDF p.108] Page 108

92

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

4.4 Screw Insertion for Interference-Fit Assembly
With the axial friction reduction of face contact derived in Sect. 4.2, we will discuss
the application of screw insertion to interference-fit PiH assembly with different
materials, and the expression of the friction wrench during assembly will be derived.
The actual situation of interference-fit PiH assembly does not satisfy the assumption of rigid bodies. After part mating, the peg diameter would decrease, while the
hole diameter would increase, as shown in Fig. 4.10.
Assume that the distribution of the contact pressure . p between the peg and hole
is only dependent on the radial coordinate .ρ; then, the distributed pressure can be
expressed by Lame equations [1] for thick-walled cylinders as:
.

where . E e =

1
Eh

Rh 2 +R 2
−υh
Rh 2 −R 2

p=

δ0 E e
2R

(4.33)

2 
 ; .δ0 is the radial interference between parts.

R 2 +r 2
+ E1p R 2 −rp 2 −υp
p

E p and . E h are the elastic modulus of the peg and hole, respectively; .υp and .υh are
the Poisson ratio of the peg and hole, respectively; . Rp and .rp are the outer and inner
radius of the peg before mating, respectively; . Rh and .rh are the outer and inner radius
of the hole before mating, respectively; and . R is the radius of parts after mating.
In the case of PiH assembly, the peg is solid, and .rp = 0 and . Rh = ∞; then, . E e
can be simplified as:

.

.

Ee =

2
1
− υh ) + E1p
E h (1



1 − υp

where . E e is only related to the material properties of the parts.

Fig. 4.10 Radius of peg and hole with interference fit before/after mating

(4.34)

## [Book2025 PDF p.109] Page 109

4.4 Screw Insertion for Interference-Fit Assembly

93

Substituting Eq. 4.33 into Eqs. 4.16 and 4.17, axial resultant friction . f a and
tangential friction torque .m t can be calculated by:
.

.

fa =

mt =

 l  2π
0

 l  2π
0

μa p Rdθ dz = 2π μa l E e δ0

(4.35)

R 2 μt pdθ dz = 2π μt l E e δ0 R

(4.36)

0

0

where .l is the insertion depth.
Equations 4.35 and 4.36 show that the friction wrench between interference-fit
PiH assembly is proportional to the elastic modulus of the parts, and the feasibility
of screw insertion is closely related to the material of parts.

4.4.1 Interference Fit of Metal Parts
Taking the interference fit between the shaft and roll bearing inner race for example,
the elastic modulus reaches to tens of Gpa, and the peg rotating with axis offset will
destroy the original mating face between parts, generating a large friction wrench.
Therefore, the traditional method of thermal expansion or contraction may be a better
choice.

4.4.2 Interference Fit of Elastic Peg and Inelastic Hole
In the situation in which a peg of elastic material is matted with an inelastic hole, the
elastic modulus of the elastic peg is much smaller than that of the hole, and radius
of the hole remains unchanged after part mating; therefore, we have the following:
m t = 2π μt l E e δ0 rh

.

.

Ee =

Ep
.
1 − υp

(4.37)
(4.38)

The equations show that the tangential torque is only related to the radius of
inelastic hole and the material property of elastic peg, and . E e is much smaller than
that of the mating of metal parts.
Combining Eqs. 4.9, 4.10, 4.35, and 4.37, we obtain:
h =

. w

mt
rh μt
rh 2
=
=
.
fa
μa
h

(4.39)

## [Book2025 PDF p.110] Page 110

94

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Equation 4.39 shows that the axial friction reduction of screw insertion still works
for the interference fit of elastic peg and inelastic hole, which will be verified in the
following experiment section.
Therefore, the interference-fit mating process of the elastic part and inelastic part
can be a suitable application for screw insertion. The axial friction reduction of
screw insertion from certain aspects accounts for the phenomenon that the stopper
of bottle may be easier to pull out when the operation is imposed with rotation. To
avoid the abnormal behavior due to the rotational and axial movement, particularly
in the area nearer to contact points or surfaces, the suggestive materials are the cork
materials which are usually used as the stopper of wine bottle, and another is the
rubber materials which can be used for sealing of equipment to keep oil or water.

4.5 Experiments
To verify axial friction reduction with screw motion, the experiment of point contact
between the peg and rigid plane and screw insertion experiment of both interferencefit and clearance-fit PiH assembly are carried out. During the experiments, the peg
is manipulated with a 6-DOF ABB IRB 1200 robot, and the forces and moments are
recorded with an F/T sensor (ABB Sensor 165) installed on the wrist of the robot.

4.5.1 Experiment of Screw Motion with Point Contact
The robotic system for point contact between an aluminum peg (size:
30 mm.×100 mm) and an aluminum contact plane is shown in Fig. 4.11a. In
the first stage of the experiment, the robot linearly moves the peg along the plane
with constant velocity; in the second stage, the peg takes a composite motion similar
to Fig. 4.2b, where the peg moves along the same line and rotates around its own
axis uniformly and simultaneously. The process is repeated with different screw
parameters ( .r/ h = 0.3, 0.6, 1, 0.2, 15, 2, 3, 4), and the axial linear velocity .va is
0.1 mm/s.
Figure 4.12 shows the force/torque data with screw parameter .r/ h = 1.2 in each
motion stage. As shown in Fig. 4.11b, the relationship of . N , f a , f t and measured
force can be expressed with:

.

⎧
⎨ Fx = N cos β0 cos θ0 − f a sin β0 cos θ0 + f t sin θ0
Fy = −N cos β0 sin θ0 + f a sin β0 sin θ0 + f t cos θ0
.
⎩
Fz = −N sin β0 − f a cos β0 .

(4.40)

During the experiments, .β0 is set to .0.5◦ , and .θ0 is calibrated with force/torque data.
Thus, the equivalent axial friction coefficient.μa and the equivalent tangential friction
coefficient .μt can be calculated.

## [Book2025 PDF p.111] Page 111

4.5 Experiments

95

Fig. 4.11 Point contact
experiment: a setup, b force
analysis diagram

Figure 4.13a shows the values of the equivalent friction coefficients .μa and .μt
changing from the linear motion stage to composite motion stage. It can be seen that,
in composite motion stage, the resultant friction is reallocated with an introduced
tangential friction . f t , resulting in decreased .μa and increased .μt . The results demonstrate the effectiveness of the friction reallocation method for axial friction reduction
proposed in Sect. 4.2.
Figure 4.13b shows the variations of .μt and .μa with respect to screw parameter
.r/ h. It can be seen that when the screw parameter .r/ h increases, .μa decreases, and .μt
increases, and the magnitude of variations becomes larger. The results are identical to
the axial friction reduction of screw motion with point contact described by Eqs. 4.9
and 4.10.
Table 4.1 provides the comparison of the ratio of measured equivalent friction
coefficients.k  = μμat and the ratio of theoretical equivalent friction coefficients.k = hr .
The results are in good agreement with Eq. 4.6 that the ratio of axial friction . f a and
tangential friction . f t is proportional to the pitch .h and in inverse ratio to radius .r .
In order to test the influence of velocity, material, and radius of peg on the axial
friction reduction, three groups of experiments are performed with different screw

## [Book2025 PDF p.112] Page 112

96

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Fig. 4.12 Force/torque data with screw parameter .r/ h = 1.2 in each motion stage

Fig. 4.13 Variations of.μa and.μt : a for screw parameter.r/ h = 1.2 in linear and composite motion
stage, b for different screw parameter .r/ h in composite motion stage

parameters .r/ h, as shown in Fig. 4.14. Table 4.2 shows the variations of .μt and
μa with respect to screw parameter .r/ h and the comparison of the measured and
theoretical ratio .k  and .k. Experimental results show that the axial friction reduction
of screw motion is effective for different axial linear velocities, material and radius
of the peg, which demonstrates the robustness of the screw insertion method.
In summary, the experimental results of screw motion with point contact verify
the effect of screw motion on axial friction reduction derived in Sect. 4.2.

.

## [Book2025 PDF p.113] Page 113

4.5 Experiments

97

Table 4.1 Results for . 30 mm aluminum peg with .va =0.1 mm/s
◦
◦
.k
.θr ( )
.w( /s)
.μt
.μa

.k

0.3
0.6
1
1.2
1.5
2
3
4

0.307
0.587
0.867
1.143
1.361
1.831
2.669
4.134

0.3438
0.6876
1.146
1.3752
1.719
2.292
3.438
4.584

0.1146
0.229
0.382
0.4584
0.573
0.764
1.146
1.528

0.0398
0.0691
0.0896
0.1003
0.1117
0.1177
0.1269
0.1272

0.1296
0.1178
0.1034
0.0878
0.0821
0.0643
0.0475
0.0308





.k /k(%)

102.43
97.85
86.66
95.25
90.70
91.57
88.98
103.39

Fig. 4.14 Different pegs: a
30 mm aluminum peg, b
. 30 mm steel peg, c
. 40 mm aluminum peg
.

4.5.2 Experiment of Screw Insertion in Interference-Fit
Peg-In-Hole Assembly
Figure 4.15 shows the robotic PiH assembly system for a rubber taper workpiece peg
(size: . 29-. 34 mm, hardness: 65 Shore A) and an aluminum workpiece hole (size:
. 30 mm.×60 mm). The PiH assembly is implemented by the conventional position
control, and the peg is manipulated in two motion strategies (linear insertion and the
reciprocate screw insertion).
The process is repeated with screw different parameters shown in Table 4.3, which
are chosen according to Eqs. 4.29, 4.30, and 4.32, insertion velocity .va is 2 mm/s ,and
reciprocate frequency . f screw is 1.11 Hz. To avoid large position and orientation errors
between the axis of the rubber taper peg and the axis of the steel hole, the trajectory
of screw insertion is calibrated beforehand.
Figure 4.16 shows the force/torque data with screw parameter.r/ h = 1. The screw
insertion process is performed in the 0–8 s stage, and then, the peg maintains stationary. During the insertion, Z direction bears most of the contact friction, and according
to the equilibrium relationship, . Fz reflects the value of the resultant axial friction . f a

## [Book2025 PDF p.114] Page 114

98

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Table 4.2 Results for screw motion with different velocity, material, and radius of peg


Setting
.k
.μt
.μa
.k
.k /k(%)
30 mm
Aluminum
0.05 mm/s

.

30 mm
Steel
0.1 mm/s

.

40 mm
Steel
0.1 mm/s

.

0.3

0.0375

0.1249

0.273

91.15

0.6
1
2
3
0.3

0.0671
0.0922
0.1166
0.1237
0.0508

0.1118
0.0922
0.0583
0.0412
0.1492

0.557
0.897
1.671
2.782
0.341

92.86
89.68
83.53
92.72
113.63

0.6
1
2
3
0.3

0.0701
0.0978
0.1190
0.1171
0.0467

0.1121
0.1086
0.0667
0.0421
0.1504

0.626
0.901
1.784
2.781
0.310

104.29
90.08
89.19
92.71
103.42

0.6
1
2
3

0.0677
0.0905
0.1070
0.1197

0.1221
0.0935
0.0601
0.0432

0.554
0.967
1.781
2.772

92.36
96.72
89.04
92.39

Fig. 4.15 Setup for interference-fit PiH assembly: a linear insertion, b screw insertion, c rubber
taper workpiece peg

## [Book2025 PDF p.115] Page 115

4.5 Experiments

99

Table 4.3 Parameters of reciprocate screw insertion
◦
No.
.r/ h
.w( /s)

.θscrew ( )

1
2
3
4
5
6

0
0.573
1.146
1.91
3.82
7.64

0
0.3
0.6
1
2
4

0
2.55
5.1
8.49
16.98
33.96

◦

Fig. 4.16 Force/torque data for linear insertion (a) and screw insertion with .r/ h = 1 (b)

and . Mz reflects the value of the resultant friction torque . Mt . Reciprocate screw insertion results in the periodic fluctuation of the forces and moments. Deeper insertion
makes the magnitude of . f a and .m t increase substantially, which is because tighter
mating of the taper peg causes larger contact pressure between parts.
Table 4.4 shows force/torque data with different screw parameters .r/ h. To eliminate the influence of periodic variations The axial friction . f a and tangential torque .m t
in the table take values in the peak force of . Fz and peak torque of . Mz , respectively;
then, the actual pitch of friction wrench .h w = m t / f a , and the matching rate . Rh is the
ratio of actual to nominal friction wrench pitch.
It can be seen that, when the screw parameter .r/ h increases, the resultant axial
friction . f a decreases, and the resultant tangential torque . Mt increases substantially.
The results are identical to the axial friction reduction of screw motion with face
contact described by Eqs. 4.9, 4.10, 4.16, and 4.17. The matching rates show good

## [Book2025 PDF p.116] Page 116

100

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Table 4.4 Results for reciprocate screw insertion

.r/ h
.m t (Nm)
. f a (N)
.h w (mm)

.h w (mm)

. Rh (%)

linear
0.3
0.6
1
2
4

0
4.5
9
15
30
60

100
81.94
85.82
89.98
92.78
96.16

0
0.202
0.357
0.465
0.761
1.514

58.73
54.8
46.22
34.45
27.34
26.24

0
3.686
7.724
13.498
27.835
57.698

agreement with Eqs. 4.19 and 4.39 that the pitch of friction wrench.h W is proportional
to the square of cylinder radius .r 2 and in inverse ratio to the pitch of screw motion .h.
In summary, the experimental results verify the axial friction reduction of reciprocate screw insertion for interference-fit PiH assembly. The peg is tapered in experiments for convenience of inserting a peg with larger radius into a hole. It should be
noted that the effects also work for the non-tapered peg because the constant radius
of metal hole is the parameter that really matters according to Eq. 4.39.

4.5.3 Experiment of Screw Insertion in Clearance-Fit
Peg-In-Hole Assembly
Figure 4.17 shows the robotic system for the assembly of an aluminum workpiece
peg (size: . 29.96 mm) and an aluminum workpiece hole (size: . 30 mm), and the
clearance is 0.04 mm. The robotic assembly process is implemented by the impedance
control, and the peg is inserted into the hole in two different motion strategies, that is
the conventional impedance control with linear insertion and the revised impedance
control with reciprocate screw insertion.

Fig. 4.17 Setup for
clearance-fit PiH assembly

## [Book2025 PDF p.117] Page 117

4.5 Experiments

101

Impedance Control with Different Motion Strategies
For conventional impedance controlled PiH process, the position errors between the
peg and hole are compensated with force/torque errors measured from the F/T sensor
by equation:
.
P = K e (F − Fref ) + Be ( Ḟ − Ḟref )
(4.41)
where . P = ( x, y, z, θ x, θ y, θ z) is the increment motion, . K e =
diag{kx , ky , .k z , kθ x , kθ y , kθ z } is the stiffness matrix, and . Be = diag{bx , by , bz ,
.bθ x , bθ y , bθ z } is the damping matrix.
During linear insertion process, the contact torque . Mz is almost 0, so the
corresponding increment rotation angle . θz for each motion step is almost 0.
In contrast, the increment rotation angle . θz for the reciprocate screw insertion
is revised to construct the screw motion, and the rotation angle round the insertion
direction for each motion step can be expressed by:
.

θzi =

z
, i = 1, 3, 5, . . .
h
z
− h , i = 2, 4, 6, . . .

(4.42)

where .i is the motion step number. The frequency of reciprocate screw motion
depends on the increment insertion depth . z and insertion velocity .va .
During the experiments, the control parameters are set as: transitional stiffness
.k x = k y = 0.006, .kz = 0.01, rotational stiffness .k θ x = k θ y = k θ z = 0.003, damping
matrix . Be = 0, and the reference force . F ref =(0,0,-50 N,0,0,0). The insertion depth
is set to 30 mm, which is measured from the bottom of chamfer along the axis of
the hole, the reciprocate screw parameters are chosen according to the constraints of
Eqs. 4.29, 4.30, and 4.32, and screw pitch .h and insertion velocity .va are the variables
for experiments.

Experimental Results
Figure 4.18a–c shows the force/torque data with different insertion velocities (.va =0.5,
1, and 2 mm/s) after each motion step of linear insertion and reciprocate screw insertion. The assembly process can be divided into three stages: (I) chamfer-cross, (II)
small contact, and (III) large contact. In large contact stage, it can be seen that the
differences in . Fx , . Fy , . Mx , . M y , . Mz between the two motion strategies are small,
while the insertion force . Fz for reciprocate screw insertion, which reflects the axial
frictional force, is evidently reduced compared with that for linear insertion, and the
change law is not affected by the changing insertion velocities. The small changes
of other forces and moments demonstrate the feasibility of screw insertion method
for clearance-fit assembly, as discussed in Sect. 4.3.
In order to test the influence factor of axial friction reduction, the reciprocate
screw insertion experiments with different screw parameters (.r/ h=0.6, 1, 1.5, 2) are
implemented with constant insertion velocity (.va =1 mm/s). The force/torque data

## [Book2025 PDF p.118] Page 118

102

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Fig. 4.18 Force/torque with respect to insertion depth for linear and screw insertion: a .va =1 mm/s,
b .va =0.5 mm/s in large contact stage, c .va =2 mm/s in large contact stage

after each motion step in large contact stage are shown in Fig. 4.19, and the results
for linear insertion are shown in the blue line for comparison. It can be seen that, the
curves of force . Fx , Fy and torque . Mx , M y , Mz fluctuate across the blue line (linear
insertion) in a small range for different .r/ h. Compared with linear insertion, the
insertion force . Fz is evidently reduced for all reciprocate screw insertions, and the
gap increases with larger.r/ h. The results are consistent with the analysis of Sect. 4.2.

## [Book2025 PDF p.119] Page 119

4.5 Experiments

103

Fig. 4.19 Force/torque data in large contact stage for linear and reciprocate screw insertion with
.r/ h = 0.6, 1, 1.5, 2

For quantitative analysis of the screw insertion method, the experiments with
different screw parameters are repeated for 10 times, and the average . F z in 22–28
mm depth are shown in Table 4.5. The results indicate that the average reduction rate
. R  Fz of . Fz accords basically with the theoretical value . R Fz calculated by Eqs. 4.7
and 4.9.
In summary, the above experimental results verify the axial friction reduction for
reciprocate screw insertion for clearance-fit PiH assembly.

## [Book2025 PDF p.120] Page 120

104

4 Model-Based Strategies: Screw Insertion for Single PiH Assembly

Table 4.5 Results for PiH assembly with different .r/ h
.r/ h
. F z (N)
. R  Fz (%)
Linear
0.6
1
1.5
2

.−11.12
.−9.58
.−8.17
.−6.63
.−5.75

0
83.6
73.7
61.7
50.4

. R Fz (%)

0
85.7
70.7
55.5
44.7

4.6 Conclusion
This chapter presents a screw insertion method for PiH assembly, which combines
the screw motion strategy with the conventional motion control approach, resulting
in reduced axial frictional force and better contact situations for mating process. The
effectiveness of the method is verified by the results of the point contact experiment and screw insertion experiment of both interference-fit and clearance-fit PiH
assembly.
For transition-fit PiH assembly, which is also a common type of engineering fit,
the actual contact state is either clearance fit or interference fit. Therefore, the axial
friction reduction of screw motion derived above still works in the case of transition
fit. Furthermore, although the above-mentioned frictions are sliding frictions, axial
friction reduction still works for the maximum static friction. The derivation of axial
static friction reduction is similar to that of sliding friction. Compared with only
applying a pushing force, the cylinder workpiece is easier to move by imposing a
pushing wrench, including an axial torque and a pushing force.

Reference
1. A. Liuti, F.R. Vedugo, N. Paone, C. Ungaro, Monitoring techniques for high accuracy interference fit assembly processes. AIP Conf. Proc. 1740(1), 060005 (2016). https://doi.org/10.1063/
1.4952677

## [Book2025 PDF p.121] Page 121

Chapter 5

Model-Based Strategies: Jamming
Analysis for Dual PiH Assembly

5.1 Theoretical Analysis
5.1.1 Model Simplification
The dual PiH assembly is the key foundation of multiple PiH assembly. Therefore, this
chapter focuses on dual PiH assembly as shown in Fig. 5.1. The assembly component
is assumed to hold the following features: (a) The round pegs and holes have the
same length. (b) Pegs and holes are rigid, whereas the connecting plate is elastic.
Because gravity mainly causes symmetrical deformation in the.Y direction, the threedimensional model can be simplified into a two-dimensional model in the.YOZ plane.

5.1.2 Deformation Analysis
The dimensional parameters of pegs and holes are set as shown in Fig. 5.2. Components with pegs or holes are both symmetric. The densities of pegs and connecting
plate are .ρ1 and .ρ2 , respectively. The height and Young’s modulus of the connecting
plate are .w and . E, respectively. There are some constrains for the deformation angle
.θ to avoid pegs being stuck outside holes.
Constraint 1: As shown in Fig. 5.3, pegs will be stuck outside holes if the deformation angle is too big. The constraint of deformation angle can be modeled as:
.

|θ | ≤ θc1 = arccos(d/D)

(5.1)

Constraint 2: The minimum and maximum distances between two pegs should
fulfill (see Fig. 5.3):
l

. min

≥ C − D, lmax ≤ C + D

© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_5

(5.2)
105

## [Book2025 PDF p.122] Page 122

106

5 Model-Based Strategies: Jamming Analysis for Dual PiH Assembly

Fig. 5.1 Geometric configuration of dual PiH: .Y axis is parallel to the link line of two top centers
of holes, and . Z axis is parallel to the hole axis, and . X axis is perpendicular to the .Y axis and . Z axis

Fig. 5.2 Dimensional parameters of pegs and holes: the overall length and width of the component
with holes are . A and . B, respectively; those of the component with pegs are .a and .b, respectively;
diameters of pegs and holes are .d and . D, respectively; the distance between the peg axes and that
between the hole axes are .c and .C, respectively; the height of pegs and that of holes are .h and . H ,
respectively. The width of connecting plate is .w

.

c − 2h sin θ − d cos θ ≥ C − D
c − 2h sin θ + d cos θ ≤ C + D

(5.3)

According to the parameters, limiting angles of Constraints 1 and 2 are .θc1 and
θ , respectively.

. c2

θ

. c1

= arccos(d/D), θc2 ≈ arcsin((D − d)/2h)

(5.4)

## [Book2025 PDF p.123] Page 123

5.1 Theoretical Analysis

107

Fig. 5.3 The deformation angle is .θ; the minimum and maximum distances between two pegs are

.l min , l max , respectively. . D, .d, .C, and .c are shown in the Fig. 5.2

Considering these two constraints, if the deformation angle .|θ | is bigger than
θ or .θc2 , jamming states in the initial assembly procedure will occur. But since
the connecting plate is elastic, the contact force in the bottom of pegs allows the
connecting plate to generate an opposite deformation when jamming, and makes
pegs approach the alignment with holes. After the approximate alignment of pegs
and holes, the deformation will become smaller than .θc2 . Therefore, contact states
can be divided into two stages: Stage 1 is large deformation stage and Stage 2 is
small deformation stage.

. c1

5.1.3 Contact State Analysis
All contact states can be theoretically divided into peg point contact with hole surface
and hole point contact with peg surface. To distinguish different contact states, intersection points between base surface and side surface of holes and pegs in the .YOZ
plane are considered as markers. Thus, the contact points, . P1 , . P2 , . P3 , . P4 , . H1 , . H2 ,
. H3 , . H4 , can be numbered, respectively, as shown in Fig. 5.4. The difference of deformation angle and insertion depth makes . P1 , . H2 , . H3 , . P4 different in two stages. To be
specific, . H2 , . H3 are intersection points between edge of hole and base surface of peg
in the large deformation stage, and between edge of hole and side surface of peg in
the small deformation stage, respectively. . P1 and . P4 are intersection points between
base surface of peg and outside surface of hole in the large deformation stage, and
between base surface of peg and inside surface of hole in the small deformation stage,
respectively.

## [Book2025 PDF p.124] Page 124

108

5 Model-Based Strategies: Jamming Analysis for Dual PiH Assembly

Fig. 5.4 One-point contact states: a large deformation stage; b small deformation stage

5.1.4 Contact Force Analysis
Contact forces can be analyzed based on known contact states. The contact force of
one-point contact state is analyzed first and contact forces are further extended to
two-point contact states. If . H1 is the contact point, and the motion direction of pegs
is downward, the mechanical model can be constructed as shown in Fig. 5.5, where

## [Book2025 PDF p.125] Page 125

5.1 Theoretical Analysis

109

Fig. 5.5 Contact force
analysis of one-point contact:
the deformation angle and
the angle of rotation are .θ, .α,
respectively; the contact
force and frictional force are
. FN , . F f , respectively; the
forces data measured by the
force sensor in the .Y , . Z
directions and the moment
data in the . X direction are
. Fy , . Fz , . M x , respectively

Fy , . Fz , and . Mx are the force data from 6 degrees of freedom (DOF) force/torque
sensor.
The initial position error is tiny so that . H1 would contact with the side surface of
left peg. Thus, directions of contact force and friction can be represented as shown in
Fig. 5.5. The reference point is assumed to be the top surface center of the component
with holes. According to the quasi-static equilibrium condition, the contact force and
friction can be calculated using:

.

Fy =
Fz =

.




(FN y + F f y )

(FN z + F f z )

(M N x + M f x )
Mx =

(5.5)

F f = μFN
According to the contact state shown in Fig. 5.5, we have:
Fy = −FN c(θ + α) + μFN s(θ + α)
Fz = −FN s(θ + α) − μFN c(θ + α)
.
−FN (s(θ + α) + μc(θ + α)) (C + D)
Mx =
2

(5.6)

The .s(θ ), .c(θ ) represent .sin(θ ), .cos(θ ), respectively. From Eq. 5.6, we can get
the relationship among . Fy , . Fz , and . Mx :

## [Book2025 PDF p.126] Page 126

110

5 Model-Based Strategies: Jamming Analysis for Dual PiH Assembly

Table 5.1 Ratios of forces and moments of one-point contact states
State
. P1
. H1
. P2
. H2
. P3
. H3
. P4
. H4

Large deformation stage

Small deformation stage

Fy
− cos(θ+α)+μ sin(θ+α) M
(C+D)
. F = − sin(θ+α)+μ cos(θ+α) , C Fx = − 2C
z
z


 P2 
Z +μ(C−D)
Fy
1 , Mx = − H
. F = −μ
C Fz
2Cμ
z



 P1 
2Z H
−μ(C+D)
Fy
1 , Mx =
.F = μ
C Fz
2Cμ
z
Fy
− cos(θ+α)+μ sin(θ+α) M
(C+D)
. F = − sin(θ+α)+μ cos(θ+α) , C Fx = − 2C
z
z


 P2 
Z +μ(C−D)
Fy
1 , Mx = − H
. F = −μ
C Fz
2Cμ
z

Fy
−μ cos(θ+α)+sin(θ+α) M
(C−D)
. F = − μ sin(θ+α)+cos(θ+α) , C Fx = − 2C
z
z


 P3 
Z H +μ(C−D)
Fy
1 , Mx =
.F = μ
C Fz
2Cμ
z
Fy
−μ cos(θ−α)+sin(θ−α) M
(C−D)
. F = μ sin(θ−α)+cos(θ−α) , C Fx = 2C
z
z


 P4 

Y H
Fy
M
. F = μ, C Fx = − C
z
z
Fy
− cos(θ−α)+μ sin(θ−α) M
(C+D)
. F = sin(θ−α)+μ cos(θ−α) , C Fx = 2C
z
z

Fy
−μ sin(θ+α)+cos(θ+α) M
(C−D)
. F = − μ cos(θ+α)+sin(θ+α) , C Fx = − 2C
z
z


 P3 
Z H +μ(C−D)
Fy
1 , Mx =
.F = μ
C Fz
2Cμ
z
Fy
−μ sin(θ−α)+cos(θ−α) M
(C−D)
. F = μ cos(θ−α)+sin(θ−α) , C Fx = 2C
z
z


 P4 
2Z H
−μ(C+D)
Fy
1 , Mx = −
. F = −μ
C Fz
2Cμ
z
Fy
− cos(θ−α)+μ sin(θ−α) M
(C+D)
. F = sin(θ−α)+μ cos(θ−α) , C Fx = 2C
z
z



 P1 
Y H 
Fy
M
. F = −μ, C Fx = C
z
z

Fy
−c(θ + α) + μs(θ + α)
=
Fz
−s(θ + α) − μc(θ + α)
.
Mx
(C + D)
=
Fz
2

(5.7)

Similarly, the ratio of forces and moments of other one-point contact states as
shown in Fig. 5.4 can be obtained as shown in Table 5.1, where . Z HPi and .Y HPi are
coordinates of peg contact points in the hole coordinate system.
It is noted that contact states of . H2 and . H3 are different in three-dimensional
space since the width of peg causes two-point contact in the . X direction rather than
one-point contact. However, the direction of the resultant force does not change, so
the above contact force analysis still works.
Next, one-point contact state is extended to two-point contact state. Arbitrary twopoint contact states can be considered as the combination of one-point contact states.
The calculation scheme of two-point contact states will be described in detail using
the model as shown in Fig. 5.6, where, left peg is inside the left hole, meanwhile,
. H1 and . P2 are contact points. Based on the quasi-static equilibrium condition and
Eq. 5.5, we can obtain:
Fy = −FN 1 c(θ + α) + FN 2 + μFN 1 s(θ + α)
Fz = −μFN 1 c(θ + α) − FN 1 s(θ + α) − μFN 2
.
Mx = −0.5FN 2 (|Z P H 2 | + μ(C − D))

(5.8)

− 0.5FN 1 (s(θ + α) + μc(θ + α)) (C + D)
As can be seen from Eq. 5.8, . Fy , . Fz , and . Mx are linear equations of . FN 1 and . FN 2 .
To generalize two-point contact state, it is important to get relationships between
one-point contact state and two-point contact state. We have following results.

## [Book2025 PDF p.127] Page 127

5.1 Theoretical Analysis

111

Fig. 5.6 Contact force
analysis of two-point contact
state: the deformation angle
and the angle of rotation are
.θ, .α, respectively; the
contact force and frictional
force are . FN 1 , FN 2 ,
. F f 1 , F f 2 , respectively; the
force data measured by the
force sensor in the .Y , . Z
directions and the moment
data in the . X direction are
. Fy , . Fz , and . M x , respectively

Lemma 1: The ratio of forces and moments in the force balancing state of twopoint contact state is the link line of two one-point contact states correspondingly.
Proof: To generalize two-point contact state, Eq. 5.8 can be written as:
Fy = k y1 FN 1 + k y2 FN 2
. Fz = k z1 FN 1 + k z2 FN 2

(5.9)

Mx = km1 FN 1 + km2 FN 2
The ratio of forces and moments of general two-point contact states are:
k

y2
km2
− kkm2
− kkz2z1 k z1 2 Fy
Mx
k y1
k
m1 k m1
.
= km1
+
k
k
k
y2
y2
Fz
− z2 k y1 km1 Fz
− z2 k z1

(5.10)

Fy
k y1 FN 1 + k y2 FN 2
=
Fz
k z1 FN 1 + k z2 FN 2

(5.11)

k y1

.

k z1

k y1

k z1

According to the above equations, it can be proved that, in the force balancing state
of two-point contact state, . Mx /Fz is the linear function of . Fy /Fz . When .k y2 , .k z2 and
.k m2 are equal to zero, Eq. 5.10 is changed to Eq. 5.7, and the two-point contact state
is degenerated to the one-point contact state. Through the above analysis, Lemma 1
is proven and will be used in the following jamming analysis.

## [Book2025 PDF p.128] Page 128

112

5 Model-Based Strategies: Jamming Analysis for Dual PiH Assembly

5.1.5 Jamming Analysis
The objective of jamming diagrams is to express relationships between forces and
moments in the two-dimensional plane and to analyze the jamming state and adjust
control parameter, respectively. According to the above contact force analysis, points
in jamming diagram represent one-point contact equilibrium state, while line segments represent two-point contact equilibrium state. Points and line segments will
form some enclosed areas, which divide the whole plane into two parts, outside
areas and inside areas. Outside areas represent jamming states where pegs cannot be
inserted, because resistant forces and moment are too large due to the contact and
friction [1], whereas inside areas represent non-jamming states where pegs can be
inserted. Contact states in Table 5.1 can be used to draw jamming diagram.
The exact relative position relationship between pegs and holes is unknown.
Therefore, it is difficult to determine the contact state exactly. However, the jamming diagram is only used to adjust a control parameter, then the most possible
jamming diagram can be chosen according to the position estimation and property of
their assembly objects. The method of using jamming diagram to adjust the control
parameter will be described in the next section.
Drawing jamming diagram is divided into two steps:
Step 1: Calculate values of . Fy /Fz and . Mx /Fz and select the most possible onepoint contact equilibrium states in the coordinate system shown in Fig. 5.7.
Step 2: Connect the above points, and link lines represent two-point contact equilibrium states.
Because of concave property of the connecting plate and geometric relationships
of pegs and holes in this experiment, we choose the most possible jamming diagrams
in two deformation stages, which are shown in Fig. 5.7. The above jamming diagrams
are formed by some quadrilaterals, and each quadrilateral represents a different contact equilibrium state. In jamming diagram, some parameters, such as . Z HPi and .Y HPi
are not constant, which are relevant to the insert depth and peg position, etc., and
jamming diagrams are dynamic. In experiments, the measured force/moment data
will be compared with dynamic jamming diagrams, and control parameters will be
adjusted.

5.1.6 Vertical Assembly Strategy Analysis
As shown in Fig. 5.8, there are two states in the assembly process: contact state and
mated state.
(a) Contact state: the control strategy is based on force position and velocity control
as shown in Fig. 5.9a, which is a common control strategy in robotics. Through forceposition and velocity control, the velocity and position of pegs can be controlled
by the forces (see Fig. 5.9a). Reference forces and moments will be set, and the
force/moment data from the force sensor will be compared with reference forces

## [Book2025 PDF p.129] Page 129

5.1 Theoretical Analysis

113

Fig. 5.7 Jamming diagrams

Fig. 5.8 Assembly states: a
Contact; b Mated. The
lowest and highest point on
pegs are . Pdown , . Pup ,
respectively

and moments. Errors will be used to guide pegs to move until holes and pegs are
mated. During the assembly process, the position of the robot flange is calculated
using robot kinematic method, and pegs are fixed on the robot flange, so the position
of pegs .x(t), . y(t), and .z(t) relative to the initial position of pegs can be calculated
in real time.

## [Book2025 PDF p.130] Page 130

114

5 Model-Based Strategies: Jamming Analysis for Dual PiH Assembly

Fig. 5.9 Control strategy and jamming factor: The real-time position of bottom center of pegs is
. x(t), . y(t), and .z(t), respectively, and the increment of them is .dx(t), .dy(t), and .dz(t), respectively.

The velocity of peg is .v(t), and the reference and real-time forces measured by the force sensor are

. F0 , . F(t), respectively. The real-time error of . F(t) is .e f (t), and the differential of .e f (t) is .def /dt.
.l 2 represents the distance between the jamming point and zero point, and .l 1 represents the distance

between the corresponding point on the jamming quadrilateral and zero point

(b) Mated state: the control strategy is still force-position and velocity control.
The reference force in the vertical direction increases, and reference forces in other
directions will be set to zero. Then pegs will move along the trajectory with minimum
contact forces. The flexible dual PiH assembly is finally finished.
As stated in the above section, jamming factor (. J f ) is adjusted according to the
jamming state during assembly process. . J f K pz and . K px y /J f are used to control
the movement of pegs. If pegs are in the jamming state, . J f decreases, then . J f K pz
controls pegs to move more slowly in the .z direction to avoid jamming state in the
next step, and . K px y /J f controls pegs to move more quickly in the .x, y direction
to escape from the jamming state. The jamming factor is calculated according to
the ratio between the position of jamming point .l2 and the position of corresponding
point on the jamming quadrilateral .l1 , which are shown in Fig. 5.9b. If a point is in the
jamming state and .l2 > l1 , then the jamming factor . J f is . J f min + (1 − J f min )(l1 /l2 ),
otherwise the jamming factor is 1. If .l2 is close to infinity, . J f will be close to . J f min
rather than 0, then the singular problem can be avoided. . J f min is the minimum value
of jamming factor, which can be chosen by users, and relationships between . J f min
and assembly results are shown in the Sect. 5.2.

## [Book2025 PDF p.131] Page 131

5.2 Experimental Results

115

5.2 Experimental Results
5.2.1 Experiment Design
The experimental system is shown in Fig. 5.10. An ABB IRB1200 robot and a 6DOF force/moment sensor are used to perform a flexible dual PiH assembly task.
In experiments, pegs are fixed on the robot end-effector, and holes are installed on
the experimental table. Pegs are pre-positioned close to holes. The material of one
connecting plate of pegs is acrylonitrile butadiene styrene (ABS), and the material of
another connecting plate of pegs is Polytetrafluoroethylene (PTFE). Both materials
are flexible. The material of holes and pegs is aluminum, which is rigid compared to
ABS and PTFE. The component parameters are shown in Table 5.2.
In the contact and mated states, the control strategy is force position and velocity
control. . K pz = 0.02, . K px y = 0.002, . K dz = 0.002, . K d x y = 0.0002, and . K v = 5. In
the contact state, reference forces .[Fx , Fy , Fz ] = [5, 10, 20] N and .[Mx , M y , Mz ] =
[0, 0, 0] Nm.
In the mated state, .[Fx , Fy , Fz ] = [0, 0, 50] N and .[Mx , M y , Mz ] = [0, 0, 0] Nm.
Moreover, because the lubrication is used during assembly process, the friction coefficient .μ = 0.1, and integral deflection angle .α = 0◦ . In the large deformation stage,

Fig. 5.10 Robotic PiH assembly
Table 5.2 Parameters
Value
a = 300 mm, b = 80 mm, c = 200 mm, w = 8 mm
Dualpeg
Dualhole

. d = 29.96 mm, h = 110 mm, ρ1 = 2.7 g/cm 3

ρ2 = 1.02 g/cm3 , EABS = 2 GPa, EPTFE = 0.5 GPa
A = 400 mm, B = 100 mm, C = 200 mm
.
D = 30 mm, H = 100 mm

## [Book2025 PDF p.132] Page 132

116

5 Model-Based Strategies: Jamming Analysis for Dual PiH Assembly

Fig. 5.11 Deformation angle measurement

the maximum of deformation angle .θ = 1◦ , which is set as the threshold of jamming diagrams, and in small deformation stage, .θ = 0.01◦ . As shown in Fig. 5.11,
real deformation angles are measured, and the measurement of real deformation
angles are .1.54◦ in large deformation stage, and .0.19◦ in small deformation stage.
Considering the measurement noise, the real deformation angles are approximate to
the theoretical values. The small error of deformation angle threshold values leads to
tiny variation of jamming factor and does not influence the whole method. Therefore,
theoretical values of deformation angle can be seen as two possible threshold values
in each stage. If a point is outside the jamming quadrilateral, this point represents
jamming state.

5.2.2 Experimental Results
The assembly task is implemented successfully (see Fig. 5.12). The flexible dual
pegs move from free state (I) to contact state (II) and mated state (III). Then pegs
are inserted deeper and deeper (IV, V). Finally, the task is accomplished as shown in
Fig. 5.12(VI).
The position and force/moment data are shown in Fig. 5.13. There are three stages
during the assembly process: A—large deformation stage, B—small deformation
stage, and C—extracting stage. All of these stages are shown in Fig. 5.13b and d.
In state 1 and state 2 of the large deformation stage, the magnitude of coordinate
curve slope is about .−3 × 10−3 mm/step (Fig. 5.13a). Because the deformation is
large and pegs are in jamming state, resistances are large such as . Fz = −12 N and
. M x = 1 Nm (Fig. 5.13c). In state 3, the magnitude of Z coordinate curve slope
increases to .6 × 10−2 mm/step, and the magnitude of . Fz decreases to .−2.8 N
(Fig. 5.13a and c), which means that the deformation and resistances decrease and
pegs start to mate with holes. In state 4, the magnitude of coordinate curve slope
increases to maximum (.0.13 mm/step), and insert depth increases continuously
(from .−2 mm to .−5 mm, Fig. 5.13a), which means that resistances decrease to
minimum (. Fz = −0.5 N, . Mx = 0.1 Nm, Fig. 5.13c).

## [Book2025 PDF p.133] Page 133

5.2 Experimental Results

117

Fig. 5.12 Assembly process

Fig. 5.13 a, b Positions of pegs in the coordinate system of holes. c, d Six-axis force/moment data.
e, f Jamming diagrams

In the small deformation stage, the jamming state appears at first, because
the magnitude of coordinate curve slope decreases from .0.63 to .0.13mm/step
(Fig. 5.13b), and magnitudes of . Fz and . Mx increase to .−30 N and .−1.3 Nm, respectively (Fig. 5.13d). After orientation adjustment, magnitudes of force and moment
decreased again (. Fz = −3 N, . Mx = −0.3 Nm), and the magnitude of coordinate
curve slope increases again (.0.97 mm/step, Fig. 5.13b and d). Moments increase
with inserted depth, but forces are always small (Fig. 5.13d), which means that the
position of pegs is correct, but the connecting plate produces symmetry deformation.
The maximum values of moments and force are .10 N and .3 Nm, respectively, which
are still small compared to the insert depth. Therefore, the deformation is not big and
it does not prevent the assembly task from completion.

## [Book2025 PDF p.134] Page 134

118

5 Model-Based Strategies: Jamming Analysis for Dual PiH Assembly

Fig. 5.14 Experiment data for 50 trials, including positions of pegs relative to the initial position
in the coordinate system of holes and six-axis force/moment data

Jamming diagrams are shown in Fig. 5.13e. In every stage, the data are divided
into four parts according to the time sequence. Relationships between forces and
moments are marked as points with different colors and shapes in different parts. In
the beginning of large deformation stage, because the positions of pegs and holes are
small, so the jamming stage appears and red and yellow points fall into outside area
of red quadrilateral (part 1 and part 2 in Fig. 5.13e). In part 3, blue points fall into
inside area of red quadrilateral (unstable state). This result shows that pegs start to
mate with holes because of the deformation of connecting plate and the motion of
pegs. In part 4, most green points fall into inside area of blue quadrilateral rather than
red quadrilateral because the contact state of pegs and holes change after deforming.
The static state changes from . H1 H2 H3 H4 to . H1 P2 P3 H4 . In the small deformation
stage, most (.79.5%) points fall into the inside area of blue quadrilateral, which means
that the whole assembly process is smooth. There are some (.20.5%) points that are
still outside blue quadrilateral, and it shows that jamming state appears, then the
jamming factor adjusts to control the movement of pegs. All of these analyses are
consistent with the results shown in Fig. 5.13a and c, which verifies the effect of
jamming diagrams in analyzing jamming states.
Fei et al.also researched the dual PiH assembly problems [1], but diameters of
their pegs and holes are.d  = 19.8 mm and. D  = 20 mm, respectively. For our model,
diameters are .d = 29.96 mm and . D = 30 mm, respectively. What’s more, the clearance between our pegs and holes is .0.04 mm, which is much smaller than theirs:

.0.2 mm. According to experiment results, the maximum value of contact force . Fz

and contact moments. M y in their assembly process are.15 N and.2 Nm, respectively.
In our experiment, after entering small deformation stage, the maximum value of . Fz 
and . M y  are about .10 N and .2 Nm, respectively. The maximum value of . Mz  is a
little bigger, which is .3 Nm, but considering the small clearance, these results are
also acceptable. The assembly task in this chapter is much more difficult than the

## [Book2025 PDF p.135] Page 135

5.2 Experimental Results

119

Fig. 5.15 Comparison between results using jamming factor and without using jamming factor

task of [1], but results are comparable with theirs, which shows the effectiveness of
our control algorithm.
In order to validate the stability of control strategies, the same assembly task is
conducted for 50 times, and the success rate is .100% as shown in Fig. 5.14. The
magnitude of coordinate curves slope is all about .0.4 mm/step, and the maximum
value of contact force and contact moments are .15 N and .0.6 Nm, respectively,
which means that the contact forces are small during the assembly process and
shows the effectiveness of jamming state analysis and control algorithm stated in
this chapter. What’s more, the assembly times are all about 24 s (Fig. 5.14), and 97%
of the assembly time for each assembly is the communication time between the
computer and the robot control center. The time efficiency can be further improved
by changing the control platform (Fig. 5.15).

## [Book2025 PDF p.136] Page 136

120

5 Model-Based Strategies: Jamming Analysis for Dual PiH Assembly

5.3 Conclusion
In this chapter, contact states, contact forces, and jamming states are analyzed in
detail for dual PiH assembly, which is helpful to understand the whole assembly
task. Firstly, contact states are divided into two stages: large deformation stage and
small deformation stage, and all possible one-point contact states are enumerated.
Secondly, the relationships between contact forces and moments are analyzed for
all one-point contact states by quasi-static analysis. The one-point contact state is
extended to a two-point contact state. Thirdly, jamming diagrams are studied, and
corresponding control strategies are designed.
In real PiH experiments, the maximum value of . Fz and . Mz is about .10 N and
.3 Nm, respectively, and the successful rate is .100% for 50 trials. The result verifies
the effectiveness of the proposed jamming analysis and control strategies. However,
there are still some limitations of the proposed method. Because the quasi-static
conditions can only be used when the effect of friction dominates inertial effects, the
proposed method in this chapter cannot be used for high-speed assembly task.

Reference
1. Y. Fei, X. Zhao, Contact and jamming analysis for three dimensional dual peg-in-hole mechanism. Mech. Mach. Theory 39(5), 477–499 (2004)

## [Book2025 PDF p.137] Page 137

Chapter 6

LFD for Hard-Measuring
Easy-Deformation PiH Assembly

6.1 Working Principle
6.1.1 The Assembly Robot System
The proposed assembly robot system consists of a real-time 3D vision sensor, an
assembly robot, and a computer (Fig. 6.1). The assembly robot generally has 6DOF, and the assembled component is mounted on the robot end effector. In hardmeasuring easy-deformation assembly, the hole is the fixed component and the peg
is the moving component. There are several markers on the demonstration peg and
the real assembled peg, and the marker locations with respect to the peg axis have
been calibrated in advance. The overall assembly process is as follows (see Fig. 6.2):
1. A small and light demonstration peg with the same fit tolerance as the real peg
is inserted into the fixed real hole, and the human assembly process is recorded
by the real-time 3D vision sensor. Obviously, the human assembly path is not
optimal, even with jamming.
2. The human assembly path is optimized using the LFD method to obtain the
optimal assembly path, which is collinear to the fixed hole axis.
3. The real peg is moved along the optimal assembly path. The assembly process
is also monitored by the real-time 3D vision sensor, and the robot motion path is
corrected using the GPR-based deformation prediction and compensation method
until the assembly process is completed.

© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_6

121

## [Book2025 PDF p.138] Page 138

122

6 LFD for Hard-Measuring Easy-Deformation PiH Assembly

Fig. 6.1 The assembly robot system
Fig. 6.2 The assembly
process

6.1.2 LFD-Based Optimal Path Planning Method
Prior to assembly, the optimal assembly path is required to avoid jamming and
damage to the assembly component. To this end, an LFD-based optimal path planning
method is proposed for hard-measuring easy-deformation assembly in this chapter.
The principle and procedure are described as follows:
The human operator assembles a small and light demonstration peg into the fixed
hole as a demonstration. Then, the assembly process is recorded by a real-time 3D
vision sensor to teach the robot. Because there is no assisted force or position sensor
to restrict manual assembly, the assembly cannot achieve high precision along the
assembly path without jamming; hence, it is not effective for the robot to directly
repeat the manual assembly path. To simplify the optimization of the manual assembly path, the human operator is asked to rotate the demonstration peg along the hole

## [Book2025 PDF p.139] Page 139

6.1 Working Principle

123

Fig. 6.3 Maximum inclined
angle and insertion distance

axis to reach the maximum inclined angle because it is impossible for the human
operator to keep the axis of the demonstration peg collinear to that of the hole.
Then, the robot learns and plans the optimal assembly path (the hole axis) by
using the following optimal path planning method.
Assume that the maximum clearance (the acceptable maximum assembly error)
between the peg and hole is .σ and that the distance the peg has entered into the hole
is .d. Then, the maximum inclined angle .θ is a function of the insertion distance .d
(see Fig. 6.3).
σ
.θ =
(6.1)
d
Clearly, the maximum inclined angle .θ decreases with the increased insertion distance of the demonstration peg; thus, the maximum inclined angle .θ of the demonstration peg is becoming increasingly smaller.
Obviously, the angle .θ is also the angle between the peg axis .v p and the hole axis
.v h . Hence, we have
.v p · v h = cos θ
(6.2)
During the assembly procedure, there will be several groups of peg axes .v p and
the corresponding maximum inclined angle .θ , composing an .n-by-3 matrix .V p and
→
vh that
an .n-by-1 matrix .φ. Due to the measurement error, there is no perfect vector .−
can fit the above equation for every peg position. Thus, we obtain a least squares
problem. Set an objective function

.

M=

n


2
→
(V pi · −
vh − cos θi )

(6.3)

i=1

→
vh to minimize the objective
The least squares problem is to find an optimal .−
function. Because the problem can be expressed in matrix form, the least squares
problem has a closed-form solution. Calculate the pseudo-inverse of the matrix .V p
pinv(V p ) = (Vp V p )−1 Vp

.

(6.4)

## [Book2025 PDF p.140] Page 140

124

6 LFD for Hard-Measuring Easy-Deformation PiH Assembly

Then, the optimal hole axis .v h can be obtained by a closed-form solution:
v = (Vp V p )−1 Vp cos φ

. h

(6.5)

The obtained hole axis .v h is the desired optimal assembly path.
In practical assembly, the robot generally moves along a given assembly path,
which determines a series of the assembled component positions. However, to insert
the peg into the hole, a correct orientation is also required (see Fig. 6.4). Note that the
peg is expected to move along the hole axis throughout the PiH assembly procedure.
Therefore, only the position of the peg is varied during the assembly process, while
the orientation of the peg is constant. Clearly, the peg axis must coincide with the
optimal assembly path.
Here, we can construct a demonstration peg coordinate system . Px yz using the
markers on the demonstration peg as shown in Fig. 6.5, and the peg axis can be
described in this coordinate system. The next step is to find an orientation of . Px yz
to allow the demonstration peg axis to coincide with the obtained optimal assembly
path. Set the real-time 3D vision sensor coordinate system as .V Sx yz . Set the rotation
matrix from . Px yz to .V Sx yz as .R. Then, we have the following constraint
v = R · v pp

. h

(6.6)

where .v h is the optimal assembly path in .V Sx yz and .v pp is the peg axis in . Px yz ,
which is calibrated in advance. Here, .R is a 3-by-3 matrix with three unknown
rotation angles; however, there is only one constraint equation for determining the
demonstration peg orientation. In other words, the peg can rotate along the optimal

Fig. 6.4 Correct orientation
versus incorrect orientation

## [Book2025 PDF p.141] Page 141

6.1 Working Principle
Fig. 6.5 Demonstration peg
coordinate system

125

Markers
Moving part

Peg

Demonstraon peg
coordinate system

Peg axis
Hole
Hole axis

Vision sensor
coordinate system

assembly path and turn upside down along any axis that is perpendicular to the
optimal assembly path, as shown in Fig. 6.6. To solve this problem and simplify the
measurement, the markers are allowed to completely face the real-time 3D vision
sensor, which restricts the other two direction rotations of the demonstration peg,
that is, the desired orientation can be determined.
At this point, the optimal assembly path is learned and planned by using the
proposed LFD-based optimal path planning method. The proposed method does not
require exact alignment of the peg and hole, and the demonstration is easy to perform
without an additional force sensor or position sensor.

Fig. 6.6 Unconstrained
motion

Unconstrained moon

## [Book2025 PDF p.142] Page 142

126

6 LFD for Hard-Measuring Easy-Deformation PiH Assembly

6.1.3 GPR-Based Deformation Prediction and Compensation
Method
After obtaining the optimal assembly path, the next step is to control the assembled
component moving along the planned optimal assembly path. The heavy-weight
component inevitably results in deformation of the robot. To improve robot motion
accuracy, a GPR-based deformation prediction and compensation method is proposed
in this chapter.

6.1.4 GPR Model Establishment
The assembled component is mounted on the robot end effector. To establish the GPRbased deformation prediction and compensation model, we control each robot joint to
move to different angles, and the corresponding poses of the assembled component
are measured by the real-time 3D vision sensor. Comparing the measured poses
with the theoretical poses of the assembled component, we can obtain . N groups of
deformation, which are set to be the output of training data .Y . A 6-by-. N matrix .X
composed of . N groups of the 6 joint angles is considered as the input of training
data.
Set a process function . f (x) between the input .X and output .Y . Define a Gaussian
process . f (x) ∼ G P(m(x), k(x, x  )), where .m(x) and .k(x, x  ) are the mean function
and covariance function of . f (x), respectively. Then, we have
m (x) = E [ f (x)]

(6.7)



k(x, x  ) = E ( f (x) − m(x)) · ( f (x  ) − m(x  ))

(6.8)

.

.

where .x, x  ∈ R d are random variables.
The robot motion error and measurement error cannot be ignored. The process
function is
. y = f (x) + ε
(6.9)
where .X and . y are samples of .X and .Y , respectively, and .ε is the error. To construct
a Gaussian process, the error .ε is assumed to obey the Gaussian distribution .ε ∼
N (0, σn2 ), where .σn2 represents the integrated error of .X and .Y .
Thus, we can obtain the prior distribution of output .Y according to the input .X:
.

Y ∼ N (0, G)

(6.10)

in which .G = K (X, X) + σn2 In is the covariance function of the distribution, where
. K (X, X) = K n = (ki, j ) and.ki, j = k(x i , x j ) presents the correlation between the two
elements .xi and .x j of the input .X. For the test input, its predicted output is subject

## [Book2025 PDF p.143] Page 143

6.1 Working Principle

127

to the joint probability distribution. Then, for a new input .x ∗ , the distribution of the
corresponding output . y ∗ is

.

Y
y∗



 

K (X, X ) + σn2 In K (x, x ∗ )
∼ N 0,
k(x ∗ , x ∗ )
K (x ∗ , x)

(6.11)

where . K (x, x ∗ ) is the covariance matrix of .X and .x ∗ , and we have . K (x, x ∗ ) =
K (x ∗ , x) . Therefore, the above distribution is a joint probability distribution of .Y
and . y ∗ . Then, the posterior distribution of the output . y ∗ is
y ∗ X, y, x ∗ ∼N ( ȳ ∗ , cov(y ∗ ))

(6.12)

ȳ ∗ = K (x ∗ , x)G −1 y

(6.13)

cov(y ∗ ) = k(x ∗ , x ∗ ) − K (x ∗ , X )G −1 K (X, x ∗ )

(6.14)

.

in which
.

.

6.1.5 Training of GPR Model
The reliability of the GPR model depends on the covariance function, and the training
of the GPR model consists of searching for the optimal mean and covariance function.
A commonly used covariance function is the square exponential function, which has
the following form:
1
k(x, x  ) = σ 2f exp(− (x − x  ) M −1 (x − x  ))
2

.

(6.15)

where . M = diag(li2 ), .li2 is the variance scale, and .σ 2f is called the signal variance [1,
2, 4]. Thus, we obtain a hyper-parameter .θ = {M, σ 2f , σn2 }, which describes the
character of the input and output of the GPR model. Therefore, the GPR training
consists of optimizing .θ by the training data.
The optimal .θ is generally obtained using the likelihood method. First, set a likelihood function . L(θ ) = − log( p(Y |X, θ )), in which . p(Y |X, θ ) is the conditional
probability of the output .Y . Typically, the likelihood function is of the following
form:
1  −1
1
n
. L(θ ) =
(6.16)
Y C Y + log |C| + log 2π
2
2
2
where .C = K n + σn2 In .

## [Book2025 PDF p.144] Page 144

128

6 LFD for Hard-Measuring Easy-Deformation PiH Assembly

Second, calculate the partial derivatives of . L(θ ), through which we obtain
.

∂ L(θ )
1
∂C
= tr ((αα  − C −1 )
)
∂θi
2
∂θi

(6.17)

where .α = C −1 Y = (K + σn2 In )−1 Y .
Finally, the optimal hyper-parameter is obtained by minimizing the partial derivatives using the steepest descent method.
At this point, the optimal hyper-parameter and the covariance function are
obtained. Then, given a new input, we can predict the output using the trained GPR
model.

6.1.6 Online GPR-Based Deformation Compensation Method
Prior to assembly, the real-time 3D vision sensor measures the manual assembly procedure to obtain the optimal assembly path. The assembled component is mounted on
the robot end effector. Then, the robot is controlled to move in space, and the assembled component poses are measured by the real-time 3D vision sensor; meanwhile,
several groups of joint angles are also recorded. Taking into account the deformation
caused by the heavy-weight component, the measured pose . M cannot completely
coincide with the theoretical pose .T , and the deformation is:
ε= M−T

.

(6.18)

Considering . N groups of joint angles . J and deformations .ε as the input and output
of the GPR model, we can train the GPR model using the above method. Then, given
a new joint angle, we can predict the deformation using the GPR model. To reach
the target pose .T regardless of robot deformation, the following control strategy is
performed.
First, calculate the corresponding joint angles using the inverse kinematics:
J = ikine(T)

. 0

(6.19)

However, taking into account the robot deformation, the assembled component cannot reach the target pose only by robot kinematics. By setting the joint angles . J0 to
be the new input, the deformation .ε0 can be predicted by the GPR model:
ε = GPR(J0 )

. 0

(6.20)

Second, the adjusted pose by robot motion is:
.

T p1 = T − ε0

(6.21)

## [Book2025 PDF p.145] Page 145

6.1 Working Principle

129

Third, we can obtain the adjusted joint angles using the inverse kinematics
J = ikine(Tp1 )

. 1

(6.22)

Finally, the actual pose of the assembled component is
.

A P1 = T p1 + ε1

(6.23)

where .ε1 = G P R(J1 ) is the deformation corresponding to the joint angles . J1 . Here,
J = J0 ; therefore, we have to determine whether . A P1 is equal to .T . Calculate the
→
v of the matrixes . A P1
corresponding Euler angles .α, .β, .γ and translation vector .−

and .T . Setting two thresholds .k1 and .k2 , if . (αi , βi , γi ) − (αT , βT , γT ) > k1 or


> k2 , we should perform the next prediction using
. (x i , yi , z i ) − (x T , yT , z T )
the new initiate joint angles . J1 and deformation .ε1 .
. 1

T p2 = T − ε1

(6.24)

. 2

J = ikine(Tp2 )

(6.25)

A P2 = T p2 + ε2

(6.26)

.

.

The process iterates until . (αi , βi , γi ) − (αT , βT , γT ) < k1 and


< k2 , and the assembled component can be con. (x i , yi , z i ) − . (x T , yT , z T )
sidered to reach the target pose .T .
Finally, control the robot movement to the joint angles . Ji , and the assembled
component will reach the target pose. Figure 6.7 shows the entire iteration procedure.
Note that the iteration is calculated by the computer, and the robot does not move
until the iteration is completed and the final joint angles are obtained; therefore, the
control process is very efficient.

6.1.7 Jam Handling Method
During the assembly procedure, the pose of the assembled component should be
monitored to avoid jams. The real-time 3D vision sensor measures the pose of the
assembled component at every target point along the planned assembly path. For
the .i-th target pose, the measured pose . Mi is compared with the predicted pose . Pi .
If the difference .m i = Mi − Pi is greater than a given threshold, it means that the
deformation prediction has a noticeable error, which would lead to a high risk of
jams. Therefore, the deformation must be predicted again using the newest training
data.
The jam handling method is performed by controlling the assembled component
to move back to the pose . Pi−1 and performing another iteration (see Fig. 6.8).

## [Book2025 PDF p.146] Page 146

130
Fig. 6.7 Flowchart of
GPR-based control method

6 LFD for Hard-Measuring Easy-Deformation PiH Assembly

Target pose

Input joint angle
Predict deformaon

Adjust pose
No
Update joint angle
Update deformaon
Predict actual pose

Reach target pose

Yes
End
Fig. 6.8 Flowchart of
dealing with jam control
strategy

Start
Iniate pose

Get joint angles &
deformaon
Update GPR model
Predict pose
No
Reach target pose
Yes
End

## [Book2025 PDF p.147] Page 147

6.2 Simulation Experiments

131

First, obtain the first group of joint angles using the above method, and then
control the robot to move to the predicted pose . A P1 . The actual pose . M1 is obtained
by the vision sensor.
Second, the deformation .ε1 = M1 − T p1 and the joint angles . J1 are added to
the GPR training data to predict the next pose . A P2 . Similarly, the actual pose . M2 is
obtained, and the GPR model is updated. The process iterates until the error.(Mi − T )
is smaller than the given threshold.
Throughout the assembly procedure, the deformation is predicted by the GPR
method without modeling the kinematics after deformation. Therefore, the proposed
deformation prediction and compensation method is suitable for different assembly
systems and payload conditions with high accuracy and efficiency.

6.2 Simulation Experiments
To verify the effectiveness of the proposed GPR method, we first perform the following simulation experiments.

6.2.1 Cantilever Beam
Set a cantilever beam as shown in Fig. 6.9, where point P represents the assembled
component, and its position changes with the angle .θ . Consequently, we have the
following kinematics:
x = L · cos θ
.
(6.27)
y = L · sin θ
Taking into account gravity acting on the assembled component, the deformation
cannot be ignored. Set the material to be aluminum, and the elasticity modulus is
. E = 71 GPa. Set the link length to be . L = 500 mm and the width and height of the
cross-section to be .b = 30 mm and .h = 50 mm, respectively. Set the gravity acting

Fig. 6.9 The cantilever
beam

## [Book2025 PDF p.148] Page 148

132

6 LFD for Hard-Measuring Easy-Deformation PiH Assembly

Fig. 6.10 Deformation of
the cantilever beam

on the assembled component to be . F = 1000 N. Then, by ignoring the gravity acting
on the cantilever beam and tensile deformation, for each joint angle, we can obtain
the deformation of point P (shown in Fig. 6.10).
F·cos θ·L
Dx = − 3E(bh
3 /12) · sin θ
F·cos θ·L 3
Dy = − 3E(bh 3 /12) · cos θ
3

.

(6.28)

Given several joint angles .θ , we can obtain several positions of point P and the
corresponding deformation . D. Then, we add measurement error to obtain the measured values . M and measured deformation .m D. Here, the measurement error is set
to be approximately 10.µm. The GPR model can now be constructed by the input .θ
and output .m D. To test the GPR model, we randomly set 10 new input joint angles
.α and calculate the theoretical deformation . Dα . Then, we place the new input .α into
the GPR model to obtain the predicted deformation . D p . Finally, the two groups of
deformations are compared to obtain the prediction error of the GPR model.
.

E R = D p − Dα

(6.29)

Table 6.1 presents the simulation results. As shown in this table, the prediction
error is approximately 10.µm, which is close to the measurement error. Figure 6.11
shows the prediction error at different joint angles, and as shown, the prediction error
is very stable and has no relation with the joint angles.

6.2.2 Assembly Robot System
We set an assembly robot using the parameters of the ABB IRB 120 robot (i.e., the
robot kinematics). Then, given a set of joint angles . J , we can obtain the theoretical
terminal pose . PT using the theoretical robot kinematics. Taking into account the
deformation caused by the assembled part, we obtain the actual terminal pose . PA .
Therefore, the deformation is . D = PA − PT . Due to the measurement error, the

## [Book2025 PDF p.149] Page 149

6.2 Simulation Experiments

133

Table 6.1 Deformation and prediction error of cantilever beam
.α/rad
. D x /mm
. D y /mm
. E R x /mm
0.003
0.213
0.290
0.556
0.833
0.929
0.933
1.074
1.518
1.570

.−7.511
.−7.175
.−6.898
.−5.419
.−3.399
.−2.692
.−2.663
.−1.705
.−0.021

0.000

0.020
1.552
2.056
3.367
3.739
3.602
3.593
3.146
0.398
.−0.051

0.011
0.018
0.016
0.017
0.018
0.017
0.017
0.014
0.013
0.014

. E R y /mm

0.011
0.018
0.014
0.012
0.015
0.017
0.013
0.018
0.020
0.012

Fig. 6.11 Prediction error in two directions

measured pose . PM is not equal to the actual pose, and the measured deformation is
D M = PM − PT , which is the output of the GPR training data.
In the proposed control system, the input and output of the GPR model are the
joint angles and deformation, respectively. To train the GPR model, we set the robot
to move 40 poses in space, and the deformations are measured by the vision sensor.
Then, the GPR model is trained by the 40 groups of training data.
To test the effectiveness of the system, let the robot randomly move to 10 poses,
obtaining 10 groups of joint angles . Jo . By placing . Jo into the GPR model, we
can obtain the predicted deformation . D P . Finally, the predicted deformation . D P is
compared with the actual deformation . D to obtain the prediction error. Here, the
measurement error of the vision sensor is set to be 10.µm.
Table 6.2 presents the simulation results, in which PD and OD are the position
and orientation deformation and .ERP and .ERO are the position and orientation pre-

.

## [Book2025 PDF p.150] Page 150

134

6 LFD for Hard-Measuring Easy-Deformation PiH Assembly

Table 6.2 Deformation and prediction error of assembly robot
Pose
PD/.µm
OD/.
.ERP /.µm

.ERO /.

1
2
3
4
5
6
7
8
9
10

13.6
13.1
13.6
13.2
18.0
11.4
13.8
14.8
17.2
15.0

103.1
96.0
94.7
90.2
99.8
94.1
52.6
95.5
98.5
81.8

209.8
185.8
163.1
181.0
196.0
141.9
91.2
176.6
197.2
156.4

16.2
14.7
16.0
14.9
22.6
12.8
16.2
17.8
21.7
17.5



Fig. 6.12 Position
prediction error

Fig. 6.13 Orientation
prediction error

diction error. As shown in this table, the prediction error is considerably less than the
deformation. Figures 6.12 and 6.13 show the position prediction error and orientation prediction error at different joint angles. As shown, the prediction error is very
stable. Hence, the proposed GPR method can reach high accuracy, and it is highly
versatile.

## [Book2025 PDF p.151] Page 151

6.3 Realistic Experiments

135

6.3 Realistic Experiments
Figure 6.14 shows the proposed assembly robot system. Here, the assembly robot is
ABB IRB 120, whose maximum payload is 3 Kg. The real-time 3D vision sensor
consists of two cameras, whose resolution is 2560.× 2480. The assembled component
is designed to be close to the maximum payload of the robot; therefore, the assembly
task can be considered to be hard-measuring and easy-deformation. The hole is
40.µm larger than the peg in diameter; thus, the accepted maximum assembly error
is 40.µm, which exceeds the robot motion accuracy.
A laser tracker is used to verify the effectiveness of the proposed GPR method. As
shown in Fig. 6.14, the laser tracker measures reflectors mounted on the assembled
component to obtain the pose of the assembled component. Here, the laser tracker
(Leica AT901) works at a distance of approximately 1 m, and the measurement accuracy is within 20.µm [3, 5].
By controlling the robot to move to several poses in space, the poses of the
assembled component are measured by the laser tracker. Then, several groups of
joint angles and the corresponding deformations are obtained. The GPR model can
be trained by setting the joint angles to be the input and deformations to be the output.
The robot is then controlled to move to 20 new locations, and the robot joint angles
. J and deformations .ε are obtained. Then, the new joint angles . J are input to the
GPR model to obtain the predicted deformations .ε p . Finally, the prediction error is
obtained by comparing .ε p with .ε.
Figures 6.15 and 6.16 show the position error and orientation error. As shown,
the position error is approximately 10–20.µm, which is close to the measurement
error, and the orientation error is approximately 10–20 arc s, which is approximately
5–10.µm offset at a distance of 100 mm. Thus, the experiment verifies that the proposed GPR method can achieve high accuracy and satisfy the requirements for hardmeasuring easy-deformation assembly.

Fig. 6.14 The experiment
system

Robot
Assembled Part Vision Sensor

Fixed Hole

## [Book2025 PDF p.152] Page 152

136

6 LFD for Hard-Measuring Easy-Deformation PiH Assembly

Posion Error
Posion Error
20.0

18.0
16.0

Error/μm

14.0
12.0

10.0
8.0
6.0
4.0
2.0

0.0
0

5

10

15

20

N

Fig. 6.15 Position prediction error of GPR

Orientaon Error

Orientaon Error

30.0

Error/arcsecond

26.0

22.0

18.0

14.0

10.0
0

5

10

15

20

N

Fig. 6.16 Orientation prediction error of GPR

As shown in Fig. 6.14, the hole and the real-time 3D vision sensor are fixed on
the platform. The markers on the demonstration peg are tracked by the real-time
3D vision sensor throughout the demonstration procedure to obtain the peg axis in
the FOV of the real-time 3D vision sensor. After the human operator performs the
assembly demonstration, the optimal assembly path is learned and planned by the
robot system using the proposed path planning method. Next, the assembled peg
is mounted on the robot end effector, and then the practical assembly is performed
along the planned assembly path.
The assembly procedure is monitored by the real-time 3D vision sensor, and the
robot motion is controlled by the above GPR-based deformation prediction and compensation method. The result indicates that the robot follows the obtained assembly
path very well, and the assembly process is successful, proving that the obtained
assembly path is the optimal one due to the tiny acceptable assembly error.

## [Book2025 PDF p.153] Page 153

References

137

References
1. M. Lázaro-Gredilla, J.Q. Candela, C.E. Rasmussen, A.R. Figueiras-Vidal, Sparse spectrum gaussian process regression. J. Mach. Learn. Res. 11, 1865–1881 (2010)
2. D. Nguyen-Tuong, M.W. Seeger, J. Peters, Model learning with local gaussian process regression. Adv. Robot. 23, 2015–2034 (2009)
3. A. Nubiola, I.A. Bonev, Absolute calibration of an ABB IRB 1600 robot using a laser tracker.
Robot. Comput.-Integr. Manuf. 29, 236–245 (2013)
4. J. Yuan, K.L. Wang, T. Yu, M. Fang, Reliable multi-objective optimization of high-speed WEDM
process based on gaussian process regression. Int. J. Mach. Tools Manuf. 48, 47–60 (2008)
5. T.L. Zobrist, J.H. Burge, W.B. Davison, H.M. Martin, Measurements of large optical surfaces
with a laser tracker. In: Advanced Optical and Mechanical Technologies in Telescopes and
Instrumentation, vol. 7018 (SPIE, 2008), pp. 1289–1300

## [Book2025 PDF p.154] Page 154

Chapter 7

LFE: Model-Free RL Method for PiH
Assembly

7.1 Introduction
The model-based control methods introduced in Chaps. 4 and 5 face challenges when
applied to various PiH assembly scenarios due to the complexity of the contact
models involved. Tuning controller parameters for new assembly tasks demands
considerable time and effort. Consequently, an advanced algorithm independent of
physical contact model analysis is essential for effective execution of multiple PiH
assembly tasks.
In contrast to the model analysis, human workers can accomplish PiH assembly tasks with their learned experience [12]. Inspired by this, industrial robots can
perform complex PiH assembly through RL algorithms. However, the following challenges still remain when DDPG algorithms are implemented in realistic industrial
assembly processes.
1. In multiple PiH assembly tasks, it is costly to collect enough experience
data to train the agent in such a large search space, mapping the observed
high-dimensional and continuous states to high-dimensional and continuous
actions [8].
2. The reward function of DRL algorithms evaluates the agent actions that the agent
performed [6]. However, it is difficult to find a perfect function to evaluate whether
the agent actions could satisfy the long-term desirability.
3. The trade-off of the exploration/exploitation strategies, the techniques for choosing actions during the learning process, largely decides the efficiency of DRL
algorithms. The previous exploration approaches for continuous actions control
tasks only try to explore the better action and novel state efficiently [3]. However, in realistic robotic tasks, the safety of the exploration action needs to be
considered first [1].

© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_7

139

## [Book2025 PDF p.155] Page 155

140

7 LFE: Model-Free RL Method for PiH Assembly

To utilize the superiority of the DDPG algorithm for performing multiple PiH
assembly tasks well, we present a Model-driven Deep Deterministic Policy Gradient
(MDDPG) algorithm that enables the robot to learn a high-level assembly policy
in realistic scenarios. The training process of the MDDPG algorithm is driven by a
traditional force control strategy rather than learning from a zero basis, which can
decrease the number of training experiments and avoid risky actions. We propose a
fuzzy reward system rather than designing a complex reward function. The proposed
fuzzy reward system incorporating prior knowledge evaluates the assembly process,
taking more comprehensive factors into account than previous works, which not only
improves the learning efficiency but also avoids the agent becoming trapped in a local
minimum.
In addition, we also present a feedback exploration strategy, which can tune the
exploration process according to the performance of the last training step. The primary exploration strategy in continuous action space is .ε−greedy exploration [2]
by picking a random action noise with probability .ε. In contrast to fixed exploration methods, an active exploration strategy is presented in [5] by applying the
Gaussian noise to the continuous action parameters. However, the aforementioned
exploratory approaches rely on collecting sufficient samples from environments and
probably result in meaningless or risky actions, which is impermissible in realistic
assembly scenarios. To eliminate the meaningless exploration trials and risky exploration actions, the feedback exploration strategy incorporates expert knowledge into
modifying exploration process.
A simplified assembly simulation model is constructed to test the effectiveness
of our algorithm and compare with the previous algorithms without a fuzzy reward
system and feedback exploration strategy. Moreover, a real-world dual PiH assembly
experiment is implemented to demonstrate the availability and generality in the real
world.
The remainder of this chapter is structured as follows. Section 7.2 explains the context of the proposed algorithm. The implemented fuzzy reward system is described
in Sect. 7.3. The details of the feedback exploration are described in Sect. 7.4. The
performance in experiments is provided in Sect. 7.5. The conclusions are drawn in
Sect. 7.6.

7.2 Method
In this section, we first define the formulation of the multiple PiH assembly task.
Then, we describe the foundation of the proposed MDDPG method, the network
setup, and the network training details.

## [Book2025 PDF p.156] Page 156

7.2 Method

141

7.2.1 Problem Formulation
The assembly skills can be learned by maximizing the expected feedback in terms
of the assembly speed and assembly quality (contact force). The observed state
.st representing the assembly environment consists of the pose of pegs and force
feedback from the F/T sensor (see Fig. 7.1a), as follows:
s = [ P t , O t , F t , M t ] ∈ R12

. t

y

(7.1)

y

where . P t = [Ptx , Pt , Ptz ](mm) and . O t = [Otx , Ot , Otz ](◦) denote the posiy
tion and orientation of pegs, respectively; . F t = [Ftx , Ft , Ftz ](N) and . M t =
y
x
z
[Mt , Mt , Mt ](Nm) denote the detected forces and torques from F/T sensor, respectively; and the subscripts.x,. y and.z denote the axes of the robot’s base coordinate (see
Fig. 7.1a). The assembly action .u t is defined to adjust the pose of the pegs along the
corresponding axis (see Fig. 7.1b). Thus, .u t is given, as follows:
y

y

u = [tx , t , tz , tx , t , tz ] ∈ R6

. t

(7.2)

The process of the assembly task can be formulated as a MDP as described
in Sect. 1.3.5. A parameterized deterministic policy is defined as .at = π(st |θ ). The
agent action .at is employed to derive the assembly action .u t . Therefore, the assembly
performance can be improved guided by a predefined reward function.

7.2.2 Network Setup
The framework of the proposed MDDPG method is illustrated in Fig. 7.2, which is
built based on the actor-critic method trained based on DPG [11]. The critic network
can approximate the agent action value . Q(st , at |ξ ) of the executed action .at at the
state .st . the agent action value indicates the long-term desirability after taking the

Fig. 7.1 Dual PiH assembly. a F/T sensor; b Assembly action

## [Book2025 PDF p.157] Page 157

142

7 LFE: Model-Free RL Method for PiH Assembly

states that are likely to follow into account. The critic network is optimized by
minimizing the loss, as follows:


L(ξ ) = Eπ (Q(st , at |ξ ) − yt )2

.

(7.3)

where . yt = rt + γ Q(st+1 , π(st+1 )|ξ ) is the target action value calculated based on
the Bellman equation. .γ ∈ (0, 1] is the discount factor. .ξ is the parameter of the
target critic network.
The actor network is used to approximate the assembly policy mapping the state
to a deterministic action .at = π(st |θ). The actor network is updated by computing
the policy gradient with respect to the actor parameters .θ by the chain rule, which is
the gradient of the policy performance .J proven in [11].


∇θ J ≈ Eπ  ∇θ Q(st , π(st |θ)|ξ )

.
= Eπ ∇a Q(st , π(st )|ξ )∇θ π(st |θ)

(7.4)

Although most of the DDPG methods can perform well using the above optimization approach [9], the data efficiency and safety guarantees are the main limitations
of applying such algorithms in realistic physical tasks. To search the optimal policies, the conventional DDPG method explores all possible actions, which requires
a substantial amount of experimental data and also probably generates some risky
actions in realistic environments. As shown in Fig. 7.2, the training process of the
proposed MDDPG method is driven by the traditional force control strategy. The
agent action .at from the actor network is dimensionless and every component is limited in the range of .[−b, +b], which is not used to control robot directly. .b denotes
the degree of learning using the proposed MDDPG method. Here, the agent action
e
.at is utilized to revise the basic actions .u t output from the force controller given the
current measured forces and moments .Ft by
u e = Kp ◦ (Ft − Fr )

(7.5)

u = u et ◦ at + u et

(7.6)

. t

. t

where .u t is the assembly action to control the robot executing the assembly behavior.
◦ represents the Hadamard product. .Kp is a vector of 6 proportional coefficients
corresponding to 6 action components respectively; .Fr is the reference forces and
moments. The basic actions can ensure that the actor network avoids exploring the
meaningless and dangerous policies, which corresponds to the agent having handled
the basic assembly skills rather than the zero basis.
For the multiple PiH assembly task, the desirability of the assembly action should
depend on both the assembly time and the contact forces rather than only optimizing
the assembly time as in [4]. Therefore, as shown in Fig. 7.2, a fuzzy reward system
in consideration of more factors is proposed to offer the rewards rather than the
previous reward functions, as described in Sect. 7.3. In addition, we utilize a feedback

.

## [Book2025 PDF p.158] Page 158

7.2 Method

143

Fig. 7.2 Framework of the proposed MDDPG method, including network architecture, assembly
environment, fuzzy reward system, and feedback exploration mechanism

exploration strategy to tune the exploration process in real time according to the
measurements and prior knowledge of assembly tasks, as described in Sect. 7.4.

7.2.3 Network Training
It is necessary to use two parallel threads during the training process of the proposed
algorithm in realistic assembly scenarios since the data collection and training processes have different frequencies. Therefore, to efficiently perform the data collection
process, a memory buffer with a finite size is used to store the experience data tuple
.(st , at , r t , st+1 ) in a first-in-first-out manner. At each training step, mini-batch-size
samples randomly taken from the memory buffer are used to update the actor and
critic networks if the number of the data tuple in memory buffer is above mini-batchsize. In addition, to guarantee fast convergence and stability, the following training
skills are implemented in the training process.
1. Copies of the actor and critic networks as the target networks are used to offer the
target values for training. The target values change slowly to improve the stability
of the training process as in supervised learning, which is essential in realistic
scenarios.

## [Book2025 PDF p.159] Page 159

144

7 LFE: Model-Free RL Method for PiH Assembly

2. The observed states from environments include four components with different
physical units (N, Nm, and mm). To avoid ineffective learning for the different state ranges, every state component is normalized in the range of .[−1, +1].
Moreover, batch normalization is implemented in all dense layers of the networks.
3. In the critic network, two different layers in the first hidden layer are utilized to
represent the state and action rather than concatenating them directly, as shown in
Fig. 7.2. Different numbers of nodes in the two layers can control the importance
of the state and action in different cases.

7.3 Fuzzy Reward System
In this section, we describe the context of the implementation of the proposed fuzzy
reward system, which can take more factors into account and describe more complex
reward logic through embedding the prior knowledge of the assembly task to set the
fuzzy rules. For the multiple PiH assembly task, the output scalar reward .r consists
of two components
.r = r 1 + r 2
(7.7)
where .r1 is the positive reward at the end of each episode to reward the agent for
accomplishing the assembly task successfully and .r2 is the negative reward at each
time step to punish a low assembly speed and large contact forces. If the assembly
task can be finished successfully with. K time steps when the depth of the pegs reaches
the goal and the contact forces never exceeds the safe boundary, then the agent can
receive a positive reward limited in the range of .[0, +1) as in
r =1−

. 1

k
kmax

(7.8)

where .kmax is the given maximum step number.
The fuzzy reward system is utilized to provide the negative reward .r2 depending
on four factors: the current depth of pegs . Dz , the current translation offset component
.z along the . z axis of the base coordinate, the maximum contact forces . Fmax and
the maximum torques . Mmax . If each input factor value is converted into fuzzy values
in five ranges during the fuzzier stage, then the membership function of the fuzzy
reward system will include 625 fuzzy rules. To simplify the membership function, a
two-layer fuzzy system with equal effects is designed that consists of three fuzzy sets:
two first-layer fuzzy sets (.Translation − Depth, .Force − Torque) and a second-layer
fuzzy set, as depicted in Fig. 7.3.
Each crisp input value of all three fuzzy sets is divided into five ranges. VB, B, N,
G, and VG denote very bad, bad, normal, good, and very good, respectively. Thus,
each fuzzy set includes 25 rules, and the total number of fuzzy rules is reduced to 75.
The fuzzy rules of the three fuzzy sets are shown in Fig. 7.4. The crisp outputs of the
first-layer fuzzy sets are limited in the range of .[−1, 0), which are the crisp inputs of

## [Book2025 PDF p.160] Page 160

7.3 Fuzzy Reward System

145

Fig. 7.3 Architecture of fuzzy reward system and details of each fuzzy set

Fig. 7.4 Fuzzy rules of the fuzzy reward system. a Rules of fuzzy set with the input of translation
and depth. b Rules of fuzzy set with the input of forces and moments. c Rules of the second-layer
fuzzy set

the second-layer fuzzy set. The crisp output of the second-layer fuzzy set as the final
negative reward is also limited in the range of .[−1, 0), as shown in Fig. 7.4b. The
output negative reward is .−1, corresponding to the maximum penalty for the worst
inputs, where the agent performs the worst assembly policy at this time step.
The defuzzifier of all three fuzzy sets in the proposed fuzzy reward system using
the weighted average functions is defined as
25

.

f (x) =

i=1

Ci

n

j=1

25 
n

i=1 j=1

g ij (x j )

g ij (x j )

(7.9)

## [Book2025 PDF p.161] Page 161

146

7 LFE: Model-Free RL Method for PiH Assembly

where .x = [x1 , · · · , xn ] and . f (x) denote the crisp input and output, respectively; .n
is the number of inputs;.g(x) is the triangular membership function, which is different
for the three fuzzy sets; .C i denotes the value of the output defined with respect to
the fuzzy rule .i, which is decided by the prior knowledge.
The fuzzy reward system could meet the flexible requirements instead of the
complex implementations utilizing an accurate function [4]. For instance, during the
assembly process, .z and . Dz contribute different importance weights to the final
reward at the different stages according to the previous assembly experience, as
shown in Fig. 7.4a. Moreover, the fuzzy reward system can easily be tuned in terms
of the different cases.

7.4 Feedback Exploration Strategy
This section introduces the implementation of the proposed feedback exploration
strategy, and the structure is depicted in Fig. 7.5. The performance of previous exploration results is estimated in cooperation with the prior knowledge to guide the
regulation mechanism, which can modify the exploration process. The implementation of the main exploration methods is directly adding random action noise to the
actor policy. However, the feedback performance cannot immediately improve the
decision ability of the agent because the parameters of the actor network are updated
step by step. To efficiently explore the optimal assembly policies, in addition to the
agent action space noise, we also add parameter space noise to the parameters of the
actor network.

Fig. 7.5 Implementation of feedback exploration strategy

## [Book2025 PDF p.162] Page 162

7.4 Feedback Exploration Strategy

147

7.4.1 Action Space Noise Exploration
In multiple PiH assembly tasks, to ensure the safety of assembly actions, the P force
controller is used as the expert advice to guide the modification of the exploration
process. The distance .ds (·) between the perturbed action .ãt and the expert action .ae
can be measured in action space at each time step as


1 N
2

.ds (ae , ãt ) =
(a i − ãti )
N i=1 e

(7.10)

where . N denotes the dimension of the agent action and .i is the index. The perturbed
assembly action .ãt is injected with . OU (μ, ξ, σ 2 ) noise, which is correlated and
controlled by the parameter .ξ , .μ is the desired average, and .σ is the variance. In
the regulation mechanism, .μ and .σ can be tuned at each time step according to the
measured distance .ds (·) and the difference value .r
r = rt − re

(7.11)

.

where the current reward .rt of the perturbed action can be calculated from fuzzy
t
t
, Mmax
, Dzt , tz ). The expert reward .re cannot be meareward system .rt = f (Fmax
t−1
sured after executing the perturbed action. The value calculated by the forces . Fmax
t−1
e
e
and torques . Mmax at the last time step, the expert action .z and the depth . Dz are
used to approximate the expert reward .re .
Therefore, .μ and .σ can be tuned by
σ

. t+1

= σt − Bσ · sigmoid

r
ds + 1

μt+1 = Bμ · tanh tz − ez

.

(7.12)
(7.13)

where . Bσ and . Bμ relate to the upper bound according to the realistic assembly tasks.
We only modify the average value of action noise with respect to the translation
component .z , and the values of other components are set to zero because of their
tiny change. This regulation implementation means that the exploration should be
decreased when the agent performs well and that the exploration should also be
increased when it performs worse than the expert.

7.4.2 Parameter Space Noise Exploration
To avoid more consistent exploration resulting from the agent action space exploration, we also inject additive Gaussian noise .N(0, σ 2 I ) into the parameters of the
current policy as the parameter space exploration noise at the end of each episode by

## [Book2025 PDF p.163] Page 163

148

7 LFE: Model-Free RL Method for PiH Assembly

θ̃ = θ + N(0, σ 2 I)

.

(7.14)

where .θ denotes the parameters of the actor network and .θ̃ denotes the perturbed
parameters.
We utilize the performance of the current episode as the short-term average reward
.r̄ m , calculated by
T

γ T −t rt + r1

r̄ =

. m

(7.15)

t=0

where .m is the index number of the episode, and .T denotes the total time step of each
episode. In addition, we measure the long-term average reward .r m of all the previous
episodes as a reference. When .r̄m > r m , the exploration process should be decreased
because the current performance has exceeded the average. Additionally, when .r̄m <
r m , the exploration process should be increased because the current performance is
worse than the average. The variance .σ can be tuned by

σ

. m+1

=

1.01 · σm ,
σm /1.01,

d p (π p , π̃ ) < δm+1
d p (π p , π̃ ) ≥ δm+1

(7.16)

where .d p (π p , π̃ ) denotes the distance between the current policy .π p from the actor
network and the perturbed policy .π̃ as in




1 N

.d p (π p , π̃ ) =
Es (π pi − π̃ i )2
N i=1

(7.17)

where . N denotes the dimension of the policy, . E denotes the expectation of the minibatch-size samples, and .δm+1 denotes the threshold value, which can be updated
by
.δm+1 = max{0, ϑr̄ m − ε}
(7.18)
where .ϑ denotes the update rate in our exploration strategy and .ε is a small constant
to ensure a decrease in exploration at each episode. The difference value .r̄m can be
calculated by
.r̄ m = r̄ m − r m
(7.19)

7.5 Experiments
Guided by the selection of hyper-parameters for the proposed algorithm in the
simulation environment, the performances of the fuzzy reward system and the
feedback exploration strategy will be demonstrated in realistic dual PiH assembly
environments.

## [Book2025 PDF p.164] Page 164

7.5 Experiments

149

7.5.1 Experimental Setup
The architecture of the dual PiH assembly experimental platform is shown in Fig. 7.6.
The material of the pegs and holes is aluminum. We can assume that the pegs and
holes are strictly rigid because the compliance of the whole assembly process mainly
depends on adjusting the position/orientation of the pegs actively. Part of the compliance is from the connectors and adapters of the whole experimental system. The
distances between the two pegs’ axes and between the two holes are 200 mm. The
assembly task is executed by a 6-DOF ABB IRB 1200 robot, and the repeated positioning accuracy of the robot is .±20 .µm. A 6-DOF F/T sensor and the pegs are
attached to the end effector of the robot, and the holes are fixed on the experimental
table. The robot base coordinate is set as the base coordinate. The position (mm) and
orientation (.◦ ) of pegs can be measured easily from robot controller.
The objective of the dual PiH assembly task is to push the pegs to the desired
position in holes. This PiH assembly task mainly includes two main phases: search
and insertion. The proposed MDDPG method is used to perform the insertion phase.
The position of holes can be set by human and measured but with large positional
error. During the search phase, the pegs are moved from a fixed initial position to
align with the holes and then move down until the distance between the top of holes
and the bottom of pegs is less than 0.5 mm. Then the pegs move down along .z-axis
of the robot base coordinate with a small step size (.−0.06 mm/step) and add a randomly selected constant noise in 6 components of the robot actions to learn the holes
position with respect to the current pegs position. When the forces (N) and torques
(Nm) can be measured and within the maximum range, it means that the search phase

Fig. 7.6 Robotic dual PiH assembly experimental platform

## [Book2025 PDF p.165] Page 165

150

7 LFE: Model-Free RL Method for PiH Assembly

is performed successfully. Then the proposed MDDPG method is utilized to accomplish the pushing process in insertion phase. The computer (Dell Precision M4800)
communicates with the robot controller via TCP/IP protocol, which is developed by
socket written in Python. The force controller reads the forces/torques values from
F/T sensor according to the specific set of RAPID instructions. In this way, collecting
the state data takes about 1.1s at each time step.

7.5.2 Experimental Results
Training
In the same way as in the simulation, the performances of the proposed fuzzy reward
system and feedback exploration strategy are demonstrated through comparisons
with the aforementioned approaches in realistic environments. In the dual PiH assembly experiments, the F/T sensor should be calibrated first. The goal depth is set to 40
mm, and the maximum number of steps .kmax is set to 65. To guarantee the safety of
the components in experiments, the maximum safe force is set to 80 N, the maximum
safe torque is set to 5 Nm during the assembly process and .b is set to 0.2. Therefore, for one episode, the robot executes the assembly action step by step until the
pegs reach the goal depth successfully or the assembly process is terminated when
the measured forces-torques exceed the maximum safe boundary or the maximum
number of steps is above 65.
However, to make efficient use of the experience data, the training process runs
for 50 times per episode. In our experiments, the precise positions of the dual holes
are not required. Moreover, to test the robustness of the proposed MDDPG method
against the initial position errors, before every assembly episode starting, the dual
pegs move to their initial position from a fixed position because the robot has errors
from repeated positioning.
As shown in Fig. 7.7a, the agent with the accurate reward function only taking
the assembly time into account can rapidly converge after training 200 episodes.
However, the agent with the accurate reward function including both the assembly
time and the contact forces cannot perform well because it is difficult to evaluate the
assembly policies by balancing the performance of the assembly time and contact
forces in the early training stage. However, as shown in Fig. 7.7b, the agent utilizing
the fuzzy reward system is able to converge and perform efficiently, similar to the
accurate reward function only measuring the assembly time. As shown in Fig. 7.7d
and c, the agent with the fuzzy reward system after training for only 200 episodes
can decrease the assembly time by approximately 20 s, and the accumulative rewards
increase by 20% in one episode.
In addition, we compare two agents using the fuzzy reward system, but one agent
only utilizes the OU noise in action space and another uses the feedback exploration
strategy in Sect. 7.4. As shown, the agent with the feedback exploration strategy
can perform efficiently. The proposed feedback exploration strategy only performs

## [Book2025 PDF p.166] Page 166

7.5 Experiments

151

Fig. 7.7 Performance in realistic assembly experiments (The episode time only includes time of
insertion phase). a Assembly time using two accurate reward functions. b Assembly time with fuzzy
reward and accurate reward function. c Accumulative reward using feedback exploration strategy.
d Assembly time using feedback exploration strategy

slightly better since the agent is only trained for approximately 200 episodes and
there are fewer exploration episodes. However, the proposed exploration strategy
can ensure that the exploration actions are safe and avoid risky exploration actions.

Test
To demonstrate the stability of the proposed algorithm, we execute the dual
PiH robotic assembly task 50 times to test the success rate. In addition, we
compare the changes in contact forces and moments during assembly processes
accomplished by the learned policies with pre-training. The agent before training equals to the P force controller and the proportional coefficient vector .Kp =
[0.002, 0.002, 0.015, 0.01, 0.01, 0.01] is pretested referring to [13].
The proposed MDDPG method using the fuzzy reward system and feedback
exploration strategy achieve a 100% success rate in the case with the same initial

## [Book2025 PDF p.167] Page 167

152

7 LFE: Model-Free RL Method for PiH Assembly

position as the training process, which means that the initial position error is limited
within 20 .µm. Although the pre-training agent only by the P force controller could
also achieve the 100% success rate in our test experiments, we focus on demonstrating
the improvement through training. As shown in Fig. 7.8, the agent after training can
perform the same assembly task through fewer steps and decrease the contact forces
and moments compared with pre-training.
Moreover, to demonstrate the robustness of the proposed algorithm against a
new initial position, we rotate the pegs along .z-axis of the robot base coordinate by
◦
.1.0 and translate along . y-axis by 0.1 mm after getting the initial position in search
phase. It’s equivalent to that the holes are set in a new initial position. As shown in
Fig. 7.9a, the new initial position leads to a large initial contact forces and moments,
and the agent before training only using the traditional P force controller cannot
finish the assembly process since it cannot decrease the contact forces . f z and then
exceeds the maximum steps in one episode. Nevertheless, the agent after training
could accomplish the same task with the same initial position shown in Fig. 7.9b. It
means that the proposed algorithm can accomplish the assembly task through the
learned high-level policy, which is robust to the new initial position.

Fig. 7.8 Performance of tasks with the same initial position. a Performance before training. b
Performance using the learned policy

Fig. 7.9 Performance of tasks with new initial position. a Performance before training. b
Performance using the learned policy

## [Book2025 PDF p.168] Page 168

7.6 Conclusion

153

Similar to the implementation in dual PiH assembly tasks, the proposed MDDPG
method can also be applied in multiple PiH assembly scenarios, which cannot be
accomplished successfully through the traditional force control algorithms relying
on the analysis of the contact model. However, the agent with the learned assembly policy probably needs to be trained again in new assembly tasks (with different
number of pegs or different size pegs) for learning the new environments. How long
should be trained depends on the complexity of the new task. For example, the agent
needs to be trained longer in new tasks with number of pegs change than the tasks
with only size change because the PiH tasks with different number means the intrinsic change of the environment model. Although this is an important limitation of our
work, we believe that it is an appropriate and general way to address the complex
multiple PiH assembly tasks in through the learned experience, which can greatly
improve the efficiency of industrial manufacturing process without analyzing the
unknown contact states and tuning the program parameters. In addition, importantly,
the proposed MDDPG method could become a general and practical approach to perform the different multiple PiH assembly tasks with the advance of transfer learning
and state representation techniques.

7.6 Conclusion
Combined with a feedback exploration strategy and fuzzy reward system, the proposed MDDPG method can perform multiple PiH assembly tasks well through the
learned high-level assembly policy. The effectiveness and robustness of the proposed
algorithm have been demonstrated through a designed simplified simulation model
and realistic dual PiH assembly experiments. However, the contact force simulator cannot accurately estimate the contact forces, which means that the simulation
training results cannot be applied in Experiments. Therefore, in future work, it is
important that the agent is trained in a more accurate simulation environment implemented by virtual robot experimentation platform [10] or physics engine Mujoco [7].
The accurate environment could improve the data efficiency of the proposed MDDPG
method because the learned policy could be applied in the realistic tasks directly or as
the initial policy. Moreover, the learned policies applied to new assembly tasks still
require re-training under the proposed algorithm, which limits its application scope.
To address this challenge, the proposed algorithm will be improved by referring to
the advantages of transfer learning.

## [Book2025 PDF p.169] Page 169

154

7 LFE: Model-Free RL Method for PiH Assembly

References
1. J. Garcıa, F. Fernández, A comprehensive survey on safe reinforcement learning. J. Mach.
Learn. Res. 16(1), 1437–1480 (2015)
2. M.J. Hausknecht, P. Stone, Deep reinforcement learning in parameterized action space (2016).
arXiv:1511.04143
3. R. Houthooft, X. Chen, Y. Duan, J. Schulman, F. De Turck, P. Abbeel, Vime: variational
information maximizing exploration, in Advances in Neural Information Processing Systems,
pp. 1109–1117 (2016)
4. T. Inoue, G. De Magistris, A. Munawar, T. Yokoya, R. Tachibana, Deep reinforcement learning
for high precision assembly tasks, in 2017 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), IEEE, pp. 819–825 (2017)
5. M. Khamassi, G. Velentzas, T. Tsitsimis, C.S. Tzafestas, Active exploration and parameterized
reinforcement learning applied to a simulated human-robot interaction task, in 2017 First IEEE
International Conference on Robotic Computing (IRC), pp. 28–35 (2017)
6. P. Kofinas, G. Vouros, A.I. Dounis, Energy management in solar microgrid via reinforcement
learning using fuzzy reward. Adv. Build. Energy Res. 12(1), 97–115 (2018)
7. V. Kumar, E. Todorov, Mujoco haptix: a virtual reality system for hand manipulation, in 2015
IEEE-RAS 15th International Conference on Humanoid Robots (Humanoids), pp. 657–663
(2015)
8. Y. Li, Deep reinforcement learning: an overview (2017). arXiv:1701.07274
9. T.P. Lillicrap, J.J. Hunt, A. Pritzel, N.M.O. Heess, T. Erez, Y. Tassa, D. Silver, D. Wierstra,
Continuous control with deep reinforcement learning (2016). arXiv:1509.02971
10. K.M. Lynch, F.C. Park, Modern Robotics (Cambridge University Press, 2017)
11. D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, M. Riedmiller, Deterministic policy
gradient algorithms, in Proceedings of the 31st International Conference on International
Conference on Machine Learning, JMLR, ICML’14, vol. 32, pp. I-387–I-395 (2014)
12. T. Tang, H.C. Lin, M. Tomizuka, A learning-based framework for robot peg-hole-insertion,
in ASME 2015 Dynamic Systems and Control Conference, American Society of Mechanical
Engineers, pp. V002T27A002–V002T27A002 (2015)
13. K. Zhang, M. Shi, J. Xu, F. Liu, K. Chen, Force control for a rigid dual peg-in-hole assembly.
Assem. Autom. 37(2), 200–207 (2017)

## [Book2025 PDF p.170] Page 170

Chapter 8

LFE: Model-Based RL for PiH Assembly

8.1 Introduction
The existing RL algorithms are data-inefficient, requiring numerous explorations
and resulting in prolonged training times. To enhance data efficiency in real-world
assembly tasks, one promising approach is to learn from imaginary experiences generated by a dynamic model of the environment, which reduces redundant exploration.
The dynamic model can predict the environment’s next state given a selected action,
thereby minimizing the need for realistic exploration. The existing RL algorithms
suffer from the drawbacks of extensive exploration, resulting in prolonged training
times and suboptimal data efficiency. To enhance the data efficiency specifically in
real-world assembly tasks, one effective approach is to learn a dynamic model of the
environment and then learn from imaginary experiences generated by the model. It
reduces the need for unnecessary exploration within the physical environment [17].
As illustrated in Fig. 8.1, by utilizing a dynamic model, future states of the environment can be predicted based on selected actions, thereby minimizing the reliance on
exploration in the real experiment.
There are mainly two ways to utilize the dynamic model. Dyna-like RL algorithms [15] learn the assembly skill from both the realistic and imaginary assembly
environment of the dynamic model in the same scheme. On the other hand, GPS
learns the parameterized policies in an imaginary assembly environment from a
dynamic model. Afterwards, the trajectory is optimized and the dynamic model is
also improved in the realistic assembly environment. GPS has shown great success
in many contact-rich manipulation tasks [6]. iLQG [9] as a common trajectory optimization algorithm is often explored to learn the optimal control strategy for robotic
assembly tasks. However, the performance of the above algorithms largely depends
on the accuracy of dynamic model. The high exploitation-exploration ratio to utilize the dynamic model easily results in producing local optima [17]. The dynamic
model is often fitted by statistical techniques, e.g., linear function regression [5],

© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_8

155

## [Book2025 PDF p.171] Page 171

156

8 LFE: Model-Based RL for PiH Assembly

Fig. 8.1 RL for robotic PiH assembly

linear Gaussian model [6], and NNs. However, the statistical dynamic model is usually a one-step prediction, which can only approximate the environment in a local
region. Additionally, the statistical dynamic model is sensitive to the hyperparameters and environmental noise, especially the non-Gaussian noise that often appears
in measurement [3, 13, 14]. Therefore, it is difficult to fit a statistical dynamic model
for an accurate environment prediction (e.g., force and pose information) with the
noise-laden and inconsistent sensor signals [17].
In contrast, human beings have the ability of multi-step (also named as variable time-scale) prediction that allows estimating the environment in a large time
range, resulting in the “optimal” action with less exploration. In this chapter, we
propose a variable time-scale prediction model to reduce the unnecessary exploration and develop a Fuzzy Logic-Driven Variable Time-Scale Prediction-based
RL (FLDVTSP-RL) to obtain the assembly action control from the predicted
environment and improve the data efficiency as shown in Fig. 8.1.
To learn variable time-scale predictions, General Value Functions (GVFs) that
expand the definition of value function through incorporating expert experience
are proposed to represent the assembly environment predictions [16]. GVFs can
be defined with different time scales to obtain more effective information than that
achieved in one-step prediction [11]. However, the utilization of learned predictions
for enhancing action control is rarely explored. Fuzzy logic systems (FLS) were
explored to solve the robotic PiH assembly problems, where the assembly expert
experience was formulated as logic rules and constraints [1]. Specifically, the predicted environment is mapped to the impedance parameters by a designed FLS. The
mapped impedance parameters of the reformulated impedance action space are utilized to derive the action baseline, which can improve the data efficiency of typical
RL algorithms largely.

## [Book2025 PDF p.172] Page 172

8.2 Variable Time-Scale Prediction Learning

157

8.2 Variable Time-Scale Prediction Learning
As shown in Fig. 8.1, the environment predictions (e.g., assembly force for the
potential subsequent assembly action) can reduce unnecessary exploration of RL
algorithm. This section focuses on how to predict the assembly environment by the
proposed variable time-scale predictions. First, we state the multiple PiH assembly
problems; second, four kinds of variable time-scale predictions are defined as GVFs;
finally, the defined GVFs are learned by off-policy TD.

8.2.1 Problem Statement
For robotic multiple PiH assembly, the holes are often fixed on the experimental
table in the workspace of the robot, and an external force sensor is mounted between
the end-effector and pegs to measure assembly force. To simplify the presentation,
the assembly force is equivalent to the output of the F/T sensor ignoring gravity. In
search phase, the robot places the pegs to measure the pose (position/orientation) of
holes, and places the pegs within the initial range, as shown in Fig. 8.2. If the peg
reaches the desired depth with the appropriate assembly force, the robot can start the
insertion phase.

Fig. 8.2 Multiple PiH assembly process

## [Book2025 PDF p.173] Page 173

158

8 LFE: Model-Based RL for PiH Assembly

8.2.2 Variable Time-Scale Prediction Definition
In the context of RL [5], the state value function .vπ (st ) denotes the prediction to
estimate the expected cumulative reward received from environments, as follows:
.
v (st ) = Eπ [G t |st ]

(8.1)

. π

.

Gt =

T


γ k−t−1 rk

(8.2)

k=t+1

where subscript .π denotes the policy, the function to select the action .at according
to state .st at time step .t. .Eπ denotes the expectation of return over the policy .π . .G t
denotes the return following time .t, which is the cumulative reward of one assembly
episode from time .t to terminal time .T . .rk denotes the reward to evaluate the selected
action given the state .st , and .γ ∈ (0, 1] is the discount function.
The state value function .vπ (st ) in Eq. 8.1 can calculate the prediction values only
given the state.st without executing the selected action of the whole episode. Similarly,
the defined prediction .vπG (st ) is extended with the pseudoreward .C, the policy .π , and
the general discount function .γ (st ), as follows:
 T


.
G
.vπ (st ) = Eπ

k=t

Ct+1

k



γ (si )|st , Ct , γ

(8.3)

i=t+1

where the defined prediction .vπG (st ) basically can answer the question, e.g., “How
much of the pseudoreward .Ct can the robot receive from the environment following
the given policy .π ?”.
The state .st that represents the pegs during assembly, as follows:
y

y

s = [Ptx , Pt , Ptz , Otx , Ot , Otz ] ∈ R6

. t

y

(8.4)

y

where . Ptx , Pt , Ptz and . Otx , Ot , Otz denote the position and orientation of pegs,
respectively, and .x, y and .z denote the axes of the robot base coordinate system. The
assembly action .u t that adjusts the pose of the pegs in Cartesian space is depicted in
Fig. 8.2, as follows:
y

y

u = [tx , t , tz , tx , t , tz ] ∈ R6

. t

y

y

(8.5)

where.[tx , t , tz ] and.[tx , t , tz ] represent the translation and rotation assembly
action components, respectively. In order to predict the subsequent assembly force,
the pseudoreward .Ct is defined according to the assembly force from the F/T sensor
as follows:
y
y
x
z
x
z
.C t = ϒ(Ft , Ft , Ft , Mt , Mt , Mt , γ (st ))
(8.6)

## [Book2025 PDF p.174] Page 174

8.2 Variable Time-Scale Prediction Learning
y

159

y

where .[Ftx , Ft , Ftz ] and .[Mtx , Mt , Mtz ] are the force and moment measured from
the F/T sensor, respectively.
The existing dynamic model can only predict the assembly force in the next
step. However, the predictions based on GVFs can obtain variable time-scale prediction with high-level features combining the PiH assembly experience. As shown in
Fig. 8.3, four kinds of predictions (in addition to the assembly force) about the environment with the following potential assembly actions are defined through designing
the policy, pseudoreward, and discount function in Eq. 8.3. The details of the defined
variable time-scale predictions are described as follows:
1. When the pseudoreward is defined according to the assembly force as in Eq. 8.6,
the predictions can be learned to answer the question “How much will the
force/torques be when following different target policies?”
2. When the pseudoreward is defined according to the designed discount function
.γ (st ) to predict the appearance of an event, e.g., “the pegs hit the holes,” the predictions can be learned to answer the question “How much will the force/torques
be when the pegs hit the holes?”
3. When the discount function .γ (st ) is extended to define the terminal function,
the variable time-scale predictions can be defined. For instance, the assembly
process will terminate when .γ (st ) is equal to 0. Therefore, .1 − γ (st ) represents
the probability that the assembly process will terminate at the state .st . .γ (st ) =
1 − 1/T determines the time-scale .T of the predictions.
4. When the pseudoreward is defined without the assembly force, the predictions
can be learned to predict “How many time steps will the robot move before the
pegs hits the holes?”

Fig. 8.3 Examples of variable time-scale predictions

## [Book2025 PDF p.175] Page 175

160

8 LFE: Model-Based RL for PiH Assembly

8.2.3 Variable Time-Scale Prediction Learning
The defined predictions .vπG (·) in Eq. 8.3 can be approximated by a linear function as
. Vπ (·|ξ ) parameterized by.ξ , which generally are implemented through data collection
and prediction learning. For prediction learning, the policy denotes the mapping
from state to the probabilities of selected possible assembly motion directions (three
translations and three rotations see Fig. 8.2). Specifically, the policy .πt to define
predictions is named as target policy. A policy named behavior policy .μt is utilized
to generate assembly action and interact with environment. If the predictions are
learned via the data generated by the given target policy, it requires the on-policy
learning [16]. For the on-policy scheme, the temporal difference (TD(.λ)) approach [5]
can update the parameters .ξ of .Vπ step by step through minimizing the TD error, as
follows:
δt = Ct+1 + γt+1 Vπ (ϕ(st+1 )|ξ v ) − Vπ (ϕ(st )|ξ v )
v
. ξ t+1 = ξ v + ηδt gt
(8.7)
gt = γt λgt−1 + ∇ξ Vπ (ϕ(st )|ξ v )
where.δt is the difference between the approximated value.Vπ (ϕ(st )) of state.st and an
accurate approximation .Ct+1 + γt+1 Vπ (ϕ(st+1 )). .ϕ(·) denotes the feature function
of state, and .η ∈ R+ is the learning rate. .gt is the eligibility trace as a short-term
memory to store the TD error, and .λ ∈ [0, 1] controls the length of the eligibility
trace.
To learn different predictions from the single source data in parallel, we implement
an efficient prediction off-policy learning scheme. For instance, based on the offpolicy learning, the predictions defined by the dangerous target policies can be learned
from the data generated by a safe behavior policy or the human demonstration, which
is essential for real-world assembly tasks. For off-policy scheme, the parameters.ξ are
updated via the off-policy TD(.λ) through combining with a correction term .ρt [16],
as follows:
ξ vt+1 = ξ v + ηδt gt


.
(8.8)
gt = ρt γt λgt−1 + ∇ξ Vπ (ϕ(st )|ξ v )
where the correction term .ρt is calculated by the importance sampling ratio .ρt =
π(at |st )
.
μ( at |st )
In summary, the off-policy scheme is more general, and the on-policy scheme
is a special case of off-policy scheme. The implementation of variable time-scale
prediction learning is summarized in Algorithm 8.1. All predictions with different
target policies can be learned from the collected data from the same behavior policy.

## [Book2025 PDF p.176] Page 176

8.3 Variable Time-Scale Prediction-Based RL Policy Learning

161

Algorithm 8.1 VTSP learning
1: Initialize replay buffer .D; number of predictions . M and weight of predictions .
2: Collect data
3: for .t = 0, . . . , N do
4: Initialize state .s0 ; .done = 0
5: while .done = 0 do
6:
Observe state .st
7:
Get action .at = .μ(st ) and execute assembly action .u t ← §(u et , at |K p , Kd ) Eq. 8.10
8:
Observe next state .st+1
9:
Get pseudoreward .Ct1 , Ct2 , Ct3 , ...; discount rate .γ 1 , γ 2 , ...
10:
Store (.st , at , [Ct1 , Ct2 , Ct3 , ...], [γ 1 , γ 2 , ...], st+1 ) in .D
11:
.done = 1 if search phase finish else .done = 0
12: end while
13: end for
14: Learn predictions
15: for .i = 0, . . . , M do
16: Initialize .Vπi , target policy .π i , feature .ϕ, discount rate .γ i and pseudoreward .C i
17: for .t = 0, . . . , T do
18:
Sample (.st , at , Cti , st+1 ) and calculate .γti
i
i
i
i
i i
i
19:
.δt = C t+1 + γt Vπ (ϕ(st+1 )|ξ t ) − Vπ (ϕ(st )|ξ t )
π (at |st )
i
i
20:
.ρt =
μ( at |st ) , .ξ v updated by TD(.λ) as Eq. 8.7
21: end for
22: end for
23: Output: weights of predictions . = [ξ 1 , ξ 2 , ξ 3 , ....]
i

8.3 Variable Time-Scale Prediction-Based RL Policy
Learning
This section focuses on how to utilize the learned variable time-scale predictions for
assembly action control. First, the preliminaries of RL algorithms for assembly action
control are introduced and the impedance action space is reformulated. Second, FLS
is used to map the predicted environment to the impedance parameter in an impedance
action space as the baseline for RL policy learning. Finally, as shown in Fig. 8.4, based
on two most popular RL algorithms (DQN [4] and DDPG [7]), FLDVTSP-DQN and
FLDVTSP-DDPG are implemented and analyzed theoretically.

8.3.1 Preliminary
On the top the foundations in Sect. 1.3.5, the RL policies .π(at |st ; θ ) are trained
to select the agent action .at and guide the assembly action through maximizing
the expected discounted return. Similarly to the problem formulation of assembly introduced in Sect. 7.2.1, the state .st ∈ R12 and assembly action .u t ∈ R6 for

## [Book2025 PDF p.177] Page 177

162

8 LFE: Model-Based RL for PiH Assembly

Fig. 8.4 Schematic of FLDVTSP-RL algorithms (FLDVTSP-DQN and FLDVTSP-DDPG)

assembly action control can be defined as depicted in Sect. 7.2.1. Reward function
Rt is designed to award the high assembly speed and avoid unsafe action, as follows:

.

⎧
⎪
⎪
⎪
⎨

−0.1, done = False and sa f e = T r ue
kT
1−
.R(st , at ) =
, done = T r ue and sa f e = T r ue
⎪
kmax
⎪
⎪
⎩
−1, sa f e = False

(8.9)

where .k T represents the final number of assembly steps, and .kmax denotes the maximum assembly steps within one episode. If the assembly task can be completed
within .kmax steps, the robot will receive a positive reward .[0, 1). At each time step
.t, if the assembly force or torque exceed the setting of the safe threshold, the robot
will receive a large negative reward .−1, and otherwise, a small negative reward
.−0.1 (Noted that this value needs to be well-designed to balance the assembly speed
and assembly force).
The agent action space .at ∈ A for RL policy learning is to adjust the pose of
pegs. For real-world assembly tasks, to reduce the training time and avoid dangerous
exploration via considering the effects of assembly force, as shown in Fig. 8.4, the
action space for FLDVTSP-DDPG and FLDVTSP-DQN is reformulated into the
impedance action space .at ∈ Ac , as follows:
u t ← §(u et , at |K p , Kd )
e
. u t = K p ◦ et + Kd ◦ ėt
et = Fr − Ft

(8.10)

## [Book2025 PDF p.178] Page 178

8.3 Variable Time-Scale Prediction-Based RL Policy Learning
y

y

163
y

y

where .Ft = [Ftx , Ft , Ftz , Mtx , Mt , Mtz ] and .Fr = [Fdx , Fd , Fdz , Mdx , Md , Mdz ]
denote the measured assembly force and reference assembly force corresponding to
the axes of the robot base coordinate system in Fig. 8.2, respectively. .et denotes the
difference between the reference assembly force and the measured assembly force,
and .ėt is the differential of .et . Basically, given the reference assembly force .Fr , an
expert assembly action .u et is derived based on the impedance controller, which can
enable robot to achieve a safe compliant interaction. The action derived from RL
policy is applied to revise the derived expert assembly actions. The performance of
the proposed impedance action space largely depends on the impedance parameters
.K p and .Kd . Therefore, the data efficiency will be largely affected by the selected
impedance parameters, a FLS can be designed to obtain the impedance parameters
of the impedance action space.

8.3.2 FLS Design
In practice, a FLS is designed to only determine the proportional parameters .K p =
y
ry
[K px , K p , K pz , K rpx , K p , K rpz ] in the impedance action space Eq. 8.10, and .Kd is
directly derived from .K p . The input of the FLS is the learned variable time-scale
predictions.Ft = Vπ (st | ) via Algorithm 8.1. As shown in Fig. 8.5, the fuzzy rules of
the FLS are employed to map the learned predictions about the subsequent assembly
force to 6 proportional parameters .K p of the impedance action space. Basically, the

Fig. 8.5 Surface view of input-output for six fuzzy inferences

## [Book2025 PDF p.179] Page 179

164

8 LFE: Model-Based RL for PiH Assembly

Table 8.1 Definition of
fuzzy logic system

Inputs

Outputs

. V Fx , . V M y

. K p ∈ [0, 0.015]

. V Fy , . V M x

. K p ∈ [0, 0.015]

. V Fx , . V Fy

. K p ∈ [0, 0.02]

. V M x , . V Fy

rx
. K p ∈ [0, 0.015]
ry
. K p ∈ [0, 0.015]
rz
. K p ∈ [0, 0.015]

. V M y , . V Fx
. V Mz , . V M x

x

y

z

optimized impedance controller based on the learned predictions provides the highlevel goals, which can reduce the unnecessary exploration and provide the stable
target implicitly.
As shown in Table 8.1 , FLS consists of six fuzzy inferences corresponding to six
proportional parameters in the impedance action space; and every fuzzy inference
consists of two kinds of predictions corresponding to two force sensor signals as
input and one proportional parameter corresponding to an element of the assembly
action as output. Specifically, the designed FLS is implemented in the following
steps:
1. The input and output of each fuzzy inference are partitioned into various fuzzy
sets through the triangular membership function in the fuzzification process. The
input of each fuzzy interference is divided into 5 fuzzy sets, and each fuzzy set
is associated with linguistic terms, e.g., “NB,” “NS,” “ZE,” “PS,” and “PB.” The
output is divided into three fuzzy sets with respect to “NS,” “ZE” and “PS.”
2. The fuzzy rules are plotted in Fig. 8.5. Each fuzzy inference includes 25 IFis “NB,” and .VM(i)y is “NB,” then
THEN rules in the following form: .R(i) : if .VF(i)
x
x(i)
.K p
is “NS.” As shown in Table 8.1, all inputs of the fuzzy inference system are
normalized in.[−1, 1], and the range of the output generally needs to be predefined
according to the real-world assembly settings.
3. The weighted average defuzzification approach [12] is utilized to calculate the
output of each proportional parameter, e.g., . K px =  , where
 = K px(1) , K px(2) , ..., K px(25)



.

and
.

25
 
= μ M (K px(1) ), ..., μ M (K px(25) ) /(
μ M (K px(i) ))

(8.11)

(8.12)

i=1

is a vector to calculate the corresponding weight of each fuzzy rule by the
triangular membership function .μ M (·).

.

## [Book2025 PDF p.180] Page 180

8.3 Variable Time-Scale Prediction-Based RL Policy Learning

165

8.3.3 FLDVTSP-DQN
DQN is generally used for the discrete assembly action control in the PiH assembly
tasks [4]. FLDVTSP-DQN is designed to improve the data efficiency of typical DQN,
and the discrete impedance action space .Ac is defined as follows:
Ac = {[Fdx , 0, Fdz , 0, 0, 0]
y

[0, Fd , Fdz , 0, 0, 0]
[0, 0, Fdz , 0, 0, 0]
[0, 0, Fdz , Mdx , 0, 0]
y
[0, 0, Fdz , 0, Md , 0]
.

[0, 0, Fdz , 0, 0, Mdz ]}

(8.13)

where the agent action .at from FLDVTSP-DQN is a one-shot vector to select the
motion direction (except the translation along .z-axis see Fig. 8.2). The assembly
action .u t ← §(u et , at |K p , Kd ) corresponding to the selected motion direction can
be calculated as .at ◦ u et , where the proportional parameters .Kp are obtained based
on the predicted environment about the subsequent assembly force by the designed
FLS. Compared to typical DQN [4], the proposed FLDVTSP-DQN can perform
impedance-based assembly behaviors. Basically, the reformulated action space can
provide the baseline for assembly policy learning, which can reduce unnecessary
exploration and make robot only learn the residual skills besides the baseline. Additionally, the reformulated action space will be optimized according to the predicted
environments by GVFs.
For multiple PiH assembly, it is difficult to accurately recognize the contact force
from the six-DoF force sensor due to the complicated coupling relations. The “optimal” motion direction can not only reduce the contact force along this direction but
also eliminate the relevant contact force along another direction. At each sample step,
the “optimal” motion direction is selected according to the action-value network, as
follows:
∗
.at = max Q (st , a|ξ )
(8.14)
a

where . Q ∗ means that motion along this direction has the largest probability to complete the assembly with higher reward. The action-value network parameterized by
.ξ is trained through minimizing the loss, as follows:
L(ξ ) = E(sm ,am )∼B [(ym − Q(sm , am |ξ ))2 ]

.

(8.15)

where . ym = rm+1 + γ maxa Q(sm+1 , a|ξ̄ ) is calculated by a target action-value network with parameters .ξ̄ . .ρπ is the probability distribution over sequences .s and .a.
We apply the same training techniques experience replay, target network, and normalization as in [4, 10]. Additionally, to improve the stability of FLDVTSP-RL
algorithms, at each training step, a minibatch of transitions .B uniformly sampled

## [Book2025 PDF p.181] Page 181

166

8 LFE: Model-Based RL for PiH Assembly

from the replay buffer .D is used to update the action-value network. The training
details of FLDVTSP-DQN are summarized in Algorithm 8.2.
Algorithm 8.2 FLDVTSP-RL
1: Input learned predictions . = [ξ 1 , ξ 2 , ...., ξ 6 ]
2: Initialize all networks and corresponding target networks; replay buffer .D
3: for each episode do
4: Initialize state of pegs .s0 randomly in limited range
5: for each sample step do
6:
Select action .at
7:
Select parameters .Kp = FLS(st , )
8:
Calculate assembly action .u t ← §(u et , at |K p , Kd )
9:
Execute .u t , observe reward .rt+1 and next state .st+1
10:
Store (.st , at , u t , rt+1 , st+1 ) in .D
11:
for each training step do
12:
Sample a minibatch of .B transitions uniformly (.sm , am , rm+1 , sm+1 ) from .D
13:
Update parameters of all networks
14:
Update parameters of all target networks
15:
end for
16: end for
17: end for

8.3.4 FLDVTSP-DDPG
Similarly to Sect. 7.2.1, FLDVTSP-DDPG is designed with a reformulated
impedance-conditioned action space, the deterministic agent action .at = π(·|s; θ) ∈
A is utilized to obtain the assembly action, as follows:
.

u t = clip {at , −b, +b} ◦ u et + u et

(8.16)

where .u et is the expert assembly action derived from the impedance controller as
in Eq. 8.10 with the reference parameters .Kp derived from the designed FLS based
on the prediction environment about the subsequent assembly force. As shown in
Fig. 8.4, at each sample step .t, the action is calculated from the actor network .at =
π(st |θ) + Nt , at ∈ [−1, 1]6 , .Nt is the exploration noise and .b is utilized to regulate
the confidence of the actor network.
At each training step, a minibatch of transitions .B are uniformly sampled from
the replay buffer .D. First, the action-value network is updated through minimizing
the error similar to that in Eq. 8.15. The target value is calculated based on Bellman
equation, as follows:
.

ym = rm+1 + γ Q(sm+1 , π(sm+1 |θ)|ξ̄ )

(8.17)

## [Book2025 PDF p.182] Page 182

8.4 Experiments

167

where .μ(sm+1 |θ) is calculated via the target actor network with parameters .θ.
Afterwards, .θ is updated based on DPG, as follows:
∇θ J (θ ) = Esm ∼B [∇a Q(sm , μ(sm )|ξ )∇θ μ(sm |θ)]

.

(8.18)

where the training settings are same as those in [8]. The training details of FLDVTSPDDPG can also refer to Algorithm 8.2.

8.4 Experiments
In this section, first, a dual PiH assembly experimental system is set up as shown
in Fig. 8.6. Second, to verify the effectiveness of variable time-scale predictions
learned by GVFs, three kinds of GVFs are evaluated. To verify the efficiency of the
FLDVTSP-RL algorithms (including FLDVTSP-DQN and FLDVTSP-DDPG), two
experiments are conducted. Finally, to evaluate the generalization performance, new
assembly tasks with smaller clearance are applied to evaluate the performance of
learned assembly policies.

8.4.1 Experimental Setup
An ABB six-DoF F/T sensor and the dual pegs are mounted to the end-effector of
the robot. The dual holes are fixed on the experimental table and the definition of
the robot base coordinate system is depicted in Fig. 8.6. All the pegs and holes are
machined from Aluminium 6061. The diameter of the pegs and holes is 29.96 mm and
30.00 mm, respectively. The distance between the two pegs’ axes and the two holes’
axes is 200.0 mm. Furthermore, to simulate a complicated assembly environment,
chamfers of 3 different sizes are designed as shown in Fig. 8.6. The search phase
aims to reach the desired depth along the .z-axis of the robot base coordinate system
within the safe threshold [80 N, 5 Nm] and then start the insertion phase.

8.4.2 VTSP Learning
As shown in Algorithm 8.1, the predictions are learned via two stages: data collection
and VTSP learning.

## [Book2025 PDF p.183] Page 183

168

8 LFE: Model-Based RL for PiH Assembly

Fig. 8.6 Dual PiH assembly platform with multiple chamfers

Data Collection
The behavior policy .μt is denoted as follows:
μt (·|·) = [0.1, 0.1, 0.5, 0.1, 0.1, 0.1]

.

(8.19)

which means that at each time step.t the robot has the probability of 0.5 to move down
along .z-axis and has equal probability 0.1 to move along the remaining directions.
Specifically, the motion magnitude is calculated via impedance controller as shown
in Eq. 8.10. The behavior policy .μt is sampled for 1000 time steps to execute and
collect data. To simulate the environmental noise, as shown in Fig. 8.6, the initial
position of the pegs is randomly set to be uniform within [.−0.03 mm, 0.03 mm], and
the initial orientation of the pegs are randomly set to be uniform within.[−0.5◦ , 0.5◦ ].
Additionally, the pegs will be reset when it has reached the desired depth, or the F/T
sensor signals exceed the set safe threshold. The assembly force measured from F/T
sensor during interactions is plotted, as shown in Fig. 8.7. The assembly tasks will
become complicated with the random initial pose, shown as the blue lines, compared
to a fixed initial pose, shown as the red lines.

Learning Predictions
Six linear functions are updated to approximate the predictions of the assembly
force signals. The features of the state of the linear function are derived by the tile
coding [11, 16]. For every dimension of the state, 10 tilings are used and every
dimension is hashed to a vector of 1024 dimensions. To eliminate the impact of the
different physical units, the assembly force measured from F/T sensor is normalized

## [Book2025 PDF p.184] Page 184

8.4 Experiments

169

Fig. 8.7 F/T sensor signals. Red lines are for a fixed initial pose; blue lines are for a random initial
pose

in .[−1, 1]. Three kinds of predictions are evaluated as follows. For clear description,
we only plot the last 200 time steps for the following results.
First, the predictions defined via the pseudoreward .Cti are utilized to approximate
how much the 6 force/torques will be when the pegs hit the holes. The pseudoreward
i
.C t is denoted as follows:
Cti = (1 − γti )Fti

.

(8.20)

where .Fti denotes the assembly force of the .i th prediction at time step .t, and .γti
will be 0 when the pegs have hit the holes; otherwise, it is 1. The true values for
the predictions are calculated by Eq. 8.1. The learned six different predictions to
approximate the assembly force can predict how much the assembly force will be
when the pegs hit the holes. As shown in Fig. 8.8, the learned predictions that are
shown as orange lines are accurate enough compared to the true value shown as the
sky-blue line.
Second, we verify the relation between the time scale of predictions and discount
rate .γ . In addition to the assembly force .Ft , we design the handcrafted pseudoreward
following the same behavior policy in Eq. 8.19 with a different discount rate .γ ,
corresponding to the different time scales of predictions. For instance, the predictions
are utilized to predict the period of an appearance of event .ℵ, e.g., when the pegs hit
the holes, as follows:

## [Book2025 PDF p.185] Page 185

170

8 LFE: Model-Based RL for PiH Assembly

Fig. 8.8 Predictions of how much assembly force will be when pegs hit holes; sky-blue lines are
true values; orange lines are learned results


Cti =

.

1, ℵ is done
0, else

(8.21)

when .γ = 0.96, the true value of learned predictions is equal to the time scale .25.
As shown in Fig. 8.9, likewise, we plot four different time-scale predictions with a
different discount rate .γ , such that the predictions with a smaller discount rate .γ are
easier to learn, and the predictions with a larger discount rate .γ are not as accurate
as the small one.
Third, to demonstrate that the predictions with two different target policies can
be learned through the off-policy scheme, two different target policies are denoted
as follows:
1
.πt (·|·) = [0.3, 0.1, 0.3, 0.1, 0.1, 0.1]
(8.22)
π 2 (·|·) = [0.05, 0.4, 0.4, 0.05, 0.05, 0.05]

. t

(8.23)

which have the different probability of selecting six motion directions. Likewise, the
predictions are utilized to predict the subsequent assembly, as shown in Fig. 8.8, if the
robots follow the actions generated by the target policy .πt1 (it has greater probability
to translate along .x-axis compared to the behavior policy in Eq. 8.19). However,
these predictions can be learned using the collected data from the behavior policy in
Eq. 8.19 instead of executing actions from the corresponding target policies.

## [Book2025 PDF p.186] Page 186

8.4 Experiments

171

Fig. 8.9 Different time-scale predictions; sky-blue lines are true values for predictions; orange
lines are learned results

As shown in Fig. 8.10, the predictions about the assembly force corresponding
to the target policy in Eqs. 8.22 and 8.23 can be effectively learned via the offpolicy scheme in Algorithm 8.1. The learned predictions are accurate at most of the
time steps compared with the true data shown in Fig. 8.10. More importantly, via
the off-policy scheme, the different target policies can be utilized to strengthen the
probability of one motion direction, which will be utilized to obtain the accurate
prediction about how much the assembly force will be if the pegs move along this
direction. In addition, the target policies can also be utilized to execute the dangerous
actions that might result in a large contact force. Therefore, via the off-policy scheme,
more useful information about the assembly environment can be learned without the
dangerous action execution. However, Fig. 8.10b shows that the error of the learned
predictions will increase when the target policy in Eq. 8.23 is far from the behavior
policy, which means that the importance ratio .ρt cannot compensate for the gap of
these two policies.

## [Book2025 PDF p.187] Page 187

172

8 LFE: Model-Based RL for PiH Assembly

Fig. 8.10 Predictions with different target policies; sky-blue lines are true values for predictions;
orange lines are learned results. a Target policy .πt1 . b Target policy .πt2

## [Book2025 PDF p.188] Page 188

8.4 Experiments

173

8.4.3 Control Performance and Analysis
FLDVTSP-DQN Versus DQN
FLDVTSP-DQN and typical DQN [4] have the same network architecture with
two fully connected layers (see Fig. 8.4). Both FLDVTSP-DQN and typical DQN
are trained for 100 episodes with the same hyperparameters settings as shown in
Table 8.2, and same reward signal as Eq. 8.9. To eliminate the impact of different
physical units, every dimension of the state given to the FLDVTSP-DQN and the
typical DQN is normalized within .[−1, 1]. Additionally, the network training techniques, e.g., the target network and experience replay are used to make the training
stable and efficient. The FLS of the FLDVTSP-DQN shown in Algorithm 8.2 is
designed according to Sect. 8.2. All GVFs to predict the subsequent assembly force
are also normalized within .[−1, 1] and input to the FLS. The range of proportional
parameters from the FLS output for impedance action space is shown in Table 8.1.
To evaluate the robustness against environmental noise, the learned assembly policies of FLDVTSP-DQN and typical DQN are applied to perform the same assembly
tasks for 30 times. As shown in Fig. 8.11a, FLDVTSP-DQN can obtain more rewards
within one episode and Fig. 8.11b shows that FLDVTSP-DQN decreases the assembly time about 44% compared to typical DQN. The 30 times assembly trajectories are

Table 8.2 Hyperparameters of DQN training
Parameters

Value

Minibatch size
Learning rate
Target net update rate
Buffer size

64
1e-3
1e-3
1e5

Fig. 8.11 Evaluation of FLDVTSP-DQN and typical DQN. a Episode reward. b Episode assembly
time

## [Book2025 PDF p.189] Page 189

174

8 LFE: Model-Based RL for PiH Assembly

Fig. 8.12 Evaluation of FLDVTSP-DQN and typical DQN. a Assembly trajectories. b Action
space (dimensionality is reduced by t-SNE for visualization)

plotted in Fig. 8.12a. FLDVTSP-DQN can achieve an average deeper insertion depth
compared to typical DQN. The reason is that the learned predictions can reduce the
unnecessary exploration during assembly. As shown in Fig. 8.12b, FLDVTSP-DQN
only needs to explore the narrow action space compared to typical DQN. The proposed impedance action space enables the robots to explore better policies efficiently.
Furthermore, the assembly force of both FLDVTSP-DQN and typical DQN for 30
times assembly are depicted in Fig. 8.13. Both FLDVTSP-DQN and typical DQN
can complete the assembly within the set safety threshold, but FLDVTSP-DQN can
achieve deeper insertion depth with fewer steps.
To test the generalization performance in new assembly tasks (diameters of peg
and hole are 29.98 mm and 30.00 mm, respectively; H7h7 tolerance), the learned
assembly policies by FLDVTSP-DQN and typical DQN are implemented for 30
times. As shown in Fig. 8.14, typical DQN cannot complete the assembly tasks
within 200 time steps in some cases and cannot achieve 100% success rate. However,
FLDVTSP-DQN can complete the assembly tasks with less time successfully and
achieve a success rate of 100%.

FLDVTSP-DDPG Versus DDPG
FLDVTSP-DDPG and typical DDPG are set to the same network architecture as
shown in Fig. 8.4, and the action threshold .B in Eq. 8.16 is set as 0.2. For fair comparison, FLDVTSP-DDPG and typical DDPG are trained for 100 episodes with the
same hyperparameters settings as in [2, 18] (see Table 8.3 ). Likewise, to evaluate the robustness against the environmental noise, the learned assembly policies
of FLDVTSP-DDPG and typical DDPG are applied to perform the same assembly
tasks for 30 times. As shown in Fig. 8.15a, FLDVTSP-DDPG can receive more reward

## [Book2025 PDF p.190] Page 190

8.4 Experiments

Fig. 8.13 Comparison of force. a Typical DQN. b FLDVTSP-DQN

175

## [Book2025 PDF p.191] Page 191

176

8 LFE: Model-Based RL for PiH Assembly

Fig. 8.14 Generalization performance of FLDVTSP-DQN and typical DQN. a Episode reward. b
Episode assembly time
Table 8.3 Hyperparameters
of DDPG training

Parameters

Value

Minibatch size
Actor learning rate
Critic learning rate
Target net update
Buffer size

64
1e-4
1e-3
1e-3
1e5

within one episode than typical DDPG and Fig. 8.15b shows that FLDVTSP-DDPG
decreases the assembly time about 24% compared to typical DDPG. The assembly trajectories of FLDVTSP-DDPG and typical DDPG are plotted in Fig. 8.16a.
FLDVTSP-DDPG can complete the search phase and achieve the deeper insertion
depth in insertion phase. As shown in Fig. 8.17, the assembly force of both FLDVTSPDDPG and DDPG are within the set safety threshold. However, FLDVTSP-DDPG
can complete the assembly tasks with fewer steps and smaller assembly force. As
shown in Fig. 8.16b, FLDVTSP-DDPG only needs to explore the narrow action space
without unnecessary exploration; obviously, the reformulated impedance action
space enable FLDVTSP-DDPG to learn more efficiently.
To test the generalization performance in new assembly tasks (diameters of peg
and hole are 29.98 mm and 30.00 mm, respectively; H7h7 tolerance), the learned
assembly policies by FLDVTSP-DDPG and typical DDPG are implemented for 30
times. As shown in Fig. 8.18, it is more difficult to complete the tight clearance
assembly. Although both FLDVTSP-DDPG and typical DDPG can achieve 100%
success rate within 200 time steps, obviously, compared to typical DDPG, FLDVTSPDDPG can receive more reward and decrease the assembly time by 24.7%.

## [Book2025 PDF p.192] Page 192

8.4 Experiments

177

Fig. 8.15 Evaluation of FLDVTSP-DDPG and typical DDPG. a Episode reward. b Episode
assembly time

Fig. 8.16 Evaluation of FLDVTSP-DDPG and typical DDPG. a Assembly trajectories. b Action
space (dimensionality is reduced by t-SNE for visualization)

FLDVTSP-DDPG Versus Model-Based RL
To demonstrate the effectiveness of our proposed FLDVTSP-DDPG compared to
previous model-based RL, four RL approaches assisted by the fitted dynamic model
are utilized to perform the PiH assembly tasks, including typical DDPG, DynaDDPG [15], BE-DDPG (DDPG with better exploration based on dynamic model),
and GPS [9]. The transition samples interacting with environment are collected and
stored in the replay buffer .D = {(st , at , st+1 )}. Afterwards, the data are sampled
from .D to fit the dynamic model.
We apply three commonly used statistical techniques to fit the dynamic model via
the collected data in the replay buffer .D: linear approximation, nonlinear approximation with a NN, and time-varying linear-Gaussian approximation. Therefore,

## [Book2025 PDF p.193] Page 193

178

8 LFE: Model-Based RL for PiH Assembly

Fig. 8.17 Comparison of force. a Typical DDPG. b FLDVTSP-DDPG

## [Book2025 PDF p.194] Page 194

8.4 Experiments

179

Fig. 8.18 Generalization performance of FLDVTSP-DDPG and typical DDPG. a Episode reward.
b Episode assembly time
Fig. 8.19 Performance of
assembly time compared to
model-based RL

for fair comparison, all aforementioned model-based RL algorithms with the linear
Gaussian-based dynamic model are trained with same settings as typical DDPG and
FLDVTSP-DDPG. All the trained assembly policies are evaluated for 100 times.
As shown in Fig. 8.19, FLDVTSP-DDPG can complete one episode of assembly
with less time, leading to the highest data efficiency. The dynamic model with bias
may mislead the assembly action learning, e.g., GPS and BE-DDPG. In contrast,
the learned predictions can enable the FLDVTSP-DDPG to avoid the trap during
training.

## [Book2025 PDF p.195] Page 195

180

8 LFE: Model-Based RL for PiH Assembly

8.5 Conclusion
This chapter proposes FLDVTSP-RL for multiple PiH assembly that are more data
efficient than existing RL algorithms. First, GVFs are used to learn the variable timescale predictions of the subsequent assembly, which can predict more information
about the assembly environment. The impedance action space for FLDVTSP-RL is
reformulated, in which the baseline is calculated based on the impedance parameters
mapped from the predicted environment by the designed FLS. The results of a dual
PiH assembly experiment demonstrate that the predictions of the subsequent assembly force can be learned through GVFs effectively. Our proposed FLDVTSP-DQN
and FLDVTSP-DDPG algorithms can perform the assembly tasks more efficiently
than the typical RL algorithms without any parameter tuning.

References
1. L. Brignone, M. Howarth, A geometrically validated approach to autonomous robotic assembly,
in IEEE/RSJ International Conference on Intelligent Robots and Systems vol. 2, pp. 1626–1631
(2002)
2. Y. Fan, J. Luo, M. Tomizuka, A learning framework for high precision industrial assembly, in
2019 International Conference on Robotics and Automation (ICRA) (IEEE, 2019), pp. 811–817
3. V.Z. Filipovic, N. Nedic, V. Stojanovic, Robust identification of pneumatic servo actuators in
the real situations. Forschung im Ingenieurwesen 75(4), 183–196 (2011)
4. T. Inoue, G. De Magistris, A. Munawar, T. Yokoya, R. Tachibana, Deep reinforcement learning
for high precision assembly tasks, in 2017 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS) (IEEE, 2017), pp. 819–825
5. J. Kober, J.A. Bagnell, J. Peters, Reinforcement learning in robotics: a survey. Int. J. Robot.
Res. 32(11), 1238–1274 (2013)
6. S. Levine, N. Wagener, P. Abbeel, Learning contact-rich manipulation skills with guided policy
search, in 2015 IEEE International Conference on Robotics and Automation (ICRA), pp. 156–
163 (2015)
7. F. Li, Q. Jiang, S. Zhang, M. Wei, R. Song, Robot skill acquisition in assembly process using
deep reinforcement learning. Neurocomputing 345, 92–102 (2019)
8. T.P. Lillicrap, J.J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver, D. Wierstra,
Continuous control with deep reinforcement learning, in ICLR (2016)
9. J. Luo, E. Solowjow, C. Wen, J.A. Ojea, A.M. Agogino, A. Tamar, P. Abbeel, Reinforcement learning on variable impedance controller for high-precision robotic assembly, in 2019
International Conference on Robotics and Automation (ICRA) (IEEE, 2019), pp. 3080–3087
10. V. Mnih, K. Kavukcuoglu, D. Silver, A.A. Rusu, J. Veness, M.G. Bellemare, A. Graves, M. Riedmiller, A.K. Fidjeland, G. Ostrovski et al., Human-level control through deep reinforcement
learning. Nature 518(7540), 529 (2015)
11. J. Modayil, A. White, R.S. Sutton, Multi-timescale nexting in a reinforcement learning robot.
Adapt. Behav. 22(2), 146–160 (2014)
12. A. Morim, E.S. Fortes, P. Reis, C. Cosenza, F. Doria, A. Gonçalves, Think fuzzy system:
developing new pricing strategy methods for consumer goods using fuzzy logic. Int. J. Fuzzy
Logic Syst. 7(1), 1–17 (2017)
13. V. Stojanovic, V. Filipovic, Adaptive input design for identification of output error model with
constrained output. Circuits Syst. Signal Proc. 33(1), 97–113 (2014)
14. V. Stojanovic, N. Nedic, Robust identification of oe model with constrained output using
optimal input design. J. Frankl. Inst. 353(2), 576–593 (2016)

## [Book2025 PDF p.196] Page 196

References

181

15. R.S. Sutton, Integrated architectures for learning, planning, and reacting based on approximating dynamic programming, in Machine Learning Proceedings 1990 (Elsevier, 1990), pp.
216–224
16. R.S. Sutton, J. Modayil, M. Delp, T. Degris, P.M. Pilarski, A. White, D. Precup, Horde: a scalable real-time architecture for learning knowledge from unsupervised sensorimotor interaction,
in The 10th International Conference on Autonomous Agents and Multiagent Systems-Volume 2,
International Foundation for Autonomous Agents and Multiagent Systems, International Foundation for Autonomous Agents and Multiagent Systems, Richland, SC, AAMAS ’11 (2011), pp.
761–768
17. D. Xing, F. Liu, S. Liu, D. Xu, Efficient insertion of partially flexible objects in precision
assembly. IEEE Trans. Autom. Sci. Eng. 16(2), 706–715 (2019). https://doi.org/10.1109/TASE.
2018.2853607
18. J. Xu, Z. Hou, W. Wang, B. Xu, K. Zhang, K. Chen, Feedback deep deterministic policy gradient
with fuzzy reward for robotic multiple peg-in-hole assembly tasks. IEEE Trans. Ind. Inf. 15,
1658–1667 (2019)

## [Book2025 PDF p.197] Page 197

Chapter 9

LFE: Hierarchical RL Method for PiH
Assembly

9.1 Introduction
In Chap. 7, a model-driven DDPG approach with the feedback exploration and a fuzzy
reward scheme to learn robotic assembly skills are presented. However, the off-policy
RL methods to solve continuous control tasks still rely on numerous interactions,
and the data-inefficiency issue largely limits the applicability in real-world tasks.
Drawing inspiration from the hierarchical mental structure employed by humans
to tackle complex tasks, Hierarchical Reinforcement Learning (HRL) [3, 17] offers
a method to learn complex policies by decomposing them down into hierarchies of
sub-policies. This approach consists of a higher-level policy and multiple lower-level
policies, facilitating efficient exploration and achieving high data-efficiency [13].
This chapter presents a data-efficient off-policy HRL algorithm. The contributions
are:
1. To learn the higher-level policy and lower-level policies from the same samples
via off-policy learning, the continuous control tasks solved by HRL methods are
reformulated as two augmented MDPs. The theorem is derived and proven.
2. To learn the higher-level policy efficiently, we omit the termination function and
derive a softmax gating policy to determine the lower-level policy interaction with
the environment with fixed temporally extended periods.
3. To learn the lower-level policies with better data-efficiency performance, the
higher-level policy derived based on the option-value network is adopted to select
the appropriate option for learning the corresponding lower-level policy.
From the practical aspect, based on the proposed impedance-conditioned action
space, the proposed HRL algorithm is adopted to solve complicated multiple PiH
assembly tasks. A simulation platform, including dual and triple PiH assembly, is set
up on Webots. The generalization performance of our proposed HRL algorithm in two
kinds of new tasks is validated and discussed in both simulations and experiments.

© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_9

183

## [Book2025 PDF p.198] Page 198

184

9 LFE: Hierarchical RL Method for PiH Assembly

9.1.1 Related Work
In the HRL community, lower-level policies are applied to generate the action to
interact with the environment; higher-level policies are learned to select the lowerlevel policies over a longer time-scale [17]. To learn the hierarchical policy, one group
of HRL methods often defines the sub-goals via a higher-level policy and learns the
lower-level policies via the typical RL methods to achieve the sub-goals [13]. The
sub-goals are often predefined corresponding to the tasks. In contrast to the fixed
sub-goals, FeUdal network [17] learns a higher-level policy to find effective varying
sub-goals via maximizing the extrinsic reward, and learns the lower-level policies
via maximizing the defined intrinsic reward based on the given sub-goals. Generally,
the sub-goals definition requires prior knowledge of the tasks; however, it is not a
trivial problem to find the effective sub-goals for complex tasks.
The hierarchical policy can be defined using latent variables instead of explicit subgoals [10]. Option-critic (OC) uses discrete latent variables, referred to as “options”
and employs a termination function to determine when to switch options [3]. A
training scheme has been developed to simultaneously update the lower-level policies
and termination functions. DAC-PPO [19] introduced two parallel augmented MDPs
to learn options for continuous control tasks. However, applying HRL in real-world
tasks faces two main challenges. Firstly, most existing HRL methods, including
DAC-PPO, heavily rely on on-policy learning [10]. Learning a hierarchical policy
from off-policy samples requires addressing the problems of learning the higher-level
policy without manual design and efficiently learning the lower-level policies from
samples generated by different lower-level policies [13]. Secondly, the termination
function’s performance is often unstable when options change frequently or are
executed for a single time step [19].

9.2 Method
9.2.1 Foundations
The control problems addressed by RL generally can be formulated as a MDP as
described in Sect. 1.3.5. The control scheme to solve the problems by HRL is shown
.o ∈ O covers all possible options. A hierarchical policy can be
in Fig. 9.1; option set
defined as .π(a|s) = o∈O πO (o|s)πo (a|s, o), which omits the termination function
compared to OC-based algorithms [3]. .πo (a|s, o) abbreviated as .πo (a|s), denotes
the lower-level policy of option .o. .πO (o|s) denotes the higher-level policy. Similarly,
.
the trajectories sampled by a hierarchical policy .π can be defined as . = {τ =
(s0 , o0 , a0 , s1 , o1 , a1 , . . . , sT )|π, O, M}. We assume that .S and .A are infinite sets,
while .O is a finite set covering all options. The objective function .J (τ ) to learn the
hierarchical policy averaged with the state-action distribution is denoted as follows:

## [Book2025 PDF p.199] Page 199

9.2 Method

185

Fig. 9.1 Control scheme: at each environment step, hierarchical policy can generate option and
action for robot to interact with environment; at each training step, hierarchical policy is updated
via off-policy samples stored in the replay buffer

 
J (π ) =

.

pπ (s)


o∈O



πO (o|s)πo (a|s, o) Q π (s, a)dads


π(a|s)

(9.1)



T
where . pπ (s) = t=0
γ t P0 (st = s) denotes the visitation frequency induced by the
hierarchical policy .π(a|s); . Q π denotes the state-action value function to estimate the
expected return of the state-action pair .(s, a). Similar to an optimization problem,
the constraints are given in the definition of state space .st ∈ S, option set .ot ∈ O,
action space .at ∈ A and reward function .R(·, ·).

9.2.2 Two Augmented MDPs
To learn the hierarchical policy via off-policy samples from .{O, M}, based on [19],
we reformulate the problems solved by HRL as two augmented MDPs: the higherlevel MDP .M H = (S H , A H , R H , P0H , P H , γ H ) utilized for option selection and
lower-level MDP .M L = (S L , A L , R L , P0L , P L , γ L ) utilized for action selection.
.
.
In the higher-level MDP, state space .S H = S × O+ × C, .O+ = O + ⊕ where .⊕
.
denotes the dummy option for clear notations, .C = {change, stay} denotes whether
.
or not to change the option; action space .A H = O; higher-level reward func.
H H
H .
H
tion . R (st , at ) = R (st , ot−1 , ct , ot ) = R(st , ot ); therefore, .E[RtH ] = R(st , ot );
.γ H is the discount factor of the higher-level MDP. Given a bijection function
H
H
H .
= {τ H =
. , the trajectories . can be mapped to new trajectories . , as .
H
H
H
H
H
H
H
(s0 , a0 , s1 , a1 , . . . , st )|π , M } induced by the transition function
H H
H
H
.P (st+1 |st , at ). Here, we have the following:
Lemma 9.1 Given the bijection function . H , .P(τ |π, O, M) = P H (τ H |π H , M H )
and . R(τ ) = R H (τ H )

## [Book2025 PDF p.200] Page 200

186

9 LFE: Hierarchical RL Method for PiH Assembly

.
Proof of Lemma 9.1 In the higher-level MDP, state space .S H = S × O+ × C, .C =
+
{change, stay}, .O = O + ⊕, .⊕ denotes the dummy option for clear notation, and
.
action space .A H = O, defines the higher-level policy .π H (atH |stH ); therefore, we
have:
.
.
P0H (s0H ) = P0H (o−1 , s0 , c0 ) = P0 (s0 )Ic0 =change,o−1 =⊕
H H
H
H .
H
H
. P (s
t+1 |st , at ) = P ((ot , st+1 , ct+1 )|(ot−1 , st , ct ), at )
.
= IatH =ot P(st+1 |st , ot )P(ct+1 |ct )
P(τ |π, O, M)
T −1

= P(s0 , o−1 , c0 )

P(ot |st , ot−1 , ct )P(st+1 |st , ot )P(ct+1 |ct )
t=0
T −1

.

= P(s0 )Ic0 =change

P(ot |st , ot−1 , ct )IatH =ot P(st+1 |st , ot )
t=0

P(ct+1 |ct )
T −1

= P H (s0H )

H
π H (atH |stH )P H (st+1
|stH , atH )
t=0

= P H (τ H |π H , M H )
Given a bijection . H mapping, the reward function . R(τ ) goes to . R(τ H ), and .P(·)
goes to .P H (·).
.
In the lower-level MDP, state space .S L = S × O, action space
.
.
.
.
L
L
L L
L
L
.A = A, . R (st , at ) = R (st , ot , at ) = R(st , at ), .E[Rt+1 ] = R(st , at ), and .γ L is
the discount factor of lower-level MDP. The lower-level policies.π L (atL |stL ) in lowerlevel MDP are denoted as .π L (at |st , ot ), which can be abbreviated as .πoL (at |st ). A
bijection function. L can be defined to map the trajectories. to new trajectories. L ,
.
.
as . L = {τ L = (s0L , a0L , s1L , a1L , . . . , sTL )|π L , M L } induced by the transition funcL
|stL , atL ). Here, we have the following:
tion .P L (st+1
Lemma 9.2 Given the bijection function . L , .P(τ |π, O, M) = P L (τ L |π L , M L )
and . R(τ ) = R L (τ L )
.
Proof of Lemma 9.2 In the lower-level MDP, state space .S L = S × O, action space
L .
L
L L
.A = A, define lower-level policy .π (at |st ), therefore, we have:
P0L = P L (s0L ) = P(s0 , o0 ) = P(s0 )P(o0 |s0 )
.

L
P L (st+1
|stL , atL ) = P L ((st+1 , ot+1 )|(st , ot ), at )

= P(st+1 |st , at )P(ot+1 |st , ot )

## [Book2025 PDF p.201] Page 201

9.2 Method

187

Therefore, we have:
T −1

P(τ |π, O, M) =P(s0 )P(o0 |s0 )

P(at |st , ot )
t=0

P(st+1 |st , at )P(ot+1 |st+1 , ot )
.

T −1

=P L (s0L )

L
π L (atL |stL )P L (st+1
|stL , atL )
t=0
L

=P (τ |π , M L )
L

L

Given a bijection . L mapping the reward function . R(τ ) to . R(τ L ) and .P(·) to .P L (·).
Lemmas 9.1 and 9.2 seem identical to DAC [19]; given the different definitions of
the higher-level policy and lower-level policies, similar to [19]. Similarly, we can
also derive the equivalence relationship of the objective as in Proposition 9.1.
Proposition 9.1

.
J =
.

=
=





R(τ )Pτ (τ |π, O, M)dτ
R H (τ H )P H (τ H |π H , M H )dτ H

(9.2)

R L (τ L )P L (τ L |π L , M L )dτ L

Accordingly, based on Proposition 9.1, the hierarchical policy .π can be learned
through optimizing the higher-level policy .π H and lower-level policies .π L with the
samples from .(π, O, M). For off-policy learning, first, we introduce the details of
sampling actions based on two MDPs (see Fig. 9.2); second, we introduce the details
of all networks and a schematic of training the hierarchical policy (see Fig. 9.3);
finally, we discuss the stable learning and convergence of our algorithm.

Fig. 9.2 Schematic of sampling actions from the hierarchical policy

## [Book2025 PDF p.202] Page 202

188

9 LFE: Hierarchical RL Method for PiH Assembly

Fig. 9.3 Schematic of training the hierarchical policy

At each environment step, the action is sampled from the hierarchical policy as
shown in Fig. 9.2. According to standard off-policy definitions [5], the target policy is
the defined policy to learn, and the behavior policy is defined to select the action with
exploration. Here, the lower-level target policies in Proposition 9.1 are defined as the
deterministic policy .μ(a|s, o), abbreviated as .μo (s). Each deterministic lower-level
policy is estimated by a separate actor network as .μo (s|θ ). The action is derived
from the defined corresponding behavior policy .ai = β o (ai |si ) = μo (si |θ) + , i =
t, . . . , t + K − 1, and. ∼ N(0, σμ ) is the Gaussian noise to enhance the exploration
of the selected lower-level policy. The collected sample .(si , ai , si+1 , Ri+1 ) is stored
in the lower-level replay buffer .D L .
As shown in Fig. 9.2, the option is selected from a gating policy .πO (o|s) every
. K time steps instead of the higher-level policy. In contrast to the typical termination
function [3], our algorithm not only can avoid the bad choice during the early learning
stage but also result in better exploration in the mature learning stage. A softmax
gating policy can be denoted to select the option .o that maximizes the conditional
expectation of the return:
.

Q πO (s, o) =



πoL (a|s)Q π (s, a)da

(9.3)

where . Q πO (s, o) is the conditional state-option value function induced by the hierarchical policy .π(·) [3]. For deterministic lower-level policies, the conditional state-

## [Book2025 PDF p.203] Page 203

9.2 Method

189

option value function in Eq. 9.3 can be defined as . Q πO (s, o) = Q π (s, μo (s|θ )) and
the gating policy is denoted as follows:
exp(Q πO (s, o))
π
o∈O exp Q O (s, o)

π (o|s) = 

. O

(9.4)

After option .oi is executedfor . K time steps, the state will transit to .st+K −1 and
−1
R j , which is the cumulative reward of the past
receives the reward . RtH = t+K
j=t
H
. K time steps. The sample .(si , oi , si+1 , Ri ) is stored in the higher-level replay buffer
.D H .

9.2.3 Higher-Level Policy Learning
With the discrete action space, the higher-level policy .π H (ot |st ) can be learned
similarly to DQN [12]. The state-option value and state value induced by the higherlevel policy .π H are denoted as follows:
Q π (s, o) =E π H [RtH |st = s, ot = o]

H
H
.
π H (o|s)Q π (s, o)
V π (s) =
H

(9.5)

o∈O

The advantage function of the state-option pair is denoted as follows:
Aπ (s, o) = Q π (s, o) − V π (s)
H

.

H

H

(9.6)

which represents the importance of the selected state-option pair. The option-value
network . Q H (st , ot ; ψ) with the parameters .ψ is utilized to estimate the state-option
value function, as shown in Fig. 9.3. At each training step, mini-batch transitions
H
.(si , oi , si+1 , Ri ) are uniformly and randomly sampled from .D H . The parameters
.ψ are updated through minimizing the loss over mini-batch samples .B H ∈ D H as
follows:
H
H
2
.L H = EB H [(Yi − Q (si , oi ; ψ)) ]
(9.7)
where the target .YiH is computed by a target option-value network as .YiH = RiH +
γ H maxo Q H (si+1 , o |ψ̄). .ψ̄ is the parameter of the target option-value network.
Additionally, the dueling DQN and soft . Q-learning can also be implemented to
estimate the state-option value function. Afterwards, with the learned state-option
value function, the “optimal” higher-level policy .π H (ot |st ) for following lower-level
policies learning is derived as a greedy policy:
o = argmaxo ∈O Q H (si , o ; ψ̄)

.

(9.8)

## [Book2025 PDF p.204] Page 204

190

9 LFE: Hierarchical RL Method for PiH Assembly

9.2.4 Lower-Level Policies Learning
As shown in Fig. 9.3, at each training step, the lower-level policies are trained
with the past samples in the lower-level replay buffer .D L . Mini-batch transitions
.(si , ai , si+1 , Ri+1 ) ∈ B L are uniformly and randomly sampled from .D L . Similar
to TD3 [6], two separate state-action value networks (named as critic networks)
L
L
. Q (si , ai |ξ 1 ), Q (si , ai |ξ 2 ) with parameters .(ξ 1 , ξ 2 ) are implemented to estimate
the state-action value function . Q π (st , at ). Based on Proposition 9.1, the higher-level
policy is used to select the most appropriate lower-level policy to train for the minibatch states .si ∈ B L . Therefore, the corresponding option .oi+1 is derived from the
current higher-level policy as in Eq. 9.8, and the action .ai+1 is obtained from the
corresponding lower-level policy .μo (si+1 |θ̄ ). They are updated through minimizing
the loss over the given mini-batch samples .B L ∈ D L as follows:
L L = EBL

.



YiL − Q L (si , ai |ξ )

2



, ξ ∈ (ξ 1 , ξ 2 )

(9.9)

where the target value is calculated as .YiL = Ri+1 + γ L min j=1,2 Q L (si+1 ,
μo (si+1 |θ̄) + |ξ̄ j ). . is clipped Gaussian noise sampled from . ∼ clip(N(0, σc ),
−c, +c), which is a practical technique to improve the performance that is resistant
to perturbation [6]. Additionally, the minimum operator can provide an upper bound
with less overestimation value, which will result in a lower variance for value estimation. Then, the DPG theorem [14] with respect to the parameters of the selected
actor network .μo (si |θ) is computed as follows:

∇θ J (θ , ξ ) = EBL ∇θ μo (si |θ)∇a Q L (si , a|ξ )|a=μo (si |θ )

.

(9.10)

9.2.5 Convergence Analysis
The step by step implementation of our algorithm is summarized in Algorithm 9.1.
Target network is a well-known technique that has been proven to provide a stable
target and improve the final performance through reducing the variance of target
approximation error [2, 12]. Accordingly, we implement the corresponding target
networks with parameters .(ψ̄, ξ̄ , θ̄ ) for all networks in Fig. 9.3. The parameters of
target networks are updated slowly with the corresponding coefficient, e.g., .ζξ  1,
as .ξ̄ ← ζξ ξ + (1 − ζξ )ξ̄ . All losses in Eqs. 9.7, 9.9, and 9.10 are trained via the
Adam optimizer [9] with the learning rate .ηψ , ηξ , ηθ , respectively. The improvement
of stable learning induced by target network has been validated empirically in [2]
and [6].

## [Book2025 PDF p.205] Page 205

9.3 Simulation

191

Algorithm 9.1 Data-efficient HRL
1: Input: number of options .O; size of .D H and .D L ; option change length . K
2: Initialize: for each option .o ∈ O, actor network .μo (s|θ) and target actor network .μo (s|θ̄)
3: Initialize: critic network . Q L (s, a|ξ ) and target critic network . Q L (s, a|ξ̄ )
4: Initialize: option-value network . Q H (s, a|ψ) and target option-value network . Q H (s, a|ψ̄)
5: for .t = 0 to .t = T do
6: Observe state .st
7: Select action .at with corresponding lower-level policy and exploration noise as .at ←
μo (st |θ̄) + Nt (0, σμ )
8: Execute action .at , observe reward . Rt and .st+1
9: Calculate cumulative reward . RtH + = Rt
10: Store transition .D L ← D L + (st , at , st+1 , Rt+1 )
11: if .t mod . K then
12:
Store transition .D H ← D H + (st , ot , st+K −1 , RtH )
13:
Choose option .ot from gating policy .ot ∼ πO (o|st )
14: end if
15: Update critic network with a mini-batch of samples .(si , ai , si+1 , Ri+1 ) ∈ B L from .D L
H ) ∈ B from .D
16: Update option-value network with a mini-batch samples .(si , oi , si+1 , Ri+1
H
H
17: if .t mod .d then
18:
Estimate .oi ∼ π H (oi |si ) for .si ∈ B L by higher-level policy in Eq. 9.8
19:
Update actor network .μo (s|θ ) for .o = oi
20:
Update all target networks
21: end if
22: end for

9.3 Simulation
Our algorithm is implemented following Algorithm 9.1 on four commonly used
MuJoCo tasks and two multiple PiH assembly tasks. We compare our method with
state-of-the-art RL methods, including off-policy RL methods, e.g., DDPG [11],
TD3 [6], and SAC [7], the on-policy RL algorithm: PPO [8] and popular HRL methods OC [3], PPOC, and DAC-PPO [19].

9.3.1 MuJoCo Continuous Control Tasks
MuJoCo tasks [15], as shown in Fig. 9.4, are often applied to compare the performance of continuous control RL methods. With the default reward settings provided
by [4], all aforementioned algorithms are trained for .5 × 105 time steps with five
different seeds, and the average cumulative reward is evaluated via 10 episodes per
1000 time steps. The network architecture is shown in Fig. 9.3, and the hyperparameters of our algorithm are listed as in Table 9.1, those for lower-level policies learning
refer to TD3 [6]. All other algorithms are implemented with the code provided by the
authors and the hyperparameters are selected to be the same as the original papers.

## [Book2025 PDF p.206] Page 206

192

9 LFE: Hierarchical RL Method for PiH Assembly

Fig. 9.4 MuJoCo tasks. a Walker2d-v2, b Ant-v2, c Hopper-v2, d HalfCheetah-v2
Table 9.1 Hyperparameters of our algorithm
Description
Lower-level replay buffer
Lower-level discount factor
Mini-batch size for lower-level policy
Higher-level replay buffer
Higher-level discount factor
Mini-batch size for higher-level policy
Noise clip threshold
Noise for exploration
Action noise for critic update
Target network update rate
Learning rate

Symbol

Value

.D L

.10

.γ L

0.99
200
5000
0.99
100
0.5
0.1
0.2
0.005
0.001

.B L
.D H
.γ H
.B H
.c
.σμ
.σc
.ζψ , ζξ , ζθ
.ηψ , ηξ , ηθ

6

In Fig. 9.5, darker lines represent the average cumulative reward over 5 seeds in
a total of 50 runs. The shaded region shows the standard deviation of the averaged
cumulative reward over 50 runs. Our algorithm (with .O = 2, K = 100) not only
achieves the highest final performance on all four tasks but also accomplishes this
level of performance in fewer steps. For HRL, how to choose the number of options is
still a long-time open question [3, 19]. We select HalfCheetah-v2 and Hopper-v2 to
discuss the effects of the option number (.O = 2, 4, 6) and option change length (. K =
20, 50, 100) on our algorithm, respectively. Note that our algorithm with .O = 1 will
degenerate into TD3. Therefore, we have omitted the result of our algorithm with
.O = 1. As shown in Fig. 9.6, a greater option change length correlates with better
stability of the target for lower-level policies learning. Inversely, if the option is
changed frequently with a small option change length, then the higher-level policy
will contribute more to exploring better lower-level policies.

## [Book2025 PDF p.207] Page 207

9.3 Simulation

193

Fig. 9.5 Qualitative performance on four MuJoCo tasks [15]

Fig. 9.6 Ablation performance on HalfCheetah-v2 and Hopper-v2. a Number of options. b Option
change length

## [Book2025 PDF p.208] Page 208

194

9 LFE: Hierarchical RL Method for PiH Assembly

9.3.2 Multiple PiH Assembly
The multiple PiH assembly tasks (dual and triple) are constructed based on
Webots [1] (see Fig. 9.7a and b). The problem formulation has been introduced in
Sect. 7.2.1. The objective for PiH assembly tasks is to reach the desired insertion
depth as quickly as possible without dangerous contact force. A reward function is
denoted as follows:
⎧
−0.1,
done = False and safe = True
⎪
⎪
⎪
⎪
k
⎨
1−
, done = True and safe = True
.R(st , at ) =
kmax
⎪
⎪
⎪
⎪
⎩ −1 + dt ,
safe = False
de

(9.11)

where .kmax denotes the maximum number of steps in one episode, and .k ∈ [0, kmax ]
denotes the final number of steps. To encourage the fewer assembly steps, .−0.1 is
received every time step. .de denotes the desired insertion depth, and .dt denotes the
final insertion depth when the assembly is completed or the forces exceed the safe
boundary. Additionally, the penalty is designed according to the force signals, and
the assembly procedure will be interrupted with reward .−1 for the absolute value of
forces exceeding the safe boundary.

Fig. 9.7 Multiple PiH assembly. a Dual. b Triple. c Assembly actions. d F/T sensor

## [Book2025 PDF p.209] Page 209

9.3 Simulation

195

Impedance-Conditioned Action Space
Action space reformulation is a practical technique to enable RL methods to perform
safely and efficiently [16], and we reformulate the action space in Eq. 7.2 by combining it with the impedance controller [18] to take the contact force into account.
First, an expert assembly action .u et is calculated as follows:
.

u et = K p ◦ et + Kd ◦ ėt , et = Fr − Ft

(9.12)

where .◦ denotes the Hadamard product; .et denotes the corresponding difference
between the desired reference forces .Fr and the current detected force signals
6
6
.Ft = [F t , M t ]; and .K p ∈ R and .Kd ∈ R are the stiffness and damping parameters
corresponding to each component in Eq. 7.2. Consequently, the assembly action .u t
is calculated as follows:
.

u t = clip {at , −b, +b} ◦ u et + u et

(9.13)

where .at ∈ [−1, 1]6 is the action derived from lower-level policies, and .b is adopted
to control the confidence of action .at . Accordingly, compared to adding noise in
the original action space Eq. 7.2, the expert assembly action .u et takes the relations
between pose and force into account, which are the constraints to enable the robots
to implement impedance-like behaviors and avoid unpredicted contact force.

Results
With the same hyperparameters in Table 9.1, we compare our algorithm (.O = 2, 4, 6)
with DDPG and TD3. The desired reference force .Fr and impedance parameters of
the impedance action space can be set according to the force signals. The desired
insertion depth .de is set as 40 mm and the maximum number of steps is set as
200. First, all algorithms are trained on the dual and triple PiH assembly tasks with
the same settings (friction = 0.5 and clearance = 1 mm). As shown in Fig. 9.8, our
algorithm with four and six options can achieve the better performance with the
better final performance and lower variance on both dual PiH assembly and triple PiH
assembly. Second, to validate the generalization performance, the learned assembly
skills are evaluated directly every 2000 time steps or retrained on new tasks. We
consider two cases, first, the learned assembly policies in dual PiH assembly (friction
= 0.5 and clearance = 1 mm) are transferred to a more complicated assembly task
with a smaller clearance (friction = 0.5 and clearance = 0.5 mm); second, the learned
assembly policies in dual PiH assembly (friction = 0.5 and clearance = 1 mm) is
transferred to triple PiH assembly (friction=0.5 and clearance=1 mm). The evaluation
and retraining performance shown in Fig. 9.9 indicate that our algorithm can still
obtain a higher cumulative reward, which means that the better generalization ability
of our algorithm is achieved due to the better exploration property.

## [Book2025 PDF p.210] Page 210

196

9 LFE: Hierarchical RL Method for PiH Assembly

Fig. 9.8 Qualitative performance. All algorithms are trained for .5 × 105 time steps with five different seeds; average cumulative reward is evaluated via 10 episodes every 1000 time steps; darker
lines represent average cumulative reward over 50 runs; shaded region represents standard deviation
over 50 runs. a Dual. b Triple

Fig. 9.9 Generalization performance. Original represents policies via same training on new tasks;
eval represents learned policies evaluated on new tasks every 2000 time steps; re-train represents
that learned policies are reloaded and retrained on new tasks. a Tight clearance. b Dual-to-triple

9.4 Experiments
With same problem statement introduced in Sect. 9.3.2, two experiments are conducted to validate the data efficiency and generalization performance of our method.

9.4.1 Experimental Setup
A dual PiH assembly platform is set up as shown in Fig. 9.10, and a 6-DoF F/T sensor
is mounted to the end-effector of an ABB IRB 4600 robot. The pegs are mounted on

## [Book2025 PDF p.211] Page 211

9.4 Experiments

197

Fig. 9.10 Robotic dual PiH assembly platform
Table 9.2 Configuration of components
Hole (mm)
Peg (mm)

Clearance (.µm)

Material

Component 1
Component 2

40
20

Aluminum
Aluminum

30.00
30.00

29.96
29.98

the F/T sensor and the holes are fixed on the experimental table. The configurations
of two groups of components are depicted in Table 9.2, and as shown in Fig. 9.10,
the distance between the two pegs’ axes and the two holes is 200 mm.

9.4.2 Comparison 1: Data Efficiency
Our algorithms are implemented with three different number of options (.O = 2, 4, 8)
and the same hyperparameters as those in Table 9.1. All algorithms are trained on
the tasks (with component 1) for 100 episodes and the maximum number of steps
of each episode is set to 150. The safe boundary of force and torque signals is set as
100 N and 8 Nm, respectively. Specifically, the snapshot of the assembly procedure
is shown in Fig. 9.10, which can be separated into three phases: approach, search,
and insertion. The impedance parameters and reference forces of the impedance
action space in Eq. 9.12 are set as depicted in Table 9.3. The cumulative reward
of one episode during the training process is plotted in Fig. 9.11. Additionally, all
learned assembly policies are evaluated every 10 episodes for 5 times, the average cumulative reward and assembly time over 5 times are depicted in Figs. 9.12
and 9.13, respectively.
DDPG often easily falls into a local minimum, and TD3 cannot improve the
assembly performance via solving the over-estimation issue, as in the simulation.
In contrast, our algorithm with three different number of options can achieve better
exploration performance and learn effective policies. As shown in Fig. 9.13, the

## [Book2025 PDF p.212] Page 212

198

9 LFE: Hierarchical RL Method for PiH Assembly

Table 9.3 Parameters of impedance action space
Items
. x
. y
.
Search

.K p
.Kd
.Fr

Insertion

.K p
.Kd
.Fr

0.015
0.005
0
0.002
0.0002
0

0.015
0.005
0
0.002
0.0002
0

z

0.002
0.005
.−50
0.02
0.002
.−80

.

x

0.02
–
0
0.015
–
0

.

y

0.02
–
0
0.015
–
0

.

z

0.02
–
0
0.015
–
0

Fig. 9.11 Cumulative reward of each training episode (comparison 1). a Our algorithm with three
different numbers of options (.O = 2, 4, 6). b Comparison with DDPG and TD3

Fig. 9.12 Average cumulative reward over five times of each evaluation step (comparison 1). a
Our algorithm with three different numbers of options (.O = 2, 4, 6). b Comparison with DDPG
and TD3

## [Book2025 PDF p.213] Page 213

9.4 Experiments

199

Fig. 9.13 Average assembly time over five times of each evaluation step (comparison 1). a Our
algorithm with three different number of options (.O = 2, 4, 6). b Comparison with DDPG and TD3

assembly time of one episode has been reduced by approximately 14%. The 50
evaluation assembly trajectories (omit the approach phase) of all algorithms during
the evaluation stage are depicted in Fig. 9.14a. Additionally, the evolution of the
insertion depth is plotted in Fig. 9.14b. Our algorithm can achieve the desired insertion
depth (.de ) faster than TD3 and DDPG. In addition to the assembly speed, the assembly
force of 50 evaluation assembly trajectories are plotted from Figs. 9.15 to 9.16. To
answer the question what different assembly skills our algorithm can learn, the output
action of one episode is depicted in Fig. 9.17. Compared with DDPG and TD3, our
algorithm with different number of options has achieved better exploration and output
effective actions.

Fig. 9.14 50 evaluation assembly trajectories (comparison 1). a 3D path. b Insertion depth

## [Book2025 PDF p.214] Page 214

200

9 LFE: Hierarchical RL Method for PiH Assembly

Fig. 9.15 Assembly force of TD3 during evaluation stage (comparison 1)

Fig. 9.16 Assembly force of our algorithm (.O = 4) during evaluation stage (comparison 1)

## [Book2025 PDF p.215] Page 215

9.4 Experiments

201

Fig. 9.17 Action during one episode of all algorithms (comparison 1)

9.4.3 Comparison 2: Generalization Performance
The learned assembly skills are reloaded and retrained on a more complicated task
with tight tolerance (component 2) for 100 episodes. The learned assembly policies are evaluated every 10 episodes for 5 times. The 50 evaluation assembly trajectories (omitting the approach phase) are plotted in Fig. 9.18. All algorithms are
terminated early due to the large contact force and jamming [18]. However, our
algorithm can explore two different kinds of strategies to obtain a higher cumulative
reward. One strategy learned by our algorithm (.O = 2) can achieve the same insertion depth with fewer time steps (Fig. 9.18b), and another strategy learned by our
algorithm (.O = 8) can explore to achieve the deeper insertion depth with a suitable
assembly action so that the assembly force will not exceed the safe boundary (see
Fig. 9.18c). Similarly, the action during one episode of all algorithms is shown in

Fig. 9.18 50 evaluation assembly trajectories (comparison 2). a 3D path. b First assembly strategy.
c Second assembly strategy

Fig. 9.19 Action during one episode of all algorithms (comparison 2)

## [Book2025 PDF p.216] Page 216

202

9 LFE: Hierarchical RL Method for PiH Assembly

Fig. 9.19, and the better exploration of our algorithm is clearly depicted. The force
of DDPG and our algorithm (.O = 8) during 50 evaluation assembly trajectories is
plotted in Figs. 9.20 and 9.21.

Fig. 9.20 Assembly force of DDPG during evaluation stage (comparison 2)

Fig. 9.21 Assembly force of our algorithm (.O = 8) during evaluation stage (comparison 2)

## [Book2025 PDF p.217] Page 217

References

203

9.5 Conclusion
This chapter presents a data-efficient HRL framework for high-dimensional continuous control tasks. The hierarchical policy is learned through optimizing higher-level
policy and lower-level policies from the same samples. Our algorithm has achieved
outstanding data-efficient performance on four MuJoCo tasks and a robotic assembly
simulation. The effectiveness is also demonstrated on a real-world robotic dual PiH
assembly task.

References
1. Webots r2019a (2019). https://www.cyberbotics.com/webots
2. O. Anschel, N. Baram, N. Shimkin, Averaged-dqn: variance reduction and stabilization for
deep reinforcement learning, in Proceedings of the 34th International Conference on Machine
Learning, JMLR. org, vol. 70, pp. 176–185 (2017)
3. P.L. Bacon, J. Harb, D. Precup, The option-critic architecture, in Proceedings of the Thirty-First
AAAI Conference on Artificial Intelligence, AAAI Press, AAAI’17, pp. 1726–1734 (2017)
4. G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman, J. Tang, W. Zaremba, A
toolkit for developing and comparing reinforcement learning algorithms (2016). https://gym.
openai.com/. arXiv:1606.01540
5. T. Degris, M. White, R.S. Sutton, Off-policy actor-critic, in Proceedings of the 29th International Conference on International Conference on Machine Learning, Omnipress, Madison,
WI, USA, ICML’12, pp. 179–186 (2012)
6. S. Fujimoto, H. van Hoof, D. Meger, Addressing function approximation error in actor-critic
methods, in Proceedings of the 35th International Conference on Machine Learning, PMLR,
Stockholmsmässan, Stockholm Sweden, Proceedings of Machine Learning Research, ed. by J.
Dy, A. Krause, vol. 80, pp 1587–1596 (2018)
7. T. Haarnoja, A. Zhou, P. Abbeel, S. Levine, Soft actor-critic: off-policy maximum entropy
deep reinforcement learning with a stochastic actor, in Proceedings of the 35th International
Conference on Machine Learning, PMLR, Proceedings of Machine Learning Research, ed. by
J. Dy, A. Krause, vol. 80, pp. 1861–1870 (2018)
8. M. Janner, J. Fu, M. Zhang, S. Levine, When to trust your model: model-based policy optimization, in Advances in Neural Information Processing Systems, pp. 12519–12530 (2019)
9. D.P. Kingma, J. Ba, Adam: a method for stochastic optimization, in 3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings ed. by Y. Bengio, Y. LeCun (2015). http://arxiv.org/abs/1412.6980
10. S. Li, R. Wang, M. Tang, C. Zhang, Hierarchical reinforcement learning with advantage-based
auxiliary rewards, in Advances in Neural Information Processing Systems (2019), pp. 1407–
1417
11. T.P. Lillicrap, J.J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver, D. Wierstra, Continuous control with deep reinforcement learning, in ICLR (2016)
12. V. Mnih, K. Kavukcuoglu, D. Silver, A.A. Rusu, J. Veness, M.G. Bellemare, A. Graves, M.
Riedmiller, A.K. Fidjeland, G. Ostrovski et al., Human-level control through deep reinforcement learning. Nature 518(7540), 529 (2015)
13. O. Nachum, S.S. Gu, H. Lee, S. Levine, Data-efficient hierarchical reinforcement learning,
in Advances in Neural Information Processing Systems 31: Annual Conference on Neural
Information Processing Systems 2018, NeurIPS 2018, December 3–8, 2018, Montréal, Canada,
vol. 31, pp. 3307–3317 (2018)

## [Book2025 PDF p.218] Page 218

204

9 LFE: Hierarchical RL Method for PiH Assembly

14. D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, M. Riedmiller, Deterministic policy
gradient algorithms, in Proceedings of the 31st International Conference on International
Conference on Machine Learning, JMLR, ICML’14, vol. 32, pp. I–387–I–395 (2014)
15. E. Todorov, T. Erez, Y. Tassa, Mujoco: a physics engine for model-based control, in 2012
IEEE/RSJ International Conference on Intelligent Robots and Systems, IEEE (2012), pp. 5026–
5033
16. P. Varin, L. Grossman, S. Kuindersma, A comparison of action spaces for learning manipulation
tasks, in 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems, IROS
2019, Macau, SAR, China, November 3–8, 2019. (IEEE, 2019), pp. 6015–6021
17. A.S. Vezhnevets, S. Osindero, T. Schaul, N. Heess, M. Jaderberg, D. Silver, K. Kavukcuoglu,
Feudal networks for hierarchical reinforcement learning, in International Conference on
Machine Learning, PMLR, pp. 3540–3549 (2017)
18. K. Zhang, J. Xu, H. Chen, J. Zhao, K. Chen, Jamming analysis and force control for flexible
dual peg-in-hole assembly. IEEE Trans. Ind. Electr. 66(3), 1930–1939 (2019). https://doi.org/
10.1109/TIE.2018.2838069
19. S. Zhang, S. Whiteson, Dac: the double actor-critic architecture for learning options, in
Advances in Neural Information Processing Systems, pp. 2012–2022 (2019)

## [Book2025 PDF p.219] Page 219

Chapter 10

LFE: Hierarchical Compliance Control
for PiH Assembly

10.1 Introduction
Impedance controllers can generate compliant behaviors to adapt to the contact
forces. RL methods with the impedance action space can acquire the compliance
of force and motion for contact-rich interactive control [2, 16, 25]. However, the
compliance at the task level to obtain the robotic generalizable skills for a family of
tasks with multiple objectives is still underexplored.
Context-based representation leverages a context variable to define a family of
tasks [22], which has been exploited in multi-task RL methods [12]. For instance,
Fig. 10.1 illustrates an object pushing task, and the robot needs to push an object
from the initial position to the target position as quickly as possible without tipping
it over [10, 23]. The object pushing tasks with multiple goal positions can be represented by a context variable. Different goal positions in the task space demand that
the robot follows different trajectories and behaves at different impedance. Generalizing across various contexts is crucial for robotics applications as it eliminates
the need for additional training on unseen tasks. In the field of multi-task learning,
Contextual Policy Search (CPS) is commonly adopted as the higher-level policy
to optimize a context-conditioned parameterized lower-level controller [11]. DMPs
have been extensively used as the lower-level controllers to regulate robot trajectories
for trajectory-shaping-based tasks (e.g., robot throwing and playing table tennis) [12].
However, DMP-based CPS approaches have limitations in addressing contact-rich
manipulation tasks, which require the proper balance between motion regulation and
compliance assignation.
This chapter presents a HC-CPS to solve the contact-rich manipulation tasks with
multiple objectives. Our primary motivation is that the RL-based lower-level policy
can learn the compliant skills to regulate the reference motion and corresponding
impedance jointly. Moreover, the higher-level contextual policy can optimize the
context-conditioned parameters to regulate the lower-level policy for multiple task
objectives. However, in contrast to DMPs with fixed policy structures, HC-CPS has
© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_10

205

## [Book2025 PDF p.220] Page 220

206

10 LFE: Hierarchical Compliance Control for PiH Assembly

Fig. 10.1 Robotic object
pushing tasks

two challenges: first, lower-level policy needs to learn the policy representation and
its parameters simultaneously; second, the higher-level contextual policy needs to
optimize the high-dimensional parameters of the lower-level policy. We leverage the
impedance-conditioned RL with parameterized action space to achieve the trade-off
between learning the policy representation by RL and providing the impedanceconditioned action space to be regulated by higher-level contextual policy.
Learning such hierarchical compliance-based contextual policy is also highly
time-consuming due to two challenges. First, the continuous context-conditioned
impedance parameters increase the difficulty of learning lower-level impedanceconditioned RL policy because the existing off-policy scheme [2, 16, 23] may exacerbate the bootstrapping errors [27]. Moreover, this issue cannot be solved by existing correction methods used in HRL with discrete latent variables [17]. Second, the
lower-level impedance-conditioned RL policy will enable contextual policy learning
to rely on the off-policy evaluation [22]. In particular, the reward bias will introduce instability in updating contextual policy. Model-based CPS can mitigate the
instability and improve the data efficiency by augmenting artificial samples [12].
The performance strongly depends on the estimated forward model [11]. Compared
to trajectory-shaping-based tasks, the forward model for contact-rich manipulation
tasks includes the transition of contact force [10]. It increases the difficulty of learning
a feasible forward model with high data efficiency. Hence, it is necessary to leverage
the previous samples collected from different objectives for the forward model learning. The HC-CPS approach and its practicality benefit from two main contributions.
First, the hierarchical compliance-based contextual policy is formulated by:
1. The parameterized impedance-conditioned action space is first proposed, which
can combine with any off-policy RL algorithms as the lower-level policy to search
the policy presentation for reference motion generation and impedance adaptation.

## [Book2025 PDF p.221] Page 221

10.1 Introduction

207

2. By selecting proper impedance parameters, the parameter space reduction enables
the higher-level contextual policy to be learned efficiently for task generalization.
Second, we further improve the data-efficiency of learning the hierarchical
compliance-based contextual policy by:
1. A variational encoder-decoder model learns the underlying constraints introduced
by context-conditioned impedance over the actions to mitigate the accumulation
of bootstrapping errors during lower-level off-policy learning. The learned underlying constraints can force the lower-level impedance-conditioned RL policy to
select the actions from similar impedance parameters.
2. To generate the artificial samples for higher-level contextual policy data-efficient
learning, we propose a composite forward model for contact-rich manipulation
tasks, including a pose and a force model. A Gaussian mixture regression-based
Gaussian process (GMR-GP) function is adopted to fit the forward model. GMR
can encapsulate the variability of impedance-conditioned trajectories into the
forward prediction with reduced reward bias.

10.1.1 Related Work
RL [21] and optimal control [20] are two important approaches to solve the sequential
decision-making problems [26], which involves a wide range of real robotic applications [11]. In the field of control theory, the linear and non-linear control systems
have been solved with various solutions by exploring the knowledge of the system
dynamics, uncertainties, and constraints [4]. However, the optimal control depends
on the strong guarantees of the model since the form of the model and cost function
are vital to obtaining the solution. In recent years, RL methods have successfully
addressed a wide range of complicated robotic problems, which are analytically
intractable such as contact-rich manipulation tasks. RL can learn the control policy
by interacting with the environment iteratively [24]. Moreover, the mutual specification of problem constraints is not required. For instance, the reformulation of action
space has promoted the RL methods to learn the policies for the diverse control
tasks with higher data efficiency [3, 16, 23]. Additionally, policy search is a group
of RL methods [5], which has been widely employed in robotic control problems
because the domain knowledge of the policy representation and the initialization can
be integrated naturally [11]. However, most existing CPS methods aim to address
the trajectory shaping tasks by combining with DMPs [12].
In contrast to DMP-based CPS [11, 12], integrating HC-CPS with RL policies
is not a straightforward task. The challenge lies in defining the structure of the
lower-level policy and identifying which parameters to learn. Additionally, learning
a hierarchical policy is always a complex endeavor. It is important to highlight that
HC-CPS and existing HRL approaches tackle distinct problems. [17]. HRL focuses
on exploring over temporally extended periods to improve the data efficiency for
addressing a single task. However, HC-CPS aims to obtain the generalization across

## [Book2025 PDF p.222] Page 222

208

10 LFE: Hierarchical Compliance Control for PiH Assembly

a family of tasks represented by a context variable. The higher-level policy in HRL
has the same state space as the lower-lever policy. The CPS approach is to learn the
mapping function from context space to a parameterized lower-level controller [11].
The lower-level impedance-conditioned RL policy learning in HC-CPS needs to
mitigate the impacts of the continuous high-dimensional impedance parameters.
The existing correction methods to relabel the stored transitions are only effective
for HRL methods with sub-goals and discrete latent variables [17].
Relative entropy policy search (REPS) has been explored to update the contextual
policy [19]. A model-based REPS approach named GP-REPS has demonstrated the
high data efficiency performance in several trajectory-shaping-based tasks [11, 12].
Probabilistic forward model learning has been extensively developed for modelbased policy search [13]. However, the forward model for real-world manipulation tasks is more demanding of high data efficiency and low long-term prediction
error [15]. The GP model has shown superior data-efficiency performance in a low
data regime [15]. However, in HC-CPS, the samples for the forward model learning are collected from different objectives. It is crucial to capture the variability
induced by context-conditioned impedance parameters. In [9], GMR was employed
to estimate a corrected prior mean for the GP model, which can capture the variability of demonstrations for trajectory reproduction. To reduce the long-term error
of reward prediction, a hybrid forward model for contact-rich tasks was proposed
to connect several discontinuous local GP models [10]. The states for manipulation
tasks usually include diverse sensor modalities [13], e.g., pose and force. The estimated forward model may become less smooth since a slight position change may
dramatically change the force. The small number of training data will further exaggerate the effect. Instead of learning an end-to-end hybrid forward model [9, 10],
we propose a composite forward model to decouple the pose and force relation. The
composite forward model enables the forward model learning to be smooth.

10.2 Method
10.2.1 Preliminaries
The control problems addressed by RL generally can be formulated as a MDP as
described in Sect. 1.3.5. By contrast, the tasks with multiple objectives are formulated
as Contextual Markov Decision Process [12], a tuple .< Z, S, A, M, P0 , γ >, .Z is
the context space to represent a family of tasks. .M is a mapping function from the
context . z ∈ Z to the MDP parameters .Mz = {Rz , T z }. A family of MDPs is defined
by context . z, and each MDP can share the state space .S. Different contexts result
in different task objectives and require varied compliant skills. Therefore, the agent
of MDP .Mz with context . z only has access to a partial state space .Sz and reward
space .Rz .

## [Book2025 PDF p.223] Page 223

10.2 Method

209

Fig. 10.2 Schematic of HC-CPS

The schematic of learning the proposed HC-CPS is shown in Fig. 10.2. Similar to
the standard CPS approach, the robotic tasks are assumed to be episodic tasks [11, 12].
The lower-level impedance-conditioned RL policy is updated every.Tu time steps, and
the higher-level contextual policy is updated every. N episodes. For.i−th episode with
an initial state .s0 ∈ P0 (s0 ), the robot observes a context . z i . In practice, the context
is sampled from a context distribution . z i ∼ μ(z). The higher-level contextual policy
.π(ω|z) is defined to generate the impedance parameters .ωi ∈  for the lower-level
impedance-conditioned RL policy .π(a|s, ωi ). . is the impedance parameter space.
At time step .t, the state .st ∈ S is observed and the agent selects an action .at ∈ A
from .π(at |st , ωi ). A reward .rt+1 is received to evaluate the state-action pair, and
the environment transits to the next state .st+1 with the probability .T z (st+1 |at , st ).
The hierarchical compliance-based contextual policy is formulated as .π(a|s, z) =

∗
ω∈ π(ω|z)π(a|s, ω). The optimal policy .π can be obtained by maximizing the
expected return:
π ∗ = argmax J (π )
π

subject to z ∼ μ(z), s0 ∼ P0 (s0 ), ωi ∼ π(·|z), ωi ∈ ,
at ∼ π(·|st , ωi ), at ∈ A,
.

st+1 ∼ T z (·|st , at ), st+1 ∈ S, rt+1 ∈ R
 
J (π ) = E[Rω,z ] =
μ(z)π(ω|z)Rω,z d zdω
  
=
μ(z)π(ω|z)P(τ |ω, z)R(τ , z)dτ d zdω

(10.1)

## [Book2025 PDF p.224] Page 224

210

10 LFE: Hierarchical Compliance Control for PiH Assembly

where .τ = {s0 , a0 , · · · , sT } is a sampled trajectory with the probability of .P(τ |ω, z).
It depends on the lower-level impedance-conditioned RL policy and the environment
dynamics:
T
−1
.P(τ |ω, z) = P0 (s0 )
π(at |st , ω)T z (st+1 |st , at )
(10.2)
t=0

T
where. R(τ , z) = i=1
ri is the corresponding sampled trajectory-dependent episodic
reward given the context . z. The lower-level impedance-conditioned RL policy and
higher-level contextual policy are approximated by a NN and a linear Gaussian
function, parameterized as .π(a|s, ω; θ ) and .π(ω|z; φ), respectively. The hierarchical policy learning in Eq. 10.1 can be considered as an optimization problem, .π ∗
with .φ ∗ and .θ ∗ can be obtained by maximizing the approximated objective function
.J (φ, θ ). The implementation of the proposed HC-CPS is described in Algorithm 1.

10.2.2 Lower-Level Impedance-Conditioned RL Policy
Learning
With the proper impedance-conditioned action space, the commonly used off-policy
RL methods for robotic tasks, e.g., DDPG [14], Soft Actor-Critic (SAC) [7], and
TD3 [6] can be applied to learn the lower-level impedance-conditioned RL policy.
This chapter mainly considers the current state-of-the-art off-policy RL methods,
SAC and TD3. The off-policy RL methods mentioned above are built on actor-critic
architecture. The architecture of learning the lower-level impedance-conditioned RL
policy by TD3 and SAC is depicted in Fig. 10.3. The actor and critic networks can

Fig. 10.3 Lower-level impedance-conditioned RL policy learning by TD3 and SAC

## [Book2025 PDF p.225] Page 225

10.2 Method

211

be updated via a similar scheme. The same training techniques can be applied to
address the overestimation and extrapolation error of the critic networks [8].
A replay buffer .D L stores the transitions from the lower-level impedanceconditioned RL policy induced by different context-conditioned impedance. At each
training step (every .Tu time step), a mini-batch .(si , ai , ri+1 , si+1 ) ∈ B L is uniformly
and randomly sampled from .D L . The mini-batch loss of learning the critic networks
is defined as follows:

2 
YiL − Q L (si , ai |ξ ) , ξ ∈ (ξ 1 , ξ 2 )
.Lc = E(si ,ai ,ri+1 ,si+1 )∼B L
(10.3)
where the target value .YiL is calculated as .ri+1 +γ L min j=1,2 Q L (si+1 , π(·|si+1 , ·;
2
.θ ) + ς |ξ̄ j ). .ς is clipped Gaussian noise sampled from .ς ∼ clip(N(0, σc ),
−c, +c). The practical technique in [6] is applied to resolve the overestimation issue
by selecting a minimum value between two critics. The critic networks can be optimized by performing the gradient descent step on the .Lc with respect to .ξ 1 , ξ 2 . With
the estimated critic network, for policy improvement by TD3, the policy gradient
with respect to the parameters of the actor networks .θ is computed as follows:
∇θ J (θ , ξ ) = EBL ∇θ π(·|si ; θ )∇a Q L (si , a|ξ )|a=π(·|si ;θ)

.

(10.4)

In actor-critic-based RL methods, such as DDPG [14], TD3 [6], and SAC [7], the
extrapolation error often exists in critic networks learning. If the out-of-distribution
action .π(·|si+1 , ·; θ ) enables the state-action .(si+1 , π(·|si+1 , ·; θ )) to be not in the
replay buffer .D L , the . Q L (si+1 , π(·|si+1 , ·; θ )) cannot provide accurate policy evaluation. The impedance-conditioned RL policy is not directly outputting the assembly
action .a ∈ A, a constrained MDP .< S, Ā, R, T̄ , P0 , γ > is introduced with a reference action space .Ā and a new transition function .T̄ : .S × Ā → S. The actor
network formed by .ā = π(ā|s, ·; θ ) is adopted to generate the agent action. The
mapping function . f (a|s, ā; ω) from reference action space .Ā to original action
space .A (assembly action) is built on top of the impedance controllers. The details
of two mapping functions . f (a|s, ā; ω) will be given in Sect. 10.3. Most importantly,
the impedance parameters .ω ∈  will exacerbate the extrapolation error for critic
network training.
The motivation for mitigating the extrapolation error introduced by impedanceconditioned action space is to constrain the underlying relation conditioned by
impedance parameters between the agent action and actuation action. We leverage
a encoder-decoder model to learn an latent representation of assembly action and
impedance parameters .[a, ω] (see Fig. 10.2). A NN . E θe encodes the input assembly action and impedance parameter conditioned by state .s into a latent space as
.ā ∼ E θe ([a, ω], s). The latent space can implicitly constrain the policy to generate
the actuation actions based on the agent actions following the possible contextconditioned impedance. A decoder NN .[a, ω] ∼ Dθd (ā, s) is adopted to reconstruct

## [Book2025 PDF p.226] Page 226

212

10 LFE: Hierarchical Compliance Control for PiH Assembly

the assembly action from the latent space. According to the normal Variational
Auto-Encoder (VAE) [1, 27] learning, the loss to train the encoder and decoder
networks is given by:
Le (s, a,ω, ā; θ e , θ d ) = βr ec ||[a, ω] − Dθd (s, E θ e ([a, ω], s))||22
.

+ βim ||ā − E θ e ([a, ω], s)||22
+ β K L KL(N(μ([a, ω]; θ e ), σ ([a, ω]; θ e ))||N(0, 1))

(10.5)

where . K L loss enables the encoder to learn a smooth distribution in latent space.
β , β , and .β K L are adopted to control the weights of each loss. After the encoder
and decoder networks are trained by the samples in .D L , the learned decoder is
applied to generate the .[at+1 , ωt+1 ] = Dθd (st+1 , āt+1 ) for Eq. 10.3. .āt+1 is sampled
from the current actor network. The VAE model holds the promise to improve the
data efficiency as it can also be trained on an offline dataset collected by expert RL
policies.

. r ec . im

10.2.3 Higher-Level Contextual Policy Learning
The optimal higher-level contextual policy can be obtained by maximizing the revised
objective, as follows:
.

π ∗ (ω|z) = argmaxπ E z∼μ(·),ω∼ π(ω|z)R z,ω
R z,ω = E z∼P(z|ω,z) [R(z, z)|ω, z]

(10.6)

where .μ(z) is the estimated context distribution. . Rω,z is estimated by the generated
trajectories given the impedance parameter .ω in context . z. On top of the CPS [12,
22], the higher-level contextual policy is considered as a conditional model . pφ (ω|z)
with parameter .φ. A parametric objective is given as follows:
.

J (φ) = Ez∼μ(·),ω∼ [ pφ (ω|z)μ(z)Rz,ω ]

(10.7)

At each iteration, the current contextual policy is evaluated for . N times. All realistic
NT
generated from a family of MDPs .T z are stored in
transitions .{si , ai , ri+1 , si+1 }i=1
the lower-level replay buffer .D L . Instead of calculating the objective in Eq. 10.7 by
N
, the GMR-GP forward model can
the samples of one iteration .{z k , ωk , Rzk ,ωk }k=1
be estimated to capture the variability of all previous samples in .D L . The estimated
forward model .T (·|·) can generate a large number of artificial trajectories . Nsim  N
and store them in the higher-level replay buffer .D H . The higher-level contextual
policy is optimized by the sampled artificial trajectories with the same update law

## [Book2025 PDF p.227] Page 227

10.2 Method

213

sim
as REPS. For each sample .{z j , ω j } Nj=1
, the episodic reward is calculated over . L
simulated trajectories, as follows:

1
. R z j ,ω j =
L

L

[ R(τ l , z j )|z j , ω j ], j = 1, · · · , Nsim

(10.8)

l

where . R(τ l , z j ) is the simulated episodic reward yielded by the current lower-level
impedance-conditioned RL policy and estimated forward model .T (·|·).

Algorithm 1 HC-CPS
1: Input: number of contextual policy update . K ; execution episodes . N ; artificial episodes . Nsim ;
M
number of rollouts . L; size of replay buffer .D N
H , .D H and .D L ; upper bound . ;
2: Initialize: .π(·|s, ω; θ ), .π(ω|z; φ), . Q L (s, a; ξ i=1,2 )
3: for .k = 0, · · · , K do
4: for .i = 0, · · · , N do
5:
Environment reset, observe context . zi ∼ μ(z) and obtain parameter .ωi ∼ π(ω|z i : φ)
6:
while not done do
Observe state .st
7:
8:
Select action .āt by .π(·|st , ωi ; θ) + Nt
9:
Obtain robot control command .at by Eq. 10.12
10:
Execute .at , calculate reward .rt+1 by Eq. 10.14
11:
Transit to next state .st+1
12:
Store transition .(st , āt , at , st+1 , rt+1 , ωi ) in .D L
13:
if .t mod .Tu then
14:
Update critic networks and lower-level impedance-conditioned RL policy.π(ā|s, ω; θ)
with .D L by Eqs. 10.3, 10.4 and 10.5
15:
end if
end while
16:
17:
Store transition .(zi , ωi , R zi ,ωi ) in .D N
H
18: end for
19: Fit composite forward model with .D L by Eqs. 10.17–10.21
20: Estimate context distribution .μ(z) with .D N
H
21: for . j = 0, · · · , Nsim do
22:
Sample context .z j ∼ μ(z)
23:
Sample parameters .ω j ∼ π(ω|z j ; φ)
24:
Generate . L artificial trajectories following Sect. 10.4.1; compute reward . Rz j ,ω j by
Eqs. 10.8 and 10.13
25:
Store transition .(z j , ω j , Rz j ,ω j ) in .D M
H
26: end for
27: Update .π(ω|z; φ) with .D M
H by REPS
28: end for

## [Book2025 PDF p.228] Page 228

214

10 LFE: Hierarchical Compliance Control for PiH Assembly

10.3 Impedance-Conditioned Action Space
We introduce the two kinds of parameterized impedance-conditioned action space,
combining current state-of-the-art RL methods as the lower-level policies for torquecontrolled and position-controlled robots, respectively.

10.3.1 Torque-Controlled Robots
This section mainly considers the commonly used 7-DoF collaborative robots for
flexible manipulation tasks. The assembly action.a ∈ R7 for torque-controlled robots
is the joint torque .τ q ∈ R7 . The reference action .ā ∈ Ā is the desired pose . x e ∈ R6
in task space or end-effector space. The state .s ∈ S consists of the robot-related state
.sr , e.g., joint angles and velocity, and task-dependent state .se , e.g., contact force. For
instance, the robot-related state .sr = [x t , ẋ t ] includes the real-time pose . x t ∈ R6 of
end-effector and corresponding velocity . ẋ t ∈ R6 . The details of mapping function
. f (τ q |s, x e ; ω = {K p , Kd }) can refer to the task-space impedance controllers [16,
23]. In practice, only the stiffness .K p ∈ R6 is derived from the learned impedance
parameter.ω, the damping.Kd ∈ R6 is derived from stiffness with a fixed relation [25].
The two manipulation tasks in [23] are extended to multiple objectives (see Fig. 10.4).
Additionally, another challenging wiping task has not been addressed by existing
RL methods [16]. We extend the wiping task to multiple objectives, the friction
coefficient of the table in the .x − y plane is selected as the context variable. All
context variables are assumed to be subject to uniform distributions. The goal pose
is selected as the context for object pushing tasks (see Fig. 10.1); the hole pose is
selected as the context for PiH tasks (see Fig. 10.5).

Fig. 10.4 Simulated manipulation tasks on MuJoCo from left to right: pushing, PiH assembly,
wiping

Fig. 10.5 PiH assembly with different hole poses

## [Book2025 PDF p.229] Page 229

10.3 Impedance-Conditioned Action Space

215

10.3.2 Position-Controlled Robots
This section mainly considers the commonly used 6-DoF rigid manipulators for
industrial applications, which run on position control given the desired joint angle
6
. q e ∈ R . The dual PiH assembly is taken as an example, as illustrated in Fig. 9.7.
Similarly to the problem formulation in Sect. 7.2.1, the state space, action space,
reward function, and two kinds of contexts are defined as follows:

State Space
The state .st ∈ S consists of the pose (position/orientation) of the pegs and the
force (force/torque), as follows:
s = [ P t , O t , F t , M t ] ∈ R12

. t

p

(10.9)

y

where .st includes the position . P t = [Ptx , Pt , Ptz ] and orientation . O t =
y
f
[Otx , Ot , Otz ] of the pegs, respectively; .st includes the measured force . F t =
y
y
x
z
x
[Ft , Ft , Ft ] and torque . M t = [Mt , Mt , Mtz ] from the F/T sensor.
Action Space
The assembly action .ut includes the position and orientation variation of endeffector (see Fig. 7.1a), as follows:
u =[

. t

x
t,

y
t,

z
t,

x
t,

y
t,

z
6
t] ∈ R

(10.10)

The diagram of a proposed hybrid force-position controller is illustrated in
Fig. 10.6. A PD position controller (.Ksp ∈ R6 , Kds ∈ R6 ) is employed to reach the
f
f
target state of the peg. A PI force controller (.K p ∈ R6 , Ki ∈ R6 ) is employed to
enable the perceived contact force to follow the reference force profile. In practice,

Fig. 10.6 Hybrid force-position controller (. is Hadamard product).

## [Book2025 PDF p.230] Page 230

216

10 LFE: Hierarchical Compliance Control for PiH Assembly

to reduce the complexity and maintain the stable behaviours, only the proportional
f
gain .Ksp and .K p are selected as the impedance parameter .ω to learn [2, 25]. The
f
corresponding .Kds and .Ki are set according to a prior relationship with the proporf
s
tional gain .K p and .K p . The relationship is task-dependent and should be empirically
tuned. Given the impedance parameters.ω and the reference force.Fr ∈ R6 , the expert
command .uet is derived as follows:

.

uet = (Ksp  est + Kds  ėst )+

f
f
f
(1 − )(K pf  et + Ki  et dt)

(10.11)

f
est = [0, 0, de − dt , 0, 0, 0], et = Fr − Ft

= diag(λ1 , · · · , λ6 ), λ j ∈ [0, 1]
where . is the Hadamard (element-wise) product and . is the selection matrix to
determine the degree of control that each controller contribute to .uet .
The objective of the dual PiH assembly is to complete the task successfully with
the minimum of assembly steps and reduce the contact force. Therefore, . is set
as .diag(0, 0, 1, 0, 0, 0). The position control is required for the translation along
the axis-.z to reach the desired insertion depth because the desired states for other
components are unknown. For the other five components in Fig. 7.1(b), the force
controller can regulate
the contact force to track the reference force profile. Moreover,

f
f
we set .Kds = 2 Ksp , Ki = 0.01K p . .est only includes the position error between
f
the desired insertion depth .de and the current insertion depth .dt . .et is the error
between the desired reference force .Fr = [0, 0, −50, 0, 0, 0] and the measured force
6
.Ft = [F t , M t ] ∈ R . The assembly action . ut is calculated as follows:
ut = sat(āt )  uet + uet
.

sat(āt ) : R6 → R6 , sat(āt ) = [sat(āt0 , · · · , sat(āt5 ))]T

(10.12)

sat(āti ) = sign(āti )min{b, |āti |},i = 0, · · · , 5
where.āt ∈ A = [−1, 1]6 is the agent action from actor network..sat(·) is the elementwise saturation function and.b < 1 is used to restrict the agent action.āt into.[−b, b]6 .
Specifically, as shown in Fig. 10.6, the desired pose . x e ∈ R6 is computed based on
e
6
.at and . ut . Afterwards, the desired joint angle . q e ∈ R is computed by . x e depending
on the inverse kinematics. Finally, to track the desired joint angle .q e , the joint torque
6
.τ q ∈ R is derived based on the inner-loop torque control.

## [Book2025 PDF p.231] Page 231

10.4 Composite Forward Model Learning

217

Reward Function
Given impedance parameter .ω and context . z, the episodic reward function . R(τ |ω, z)
for higher-level contextual policy training is designed as follows:
.

R(τ |ω, z) = c1

(st ) =

.

dT
kT
− c2
− c3 (st ) − c4
de
ke

at at

(10.13)

t

1, done = True and safe = True
−1, safe = False

(10.14)

where
first term is to minimize the distance from final insertion depth .dT =
T the
z
to
the desired insertion depth .de ; the second term is to encourage the
t=1 t
minimum number of assembly steps;.k T is the final number of assembly steps and.ke is
the desired maximal number of assembly steps; the third term .(st ) is to penalize the
large force signals and encourage the successful completion, as shown in Eq. 10.14;
the fourth term is to encourage the energy-efficient assembly action. .c1 , .c2 , .c3 , and .c4
are utilized to balance the weight of each term. The dense reward function is given
to evaluate the performance at each time step, as follows:

r =

. t

⎧ z
1
⎪
t
⎪
⎪
⎨ de − ke , done = False and safe = True
⎪
⎪
⎪
⎩

1, done = True and safe = True
−1, safe = False

(10.15)

Context Space
The desired insertion depth .de and desired number of assembly steps .ke are selected
as the context variable. The tasks with different contexts will result in different reward
functions (see Eqs. 10.14 and 10.13). The previous RL approaches [2, 16] have to
retrain the policy under each specific objective. Otherwise, the task with a deeper
desired insertion depth requires more assembly steps.

10.4 Composite Forward Model Learning
The composite forward model is estimated for higher-level contextual policy learning. It is separated as a force model and a pose model, which are then fitted by
GMR-GP.

## [Book2025 PDF p.232] Page 232

218

10 LFE: Hierarchical Compliance Control for PiH Assembly

10.4.1 Composite Forward Model
A discrete-time stochastic forward model is defined as:
s

. t+1

= T (st , at ) + ς

(10.16)

where .ς ∼ N(0, σ 2ς ) is the zero-mean Gaussian noise. The transition function .T is
assumed to be expressed by two different Gaussian processes. We take the dual PiH
assembly to demonstrate the implementation of our forward model. The state .st for
manipulation tasks usually includes the pose and the force. Instead of estimating a
mapping function, the proposed composite forward model decouples the pose and
force relations with two separated models. Based on the quasi-static assumption and
jamming analysis [18], a contact force model is trained to estimate the peg-hole conp
f
tact situation, which estimates the relationship between the pose .st and force .st . The
p
p
p
f
f
f
input data of the force model is. X f = [s1 , s2 , . . . , s N ], while.Y f = [s1 , s2 , . . . , s N ]
is taken as the target output of the training data. A pose model is trained to estimate the
kinematic motion law of the robot end-effector under environmental constraints. The
p
pose model takes . X p = [x 1 , x 2 , . . . , x N ] as the input data where . x t = [st , at ] ;
and the target output of the pose model is converted into the pose differences of two
p
p
p
p
p
p
time steps as .Y p = [ 1 , 2 , . . . , N ], t = st+1 − st . However, the force usually changes dramatically in contact-rich tasks. And we find that this normalization
cannot be applied in the force model simultaneously.
The estimated forward model can generate the artificial trajectories following the
instruction in Fig. 10.7, and the expected episodic reward is accordingly calculated by
Eqs. 10.13 and 10.14. To generate an artificial trajectory, at each forward prediction
step, the pose model takes the state .st and assembly action .at as input and outputs the
p
p
next pose .st+1 . The force model takes the next pose .st+1 as input to calculate the next
f
force .st+1 . Then, the simulated reward .rt+1 is calculated according to Eq. 10.14, and
the next assembly action.at+1 is sampled from the lower-level impedance-conditioned
RL policy .π(a|s, ω).

Fig. 10.7 Schematic of
forward prediction by
composite forward model

## [Book2025 PDF p.233] Page 233

10.4 Composite Forward Model Learning

219

10.4.2 GMR-GP
Following the guidance in Fig. 10.7, we take the pose model as an example to introduce the forward prediction, and the force model can follow the same implementation.
The GMR-GP model for the pose model is given by:
T p (x) ∼ GP(m(x), K(x, x))
C

.

m(x) = mc (x), K(x, x) =

i (x)i ( x)

i Ki (x, x)

(10.17)

i=1

where . x is the input variable. .m(·) ∈ R D and .K(·, ·) ∈ R D×D are the prior mean
function and prior kernel function. The joint distribution of the input data and output data in replay buffer .D L is encoded by a GMM model with .C components as

C
.
i ). .ζi , . mi and . i are the prior, mean and covariance matrix of the
i=1 ζi N(mi ,
.i-th component, which can be optimized via the EM algorithm. Given a new observed
p
sample . x t = [st , at ] , the conditional mean .mc (x t ) and the conditional covariance matrices . i (x t ) in Eq. 10.17 are calculated from the conditional distribution
fitted by GMR, as follows:
C
.

mc (x t ) =


i (x t ) miY +

YX
i

X −1
(x t − miX )
i



(10.18)

i
X −1 XY
i
i


X
X
ζi N x t |mi , i
.i (x t ) = 


C
X
X
i ζi N x t |mi , i
.

i =

Y
i −

YX
i

(10.19)
(10.20)

where .Ki (x, x) and .i (x) are the separate kernel function and the responsibility of
i−th component. More details can be found in the standard GMM model fitting [9].
Given the new observed sample . x t , the one-step prediction of state difference . t
can be yielded from:

.

p(
.

t |x t ; D L ) = N(

t | m(x t ),

mt (x t ) = m (x t ) + E f [
c

(x t ); D L )
t ],

t (x t ) = varf [

t]

(10.21)

where . E f [ t ] and .varf [ t ] can be calculated with the training data in .D L following
standard GP model learning [5].

## [Book2025 PDF p.234] Page 234

220

10 LFE: Hierarchical Compliance Control for PiH Assembly

10.5 Simulation
As introduced in Sect. 10.3, 3 contact-rich manipulation tasks with multiple objectives are formulated. VICES [16] is the current most popular RL method to learn
variable impedance skills for robotic manipulation tasks, which is implemented with
SAC. For a fair comparison, the presented HC-CPS is also implemented with SAC
to learn the lower-level impedance-conditioned RL policy. Furthermore, all the tasks
mentioned above are formulated on the top of the public package RoboSuite powered
by MuJoCo physics engine. All methods are run .1 × 106 time steps with the same
hyper-parameters as [16] for lower-level RL policies training. The mean and variance
of episodic reward over five seeds are plotted in Fig. 10.8a–e. The shaded region is
half a standard deviation of the average evaluation over five trials. As shown in the
Fig. 10.8a and b, the presented HC-CPS can achieve a higher success rate in insertion
task and smaller residual error of block position than VICES-SAC [16]. Furthermore,
as shown in the Fig. 10.8c and d, the HC-CPS can solve multiple objectives with better
performance than VICES-SAC, our approach can obtain the higher episode reward
with small variance.
To further validate the impact of the encoder-decoder model, the VICES and our
approach are implemented by TD3 and SAC, which run with and without the VAE
model on the most complicated wiping task, respectively. All methods are run.1 × 106
time steps with five seeds. The mean reward and standard deviation of each method
are plotted in Fig. 10.8e and f. As shown in Fig. 10.8e, our approach learned by SAC
can perform much better than VICES-SAC. Furthermore, both our approach with
the VAE model and VICES with the VAE model can achieve higher episode reward
than the same training scheme without the VAE model. Additionally, as shown in
Fig. 10.8f, based on our implementation, we find that VICES-TD3 performs worse
than VICES-SAC, and our approach learned by SAC also performs well than TD3.
However, the encoder-decoder model can be learned with the offline data, which
means that the data from SAC could be utilized to train the encoder-decoder model
in TD3. Our approach learned by TD3 and VICES-TD3 is implemented with the VAE
model and the same training scheme without the VAE model. As shown in Fig. 10.8f,
our approach learned by TD3 with the VAE model can perform much better than
the same training scheme without the VAE model. Additionally, VICES-TD3 with
the VAE model can also perform better than VICES-TD3 without the VAE model.
Therefore, the proposed encoder-decoder model can improve the data efficiency of
the lower-level impedance-conditioned RL policy in both the proposed HC-CPS and
VICES.

## [Book2025 PDF p.235] Page 235

10.5 Simulation

221

Fig. 10.8 Performance on two manipulation tasks. a residual position error of block position on
pushing task; b success rate on insertion task; c episode reward on pushing task; d episode reward
of insertion task; e episode reward of ours-SAC and VICES-SAC on wiping task; f episode reward
of ours-TD3 and VICES-TD3 on wiping task

## [Book2025 PDF p.236] Page 236

222

10 LFE: Hierarchical Compliance Control for PiH Assembly

10.6 Experiments
10.6.1 Experimental Setup
A dual PiH assembly experimental platform is set up as shown in Fig. 10.9. A 6DOF F/T sensor (M33XX manufactured by Sunrise Instruments) is mounted on the
end-effector of an ABB IRB 1200 robot. The resolution of our F/T sensor is [0.03 N,
0.03 N, 0.11 N, 0.003 Nm, 0.003 Nm, 0.003 Nm]. The raw force data are collected
by the data acquisition card at 1000 Hz, and the raw force data are smoothed using
a moving average filter with window length 50. The pegs are mounted on the F/T
sensor, and the holes are fixed on the experimental table. The diameter of the pegs
and holes is 29.96 and 30.0 mm, respectively, and the distance between the two pegs’
axes and the two holes is 200 mm. The parameter space .ω for .K p of three translation
components (. x , y , z ) are set as [1, 3], [1, 3] (m/N), and [7, 17] (m/mm).
Furthermore, the parameter .K p of the 3 rotational components .( x , y , z ) are
all set to be 0.003 (.deg /Nm) in the search phase and to 0.0025 (.deg /Nm) in the
insert phase. The parameters .Kd and .Ki for rotational components are set to zero.
The safe boundary in Eq. 10.13 are set as [–50, 50 N] and [–5, 5 Nm] for force and
torque in Fig. 7.1a, respectively.

10.6.2 Performance of Composite Forward Model
The prediction performance is evaluated by the Root Mean Square Error (RMSE)
and Mean Standard Deviation (MSD). The pose model and force model introduced
in Sect. 10.4 are trained by three kinds of forward models (GP, GMR, and GMRGP). Additionally, a commonly used end-to-end GP model [5] is also implemented

Fig. 10.9 Robotic dual PiH assembly platform

## [Book2025 PDF p.237] Page 237

10.6 Experiments

223

Table 10.1 Comparison of forward model
y
. Ft (N)

. Ftz (N)

. Mtx (Nm)

y
. Mt (Nm)

. Mtz (Nm)

Algorithm (Dataset) RMSE MSD

RMSE MSD

RMSE MSD

RMSE MSD

RMSE MSD

RMSE MSD

GPR (.D15
L )

2.67 2.98

2.38 2.48

8.67 10.89

1.38 1.30

0.51 0.47

0.32 0.40

GPR (.D30
L )

2.86 3.59

2.50 2.63

9.34 13.30

1.41 1.39

0.51 0.49

0.33 0.47

GMR (.D15
L )

1.68 1.43

1.31 0.90

4.09 3.21

0.56 0.46

0.23 0.16

0.24 0.18

GMR (.D30
L )

2.14 1.60

1.23 0.94

5.56 5.02

0.63 0.57

0.21 0.19

0.24 0.17

GMR-GP (.D15
L )

1.57 1.45

1.13 1.29

4.08 2.60

0.33 0.73

0.21 0.50

0.22 0.56

GMR-GP (.D30
L )

1.85 1.54

1.10 1.29

4.78 2.68

0.54 0.91

0.21 0.54

0.22 0.55

GP (.D15
L ) [5]

2.81 1.19

1.70 0.91

4.28 2.14

0.60 0.20

0.53 0.13

0.22 0.10

. Ftx (N)

as the baseline. All the four forward models are trained on two datasets, .D15
L and
30
.D L , which represent the datasets including the data of 15 episodes and 30 episodes,
respectively.
The pose model performance of GMR and GMR-GP is close to that of the end-toend GP model [5]. However, as concluded in Table 10.1, compared to the GP model,
GMR-GP (.C = 15) for force model can achieve lower RMSE, while compared to
GMR (.C = 15), GMR-GP for force model has higher MSD to handle larger uncertainties. Furthermore, the similar performance is achieved on the datasets of .D30
L vs
15
.D L . Additionally, compared to the end-to-end GP model on force predicting, the
GMR-GP force model can decrease the RMSE by approximately .30% on average.
The force model is trained using the collected data of the insertion depth (5–
20 mm). In order to demonstrate the generalization of our model, at each episode,
we give a random initial displacement for the peg pose. The estimated force model
is then evaluated on the partially unseen insertion depth (12–27 mm). The measured
force data and the predicted results of the first 35 time steps are depicted in Fig. 10.10.
Compared to GMR and GP, GMR-GP shows better generalization performance on
unseen depth. Following the instruction in Fig. 10.7, the proposed composite forward
model and the end-to-end GP model are applied to simulate 20 assembly trajectories,
respectively. As depicted in Figs. 10.11 and 10.12, the sampled actual trajectories
including peg pose and measured force data are plotted as the ground truth. The
trajectories (green lines) obtained by the end-to-end GP model cannot be close to the
sampled actual trajectories. The trajectories (red lines) generated by our composite
forward model can fit the pose and force variation of the actual assembly trajectories.
Therefore, our composite forward model is more effective for HC-CPS learning in
robotics.

## [Book2025 PDF p.238] Page 238

224

10 LFE: Hierarchical Compliance Control for PiH Assembly

Fig. 10.10 Generalization comparison of force model (.x−axis is assembly steps, and . y−axis is
y
force or torque; for each model, from left to right is .{Ftx (N ), Ft (N ), Ftz (N )}; blue lines are true
values, and orange lines are the predicted trajectories with the shaded region representing variance)

Fig. 10.11 Simulated pose transitions and sampled pose transitions of 20 assembly trajectories

10.6.3 Performance of HC-CPS
We compare the performance of HC-CPS with the help of our composite forward
model (model-based version) and model-free version without using the artificial
samples.

## [Book2025 PDF p.239] Page 239

10.6 Experiments

225

Fig. 10.12 Simulated force transitions and sampled force transitions of 20 assembly trajectories

Different Desired Insertion Depths
Both model-based HC-CPS and model-free HC-CPS are run for 170 episodes.
The maximum number of steps .ke in Eq. 10.14 for one episode is set to 200. The
first 20 episodes with random exploration and non-training (shadow region) are
adopted to collect the data covering different context values .de ∈ [10mm, 30mm].
In the following 150 episodes, the higher-level contextual policy is updated every
5 episodes (. K = 30, N = 5), and at each training iteration, the higher-level contextual policy is updated with the simulated trajectories (. Nsim = 2N ). As shown in
Fig. 10.13a, in contrast to the model-free HC-CPS, model-based HC-CPS can achieve
higher normalized episodic reward (. R(τ |ω, z)/k T ) after 150 training episodes. The
assembly steps of all 170 episodes are plotted in the form of a scatterplot presented in
Fig. 10.13b. At the early training stage (the first 20 episodes in the shadow region), the
points representing assembly steps are highly dispersed as all contexts are randomly
sampled from the given range of desired insertion depth. However, the model-based
HC-CPS will degenerate to the lower-level impedance-conditioned RL policy. More
assembly steps are required to complete a single task with a greater insertion depth.
After training the higher-level contextual policy of 40 episodes, regardless of the
chosen context value, the model-based HC-CPS shows a clear trend (see red dashed
line) that the tasks are completed with a similar number of assembly steps, and the
points gradually gather in one region as shown in Fig. 10.13b.

Different Desired Number of Assembly Steps
The desired assembly steps .ke as context variable are trained with the objective of
the same desired insertion depth .de = 25mm. At each episode, a context is sam-

## [Book2025 PDF p.240] Page 240

226

10 LFE: Hierarchical Compliance Control for PiH Assembly

Fig. 10.13 Performance on different desired insertion depths. a episode reward of model-based
HC-CPS and model-free HC-CPS; b actual assembly steps (blue points: assembly successful;
green points: assembly steps exceed the limit, assembly unfinished; red points: force exceeds safety
boundary, assembly failed; red dashed line: the fitted trend of assembly steps)

Fig. 10.14 Performance on different desired number of assembly steps. a episode reward of modelbased CPS and model-free CPS; b assembly performance of a task with different desired assembly
steps; different color points represent different desired assembly steps; different color lines represent
the trend of each desired assembly steps after training

pled uniformly from the context space with four assembly steps .[ke = 100, ke =
150, ke = 200, ke = 250]. Both model-based HC-CPS and model-free HC-CPS are
run for 200 episodes. In the first 30 episodes (shadow region), the higher-level contextual policy randomly outputs the impedance parameters. After 170 episodes of
training (. K = 34, N = 5), the normalized episode reward of model-based HC-CPS
and model-free HC-CPS is plotted in Fig. 10.14a. The proposed composite forward model enables model-based HC-CPS to achieve higher episode reward than
model-free HC-CPS. As shown in Fig. 10.14b, during the first 30 episodes, the robot
reaches the desired insertion depth with a random number of assembly steps. Then,

## [Book2025 PDF p.241] Page 241

References

227

the robot can accomplish the task with fewer assembly steps since the lower-level
impedance-conditioned RL policy is learned faster than the higher-level contextual
policy. Finally, four dashed lines in Fig. 10.14b indicate the trend of the actual number of assembly steps. The learned higher-level contextual policy enables the robot
to accomplish the task with assembly steps close to the desired value.

10.7 Conclusion
A HC-CPS approach is presented to solve the robotic manipulation tasks with multiple objectives. The implementation of HC-CPS based on two kinds of lower-level
impedance-conditioned RL policies is introduced. The effectiveness of the proposed
HC-CPS is validated on three contact-rich manipulation tasks in simulation and the
real-world dual PiH assembly with two different kinds of contexts.
Some limitations can be addressed in future work to improve the capability of
addressing more robotic tasks. First, the context variable could be well- defined
to represent the task objectives. The higher-level contextual policy uses the original physical parameters directly. A promising direction is to cope with the context
through the feature extraction or other factorization approach. Second, in the context
of RL, all hierarchical policy learning methods need to struggle with the trade-off
between the higher-level policy and lower-level policy. Like all REPS-based methods, the higher-level contextual policy is sensitive to the initial policy. Therefore, in
the dual PiH assembly tasks, in order to demonstrate the performance of HC-CPS
within only 200 episodes, the lower-level RL policy should be stable by reducing the
.b in Eq. 10.12, and the impact of the encoder-decoder model will become minimal.
After a long-time of training, the lower-level RL policy can also solve quite complicated robotic problems, and a part of generalization can be obtained. However, most
successful performance is mainly validated in simulation. The impact of higher-level
contextual policy may become minimal when the lower-level RL policy is unstable.

References
1. A. Allshire, R. Martín-Martín, C. Lin, S. Manuel, S. Savarese, A. Garg, Laser: Learning a
latent action space for efficient reinforcement learning, in IEEE International Conference on
Robotics and Automation, ICRA 2021, Xi’an, China, May 30–June 5, 2021 (IEEE, 2021), pp.
6650–6656
2. C.C. Beltran-Hernandez, D. Petit, I.G. Ramirez-Alpizar, T. Nishi, S. Kikuchi, T. Matsubara et
al., Learning force control for contact-rich manipulation tasks with rigid position-controlled
robots. IEEE Robot. Autom. Lett. 5(4), 5709–5716 (2020)
3. M. Bogdanovic, M. Khadiv, L. Righetti, Learning variable impedance control for contact sensitive tasks. IEEE Robot. Autom. Lett. 5(4), 6129–6136 (2020)
4. T. Chen, A. Babanin, A. Muhammad, B. Chapron, C. Chen, Modified evolved bat algorithm of
fuzzy optimal control for complex nonlinear systems. Rom. J. Inf. Sci. Technol. 23, T28–T40
(2020)

## [Book2025 PDF p.242] Page 242

228

10 LFE: Hierarchical Compliance Control for PiH Assembly

5. M. Deisenroth, C.E. Rasmussen, PILCO: a model-based and data-efficient approach to policy
search, in Proceedings of the 28th International Conference on Machine Learning, ICML 2011,
Bellevue, Washington, USA, June 28–July 2, 2011 (Omnipress, 2011), pp. 465–472
6. S. Fujimoto, H. van Hoof, D. Meger, Addressing function approximation error in actor-critic
methods, in Proceedings of the 35th International Conference on Machine Learning, PMLR,
Stockholmsmässan, Stockholm Sweden, ed. by J. Dy, A. Krause. Proceedings of Machine Learning Research, vol. 80 (2018), pp. 1587–1596
7. T. Haarnoja, A. Zhou, P. Abbeel, S. Levine, Soft actor-critic: off-policy maximum entropy
deep reinforcement learning with a stochastic actor, in Proceedings of the 35th International
Conference on Machine Learning, PMLR, ed. by J. Dy, A. Krause. Proceedings of Machine
Learning Research, vol. 80 (2018) pp. 1861–1870
8. J. Ibarz, J. Tan, C. Finn, M. Kalakrishnan, P. Pastor, S. Levine, How to train your robot with
deep reinforcement learning: lessons we have learned. Int. J. Robot. Res. 40(4–5), 698–721
(2021)
9. N. Jaquier, D. Ginsbourger, S. Calinon, Learning from demonstration with model-based gaussian process, in 3rd Annual Conference on Robot Learning, CoRL 2019, Osaka, Japan, October 30–November 1, 2019, Proceedings, PMLR, PMLR. Proceedings of Machine Learning
Research, vol. 100 (2019), pp. 247–257
10. S.A. Khader, H. Yin, P. Falco, D. Kragic, Data-efficient model learning and prediction for
contact-rich manipulation tasks. IEEE Robot. Autom. Lett. 5(3), 4321–4328 (2020)
11. J. Kober, J.A. Bagnell, J. Peters, Reinforcement learning in robotics: a survey. Int. J. Robot.
Res. 32(11), 1238–1274 (2013)
12. A. Kupcsik, M.P. Deisenroth, J. Peters et al., Model-based contextual policy search for dataefficient generalization of robot skills. Artif. Intell. 247, 415–439 (2017)
13. S. Levine, N. Wagener, P. Abbeel, Learning contact-rich manipulation skills with guided policy
search, in 2015 IEEE International Conference on Robotics and Automation (ICRA) (2015),
pp. 156–163
14. T.P. Lillicrap, J.J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver, D. Wierstra, Continuous control with deep reinforcement learning, in ICLR (2016)
15. J. Lim, S. Ha, J. Choi, Prediction of reward functions for deep reinforcement learning via
gaussian process regression. IEEE/ASME Trans. Mechatron. 25(4), 1739–1746 (2020)
16. R. Martín-Martín, M.A. Lee, R. Gardner, S. Savarese, J. Bohg, A. Garg, Variable impedance
control in end-effector space: an action space for reinforcement learning in contact-rich tasks,
in 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems, IROS 2019,
Macau, SAR, China, November 3–8, 2019 (IEEE, 2019), pp. 1010–1017
17. O. Nachum, S.S. Gu, H. Lee, S. Levine, Data-efficient hierarchical reinforcement learning,
in Advances in Neural Information Processing Systems 31: Annual Conference on Neural
Information Processing Systems 2018, NeurIPS 2018, December 3–8, 2018, Montréal, Canada,
vol. 31 (2018), pp. 3307–3317
18. H. Park, J. Park, D.H. Lee, J.H. Park, M.H. Baeg, J.H. Bae, Compliance-based robotic peg-inhole assembly strategy without force feedback. IEEE Trans. Ind. Electron. 64(8), 6299–6309
(2017)
19. J. Peters, K. Mulling, Y. Altun, Relative entropy policy search, in Proceedings of the TwentyFourth AAAI Conference on Artificial Intelligence, AAAI 2010, Atlanta, Georgia, USA, July
11–15, 2010 (AAAI Press, 2010), pp. 1607–1612
20. S. Schaal, P. Mohajerian, A. Ijspeert, Dynamics systems versus optimal control-a unifying
view. Prog. Brain Res. 165, 425–445 (2007)
21. R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction (MIT Press, 2018)
22. S. Tosatto, G. Chalvatzaki, J. Peters, Contextual latent-movements off-policy optimization for
robotic manipulation skills, in IEEE International Conference on Robotics and Automation,
ICRA 2021, Xi’an, China, May 30–June 5, 2021 (IEEE, 2021), pp. 10815–10821
23. P. Varin, L. Grossman, S. Kuindersma, A comparison of action spaces for learning manipulation
tasks, in 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems, IROS
2019, Macau, SAR, China, November 3–8, 2019 (IEEE, 2019), pp. 6015–6021

## [Book2025 PDF p.243] Page 243

References

229

24. I.A. Zamfirache, R.E. Precup, R.C. Roman, E.M. Petriu, Policy iteration reinforcement
learning-based control using a grey wolf optimizer algorithm. Inf. Sci. 585, 162–175 (2022)
25. X. Zhang, L. Sun, Z. Kuang, M. Tomizuka, Learning variable impedance control via inverse
reinforcement learning for force-related tasks. IEEE Robot. Autom. Lett. 6(2), 2225–2232
(2021)
26. C. Zhao, C.L. Lin, W. Chen, M.K. Chen, J. Wang, Visual heart rate estimation and negative
feedback control for fitness exercise. Biomed. Signal Process. Control 56, 101680 (2020)
27. W. Zhou, S. Bajracharya, D. Held, PLAS: Latent action space for offline reinforcement learning.
CoRL, PMLR, Proc. Mach. Learn. Res. 155, 1719–1735 (2020)

## [Book2025 PDF p.244] Page 244

Chapter 11

Concluding Remarks

This monograph uses PiH assembly strategies as an entry point to study robotic
intelligent assembly. In Chap. 1, a brief introduction of PiH assembly strategies is
first presented, including the reason why this monograph selects PiH assembly as
the task. The typical PiH system is divided into manipulators, mating parts, and
sensing system. Also, the assembly strategies are divided into two aspects according
to high-level planning, namely, (i) Model-based strategies and (ii), (iii) Learningbased strategies (including (ii) LFDs and (iii) LFE).
Chapters 4 and 5 present two model-based strategies to avoid jamming in different
PiH tasks. In Chap. 4, we introduce a screw insertion method for axial friction reduction. The effect of screw motion on axial friction reduction is analyzed with point
contact and face contact. The screw insertion method in clearance-fit PiH assembly
with point contact is discussed. This method outperforms the conventional linear
insertion method for jamming prevention. The reciprocate screw insertion strategy
is also investigated to reduce the influence of axis offset on screw insertion. The
screw insertion method in interference-fit PiH assembly with face contact is discussed. The effectiveness of axial friction reduction is validated through experiments
involving point contact with screw motion and screw insertion in clearance-fit and
interference-fit PiH assemblies.
In Chap. 5, to address challenges with flexible component assembly, we employ
contact state analysis, jamming analysis, and force control strategies for dual flexible PiH assembly. We enumerate contact states during large and small deformation
stages. Additionally, we derive the relationship between forces and torques, analyze jamming states, and present control strategies. Experimental results validate the
effectiveness of our approach.
While model-based strategies offer a structured approach, they can be costly in
terms of model construction and may struggle with environmental uncertainties and
generalization to new tasks. To overcome these challenges, we further shift our focus
to learning-based strategies, which are better equipped to solve PiH assembly tasks
that pose challenges for model-based approaches.
© Huazhong University of Science and Technology Press 2025
J. Xu et al., Robotic Intelligent Assembly, Research on Intelligent Manufacturing,
https://doi.org/10.1007/978-981-96-2657-1_11

231

## [Book2025 PDF p.245] Page 245

232

11 Concluding Remarks

In Chap. 6, for hard-measuring easy-deformation assembly task, we develop an
LFD-based optimal path planning method. A real-time 3D vision sensor is used
to record the human operator assembly procedure, and an optimal assembly path
is learned and planned from the human demonstration. In addition, a GPR-based
deformation prediction and compensation method is presented to improve the robot
motion accuracy. Simulation and realistic experiment results verify that the proposed
GPR-based deformation compensation method can achieve high accuracy.
To enhance automation in the PiH assembly process and reduce dependence on
manual demonstrations, we further study LFE methods in Chaps. 7, 8, 9, and 10. The
assembly task is formulated as a MDP. In Chap. 7, a MDDPG algorithm is proposed
to accomplish the assembly task through the learned policy without analyzing the
contact states. A feedback exploration strategy is proposed to ensure that the algorithm can efficiently explore the optimal assembly policy and avoid risky actions,
which addresses the data efficiency and guarantees stability in realistic assembly
scenarios.
However, the model-free RL method relies heavily on prior knowledge and has
limited transferability to new tasks. To address these challenges, we propose a general framework in Chap. 8 that leverages prior samples stored in the replay buffer.
The assembly environment is predicted by a VTSP defined as GVFs, reducing the
unnecessary exploration. FLDVTSP-RL is proposed for assembly action control to
improve the efficiency of the RL algorithm, in which the predicted environment is
mapped to the impedance parameter in the proposed impedance action space by a
FLS
To further improve the data efficiency, a data-efficient HRL via off-policy learning
strategy is proposed in Chap. 9. Two augmented MDPs are reformulated to learn the
higher-level policy and lower-level policy from the same samples. To learn a higherlevel policy that leads to efficient exploration, a softmax gating policy is derived
to determine the lower-level policy to interact with the environment. To learn the
lower-level policies via off-policy samples from one lower-level replay buffer, the
higher-level policy derived by the option-value network is adopted to select the
appropriate option for learning the corresponding lower-level policy.
While the strategies mentioned above primarily address individual tasks, the challenge of generalization to new tasks remains. To tackle this, we introduce an HCCPS approach in Chap. 10, which enables robots to learn compliant skills for force,
motion, and task adaptation. The parameterized impedance-conditioned action space
is proposed for the lower-level policy to obtain the compliance for reference motion
regulation and contact force control. A linear Gaussian contextual policy is formulated as the higher-level policy to optimize the context-conditioned impedance
parameters for task generalization. Therefore, a family of contact-rich manipulation
tasks with multiple objectives is achieved. Furthermore, we enhance the data efficiency through two key approaches: a variation encoder-decoder model is proposed
to estimate the underlying constraints of impedance parameters relative to actions,
reducing extrapolation errors in lower-level off-policy learning; we introduce a composite forward model that generates artificial trajectories, mitigating the reward bias
in higher-level contextual policy learning.

## [Book2025 PDF p.246] Page 246

References

233

While the proposed approaches address several challenges in PiH assembly, future
work can further enhance the capability of solving more complex robotic assembly
tasks. The prediction learning methods introduced can be viewed as a means to discover robotic assembly knowledge. However, the FLS that maps learned predictions
through GVFs relies on prior task knowledge. Future efforts could focus on updating the FLS using nature-inspired parameter tuning approaches [1–3]. Additionally,
improving the safety and efficiency of applying RL methods in real-world manufacturing scenarios remains an area for exploration, such as constraining the output
through optimal input design to enhance stability and practicality. The proposed HRL
method shows promise in solving complex assembly tasks by identifying effective
sub-policies. However, the process of discovering and defining lower-level policies
remains unclear.

References
1. D. Pršić, N. Nedić, V. Stojanović, A nature inspired optimal control of pneumatic-driven parallel
robot platform. Proc. Inst. Mech. Eng. Part C: J. Mech. Eng. Sci. 231(1), 59–71 (2017)
2. V. Stojanovic, N. Nedic, A nature inspired parameter tuning approach to cascade control for
hydraulically driven parallel robot platform. J. Opt. Theory Appl. 168, 332–347 (2016)
3. V. Stojanovic, N. Nedic, D. Prsic, L. Dubonjic, V. Djordjevic, Application of cuckoo search
algorithm to constrained control problem of a parallel robot platform. Int. J. Adv. Manuf. Technol.
87(9), 2497–2507 (2016)
