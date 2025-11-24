---
date: 2025-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: FRESA
categories: ["papers"]
tags: ["smplx", "deformation", "generalized", "cvpr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "FRESA: Feedforward Reconstruction of Personalized Skinned Avatars from Few Images"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 23
---

## `FRESA`: Feedforward Reconstruction of Personalized Skinned Avatars from Few Images

> Rong Wang, Fabian Prada, Ziyan Wang, Zhongshi Jiang, Chengxiang Yin, Junxuan Li, Shunsuke Saito, Igor Santesteban, Javier Romero, Rohan Joshi, Hongdong Li, Jason Saragih, Yaser Sheikh

{{< keywordList >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="rongakowang/FRESA" >}}

### Abstract
{{< lead >}}
We present a novel method for reconstructing personalized 3D human avatars with realistic animation from only a few images. Due to the large variations in body shapes, poses, and cloth types, existing methods mostly require hours of per-subject optimization during inference, which limits their practical applications. In contrast, we learn a universal prior from over a thousand clothed humans to achieve instant feedforward generation and zero-shot generalization. Specifically, instead of rigging the avatar with shared skinning weights, we jointly infer personalized avatar shape, skinning weights, and pose-dependent deformations, which effectively improves overall geometric fidelity and reduces deformation artifacts. Moreover, to normalize pose variations and resolve coupled ambiguity between canonical shapes and skinning weights, we design a 3D canonicalization process to produce pixel-aligned initial conditions, which helps to reconstruct fine-grained geometric details. We then propose a multi-frame feature aggregation to robustly reduce artifacts introduced in canonicalization and fuse a plausible avatar preserving person-specific identities. Finally, we train the model in an end-to-end framework on a large-scale capture dataset, which contains diverse human subjects paired with high-quality 3D scans. Extensive experiments show that our method generates more authentic reconstruction and animation than state-of-the-arts, and can be directly generalized to inputs from casually taken phone photos.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2503.19207" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="FRESA teaser"
    caption="`FRESA` teaser."
    >}}


{{< figure
    src="pipeline.png"
    alt="FRESA overview"
    caption="`FRESA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}
{{<badge label="test" message="Dome Data" color="deepskyblue" logo="github" link="https://github.com/rongakowang/FRESA" target="_blank">}}