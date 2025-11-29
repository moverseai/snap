---
date: 2025-11-28T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HRM2Avatar
categories: ["papers"]
tags: ["splats", "smplx", "clothing", "texture", "monocular", "siggraph_asia25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "HRM2Avatar: High-Fidelity Real-Time Mobile Avatars from Monocular Phone Scans"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 28
---

## `HRM2Avatar`: High-Fidelity Real-Time Mobile Avatars from Monocular Phone Scans

> Chao Shi, Shenghao Jia, Jinhui Liu, Yong Zhang, Liangchao Zhu, Zhonglei Yang, Jinze Ma, Chaoyue Niu, Chengfei Lv

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH Asia* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="alibaba/Taobao3D" >}}

### Abstract
{{< lead >}}
We present HRM2Avatar, a novel framework for creating high-fidelity avatars from monocular phone scans, which can be rendered and animated in real-time on mobile devices. Monocular capture with commodity smartphones provides a low-cost, pervasive alternative to studio-grade multi-camera rigs, making avatar digitization accessible to non-expert users. Reconstructing high-fidelity avatars from single-view video sequences poses significant challenges due to deficient visual and geometric data relative to multi-camera setups. To address these limitations, at the data level, our method leverages two types of data captured with smartphones: static pose sequences for detailed texture reconstruction and dynamic motion sequences for learning pose-dependent deformations and lighting changes. At the representation level, we employ a lightweight yet expressive representation to reconstruct high-fidelity digital humans from sparse monocular data. First, we extract explicit garment meshes from monocular data to model clothing deformations more effectively. Second, we attach illumination-aware Gaussians to the mesh surface, enabling high-fidelity rendering and capturing pose-dependent lighting changes. This representation efficiently learns high-resolution and dynamic information from our tailored monocular data, enabling the creation of detailed avatars. At the rendering level, real-time performance is critical for rendering and animating high-fidelity avatars in AR/VR, social gaming, and on-device creation, demanding sub-frame responsiveness. Our fully GPU-driven rendering pipeline delivers 120 FPS on mobile devices and 90 FPS on standalone VR devices at 2K resolution, over 2.7× faster than representative mobile-engine baselines. Experiments show that HRM2Avatar delivers superior visual realism and real-time interactivity at high resolutions, outperforming state-of-the-art monocular methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2510.13587" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.jpg"
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
{{<badge label="test" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="ExAvatar" color="steelblue" logo="github" link="https://github.com/mks0601/ExAvatar_RELEASE" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}
{{<badge label="body--NeRF" message="Vid2Avatar" color="palegreen" logo="github" link="https://github.com/MoyGcc/vid2avatar" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--NeRF" message="Vid2Avatar-Pro" color="palegreen" logo="github" link="" target="_blank">}}

#### Performance
{{<badge label="train" message="RTX4090" color="informational" logo="link" >}}
{{<badge label="train" message="7h" color="informational" logo="link" >}}

{{<badge label="render" message="Apple--Vision--Pro" color="informational" logo="link" >}}
{{<badge label="render" message="2K" color="informational" logo="link" >}}
{{<badge label="render" message="11ms" color="informational" logo="link" >}}