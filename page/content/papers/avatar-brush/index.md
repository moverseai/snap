---
date: 2025-11-24T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: AvatarBrush
categories: ["papers"]
tags: ["splats", "smplx", "monocular", "arxiv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "AvatarBrush: Monocular Reconstruction of Gaussian Avatars with Intuitive Local Editing"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 24
---

## `AvatarBrush`: Monocular Reconstruction of Gaussian Avatars with Intuitive Local Editing

> Mengtian Li, Shengxiang Yao, Yichen Pan, Haiyao Xiao, Zhongmei Li,  Zhifeng Xie, Keyu Chen

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
The efficient reconstruction of high-quality and intuitively editable human avatars presents a pressing challenge in the field of computer vision. Recent advancements, such as 3DGS, have demonstrated impressive reconstruction efficiency and rapid rendering speeds. However, intuitive local editing of these representations remains a significant challenge. In this work, we propose AvatarBrush, a framework that reconstructs fully animatable and locally editable avatars using only a monocular video input. We propose a three-layer model to represent the avatar and, inspired by mesh morphing techniques, design a framework to generate the Gaussian model from local information of the parametric body model. Compared to previous methods that require scanned meshes or multi-view captures as input, our approach reduces costs and enhances editing capabilities such as body shape adjustment, local texture modification, and geometry transfer. Our experimental results demonstrate superior quality across two datasets and emphasize the enhanced, user-friendly, and localized editing capabilities of our method.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2511.19189" target="_blank" >}}
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
    alt="Method (generation)"
    caption="Method (generation)."
    >}}


### Results

#### Data
{{<badge label="test" message="X--Humans" color="goldenrod" logo="github" link="https://xhumans.ait.ethz.ch/" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="SplattingAvatar" color="lemonchiffon" logo="github" link="https://github.com/initialneil/SplattingAvatar" target="_blank">}}
{{<badge label="body--Splats" message="HAHA" color="azure" logo="github" link="https://github.com/david-svitov/HAHA" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}
{{<badge label="body--Splats" message="NECA" color="darkolivegreen" logo="github" link="https://github.com/iSEE-Laboratory/NECA" target="_blank">}}


#### Performance
{{<badge label="train" message="RTX4090" color="informational" logo="link" >}}
{{<badge label="train" message="1.5h" color="informational" logo="link" >}}

{{<badge label="render" message="RTX4090" color="informational" logo="link" >}}
{{<badge label="render" message="18ms" color="informational" logo="link" >}}