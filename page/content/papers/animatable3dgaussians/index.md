---
date: 2024-03-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Animatable 3D Gaussian
categories: ["papers"]
tags: ["splats", "smpl", "acmmm24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Animatable 3D Gaussian: Fast and High-Quality Reconstruction of Multiple Human Avatars"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 8
---

## Animatable 3D Gaussian: Fast and High-Quality Reconstruction of Multiple Human Avatars

> Yang Liu, Xiang Huang, Minghan Qin, Qinwei Lin, Haoqian Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *ACM Multimedia* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="jimmyYliu/Animatable-3d-Gaussian" >}}

### Abstract
{{< lead >}}
Neural radiance fields are capable of reconstructing high-quality drivable human avatars but are expensive to train and render and not suitable for multi-human scenes with complex shadows. To reduce consumption, we propose Animatable 3D Gaussian, which learns human avatars from input images and poses. We extend 3D Gaussians to dynamic human scenes by modeling a set of skinned 3D Gaussians and a corresponding skeleton in canonical space and deforming 3D Gaussians to posed space according to the input poses. We introduce a multi-head hash encoder for pose-dependent shape and appearance and a time-dependent ambient occlusion module to achieve high-quality reconstructions in scenes containing complex motions and dynamic shadows. On both novel view synthesis and novel pose synthesis tasks, our method achieves higher reconstruction quality than InstantAvatar with less training time (1/60), less GPU memory (1/4), and faster rendering speed (7x). Our method can be easily extended to multi-human scenes and achieve comparable novel view synthesis results on a scene with ten people in only 25 seconds of training.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2311.16482" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="method.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="MonoHuman" color="darkmagenta" logo="github" link="https://github.com/Yzmblog/MonoHuman" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}


#### Performance
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}

{{<badge label="render" message="9ms" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
