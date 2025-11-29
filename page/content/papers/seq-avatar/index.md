---
date: 2025-10-10T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SeqAvatar
categories: ["papers"]
tags: ["splats", "smpl", "iccv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Sequential Gaussian Avatars with Hierarchical Motion Context"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 30
---

## Sequential Gaussian Avatars with Hierarchical Motion Context

> Wangze Xu, Yifan Zhan, Zhihang Zhong, Xiao Sun

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="zezeaaa/SeqAvatar" >}}

### Abstract
{{< lead >}}
The emergence of neural rendering has significantly advanced the rendering quality of 3D human avatars, with the recently popular 3DGS technique enabling real-time performance. However, SMPL-driven 3DGS human avatars still struggle to capture fine appearance details due to the complex mapping from pose to appearance during fitting. In this paper, we propose SeqAvatar, which excavates the explicit 3DGS representation to better model human avatars based on a hierarchical motion context. Specifically, we utilize a coarse-to-fine motion conditions that incorporate both the overall human skeleton and fine-grained vertex motions for non-rigid deformation. To enhance the robustness of the proposed motion conditions, we adopt a spatio-temporal multi-scale sampling strategy to hierarchically integrate more motion clues to model human avatars. Extensive experiments demonstrate that our method significantly outperforms 3DGS-based approaches and renders human avatars orders of magnitude faster than the latest NeRF-based models that incorporate temporal context, all while delivering performance that is at least comparable or even superior.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2411.16768" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="method.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="I3D--Human" color="lemonchiffon" logo="link" link="https://github.com/Yifever20002/Dyco" target="_blank">}}
{{<badge label="test" message="DNA--Rendering" color="darkorange" style="plastic" logo="github" link="https://dna-rendering.github.io/" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}
{{<badge label="body--Splats" message="DyCo" color="lightpink" logo="github" link="https://github.com/Yifever20002/Dyco" target="_blank">}}

#### Performance

{{<badge label="train" message="5mins" color="informational" logo="link" >}}
{{<badge label="train" message="RTX4090" color="informational" logo="link" >}}

{{<badge label="render" message="22ms" color="informational" logo="link" >}}
