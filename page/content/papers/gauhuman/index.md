---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GauHuman
categories: ["papers"]
tags: ["splats", "smpl", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "GauHuman: Articulated Gaussian Splatting from Monocular Human Videos"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 18
---

## `GauHuman`: Articulated Gaussian Splatting from Monocular Human Videos

> Mingwei Li, Jiachen Tao, Zongxin Yang, Yi Yang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="skhu101/GauHuman" >}}

### Abstract
{{< lead >}}
We present, GauHuman, a 3D human model with Gaussian Splatting for both fast training (1~2 minutes) and real-time rendering (up to 189 FPS), compared with existing NeRF-based implicit representation modelling frameworks demanding hours of training and seconds of rendering per frame. Specifically, GauHuman encodes Gaussian Splatting in the canonical space and transforms 3D Gaussians from canonical space to posed space with linear blend skinning (LBS), in which effective pose and LBS refinement modules are designed to learn fine details of 3D humans under negligible computational cost. Moreover, to enable fast optimization of GauHuman, we initialize and prune 3D Gaussians with 3D human prior, while splitting/cloning via KL divergence guidance, along with a novel merge operation for further speeding up. Extensive experiments on ZJU_Mocap and MonoCap datasets demonstrate that GauHuman achieves state-of-the-art performance quantitatively and qualitatively with fast training and real-time rendering speed. Notably, without sacrificing rendering quality, GauHuman can fast model the 3D human performer with ~13k 3D Gaussians.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2312.02973" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="GauHuman teaser"
    caption="`GauHuman` teaser."
    >}}

{{< figure
    src="overview.png"
    alt="GauHuman overview"
    caption="`GauHuman` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DeepCap" color="cyan" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--NeRF" message="InstantNVR" color="fuchsia" logo="github" link="https://github.com/zju3dv/instant-nvr" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="Anim--NeRF" color="yellow" logo="github" link="https://github.com/JanaldoChen/Anim-NeRF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}

#### Performance
{{<badge label="train" message="1--4m" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}

{{<badge label="render" message="6ms" color="informational" logo="link" >}}