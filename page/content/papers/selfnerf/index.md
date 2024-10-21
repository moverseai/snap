---
date: 2022-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SelfNeRF
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "arxiv22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "SelfNeRF: Fast Training NeRF for Human from Monocular Self-rotating Video"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 25
---

## `SelfNeRF`: Fast Training NeRF for Human from Monocular Self-rotating Video

> Bo Peng, Jun Hu, Jingtao Zhou, Juyong Zhang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2022 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
In this paper, we propose SelfNeRF, an efficient neural radiance field based novel view synthesis method for human performance. Given monocular self-rotating videos of human performers, SelfNeRF can train from scratch and achieve high-fidelity results in about twenty minutes. Some recent works have utilized the neural radiance field for dynamic human reconstruction. However, most of these methods need multi-view inputs and require hours of training, making it still difficult for practical use. To address this challenging problem, we introduce a surface-relative representation based on multi-resolution hash encoding that can greatly improve the training speed and aggregate inter-frame information. Extensive experimental results on several different datasets demonstrate the effectiveness and efficiency of SelfNeRF to challenging monocular videos.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2210.01651" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="SelfNeRF overview"
    caption="`SelfNeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}

#### Performance
{{<badge label="train" message="12--20mins" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
