---
date: 2023-06-20T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Vid2Avatar
categories: ["papers"]
tags: ["nerf", "smpl", "sdf", "monocular", "cvpr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Vid2Avatar: 3D Avatar Reconstruction from Videos in the Wild via Self-supervised Scene Decomposition"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 5
---

## `Vid2Avatar`: 3D Avatar Reconstruction from Videos in the Wild via Self-supervised Scene Decomposition

> Chen Guo, Tianjian Jiang, Xu Chen, Jie Song, Otmar Hilliges

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} SDF {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="MoyGcc/vid2avatar" >}}

### Abstract
{{< lead >}}
We present Vid2Avatar, a method to learn human avatars from monocular in-the-wild videos. Reconstructing humans that move naturally from monocular in-the-wild videos is difficult. Solving it requires accurately separating humans from arbitrary backgrounds. Moreover, it requires reconstructing detailed 3D surface from short video sequences, making it even more challenging. Despite these challenges, our method does not require any groundtruth supervision or priors extracted from large datasets of clothed human scans, nor do we rely on any external segmentation modules. Instead, it solves the tasks of scene decomposition and surface reconstruction directly in 3D by modeling both the human and the background in the scene jointly, parameterized via two separate neural fields. Specifically, we define a temporally consistent human representation in canonical space and formulate a global optimization over the background model, the canonical human shape and texture, and per-frame human pose parameters. A coarse-to-fine sampling strategy for volume rendering and novel objectives are introduced for a clean separation of dynamic human and static background, yielding detailed and robust 3D human geometry reconstructions. We evaluate our methods on publicly available datasets and show improvements over prior art.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2023/papers/Guo_Vid2Avatar_3D_Avatar_Reconstruction_From_Videos_in_the_Wild_via_CVPR_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="Vid2Avatar overview"
    caption="`Vid2Avatar` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="MonoPerfCap" color="coral" logo="link" link="https://vcai.mpi-inf.mpg.de/projects/wxu/MonoPerfCap/" target="_blank">}}
{{<badge label="test" message="NeuMan" color="white" logo="github" link="apple/ml-neuman" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="HumanNeRF" color="blue" logo="github" link="chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="apple/ml-neuman" target="_blank">}}

#### Performance
{{<badge label="train" message="36--48h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
