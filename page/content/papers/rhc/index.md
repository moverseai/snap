---
date: 2025-12-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: RHC
categories: ["papers"]
tags: ["splats", "skeleton", "texture", "relight", "arxiv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 35
---

## Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views

> Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Relight {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
We present Relightable Holoported Characters (RHC), a novel person-specific method for free-view rendering and relighting of full-body and highly dynamic humans solely observed from sparse-view RGB videos at inference. In contrast to classical one-light-at-a-time (OLAT)-based human relighting, our transformer-based RelightNet predicts relit appearance within a single network pass, avoiding costly OLAT-basis capture and generation. For training such a model, we introduce a new capture strategy and dataset recorded in a multi-view lightstage, where we alternate frames lit by random environment maps with uniformly lit tracking frames, simultaneously enabling accurate motion tracking and diverse illumination as well as dynamics coverage. Inspired by the rendering equation, we derive physics-informed features that encode geometry, albedo, shading, and the virtual camera view from a coarse human mesh proxy and the input views. Our RelightNet then takes these features as input and cross-attends them with a novel lighting condition, and regresses the relit appearance in the form of texel-aligned 3D Gaussian splats attached to the coarse mesh proxy. Consequently, our RelightNet implicitly learns to efficiently compute the rendering equation for novel lighting conditions within a single feed-forward pass. Experiments demonstrate our method’s superior visual fidelity and lighting reproduction compared to state-of-the-art approaches.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2512.00255" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="RHC teaser"
    caption="`RHC` teaser."
    >}}

{{< figure
    src="method.jpg"
    alt="RHC overview"
    caption="`RHC` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="RHC" color="darkorange" style="plastic" logo="link" link="https://vcai.mpi-inf.mpg.de/projects/RHC/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="Relighting4D" color="yellow" logo="github" link="FrozenBurning/Relighting4D" target="_blank">}}
{{<badge label="body--Splats" message="MeshAvatar" color="limegreen" logo="github" link="https://github.com/shad0wta9/meshavatar" target="_blank">}}
{{<badge label="body--Splats" message="IntrinsicAvatar" color="azure" logo="github" link="https://github.com/taconite/IntrinsicAvatar" target="_blank">}}
{{<badge label="test" message="HoloChar" color="darkblue" logo="github" link="https://vcai.mpi-inf.mpg.de/projects/holochar/" target="_blank">}}



#### Performance

{{<badge label="train" message="4_x_H100" color="informational" logo="link" >}}
