---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NeuralHumanPerfomer
categories: ["papers"]
tags: ["nerf", "smpl", "neurips21"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Neural Human Performer: Learning Generalizable Radiance Fields for Human Performance Rendering"
summary: TODO
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 6
---

## `Neural Human Performer`: Learning Generalizable Radiance Fields for Human Performance Rendering

> Youngjoong Kwon, Dahun Kim, Duygu Ceylan, Henry Fuchs

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *NeurIPS* 2021 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="YoungJoongUNC/Neural_Human_Performer" >}}

### Abstract
{{< lead >}}
In this paper, we aim at synthesizing a free-viewpoint video of an arbitrary human
performance using sparse multi-view cameras. Recently, several works have addressed this problem by learning person-specific neural radiance fields (NeRF) to capture the appearance of a particular human. In parallel, some work proposed to use pixel-aligned features to generalize radiance fields to arbitrary new scenes and objects. Adopting such generalization approaches to humans, however, is highly challenging due to the heavy occlusions and dynamic articulations of body parts. To tackle this, we propose Neural Human Performer, a novel approach that learns generalizable neural radiance fields based on a parametric human body model for robust performance capture. Specifically, we first introduce a temporal transformer that aggregates tracked visual features based on the skeletal body motion over time. Moreover, a multi-view transformer is proposed to perform cross-attention between the temporally-fused features and the pixel-aligned features at each time step to integrate observations on the fly from multiple views. Experiments on the ZJU-MoCap and AIST datasets show that our method significantly outperforms recent generalizable NeRF methods on unseen identities and poses.
{{< /lead >}}

{{< button href="https://proceedings.neurips.cc/paper/2021/file/cf866614b6b18cda13fe699a3a65661b-Paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="Neural Human Performer overview"
    caption="`Neural Human Performer` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="AIST++" color="navy" logo="github" link="https://google.github.io/aistplusplus_dataset/factsfigures.html" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}