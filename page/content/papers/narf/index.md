---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NARF
categories: ["papers"]
tags: ["nerf", "skeleton", "iccv21"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: Neural Articulated Radiance Field
summary: TODO
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 5
---

## `NARF`: Neural Articulated Radiance Field

> Atsuhiro Noguchi, Xiao Sun, Stephen Lin, Tatsuya Harada

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2021 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="nogu-atsu/NARF" >}}

### Abstract
{{< lead >}}
We present Neural Articulated Radiance Field (NARF), a novel deformable 3D representation for articulated objects learned from images. While recent advances in 3D implicit representation have made it possible to learn models of complex objects, learning pose-controllable representations of articulated objects remains a challenge, as current methods require 3D shape supervision and are unable to render appearance. In formulating an implicit representation of 3D articulated objects, our method considers only the rigid transformation of the most relevant object part in solving for the radiance field at each 3D location. In this way, the proposed method represents pose-dependent changes without significantly increasing the computational complexity. NARF is fully differentiable and can be trained from images with pose annotations. Moreover, through the use of an autoencoder, it can learn appearance variations over multiple instances of an object class. Experiments show that the proposed method is efficient and can generalize well to novel poses.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2104.03110" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="NARF overview"
    caption="`NARF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="THuman" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/DeepHuman/tree/master/THUmanDataset" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}


#### Performance
{{<badge label="train" message="24h" color="informational" logo="link" >}}
{{<badge label="train" message="4_x_V100" color="informational" logo="link" >}}
