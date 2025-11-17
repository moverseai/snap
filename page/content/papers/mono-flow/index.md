---
date: 2022-04-25T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: MoCo-Flow
categories: ["papers"]
tags: ["nerf", "smpl", "texture", "deformation", "monocular", "eurographics22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "MoCo-Flow: Neural Motion Consensus Flow for Dynamic Humans in Stationary Monocular Cameras"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 28
---

## `MoCo-Flow`: Neural Motion Consensus Flow for Dynamic Humans in Stationary Monocular Cameras

> Xuelin Chen, Weiyu Li, Daniel Cohen-Or, Niloy J. Mitra, Baoquan Chen

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *Eurographics* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="wyysf-98/MoCo_Flow" >}}

### Abstract
{{< lead >}}
Synthesizing novel views of dynamic humans from stationary monocular cameras is a popular scenario. This is particularly attractive as it does not require static scenes, controlled environments, or specialized hardware. In contrast to techniques that exploit multi-view observations to constrain the modeling, given a single fixed viewpoint only, the problem of modeling the dynamic scene is significantly more under-constrained and ill-posed. In this paper, we introduce Neural Motion Consensus Flow (MoCo-Flow), a representation that models the dynamic scene using a 4D continuous time-variant function. The proposed representation is learned by an optimization which models a dynamic scene that minimizes the error of rendering all observation images. At the heart of our work lies a novel optimization formulation, which is constrained by a motion consensus regularization on the motion flow. We extensively evaluate MoCo-Flow on several datasets that contain human motions of varying complexity, and compare, both qualitatively and quantitatively, to several baseline methods and variants of our methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2106.04477" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="MoCo-Flow teaser"
    caption="`MoCo-Flow` teaser."
    >}}

{{< figure
    src="method.png"
    alt="MoCo-Flow overview"
    caption="`MoCo-Flow` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="AIST++" color="navy" logo="github" link="https://google.github.io/aistplusplus_dataset/factsfigures.html" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}