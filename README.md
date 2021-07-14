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
TODO
## 评估标准
TODO
## 相关论文
1.Rethinking RGB-D Salient Object Detection:Models, Datasets, and Large-Scale Benchmarks

  基于手工特征的深度质量评估
  
  https://www.wolai.com/2MssVsDhYRShMwEMCBq842?theme=light
  
2.DPANet: Depth Potentiality-Aware Gated Attention Network for RGB-D Salient Object Detection

  在不增加训练标签（即深度质量标签）的情况下，我们建模了一个面向任务的深度潜力感知模块，它可以自适应地感知输入深度图的潜力 ，并进一步削弱由不可靠的深度信息造成的污染
  
  https://www.wolai.com/3nvkcUdL1w6oCAmE5crn5Q?theme=light
  
3.CDNet: Complementary Depth Network for RGB-D Salient Object Detection（**待商讨**）

  为了减轻低质量的深度图对RGB-DSOD的影响，选择显著性信息的深度图作为训练目标，并利用RGB特征来估计有意义的深度图。此外，为了学习鲁棒的深度特征以进行精确预测，提出了一种新的动态方案，将使用自适应   权重从原始和估计的深度图中提取的深度特征。
  
  https://www.wolai.com/7N4VUKnk1GcP3pPsA3H1vS?theme=light
  
  
## 相关代码
1.https://github.com/DengPingFan/D3NetBenchmark

2.https://github.com/JosephChenHub/DPANet

3.https://github.com/blanclist/CDNet

## 运行环境
TODO
## 实验
TODO
