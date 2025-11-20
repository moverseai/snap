---
date: 2025-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: UMA
categories: ["papers"]
tags: ["splats", "smplx", "deformation", "texture", "arxiv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "UMA: Ultra-detailed Human Avatars via Multi-level Surface Alignment"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 20
---

## `UMA`: Ultra-detailed Human Avatars via Multi-level Surface Alignment

> Heming Zhu, Guoxing Sun, Christian Theobalt, Marc Habermann

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
Learning an animatable and clothed human avatar model with vivid dynamics and photorealistic appearance from multi-view videos is an important foundational research problem in computer graphics and vision. Fueled by recent advances in implicit representations, the quality of the animatable avatars has achieved an unprecedented level by attaching the implicit representation to drivable human template meshes. However, they usually fail to preserve highest level of detail, e.g., fine textures and yarn-level patterns, particularly apparent when the virtual camera is zoomed in and when rendering at 4K resolution and higher. We argue that this limitation stems from inaccurate surface tracking, specifically, depth misalignment and surface drift between character geometry and the ground truth surface, which forces the detailed appearance model to compensate for geometric errors. To address this, we adopt a latent deformation model and supervise the 3D deformation of the animatable character using guidance from foundational 2D video point trackers, which offer improved robustness to shading and surface variations, and are less prone to local minima than differentiable rendering. To mitigate the drift over time and lack of 3D awareness of 2D point trackers, we introduce a cascaded training strategy that generates consistent 3D point tracks by anchoring point tracks to the rendered avatar, which ultimately supervise our avatar at vertex and texel level. Furthermore, a lightweight Gaussian texture super-resolution module is employed to reconstruct challenging appearance details and micro-level structures using localized information. To validate the effectiveness of our approach, we introduce a novel dataset comprising five multi-view video sequences, each over 10 minutes in duration, captured using 40 calibrated 6K-resolution cameras, featuring subjects dressed in clothing with challenging texture patterns and wrinkle deformations. Our approach demonstrates significantly improved performance in rendering quality and geometric accuracy over the prior state of the art.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2506.01802" target="_blank" >}}
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
{{<badge label="test" message="UMA" color="lightcyan" style="plastic" logo="github" link="https://vcai.mpi-inf.mpg.de/projects/UMA/" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="AnimatableGaussians" color="darkred" logo="github" link="https://github.com/lizhe00/AnimatableGaussians" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--Splats" message="MeshAvatar" color="limegreen" logo="github" link="https://github.com/shad0wta9/meshavatar" target="_blank">}}
{{<badge label="body--Splats" message="ASH" color="lightsteelblue" logo="github" link="https://github.com/kv2000/ASH" target="_blank">}}
{{<badge label="body--Splats" message="TriHuman" color="mediumorchid" logo="github" link="" target="_blank">}}

#### Performance

{{<badge label="train" message="24h" color="informational" logo="link" >}}
{{<badge label="train" message="2_x_H100" color="informational" logo="link" >}}

{{<badge label="render" message="55ms" color="informational" logo="link" >}}