---
date: 2024-10-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: MeshAvatar
categories: ["papers"]
tags: ["nerf", "smpl", "smplx", "texture", "relight", "eccv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "MeshAvatar: Learning High-quality Triangular Human Avatars from Multi-view Videos"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 26
---

## `MeshAvatar`: Learning High-quality Triangular Human Avatars from Multi-view Videos

> Yushuo Chen, Zerong Zheng, Zhe Li, Chao Xu, Yebin Liu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Relight {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="shad0wta9/meshavatar" >}}

### Abstract
{{< lead >}}
We present a novel pipeline for learning high-quality triangular human avatars from multi-view videos. Recent methods for avatar learning are typically based on neural radiance fields (NeRF), which is not compatible with traditional graphics pipeline and poses great challenges for operations like editing or synthesizing under different environments. To overcome these limitations, our method represents the avatar with an explicit triangular mesh extracted from an implicit SDF field, complemented by an implicit material field conditioned on given poses. Leveraging this triangular avatar representation, we incorporate physics-based rendering to accurately decompose geometry and texture. To enhance both the geometric and appearance details, we further employ a 2D UNet as the network backbone and introduce pseudo normal ground-truth as additional supervision. Experiments show that our method can learn triangular avatars with high-quality geometry reconstruction and plausible material decomposition, inherently supporting editing, manipulation or relighting operations.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2407.08414" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="overview.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="AvatarReX" color="gold" style="plastic" logo="github" link="https://github.com/lizhe00/AnimatableGaussians/blob/master/AVATARREX_DATASET.md" target="_blank">}}
{{<badge label="test" message="ActorsHQ" color="silver" logo="link" link="https://actors-hq.com/#dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}
{{<badge label="body--NeRF" message="AvatarReX" color="gold" logo="github" link="" target="_blank">}}


#### Performance
{{<badge label="train" message="16h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}

{{<badge label="render" message="180ms" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
