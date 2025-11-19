---
date: 2025-09-26T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: PICA
categories: ["papers"]
tags: ["splats", "smplx", "clothing", "tvcg25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "PICA: Physics-Integrated Clothed Avatar"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 12
---

## `PICA`: Physics-Integrated Clothed Avatar

> Bo Peng, Yunfan Tao, Haoyu Zhan, Yudong Guo, Juyong Zhang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="email" >}} *TVCG* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
We introduce PICA, a novel representation for high-fidelity animatable clothed human avatars with physics-accurate dynamics, even for loose clothing. Previous neural rendering-based representations of animatable clothed humans typically employ a single model to represent both the clothing and the underlying body. While efficient, these approaches often fail to accurately represent complex garment dynamics, leading to incorrect deformations and noticeable rendering artifacts, especially for sliding or loose garments. Furthermore, previous works represent garment dynamics as pose-dependent deformations and facilitate novel pose animations in a data-driven manner. This often results in outcomes that do not faithfully represent the mechanics of motion and are prone to generating artifacts in out-of-distribution poses. To address these issues, we adopt two individual 3D Gaussian Splatting (3DGS) models with different deformation characteristics, modeling the human body and clothing separately. This distinction allows for better handling of their respective motion characteristics. With this representation, we integrate a GNN-based clothed body physics simulation module to ensure an accurate representation of clothing dynamics.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2407.05324" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.jpg"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="pipeline.jpg"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data

{{<badge label="test" message="ActorsHQ" color="silver" logo="link" link="https://actors-hq.com/#dataset" target="_blank">}}

#### Comparisons

{{<badge label="body--Splats" message="AnimatableGaussians" color="darkred" logo="github" link="https://github.com/lizhe00/AnimatableGaussians" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}


#### Performance
{{<badge label="train" message="A100" color="informational" logo="link" >}}
{{<badge label="train" message="100mins" color="informational" logo="link" >}}

{{<badge label="render" message="A100" color="informational" logo="link" >}}
{{<badge label="render" message="83ms" color="informational" logo="link" >}}
