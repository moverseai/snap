---
date: 2025-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: 2DGS-Avatar
categories: ["papers"]
tags: ["splats", "smplx", "arxiv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 17
---

## `2DGS-Avatar`: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting

> Qipeng Yan, Mingyang Sun, Lihua Zhang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
Real-time rendering of high-fidelity and animatable avatars from monocular videos remains a challenging problem in computer vision and graphics. Over the past few years, the Neural Radiance Field (NeRF) has made significant progress in rendering quality but behaves poorly in run-time performance due to the low efficiency of volumetric rendering. Recently, methods based on 3D Gaussian Splatting (3DGS) have shown great potential in fast training and real-time rendering. However, they still suffer from artifacts caused by inaccurate geometry. To address these problems, we propose 2DGS-Avatar, a novel approach based on 2D Gaussian Splatting (2DGS) for modeling animatable clothed avatars with high-fidelity and fast training performance. Given monocular RGB videos as input, our method generates an avatar that can be driven by poses and rendered in real-time. Compared to 3DGS-based methods, our 2DGS-Avatar retains the advantages of fast training and rendering while also capturing detailed, dynamic, and photo-realistic appearances. We conduct abundant experiments on popular datasets such as AvatarRex and THuman4.0, demonstrating impressive performance in both qualitative and quantitative metrics.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2503.02452" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="feature.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="pipeline.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="THuman4" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/THUman4.0-Dataset" target="_blank">}}
{{<badge label="test" message="AvatarReX" color="gold" style="plastic" logo="github" link="https://github.com/lizhe00/AnimatableGaussians/blob/master/AVATARREX_DATASET.md" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="AnimatableGaussians" color="darkred" logo="github" link="https://github.com/lizhe00/AnimatableGaussians" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}

#### Performance

{{<badge label="render" message="16ms" color="informational" logo="link" >}}
{{<badge label="render" message="RTX4070" color="informational" logo="link" >}}

