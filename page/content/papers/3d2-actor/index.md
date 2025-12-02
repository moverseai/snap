---
date: 2025-02-25T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: 3D2-Actor
categories: ["papers"]
tags: ["splats", "smpl", "aaai25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "3D2-Actor: Learning Pose-Conditioned 3D-Aware Denoiser for Realistic Gaussian Avatar Modeling"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 37
---

## `3D2-Actor`: Learning Pose-Conditioned 3D-Aware Denoiser for Realistic Gaussian Avatar Modeling

> Zichen Tang, Hongyu Yang, Hanchen Zhang, Jiaxin Chen, Di Huang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *AAAI* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="silence-tang/GaussianActor" >}}

### Abstract
{{< lead >}}
Advancements in neural implicit representations and differentiable rendering have markedly improved the ability to learn animatable 3D avatars from sparse multi-view RGB videos. However, current methods that map observation space to canonical space often face challenges in capturing posedependent details and generalizing to novel poses. While diffusion models have demonstrated remarkable zero-shot capabilities in 2D image generation, their potential for creating animatable 3D avatars from 2D inputs remains underexplored. In this work, we introduce 3D2-Actor, a novel approach featuring a pose-conditioned 3D-aware human modeling pipeline that integrates iterative 2D denoising and 3D rectifying steps. The 2D denoiser, guided by pose cues, generates detailed multi-view images that provide the rich feature set necessary for high-fidelity 3D reconstruction and pose rendering. Complementing this, our Gaussian-based 3D rectifier renders images with enhanced 3D consistency through a two-stage projection strategy and a novel local coordinate representation. Additionally, we propose an innovative sampling strategy to ensure smooth temporal continuity across frames in video synthesis. Our method effectively addresses the limitations of traditional numerical solutions in handling ill-posed mappings, producing realistic and animatable 3D human avatars. Experimental results demonstrate that 3D2-Actor excels in high-fidelity avatar modeling and robustly generalizes to novel poses. 
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2412.11599" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="pipeline.png"
    alt="3D2-Actor pipeline"
    caption="`3D2-Actor` pipeline."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}

