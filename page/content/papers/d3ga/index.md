---
date: 2025-03-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: D3GA
categories: ["papers"]
tags: ["splats", "skeleton", "deformation", "3dv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "D3GA - Drivable 3D Gaussian Avatars"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 1
---

## `D3GA` - Drivable 3D Gaussian Avatars

> Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito, Michael Zollhöfer, Justus Thies, Javier Romero

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *3DV* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="facebookresearch/D3GA" >}}

### Abstract
{{< lead >}}
We present Drivable 3D Gaussian Avatars (D3GA), a multi-layered 3D controllable model for human bodies that utilizes 3D Gaussian primitives embedded into tetrahedral cages. The advantage of using cages compared to commonly employed linear blend skinning (LBS) is that primitives like 3D Gaussians are naturally re-oriented and their kernels are stretched via the deformation gradients of the encapsulating tetrahedron. Additional offsets are modeled for the tetrahedron vertices, effectively decoupling the low-dimensional driving poses from the extensive set of primitives to be rendered. This separation is achieved through the localized influence of each tetrahedron on 3D Gaussians, resulting in improved optimization. Using the cage-based deformation model, we introduce a compositional pipeline that decomposes an avatar into layers, such as garments, hands, or faces, improving the modeling of phenomena like garment sliding. These parts can be conditioned on different driving signals, such as keypoints for facial expressions or joint-angle vectors for garments and the body. Our experiments on two multi-view datasets with varied body shapes, clothes, and motions show higher-quality results. They surpass PSNR and SSIM metrics of other SOTA methods using the same data while offering greater flexibility and compactness.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2311.08581" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.jpg"
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
{{<badge label="test" message="Goliath" color="black" style="plastic" logo="github" link="https://github.com/facebookresearch/goliath?tab=readme-ov-file#data" target="_blank">}}
{{<badge label="test" message="ActorsHQ" color="silver" logo="link" link="https://actors-hq.com/#dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="AnimatableGaussians" color="darkred" logo="github" link="https://github.com/lizhe00/AnimatableGaussians" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}


#### Performance
{{<badge label="train" message="V100" color="informational" logo="link" >}}

{{<badge label="render" message="V100" color="informational" logo="link" >}}
{{<badge label="render" message="1024_x_667" color="informational" logo="link" >}}
