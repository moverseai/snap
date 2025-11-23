---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NECA
categories: ["papers"]
tags: ["nerf", "smpl", "relight", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "NECA: Neural Customizable Human Avatar"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 42
---

## `NECA`: Neural Customizable Human Avatar

> Junjin Xiao, Qing Zhang1, Zhan Xu, Wei-Shi Zheng

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Relight {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="iSEE-Laboratory/NECA" >}}

### Abstract
{{< lead >}}
Human avatar has become a novel type of 3D asset with various applications. Ideally, a human avatar should be fully customizable to accommodate different settings and environments. In this work, we introduce NECA, an approach capable of learning versatile human representation from monocular or sparse-view videos, enabling granular customization across aspects such as pose, shadow, shape, lighting and texture. The core of our approach is to represent humans in complementary dual spaces and predict disentangled neural fields of geometry, albedo, shadow, as well as an external lighting, from which we are able to derive realistic rendering with high-frequency details via volumetric rendering. Extensive experiments demonstrate the advantage of our method over the state-of-the-art methods in photorealistic rendering, as well as various editing tasks such as novel pose synthesis and relighting
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2024/papers/Xiao_NECA_Neural_Customizable_Human_Avatar_CVPR_2024_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="NECA teaser"
    caption="`NECA` teaser."
    >}}

{{< figure
    src="method.png"
    alt="NECA overview"
    caption="`NECA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}
