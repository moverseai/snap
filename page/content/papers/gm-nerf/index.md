---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GM-NeRF
categories: ["papers"]
tags: ["nerf", "smpl", "generalized", "cvpr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "GM-NeRF: Learning Generalizable Model-based Neural Radiance Fields from Multi-view Images"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 4
---

## `GM-NeRF`: Learning Generalizable Model-based Neural Radiance Fields from Multi-view Images

> Jianchuan Chen, Wentao Yi, Liqian Ma, Xu Jia, Huchuan Lu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="JanaldoChen/GM-NeRF" >}}

### Abstract
{{< lead >}}
In this work, we focus on synthesizing high-fidelity novel view images for arbitrary human performers, given a set of sparse multi-view images. It is a challenging task due to the large variation among articulated body poses and heavy self-occlusions. To alleviate this, we introduce an effective generalizable framework Generalizable Model-based Neural Radiance Fields (GM-NeRF) to synthesize freeviewpoint images. Specifically, we propose a geometryguided attention mechanism to register the appearance code from multi-view 2D images to a geometry proxy which can alleviate the misalignment between inaccurate geometry prior and pixel space. On top of that, we further conduct neural rendering and partial gradient backpropagation for efficient perceptual supervision and improvement of the perceptual quality of synthesis. To evaluate our method, we conduct experiments on synthesized datasets THuman2.0 and Multi-garment, and real-world datasets Genebody and ZJUMocap. The results demonstrate that our approach outperforms state-of-the-art methods in terms of novel view synthesis and geometric reconstruction.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_GM-NeRF_Learning_Generalizable_Model-Based_Neural_Radiance_Fields_From_Multi-View_Images_CVPR_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="GM-NeRF overview"
    caption="`GM-NeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}
{{<badge label="test" message="GeneBody" color="violet" logo="link" link="https://generalizable-neural-performer.github.io/genebody.html" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="A--NeRF" color="orange" logo="github" link="https://github.com/LemonATsu/A-NeRF" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}

#### Performance
{{<badge label="train" message="2_x_RTX3090" color="informational" logo="link" >}}
