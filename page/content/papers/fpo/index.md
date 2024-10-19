---
date: 2022-06-21T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: FPO
categories: ["papers"]
tags: ["nerf", "deformation", "cvpr22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Fourier PlenOctrees for Dynamic Radiance Field Rendering in Real-time"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 20
---

## Fourier PlenOctrees for Dynamic Radiance Field Rendering in Real-time

> Liao Wang1∗
Jiakai Zhangi, Xinhang Liu, Fuqiang Zhao, Yanshun Zhang, Yingliang Zhang, Minye Wu, Jingyi Yu, Lan Xu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2022 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Implicit neural representations such as Neural Radiance Field (NeRF) have focused mainly on modeling static objects captured under multi-view settings where real-time rendering can be achieved with smart data structures, e.g., PlenOctree. In this paper, we present a novel Fourier PlenOctree (FPO) technique to tackle efficient neural modeling and real-time rendering of dynamic scenes captured under the free-view video (FVV) setting. The key idea in our FPO is a novel combination of generalized NeRF, PlenOctree representation, volumetric fusion and Fourier transform. To accelerate FPO construction, we present a novel coarse-to-fine fusion scheme that leverages the generalizable NeRF technique to generate the tree via spatial blending. To tackle dynamic scenes, we tailor the implicit network to model the Fourier coefficients of timevarying density and color attributes. Finally, we construct the FPO and train the Fourier coefficients directly on the leaves of a union PlenOctree structure of the dynamic sequence. We show that the resulting FPO enables compact memory overload to handle dynamic objects and supports efficient fine-tuning. Extensive experiments show that the proposed method is 3000 times faster than the original NeRF and achieves over an order of magnitude acceleration over SOTA while preserving high visual quality for the free-viewpoint rendering of unseen dynamic scenes.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2022/papers/Wang_Fourier_PlenOctrees_for_Dynamic_Radiance_Field_Rendering_in_Real-Time_CVPR_2022_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="FPO overview"
    caption="`FPO` overview."
    >}}

### Results

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="2h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="render" message="800_x_800" color="informational" logo="link" >}}
{{<badge label="render" message="10ms" color="informational" logo="link" >}}
