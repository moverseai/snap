---
date: 2025-10-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: STG-Avatar
categories: ["papers"]
tags: ["splats", "smpl", "monocular", "arxiv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "STG-Avatar: Animatable Human Avatars via Spacetime Gaussian"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 29
---

## `STG-Avatar`: Animatable Human Avatars via Spacetime Gaussian

> Guangan Jiang, Tianzi Zhang, Dong Li, Zhenjun Zhao, Haoang Li, Mingrui Li, Hongyu Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="jiangguangan/STG-Avatar" >}}

### Abstract
{{< lead >}}
Realistic animatable human avatars from monocular videos are crucial for advancing human-robot interaction and enhancing immersive virtual experiences. While recent research on 3DGS-based human avatars has made progress, it still struggles with accurately representing detailed features of non-rigid objects (e.g., clothing deformations) and dynamic regions (e.g., rapidly moving limbs). To address these challenges, we present STG-Avatar, a 3DGS-based framework for highfidelity animatable human avatar reconstruction. Specifically, our framework introduces a rigid-nonrigid coupled deformation framework that synergistically integrates Spacetime Gaussians (STG) with linear blend skinning (LBS). In this hybrid design, LBS enables real-time skeletal control by driving global pose transformations, while STG complements it through spacetimeadaptive optimization of 3D Gaussians. Furthermore, we employ optical flow to identify high-dynamic regions and guide the adaptive densification of 3D Gaussians in these regions. Experimental results demonstrate that our method consistently outperforms state-of-the-art baselines in both reconstruction quality and operational efficiency, achieving superior quantitative metrics while retaining real-time rendering capabilities.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2510.22140" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="STG-Avatar overview"
    caption="`STG-Avatar` overview."
    >}}

{{< figure
    src="method.png"
    alt="STG-Avatar details"
    caption="`STG-Avatar` details."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="THuman4" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/THUman4.0-Dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}

#### Performance
{{<badge label="train" message="25mins" color="informational" logo="link" >}}
{{<badge label="train" message="RTX4090" color="informational" logo="link" >}}

{{<badge label="render" message="16ms" color="informational" logo="link" >}}
