---
date: 2023-08-17T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: IntrinsicNGP
categories: ["papers"]
tags: ["nerf", "smpl", "tvcg23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "IntrinsicNGP: Intrinsic Coordinate based Hash
Encoding for Human NeRF"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 4
---

## `IntrinsicNGP`: Intrinsic Coordinate based Hash Encoding for Human NeRF

> Bo Peng, Jun Hu, Jingtao Zhou, Xuan Gao, Juyong Zhang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *TVCG* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Recently, many works have been proposed to use the neural radiance field for novel view synthesis of human performers. However, most of these methods require hours of training, making them difficult for practical use. To address this challenging problem, we propose IntrinsicNGP, which can be trained from scratch and achieve high-fidelity results in a few minutes with videos of a human performer. To achieve this goal, we introduce a continuous and optimizable intrinsic coordinate instead of the original explicit Euclidean coordinate in the hash encoding module of InstantNGP. With this novel intrinsic coordinate, IntrinsicNGP can aggregate interframe information for dynamic objects using proxy geometry shapes. Moreover, the results trained with the given rough geometry shapes can be further refined with an optimizable offset field based on the intrinsic coordinate. Extensive experimental results on several datasets demonstrate the effectiveness and efficiency of IntrinsicNGP. We also illustrate the ability of our approach to edit the shape of reconstructed objects.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2302.14683" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="IntrinsicNGP overview"
    caption="`IntrinsicNGP` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}