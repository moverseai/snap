---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: InstantAvatar
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "cvpr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "InstantAvatar: Learning Avatars from Monocular Video in 60 Seconds"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 1
---

## `InstantAvatar`: Learning Avatars from Monocular Video in 60 Seconds

> Tianjian Jiang, Xu Chen, Jie Song, Otmar Hilliges

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL  {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="tijiang13/InstantAvatar" >}}

### Abstract
{{< lead >}}
In this paper, we take a significant step towards realworld applicability of monocular neural avatar reconstruction by contributing InstantAvatar, a system that can reconstruct human avatars from a monocular video within seconds, and these avatars can be animated and rendered at an interactive rate. To achieve this efficiency we propose a carefully designed and engineered system, that leverages emerging acceleration structures for neural fields, in combination with an efficient empty space-skipping strategy for dynamic scenes. We also contribute an efficient implementation that we will make available for research purposes. Compared to existing methods, InstantAvatar converges 130× faster and can be trained in minutes instead of hours. It achieves comparable or even better reconstruction quality and novel pose synthesis results. When given the same time budget, our method significantly outperforms SoTA methods. InstantAvatar can yield acceptable visual quality in as little as 10 seconds training time.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2212.10550" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="InstantAvatar overview"
    caption="`InstantAvatar` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="Anim--NeRF" color="yellow" logo="github" link="https://github.com/JanaldoChen/Anim-NeRF" target="_blank">}}

#### Performance
{{<badge label="train" message="60sec" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="render" message="66ms" color="informational" logo="link" >}}
{{<badge label="render" message="540_x_540" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3090" color="informational" logo="link" >}}