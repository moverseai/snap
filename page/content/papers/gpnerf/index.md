---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GP-NeRF
categories: ["papers"]
tags: ["nerf", "smpl", "eccv22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Geometry-Guided Progressive NeRF for Generalizable
and Efficient Neural Human Rendering"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 3
---

## `GP-NeRF`: Geometry-Guided Progressive NeRF for Generalizable and Efficient Neural Human Rendering

> Mingfei Chen, Jianfeng Zhang, Xiangyu Xu, Lijuan Liu, Yujun Cai, Jiashi
Feng, Shuicheng Yan

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="sail-sg/GP-Nerf" >}}

### Abstract
{{< lead >}}
In this work we develop a generalizable and efficient Neural Radiance Field (NeRF) pipeline for high-fidelity free-viewpoint human body synthesis under settings with sparse camera views. Though existing NeRF-based methods can synthesize rather realistic details for human body, they tend to produce poor results when the input has self-occlusion, especially for unseen humans under sparse views. Moreover, these methods often require a large number of sampling points for rendering, which leads to low efficiency and limits their realworld applicability. To address these challenges, we propose a Geometry-guided Progressive NeRF (GP-NeRF). In particular, to better tackle self-occlusion, we devise a geometry-guided multi-view feature integration approach that utilizes the estimated geometry prior to integrate the incomplete information from input views and construct a complete geometry volume for the target human body. Meanwhile, for achieving higher rendering efficiency, we introduce a progressive rendering pipeline through geometry guidance, which leverages the geometric feature volume and the predicted density values to progressively reduce the number of sampling points and speed up the rendering process. Experiments on the ZJU-MoCap and THUman datasets show that our method outperforms the stateof-the-arts significantly across multiple generalization settings, while the time cost is reduced > 70% via applying our efficient progressive rendering pipeline.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2112.04312" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.png"
    alt="GP-NeRF overview"
    caption="`GP-NeRF` overview."
    >}}

{{< figure
    src="details.png"
    alt="GP-NeRF details"
    caption="`GP-NeRF` details."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="THuman" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/DeepHuman/tree/master/THUmanDataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}

#### Performance
{{<badge label="render" message="175ms" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3090" color="informational" logo="link" >}}
