---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HumanNeRF-SE
categories: ["papers"]
tags: ["nerf", "smpl", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "A Simple yet Effective Approach to Animate HumanNeRF with Diverse Poses"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 43
---

## A Simple yet Effective Approach to Animate HumanNeRF with Diverse Poses

> Caoyuan Ma, Yu-Lun Liu, Zhixiang Wang, Wu Liu, Xinchen Liu, Zheng Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="Miles629/HumanNeRF-SE" >}}

### Abstract
{{< lead >}}
We present HumanNeRF-SE, a simple yet effective method that synthesizes diverse novel pose images with simple input. Previous HumanNeRF works require a large number of optimizable parameters to fit the human images. Instead, we reload these approaches by combining explicit and implicit human representations to design both generalized rigid deformation and specific non-rigid deformation. Our key insight is that explicit shape can reduce the sampling points used to fit implicit representation, and frozen blending weights from SMPL constructing a generalized rigid deformation can effectively avoid overfitting and improve pose generalization performance. Our architecture involving both explicit and implicit representation is simple yet effective. Experiments demonstrate our model can synthesize images under arbitrary poses with few-shot input and increase the speed of synthesizing images by 15 times through a reduction in computational complexity without using any existing acceleration modules. Compared to the state-of-the-art HumanNeRF studies, HumanNeRF-SE achieves better performance with fewer learnable parameters and less training time.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2312.02232" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="HumanNeRF-SE teaser"
    caption="`HumanNeRF-SE` teaser."
    >}}

{{< figure
    src="method.png"
    alt="HumanNeRF-SE pipeline"
    caption="`HumanNeRF-SE` pipeline."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="MonoHuman" color="darkmagenta" logo="github" link="https://github.com/Yzmblog/MonoHuman" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}