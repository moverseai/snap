---
date: 2025-10-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HGG
categories: ["papers"]
tags: ["splats", "smpl", "generalized", "iccv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Learning Efficient and Generalizable Human Representation with Human Gaussian Model"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 2
---

## Learning Efficient and Generalizable Human Representation with Human Gaussian Model

> Yifan Liu, Shengjun Zhang, Chensheng Dai, Yang Chen, Hao Liu, Chen Li, Yueqi Duan

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="Simon-Dcs/Human_Gaussian_Graph" >}}

### Abstract
{{< lead >}}
Modeling animatable human avatars from videos is a long-standing and challenging problem. While conventional methods require per-instance optimization, recent feed-forward methods have been proposed to generate 3D Gaussians with a learnable network. However, these methods predict Gaussians for each frame independently, without fully capturing the relations of Gaussians from different timestamps. To address this, we propose Human Gaussian Graph to model the connection between predicted Gaussians and human SMPL mesh, so that we can leverage information from all frames to recover an animatable human representation. Specifically, the Human Gaussian Graph contains dual layers where Gaussians are the first layer nodes and mesh vertices serve as the second layer nodes. Based on this structure, we further propose the intra-node operation to aggregate various Gaussians connected to one mesh vertex, and inter-node operation to support message passing among mesh node neighbors. Experimental results on novel view synthesis and novel pose animation demonstrate the efficiency and generalization of our method.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_Learning_Efficient_and_Generalizable_Human_Representation_with_Human_Gaussian_Model_ICCV_2025_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach
{{< figure
    src="teaser.png"
    alt="Human Gaussian Graph Teaser"
    caption="Human Gaussian Graph Teaser."
    >}}

{{< figure
    src="overview.png"
    alt="Human Gaussian Graph Overview"
    caption="Human Gaussian Graph Overview."
    >}}

### Results

#### Data
{{<badge label="test" message="MVHumanNet" color="thistle" logo="github" link="https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}
{{<badge label="body--Splats" message="ExAvatar" color="steelblue" logo="github" link="https://github.com/mks0601/ExAvatar_RELEASE" target="_blank">}}

#### Performance
{{<badge label="train" message="8_x_A800" color="informational" logo="link" >}}

{{<badge label="render" message="A800" color="informational" logo="link" >}}
{{<badge label="render" message="8ms" color="informational" logo="link" >}}