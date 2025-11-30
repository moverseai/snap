---
date: 2025-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: RoGSplat
categories: ["papers"]
tags: ["splats", "smpl", "generalized", "cvpr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 31
---

## `RoGSplat`: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images

> Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="iSEE-Laboratory/RoGSplat" >}}

### Abstract
{{< lead >}}
This paper presents RoGSplat, a novel approach for synthesizing high-fidelity novel views of unseen human from sparse multi-view images, while requiring no cumbersome per-subject optimization. Unlike previous methods that typically struggle with sparse views with few overlappings and are less effective in reconstructing complex human geometry, the proposed method enables robust reconstruction in such challenging conditions. Our key idea is to lift SMPL vertices to dense and reliable 3D prior points representing accurate human body geometry, and then regress human Gaussian parameters based on the points. To account for possible misalignment between SMPL model and images, we propose to predict image-aligned 3D prior points by leveraging both pixel-level features and voxel-level features, from which we regress the coarse Gaussians. To enhance the ability to capture high-frequency details, we further render depth maps from the coarse 3D Gaussians to help regress finegrained pixel-wise Gaussians. Experiments on several benchmark datasets demonstrate that our method outperforms state-of-the-art methods in novel view synthesis and crossdataset generalization. 
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2503.14198" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="RoGSplat teaser"
    caption="`RoGSplat` teaser."
    >}}

{{< figure
    src="overview.png"
    alt="RoGSplat overview"
    caption="`RoGSplat` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}
{{<badge label="test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}
{{<badge label="body--NeRF" message="GP--NeRF" color="lightgray" logo="github" link="https://github.com/sail-sg/GP-Nerf" target="_blank">}}
{{<badge label="body--NeRF" message="SHERF" color="mediumblue" logo="github" link="https://github.com/skhu101/SHERF" target="_blank">}}
{{<badge label="body--Splats" message="GHG" color="plum" logo="github" link="https://github.com/humansensinglab/Generalizable-Human-Gaussians" target="_blank">}}

#### Performance
{{<badge label="train" message="RTX4090" color="informational" logo="link" >}}
{{<badge label="train" message="20h" color="informational" logo="link" >}}

{{<badge label="inference" message="180ms" color="informational" logo="link" >}}
{{<badge label="inference" message="512_x_512" color="informational" logo="link" >}}