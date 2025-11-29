---
date: 2025-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: DUT
categories: ["papers"]
tags: ["splats", "skeleton", "generalized", "texture", "cvpr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 25
---

## Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures

> Guoxing Sun, Rishabh Dabral, Heming Zhu, Pascal Fua, Christian Theobalt, Marc Habermann

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="sunshinnnn/dut" >}}

### Abstract
{{< lead >}}
Real-time free-view human rendering from sparse-view RGB inputs is a challenging task due to the sensor scarcity and the tight time budget. To ensure efficiency, recent methods leverage 2D CNNs operating in texture space to learn rendering primitives. However, they either jointly learn geometry and appearance, or completely ignore sparse image information for geometry estimation, significantly harming visual quality and robustness to unseen body poses. To address these issues, we present Double Unprojected Textures, which at the core disentangles coarse geometric deformation estimation from appearance synthesis, enabling robust and photorealistic 4K rendering in real-time. Specifically, we first introduce a novel image-conditioned template deformation network, which estimates the coarse deformation of the human template from a first unprojected texture. This updated geometry is then used to apply a second and more accurate texture unprojection. The resulting texture map has fewer artifacts and better alignment with input views, which benefits our learning of finer-level geometry and appearance represented by Gaussian splats. We validate the effectiveness and efficiency of the proposed method in quantitative and qualitative experiments, which significantly surpasses other state-of-the-art methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2412.13183" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="DUT teaser"
    caption="`DUT` teaser."
    >}}

{{< figure
    src="method.png"
    alt="DUT overview"
    caption="`DUT` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="ASH" color="green" logo="github" link="https://gvv-assets.mpi-inf.mpg.de/ASH/" target="_blank">}}
{{<badge label="test" message="THuman4" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/THUman4.0-Dataset" target="_blank">}}
{{<badge label="test" message="DVA" color="gainsboro" logo="github" link="https://github.com/facebookresearch/dva" target="_blank">}}
{{<badge label="test" message="ENeRF" color="lightcoral" logo="github" link="https://github.com/zju3dv/ENeRF" target="_blank">}}
{{<badge label="test" message="HoloChar" color="darkblue" logo="github" link="https://vcai.mpi-inf.mpg.de/projects/holochar/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="ENeRF" color="lightcoral" logo="github" link="https://github.com/zju3dv/ENeRF" target="_blank">}}
{{<badge label="body--Splats" message="DVA" color="gainsboro" logo="github" link="https://github.com/facebookresearch/dva" target="_blank">}}
{{<badge label="body--Splats" message="GHG" color="plum" logo="github" link="https://github.com/humansensinglab/Generalizable-Human-Gaussians" target="_blank">}}
{{<badge label="test" message="HoloChar" color="darkblue" logo="github" link="https://github.com/ashwath98/deepcharacters" target="_blank">}}



#### Performance
{{<badge label="render" message="38ms" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3090" color="informational" logo="link" >}}
