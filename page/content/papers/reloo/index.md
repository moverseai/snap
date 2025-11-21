---
date: 2024-10-23T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: ReLoo
categories: ["papers"]
tags: ["nerf", "smpl", "deformation", "clothing", "eccv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "ReLoo: Reconstructing Humans Dressed in Loose Garments from Monocular Video in the Wild"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 40
---

## `ReLoo`: Reconstructing Humans Dressed in Loose Garments from Monocular Video in the Wild

> Chen Guo, Tianjian Jiang, Manuel Kaufmann, Chengwei Zheng, Julien Valentin, Jie Song, Otmar Hilliges

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="eth-ait/ReLoo" >}}

### Abstract
{{< lead >}}
While previous years have seen great progress in the 3D reconstruction of humans from monocular videos, few of the state-of-the-art methods are able to handle loose garments that exhibit large non-rigid surface deformations during articulation. This limits the application of such methods to humans that are dressed in standard pants or T-shirts. We present ReLoo , a novel method that overcomes this limitation and reconstructs high-quality 3D models of humans dressed in loose garments from monocular in-the-wild videos. To tackle this problem, we first establish a layered neural human representation that decomposes clothed humans into a neural inner body and outer clothing. On top of the layered neural representation, we further introduce a non-hierarchical virtual bone deformation module for the clothing layer that can freely move, which allows the accurate recovery of non-rigidly deforming loose clothing. A global optimization is formulated that jointly optimizes the shape, appearance, and deformations of both the human body and clothing over the entire sequence via multi-layer differentiable volume rendering. To evaluate ReLoo, we record subjects with dynamically deforming garments in a multi-view capture studio. The evaluation of our method, both on existing and our novel dataset, demonstrates its clear superiority over prior art on both indoor datasets and in-the-wild videos.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2409.15269" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="ReLoo overview"
    caption="`ReLoo` overview."
    >}}

{{< figure
    src="pipeline.png"
    alt="ReLoo overview"
    caption="`ReLoo` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="MonoLoose" color="darkgoldenrod" logo="github" link="https://moygcc.github.io/ReLoo/" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="Vid2Avatar" color="palegreen" logo="github" link="https://github.com/MoyGcc/vid2avatar" target="_blank">}}
{{<badge label="body--NeRF" message="SCARF" color="black" logo="github" link="https://github.com/yfeng95/SCARF" target="_blank">}}