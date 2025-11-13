---
date: 2023-11-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SplatArmor
categories: ["papers"]
tags: ["splats", "smpl", "monocular", "arxiv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "SplatArmor: Articulated Gaussian splatting for animatable humans from monocular RGB videos"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 27
---

## `SplatArmor`: Articulated Gaussian splatting for animatable humans from monocular RGB videos

> Rohit Jena, Ganesh Iyer, Siddharth Choudhary, Brandon M. Smith, Pratik Chaudhari, James C. Gee

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
We propose SplatArmor, a novel approach for recovering detailed and animatable human models by 'armoring' a parameterized body model with 3D Gaussians. Our approach represents the human as a set of 3D Gaussians within a canonical space, whose articulation is defined by extending the skinning of the underlying SMPL geometry to arbitrary locations in the canonical space. To account for pose-dependent effects, we introduce a SE(3) field, which allows us to capture both the location and anisotropy of the Gaussians. Furthermore, we propose the use of a neural color field to provide color regularization and 3D supervision for the precise positioning of these Gaussians. We show that Gaussian splatting provides an interesting alternative to neural rendering based methods by leverging a rasterization primitive without facing any of the non-differentiability and optimization challenges typically faced in such approaches. The rasterization paradigms allows us to leverage forward skinning, and does not suffer from the ambiguities associated with inverse skinning and warping. We show compelling results on the ZJU MoCap and People Snapshot datasets, which underscore the effectiveness of our method for controllable human synthesis.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2311.10812" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.png"
    alt="SplatArmor overview"
    caption="`SplatArmor` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="Anim--NeRF" color="yellow" logo="github" link="https://github.com/JanaldoChen/Anim-NeRF" target="_blank">}}
{{<badge label="body--NeRF" message="SANeRF" color="teal" logo="github" link="https://github.com/pfnet-research/surface-aligned-nerf" target="_blank">}}

#### Performance
{{<badge label="train" message="70m" color="informational" logo="link" >}}