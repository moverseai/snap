---
date: 2025-10-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HADES
categories: ["papers"]
tags: ["splats", "smplx", "iccv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "HADES: Human Avatar with Dynamic Explicit Hair Strands"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 34
---

## `HADES`: Human Avatar with Dynamic Explicit Hair Strands

> Zhanfeng Liao, Hanzhang Tu, Cheng Peng, Hongwen Zhang, Boyao Zhou, Yebin Liu

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
We introduce HADES, the first framework to seamlessly integrate dynamic hair into human avatars. HADES represents hair as strands bound to 3D Gaussians, with roots attached to the scalp. By modeling inertial and velocityaware motion, HADES is able to simulate realistic hair dynamics that naturally align with body movements. To enhance avatar fidelity, we incorporate multi-scale data and address color inconsistencies across cameras using a lightweight MLP-based correction module, which generates color correction matrices for consistent color tones. Besides, we resolve rendering artifacts, such as hair dilation during zoom-out, through a 2D Mip filter and physically constrained hair radii. Furthermore, a temporal fusion module is introduced to ensure temporal coherence by modeling historical motion states. Experimental results demonstrate that HADES achieves high-fidelity avatars with realistic hair dynamics, outperforming existing state-of-the-art solutions in terms of realism and robustness.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/ICCV2025/papers/Liao_HADES_Human_Avatar_with_Dynamic_Explicit_Hair_Strands_ICCV_2025_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="overview.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="HADES" color="deeppink" style="plastic" logo="github" link="" target="_blank">}}
{{<badge label="test" message="ActorsHQ" color="silver" logo="link" link="https://actors-hq.com/#dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="AnimatableGaussians" color="darkred" logo="github" link="https://github.com/lizhe00/AnimatableGaussians" target="_blank">}}

