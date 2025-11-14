---
date: 2024-10-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: RNA
categories: ["papers"]
tags: ["nerf", "skeleton", "texture", "relight", "eccv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Relightable Neural Actor with Intrinsic Decomposition and Pose Control"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 5
---

## Relightable Neural Actor with Intrinsic Decomposition and Pose Control

> Diogo C. Luvizon, Vladislav Golyanik, Adam Kortylewski, Marc Habermann, Christian Theobalt

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Relight {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="dluvizon/relightable-neural-actor" >}}

### Abstract
{{< lead >}}
Creating a digital human avatar that is relightable, drivable, and photorealistic is a challenging and important problem in Vision and Graphics. Humans are highly articulated creating pose-dependent appearance effects like self-shadows and wrinkles, and skin as well as clothing require complex and space-varying BRDF models. While recent human relighting approaches can recover plausible material-light decompositions from multi-view video, they do not generalize to novel poses and still suffer from visual artifacts. To address this, we propose Relightable Neural Actor, the first video-based method for learning a photorealistic neural human model that can be relighted, allows appearance editing, and can be controlled by arbitrary skeletal poses. Importantly, for learning our human avatar, we solely require a multi-view recording of the human under a known, but static lighting condition. To achieve this, we represent the geometry of the actor with a drivable density field that models pose-dependent clothing deformations and provides a mapping between 3D and UV space, where normal, visibility, and materials are encoded. To evaluate our approach in real-world scenarios, we collect a new dataset with four actors recorded under different light conditions, indoors and outdoors, providing the first benchmark of its kind for human relighting, and demonstrating state-of-the-art relighting results for novel human poses.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2312.11587" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.jpg"
    alt="RNA teaser"
    caption="`RNA` teaser."
    >}}

{{< figure
    src="method.jpg"
    alt="RNA method"
    caption="`RNA` method."
    >}}

### Results

#### Data
{{<badge label="test" message="RDA" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/RNA" target="_blank">}}

#### Comparisons
{{<badge label="skeleton--NeRF" message="NeuralActor" color="blue" logo="github" link="lingjie0206/Neural_Actor_Main_Code" target="_blank">}}

#### Performance
{{<badge label="train" message="4_x_A40" color="informational" logo="link" >}}
{{<badge label="train" message="1d" color="informational" logo="link" >}}