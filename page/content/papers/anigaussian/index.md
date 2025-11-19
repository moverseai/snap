---
date: 2025-02-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: AniGaussian
categories: ["papers"]
tags: ["splats", "smpl", "monocular", "arxiv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "AniGaussian: Animatable Gaussian Avatar with Pose-guided Deformation"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 13
---

## `AniGaussian`: Animatable Gaussian Avatar with Pose-guided Deformation

> Mengtian Li, Shengxiang Yao, Chen Kai, Zhifeng Xie, Keyu Chen, Yu-Gang Jiang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
Recent advancements in Gaussian-based human body reconstruction have achieved notable success in creating animatable avatars. However, there are ongoing challenges to fully exploit the SMPL model’s prior knowledge and enhance the visual fidelity of these models to achieve more refined avatar reconstructions. In this paper, we introduce AniGaussian which addresses the above issues with two insights. First, we propose an innovative pose guided deformation strategy that effectively constrains the dynamic Gaussian avatar with SMPL pose guidance, ensuring that the reconstructed model not only captures the detailed surface nuances but also maintains anatomical correctness across a wide range of motions. Second, we tackle the expressiveness limitations of Gaussian models in representing dynamic human bodies. We incorporate rigid-based priors from previous works to enhance the dynamic transform capabilities of the Gaussian model. Furthermore, we introduce a split-with-scale strategy that significantly improves geometry quality. The ablative study experiment demonstrates the effectiveness of our innovative model design. Through extensive comparisons with existing methods, AniGaussian demonstrates superior performance in both qualitative result and quantitative metrics.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2502.19441" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
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
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}
