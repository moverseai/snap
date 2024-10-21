---
date: 2023-06-20T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: MonoHuman
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "cvpr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "MonoHuman: Animatable Human Neural Field from Monocular Video"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 5
---

## `MonoHuman`: Animatable Human Neural Field from Monocular Video

> Zhengming Yu, Wei Cheng, Xian Liu, Wayne Wu, Kwan-Yee Lin

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="Yzmblog/MonoHuman" >}}

### Abstract
{{< lead >}}
Animating virtual avatars with free-view control is crucial for various applications like virtual reality and digital entertainment. Previous studies attempt to utilize the representation power of neural radiance field (NeRF) to reconstruct the human body from monocular videos. Recent works propose to graft a deformation network into the NeRF to further model the dynamics of the human neural field for animating vivid human motions. However, such pipelines either rely on pose-dependent representations or fall short of motion coherency due to frame-independent optimization, making it difficult to generalize to unseen pose sequences realistically.

In this paper, we propose a novel framework MonoHuman, which robustly renders view-consistent and high-fidelity avatars under arbitrary novel poses. Our key insight is to model the deformation field with bi-directional constraints and explicitly leverage the off-the-peg keyframe information to reason the feature correlations for coherent results. In particular, we first propose a Shared Bidirectional Deformation module, which creates a pose-independent generalizable deformation field by disentangling backward and forward deformation correspondences into shared skeletal motion weight and separate non-rigid motions. Then, we devise a Forward Correspondence Search module, which queries the correspondence feature of keyframes to guide the rendering network. The rendered results are thus multi-view consistent with high fidelity, even under challenging novel pose settings. Extensive experiments demonstrate the superiority of our proposed MonoHuman over state-of-the-art methods.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2023/papers/Yu_MonoHuman_Animatable_Human_Neural_Field_From_Monocular_Video_CVPR_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="MonoHuman overview"
    caption="`MonoHuman` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="blue" logo="github" link="chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="apple/ml-neuman" target="_blank">}}

#### Performance
{{<badge label="train" message="70h" color="informational" logo="link" >}}
{{<badge label="train" message="V100" color="informational" logo="link" >}}
