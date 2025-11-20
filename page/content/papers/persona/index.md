---
date: 2025-10-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: PERSONA
categories: ["papers"]
tags: ["splats", "smplx", "monocular", "deformation", "generalized", "iccv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "PERSONA: Personalized Whole-Body 3D Avatar with Pose-Driven Deformations from a Single Image"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 19
---

## `PERSONA`: Personalized Whole-Body 3D Avatar with Pose-Driven Deformations from a Single Image

> Geonhee Sim, Gyeongsik Moon

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="mks0601/PERSONA_RELEASE" >}}

### Abstract
{{< lead >}}
Two major approaches exist for creating animatable human avatars. The first, a 3D-based approach, optimizes a NeRF- or 3DGS-based avatar from videos of a single person, achieving personalization through a disentangled identity representation. However, modeling pose-driven deformations, such as non-rigid cloth deformations, requires numerous pose-rich videos, which are costly and impractical to capture in daily life. The second, a diffusion-based approach, learns  pose-driven deformations from large-scale in-the-wild videos but struggles with identity preservation and pose-dependent identity entanglement. We present PERSONA, a framework that combines the strengths of both approaches to obtain a personalized 3D human avatar with pose-driven deformations from a single image. PERSONA leverages a diffusion-based approach to generate pose-rich videos from the input image and optimizes a 3D avatar based on them. To ensure high authenticity and sharp renderings across diverse poses, we introduce balanced sampling and geometry-weighted optimization. Balanced sampling oversamples the input image to mitigate identity shifts in diffusion-generated training videos. Geometry-weighted optimization prioritizes geometry constraints over image loss, preserving rendering quality in diverse poses.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2508.09973" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="method1.png"
    alt="Method (generation)"
    caption="Method (generation)."
    >}}


{{< figure
    src="method2.png"
    alt="Method (sampling)"
    caption="Method (sampling)."
    >}}


{{< figure
    src="method3.png"
    alt="Method (optimization)"
    caption="Method (optimization)."
    >}}


{{< figure
    src="method4.png"
    alt="Method (architecture)"
    caption="Method (architecture)."
    >}}

### Results

#### Data
{{<badge label="test" message="X--Humans" color="goldenrod" logo="github" link="https://xhumans.ait.ethz.ch/" target="_blank">}}
{{<badge label="test" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="ExAvatar" color="steelblue" logo="github" link="https://github.com/mks0601/ExAvatar_RELEASE" target="_blank">}}
{{<badge label="body--NeRF" message="X--Avatar" color="rebeccapurple" logo="github" link="https://github.com/Skype-line/X-Avatar" target="_blank">}}
{{<badge label="body--Splats" message="AniGS" color="goldenrod" logo="github" link="https://github.com/aigc3d/AniGS" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--NeRF" message="Vid2Avatar" color="palegreen" logo="github" link="https://github.com/MoyGcc/vid2avatar" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Performance
{{<badge label="train" message="A6000" color="informational" logo="link" >}}
{{<badge label="train" message="1--2h" color="informational" logo="link" >}}

{{<badge label="render" message="A6000" color="informational" logo="link" >}}
{{<badge label="render" message="38ms" color="informational" logo="link" >}}