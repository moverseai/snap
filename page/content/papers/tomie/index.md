---
date: 2025-10-10T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: ToMiE
categories: ["papers"]
tags: ["splats", "smpl", "clothing", "iccv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "ToMiE: Towards Explicit Exoskeleton for the Reconstruction of Complicated 3D Human Avatars"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 15
---

## `ToMiE`: Towards Explicit Exoskeleton for the Reconstruction of Complicated 3D Human Avatars

> Yifan Zhan, Qingtian Zhu, Muyao Niu, Mingze Ma, Jiancheng Zhao, Zhihang Zhong, Xiao Sun, Yu Qiao, Yinqiang Zheng

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="Yifever20002/ToMiE" >}}

### Abstract
{{< lead >}}
In this paper, we highlight a critical yet often overlooked factor in most 3D human tasks, namely modeling complicated 3D human with with hand-held objects or loose-fitting clothing. It is known that the parameterized formulation of SMPL is able to fit human skin; while hand-held objects and loose-fitting clothing, are difficult to get modeled within the unified framework, since their movements are usually decoupled with the human body. To enhance the capability of SMPL skeleton in response to this situation, we propose a growth strategy that enables the joint tree of the skeleton to expand adaptively. Specifically, our method, called ToMiE, consists of parent joints localization and external joints optimization. For parent joints localization, we employ a gradient-based approach guided by both LBS blending weights and motion kernels. Once the external joints are obtained, we proceed to optimize their transformations in SE(3) across different frames, enabling rendering and explicit animation. ToMiE manages to outperform other methods across various cases with hand-held objects and loose-fitting clothing, not only in rendering quality but also by offering free animation of grown joints, thereby enhancing the expressive ability of SMPL skeleton for a broader range of applications.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2410.08082" target="_blank" >}}
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
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DNA--Rendering" color="darkorange" style="plastic" logo="github" link="https://dna-rendering.github.io/" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}
