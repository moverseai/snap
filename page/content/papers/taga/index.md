---
date: 2025-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: TAGA
categories: ["papers"]
tags: ["splats", "monocular", "cvpr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "TAGA: Self-supervised Learning for Template-free Animatable Gaussian Articulated Model"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 33
---

## `TAGA`: Self-supervised Learning for Template-free Animatable Gaussian Articulated Model

> Zhichao Zhai, Guikun Chen, Wenguan Wang, Dong Zheng, Jun Xiao

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="zhichao-zhai/TAGA" >}}

### Abstract
{{< lead >}}
Decoupling from customized parametric templates represents a crucial step toward the creation of fully flexible, animatable articulated models. While existing template-free methods can achieve high-fidelity reconstruction in observed views, they struggle to recover plausible canonical models, resulting in suboptimal animation quality. This limitation stems from overlooking the fundamental ambiguity in canonical reconstruction, where multiple canonical models could explain the same observed views. By revealing the entanglement between the canonical ambiguity and incorrect skinning, we present a self-supervised framework that learns both plausible skinning and accurate canonical geometry using only sparse pose data. Our method, TAGA, uses explicit 3D Gaussians as skinning carriers and characterizes the ambiguity as “Ambiguous Gaussians” with incorrect skinning weights. TAGA then corrects ambiguous Gaussians in the observation space using anomaly detection. With the corrected ones, we enforce cycle consistency constraints on both geometry and skinning to refine the corresponding Gaussians in the canonical space through a new backward method. Compared to existing state-of-the-art template-free methods, TAGA delivers superior visual fidelity for novel views and poses, while significantly improving training and rendering speeds. Experiments on challenging datasets with limited pose variations further demonstrate the robustness and generality of TAGA.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2025/papers/Zhai_TAGA_Self-supervised_Learning_for_Template-free_Animatable_Gaussian_Articulated_Model_CVPR_2025_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="TAGA teaser"
    caption="`TAGA` teaser."
    >}}

{{< figure
    src="overview.png"
    alt="TAGA pipeline"
    caption="`TAGA` pipeline."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="InstantNVR" color="fuchsia" logo="github" link="https://github.com/zju3dv/instant-nvr" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--NeRF" message="TAVA" color="coral" logo="github" link="facebookresearch/tava" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}

#### Performance
{{<badge label="train" message="30m" color="informational" logo="link" >}}
{{<badge label="render" message="7ms" color="informational" logo="link" >}}