---
date: 2025-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: AniGS
categories: ["papers"]
tags: ["splats", "smplx", "generalized", "cvpr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 14
---

## `AniGS`: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction

> Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu1, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="aigc3d/AniGS" >}}

### Abstract
{{< lead >}}
Generating animatable human avatars from a single image is essential for various digital human modeling applications. Existing 3D reconstruction methods often struggle to capture fine details in animatable models, while generative approaches for controllable animation, though avoiding explicit 3D modeling, suffer from viewpoint inconsistencies in extreme poses and computational inefficiencies. In this paper, we address these challenges by leveraging the power of generative models to produce detailed multi-view canonical pose images, which help resolve ambiguities in animatable human reconstruction. We then propose a robust method for 3D reconstruction of inconsistent images, enabling real-time rendering during inference. Specifically, we adapt a transformer-based video generation model to generate multi-view canonical pose images and normal maps, pretraining on a large-scale video dataset to improve generalization. To handle view inconsistencies, we recast the reconstruction problem as a 4D task and introduce an efficient 3D modeling approach using 4D Gaussian Splatting. Experiments demonstrate that our method achieves photorealistic, real-time animation of 3D human avatars from in-the-wild images, showcasing its effectiveness and generalization capability.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2025/papers/Qiu_AniGS_Animatable_Gaussian_Avatar_from_a_Single_Image_with_Inconsistent_CVPR_2025_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="AniGS teaser"
    caption="`AniGS` teaser."
    >}}


{{< figure
    src="pipeline.png"
    alt="AniGS overview"
    caption="`AniGS` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}
{{<badge label="test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}
{{<badge label="test" message="2K2K" color="lawngreen" logo="github" link="https://github.com/SangHunHan92/2K2K" target="_blank">}}
{{<badge label="test" message="CustomHumans" color="brown" logo="github" link="https://custom-humans.github.io/#download" target="_blank">}}

#### Performance
{{<badge label="inference" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="inference" message="10mins" color="informational" logo="link" >}}
