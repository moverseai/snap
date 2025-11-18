---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: MoCo-NeRF
categories: ["papers"]
tags: ["nerf", "skeleton", "deformation", "eccv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Motion-Oriented Compositional Neural Radiance Fields for Monocular Dynamic Human Modeling"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 34
---

## Motion-Oriented Compositional Neural Radiance Fields for Monocular Dynamic Human Modeling

> Jaehyeok Kim,  Dongyoon Wee,  Dan Xu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="stevejaehyeok/MoCo-NeRF" >}}

### Abstract
{{< lead >}}
This paper introduces Motion-oriented Compositional Neu-ral Radiance Fields (MoCo-NeRF), a framework designed to perform free-viewpoint rendering of monocular human videos via novel non-rigid motion modeling approach. In the context of dynamic clothed humans, complex cloth dynamics generate non-rigid motions that are intrinsically distinct from skeletal articulations and critically important for the rendering quality. The conventional approach models non-rigid motions as spatial (3D) deviations in addition to skeletal transformations. However, it is either time-consuming or challenging to achieve optimal quality due to its high learning complexity without a direct supervision. To target this problem, we propose a novel approach of modeling non-rigid motions as radiance residual fields to benefit from more direct color supervision in the rendering and utilize the rigid radiance fields as a prior to reduce the complexity of the learning process. Our approach utilizes a single multiresolution hash encoding (MHE) to concurrently learn the canonical T-pose representation from rigid skeletal motions and the radiance residual field for non-rigid motions. Additionally, to further improve both training efficiency and usability, we extend MoCo-NeRF to support simultaneous training of multiple subjects within a single framework, thanks to our effective design for modeling non-rigid motions. This scalability is achieved through the integration of a global MHE and learnable identity codes in addition to multiple local MHEs. We present extensive results on ZJU-MoCap and MonoCap, clearly demonstrating state-of-the-art performance in both single- and multi-subject settings.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2407.11962v2" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="MoCo-NeRF teaser"
    caption="`MoCo-NeRF` teaser."
    >}}

{{< figure
    src="method.png"
    alt="MoCo-NeRF overview"
    caption="`MoCo-NeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DeepCap" color="cyan" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons


{{<badge label="body--NeRF" message="InstantNVR" color="fuchsia" logo="github" link="https://github.com/zju3dv/instant-nvr" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}

#### Performance
{{<badge label="train" message="1--2h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
