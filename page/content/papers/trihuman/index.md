---
date: 2024-10-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: TriHuman
categories: ["papers"]
tags: ["nerf", "skeleton", "texture", "deformation", "tog24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "TriHuman: A Real-time and Controllable Tri-plane Representation for Detailed Human Geometry and Appearance Synthesis"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 13
---

## `TriHuman`: A Real-time and Controllable Tri-plane Representation for Detailed Human Geometry and Appearance Synthesis

> Heming Zhu, Fangneng Zhan, Christian Theobalt, Marc Habermann

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *ToG* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Creating controllable, photorealistic, and geometrically detailed digital doubles of real humans solely from video data is a key challenge in Computer Graphics and Vision, especially when real-time performance is required. Recent methods attach a neural radiance field (NeRF) to an articulated structure, e.g., a body model or a skeleton, to map points into a pose canonical space while conditioning the NeRF on the skeletal pose. These approaches typically parameterize the neural field with a multi-layer perceptron (MLP) leading to a slow runtime. To address this drawback, we propose TriHuman a novel human-tailored, deformable, and efficient tri-plane representation, which achieves real-time performance, state-of-the-art pose-controllable geometry synthesis as well as photorealistic rendering quality. At the core, we non-rigidly warp global ray samples into our undeformed tri-plane texture space, which effectively addresses the problem of global points being mapped to the same tri-plane locations. We then show how such a tri-plane feature representation can be conditioned on the skeletal motion to account for dynamic appearance and geometry changes. Our results demonstrate a clear step toward higher quality in terms of geometry and appearance modeling of humans as well as runtime performance.
{{< /lead >}}

{{< button href="https://dl.acm.org/doi/pdf/10.1145/3697140" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="TriHumans overview"
    caption="`TriHumans` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="skeleton--NeRF" message="NeuralActor" color="blue" logo="github" link="lingjie0206/Neural_Actor_Main_Code" target="_blank">}}
{{<badge label="skeleton--NeRF" message="HDHumans" color="blue" logo="link" target="_blank">}}
{{<badge label="body--NeRF" message="TAVA" color="coral" logo="github" link="facebookresearch/tava" target="_blank">}}

#### Performance
{{<badge label="train" message="2d" color="informational" logo="link" >}}
{{<badge label="train" message="A100" color="informational" logo="link" >}}