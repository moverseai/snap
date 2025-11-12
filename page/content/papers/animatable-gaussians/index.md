---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: AnimatableGaussians
categories: ["papers"]
tags: ["splats", "smplx", "texture", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 7
---

## `Animatable Gaussians`: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling

> Zhe Li, Zerong Zheng, Lizhen Wang, Yebin Liu

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="lizhe00/AnimatableGaussians" >}}

### Abstract
{{< lead >}}
Modeling animatable human avatars from RGB videos is a long-standing and challenging problem. Recent works usually adopt MLP-based neural radiance fields (NeRF) to represent 3D humans, but it remains difficult for pure MLPs to regress pose-dependent garment details. To this end, we introduce Animatable Gaussians, a new avatar representation that leverages powerful 2D CNNs and 3D Gaussian splatting to create high-fidelity avatars. To associate 3D Gaussians with the animatable avatar, we learn a parametric template from the input videos, and then parameterize the template on two front & back canonical Gaussian maps where each pixel represents a 3D Gaussian. The learned template is adaptive to the wearing garments for modeling looser clothes like dresses. Such template-guided 2D parameterization enables us to employ a powerful StyleGAN-based CNN to learn the pose-dependent Gaussian maps for modeling detailed dynamic appearances. Furthermore, we introduce a pose projection strategy for better generalization given novel poses. Overall, our method can create lifelike avatars with dynamic, realistic and generalized appearances. Experiments show that our method outperforms other state-of-the-art approaches.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2311.16096v3" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.jpg"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="overview.jpg"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="THuman4" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/THUman4.0-Dataset" target="_blank">}}
{{<badge label="test" message="AvatarReX" color="gold" style="plastic" logo="github" link="https://github.com/lizhe00/AnimatableGaussians/blob/master/AVATARREX_DATASET.md" target="_blank">}}
{{<badge label="test" message="ActorsHQ" color="silver" logo="link" link="https://actors-hq.com/#dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="TAVA" color="coral" logo="github" link="facebookresearch/tava" target="_blank">}}
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}
{{<badge label="body--NeRF" message="AvatarReX" color="gold" logo="github" link="" target="_blank">}}


#### Performance
{{<badge label="train" message="2d" color="informational" logo="link" >}}
{{<badge label="train" message="RTX4090" color="informational" logo="link" >}}

{{<badge label="render" message="40ms" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="render" message="1024_x_1024" color="informational" logo="link" >}}
