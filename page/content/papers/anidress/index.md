---
date: 2024-01-07T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: AniDress
categories: ["papers"]
tags: ["nerf", "smpl", "clothing", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "AniDress: Animatable Loose-Dressed Avatar from Sparse Views Using Garment Rigging Model"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 38
---

## `AniDress`: Animatable Loose-Dressed Avatar from Sparse Views Using Garment Rigging Model

> Beijia Chen, Yuefan Shen, Qing Shuai, Xiaowei Zhou, Kun Zhou, Youyi Zheng

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
Recent communities have seen significant progress in building photo-realistic animatable avatars from sparse multi-view videos. However, current workflows struggle to render realistic garment dynamics for loose-fitting characters as they predominantly rely on naked body models for human modeling while leaving the garment part un-modeled. This is mainly due to that the deformations yielded by loose garments are highly non-rigid, and capturing such deformations often requires dense views as supervision. In this paper, we introduce AniDress, a novel method for generating animatable human avatars in loose clothes using very sparse multi-view videos (4-8 in our setting). To allow the capturing and appearance learning of loose garments in such a situation, we employ a virtual bone-based garment rigging model obtained from physics-based simulation data. Such a model allows us to capture and render complex garment dynamics through a set of low-dimensional bone transformations. Technically, we develop a novel method for estimating temporal coherent garment dynamics from a sparse multi-view video. To build a realistic rendering for unseen garment status using coarse estimations, a pose-driven deformable neural radiance field conditioned on both body and garment motions is introduced, providing explicit control of both parts. At test time, the new garment poses can be captured from unseen situations, derived from a physics-based or neural network-based simulator to drive unseen garment dynamics. To evaluate our approach, we create a multi-view dataset that captures loose-dressed performers with diverse motions. Experiments show that our method is able to render natural garment dynamics that deviate highly from the body and generalize well to both unseen views and poses, surpassing the performance of existing methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2401.15348" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="AniDress teaser"
    caption="`AniDress` teaser."
    >}}

{{< figure
    src="method.png"
    alt="AniDress overview"
    caption="`AniDress` overview."
    >}}

{{< figure
    src="method2.png"
    alt="AniDress details"
    caption="`AniDress` details."
    >}}

### Results

#### Data
{{<badge label="test" message="AniDress" color="forestgreen" logo="github" link="https://yuefanshen.net/AniDress" target="_blank">}}


#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="UV Volumes" color="wheat" logo="github" link="https://github.com/fanegg/UV-Volumes" target="_blank">}}
