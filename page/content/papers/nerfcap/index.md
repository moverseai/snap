---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NerfCap
categories: ["papers"]
tags: ["nerf", "smpl", "deformation", "tvcg22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "NerfCap: Human Performance Capture with
Dynamic Neural Radiance Fields"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 8
---

## `NerfCap`: Human Performance Capture with Dynamic Neural Radiance Fields

> Kangkan Wang, Sida Peng, Xiaowei Zhou, Jian Yang, Guofeng Zhang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *TVCG* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="wangkangkan/nerfcap" >}}

### Abstract
{{< lead >}}
This paper addresses the challenge of human performance capture from sparse multi-view or monocular videos. Given a template mesh of the performer, previous methods capture the human motion by non-rigidly registering the template mesh to images with 2D silhouettes or dense photometric alignment. However, the detailed surface deformation cannot be recovered from the silhouettes, while the photometric alignment suffers from instability caused by appearance variation in the videos. To solve these problems, we propose NerfCap, a novel performance capture method based on the dynamic neural radiance field (NeRF) representation of the performer. Specifically, a canonical NeRF is initialized from the template geometry and registered to the video frames by optimizing the deformation field and the appearance model of the canonical NeRF. To capture both large body motion and detailed surface deformation, NerfCap combines linear blend skinning with embedded graph deformation. In contrast to the mesh-based methods that suffer from fixed topology and texture, NerfCap is able to flexibly capture complex geometry and appearance variation across the videos, and synthesize more photo-realistic images. In addition, NerfCap can be pre-trained end to end in a self-supervised manner by matching the synthesized videos with the input videos. Experimental results on various datasets show that NerfCap outperforms prior works in terms of both surface reconstruction accuracy and novel-view synthesis quality.
{{< /lead >}}

{{< button href="http://www.cad.zju.edu.cn/home/gfzhang/papers/NerfCap/NerfCap_TVCG_2022.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="NerfCap overview"
    caption="`NerfCap` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="DeepCap" color="cyan" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}

#### Performance
{{<badge label="train" message="3d" color="informational" logo="link" >}}
{{<badge label="train" message="2080_Ti" color="informational" logo="link" >}}
{{<badge label="finetune" message="1h" color="informational" logo="link" >}}
