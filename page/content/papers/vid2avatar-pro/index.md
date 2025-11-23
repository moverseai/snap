---
date: 2025-06-20T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Vid2Avatar-Pro
categories: ["papers"]
tags: ["splats", "smplx", "monocular", "cvpr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Vid2Avatar-Pro: Authentic Avatar from Videos in the Wild via Universal Prior"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 18
---

## `Vid2Avatar-Pro`: Authentic Avatar from Videos in the Wild via Universal Prior

> Chen Guo, Junxuan Li, Yash Kant, Yaser Sheikh, Shunsuke Saito, Chen Cao

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
We present Vid2Avatar-Pro, a method to create photorealistic and animatable 3D human avatars from monocular in-the-wild videos. Building a high-quality avatar that supports animation with diverse poses from a monocular video is challenging because the observation of pose diversity and view points is inherently limited. The lack of pose variations typically leads to poor generalization to novel poses, and avatars can easily overfit to limited input view points, producing artifacts and distortions from other views. In this work, we address these limitations by leveraging a universal prior model (UPM) learned from a large corpus of multi-view clothed human performance capture data. We build our representation on top of expressive 3D Gaussians with canonical front and back maps shared across identities. Once the UPM is learned to accurately reproduce the large-scale multi-view human images, we fine-tune the model with an in-the-wild video via inverse rendering to obtain a personalized photorealistic human avatar that can be faithfully animated to novel human motions and rendered from novel views. The experiments show that our approach based on the learned universal prior sets a new state-of-the-art in monocular avatar reconstruction by substantially outperforming existing approaches relying only on heuristic regularization or a shape prior of minimally clothed bodies (e.g., SMPL) on publicly available datasets.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2503.01610" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Vid2Avatar Pro teaser"
    caption="`Vid2Avatar Pro` teaser."
    >}}

{{< figure
    src="method.png"
    alt="Vid2Avatar Pro overview"
    caption="`Vid2Avatar Pro` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="MonoPerfCap" color="coral" logo="link" link="https://vcai.mpi-inf.mpg.de/projects/wxu/MonoPerfCap/" target="_blank">}}
{{<badge label="test" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="HumanNeRF" color="blue" logo="github" link="chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}
{{<badge label="body--NeRF" message="Vid2Avatar" color="palegreen" logo="github" link="https://github.com/MoyGcc/vid2avatar" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--Splats" message="ExAvatar" color="steelblue" logo="github" link="https://github.com/mks0601/ExAvatar_RELEASE" target="_blank">}}
