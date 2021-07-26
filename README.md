# Benchmark
深度估计和深度质量评估的Benchmark

# 一些说明
所有文档均在readme填写，readme使用Markdown语言

所有资源均使用git管理

https://markdown.com.cn/  markdown教程

https://www.liaoxuefeng.com/wiki/896043488029600 git教程

## 研究计划
梳理相关论文

建立仓库，整理文档和资源

统一baseline和运行环境，评估标准，数据集

跑程序

## 数据集
该网址提供了数据集的下载链接

http://dpfan.net/d3netbenchmark/
## 评估标准
与该Benchmark保持一致

http://dpfan.net/d3netbenchmark/
## 相关论文
- D3-Rethinking RGB-D Salient Object Detection:Models, Datasets, and Large-Scale Benchmarks

  基于手工特征的深度质量评估

  https://www.wolai.com/2MssVsDhYRShMwEMCBq842?theme=light

- DPANet: Depth Potentiality-Aware Gated Attention Network for RGB-D Salient Object Detection

  在不增加训练标签（即深度质量标签）的情况下，我们建模了一个面向任务的深度潜力感知模块，它可以自适应地感知输入深度图的潜力 ，并进一步削弱由不可靠的深度信息造成的污染

  https://www.wolai.com/3nvkcUdL1w6oCAmE5crn5Q?theme=light

- CDNet: Complementary Depth Network for RGB-D Salient Object Detection（**待商讨**）

  为了减轻低质量的深度图对RGB-DSOD的影响，选择显著性信息的深度图作为训练目标，并利用RGB特征来估计有意义的深度图。此外，为了学习鲁棒的深度特征以进行精确预测，提出了一种新的动态方案，将使用自适应   权重从原始和估计的深度图中提取的深度特征。

  https://www.wolai.com/7N4VUKnk1GcP3pPsA3H1vS?theme=light

- DAS-Is Depth Really Necessary for Salient Object Detection

  在测试时不输入深度图，把深度图视为一种约束来进行SOD
  
  https://www.wolai.com/am9Tahbx9CGViVT6KF4Mru?theme=dark.
  
- SDF-Improved Saliency Detection in RGB-D Images Using Two-Phase Depth Estimation and Selective Deep Fusion

  三模态（RGB+Depth+估计深度图）（手工特征来估计深度）
  
- DQAM-Knowing Depth Quality In Advance: A Depth Quality Assessment Method For RGB-D Salient Object Detection

  深度质量评估
  
  https://www.wolai.com/5x6joGnnKCwPTh7wGv3Yqe?theme=dark
  
- W. Ji, J. Li, M. Zhang, Y. Piao, and H. Lu. Accurate rgb-d salient object detection via collaborative learning. In ECCV, 2020.

  开发一个联合学习框架实现 RGB-D SOD，利用三个组件（即，边缘检测、粗略显著性物体检测
和深度估计）联合提升 SOD 性能

- Depth Quality-Inspired Feature Manipulation for Efficient RGB-D Salient Object Detection

  利用边缘Divce系数评估深度图质量，并加入空间注意力掩膜，使用二者作为门控参数进行融合。

## 相关代码
- https://github.com/DengPingFan/D3NetBenchmark
- https://github.com/JosephChenHub/DPANet
- https://github.com/blanclist/CDNet
- [DASNet 2020 (cvteam.net)](http://cvteam.net/projects/2020/DASNet/)
- [XueHaoWang-Beijing/DQSF: Depth Quality-aware Selective Saliency Fusion for RGB-D Image Salient Object Detection (github.com)](https://github.com/XueHaoWang-Beijing/DQSF)
- https://github.com/jiwei0921/CoNet
- https://github.com/zwbx/DFM-Net.
## 运行环境
TODO
## 实验
TODO
