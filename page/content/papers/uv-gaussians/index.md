---
date: 2024-03-07T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: UV Gaussians
categories: ["papers"]
tags: ["splats", "smplx", "deformation", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "UV Gaussians: Joint Learning of Mesh Deformation and Gaussian Textures for Human Avatar Modeling"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 37
---

## `UV Gaussians`: Joint Learning of Mesh Deformation and Gaussian Textures for Human Avatar Modeling

> Yujiao Jiang, Qingmin Liao, Xiaoyu Li, Li Ma, Qi Zhang, Chaopeng Zhang, Zongqing Lu, Ying Shan

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
We propose UV Gaussians, which model the 3D human body by jointly learning mesh deformations and 2D UV-space Gaussian textures. Rather than optimizing the properties of Gaussians points in 3D space, we utilize the embedding of UV map to learn Gaussian textures in 2D space, leveraging the capabilities of powerful 2D networks to extract features. Additionally, through an independent Mesh network, we optimize pose-dependent geometric deformations, thereby guiding Gaussian rendering and significantly enhancing rendering quality. We collect and process a new dataset of human motion, which includes multi-view images, scanned models, parametric model registration, and corresponding texture maps. Experimental results demonstrate that our method achieves state-of-the-art synthesis of novel view and novel pose.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2403.11589" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.jpg"
    alt="UV Gaussians teaser"
    caption="`UV Gaussians` teaser."
    >}}

{{< figure
    src="method.jpg"
    alt="UV Gaussians overview"
    caption="`UV Gaussians` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="UV--Gaussians" color="seagreen" logo="github" link="https://alex-jyj.github.io/UV-Gaussians/" target="_blank">}}


#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--NeRF" message="UV Volumes" color="wheat" logo="github" link="https://github.com/fanegg/UV-Volumes" target="_blank">}}

#### Performance

{{<badge label="train" message="3d" color="informational" logo="link" >}}
{{<badge label="train" message="A100" color="informational" logo="link" >}}