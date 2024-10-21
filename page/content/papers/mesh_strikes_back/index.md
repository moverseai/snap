---
date: 2023-03-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Mesh Strikes Back
categories: ["papers"]
tags: ["smpl", "texture", "arxiv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Mesh Strikes Back: Fast and Efficient Human Reconstruction from RGB videos"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 7
---

## `Mesh Strikes Back`: Fast and Efficient Human Reconstruction from RGB videos

> Rohit Jena1, Pratik Chaudhari, James C. Gee, Ganesh Iyer, Siddharth Choudhary, Brandon M. Smith

{{< keywordList >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Human reconstruction and synthesis from monocular RGB videos is a challenging problem due to clothing, occlusion, texture discontinuities and sharpness, and framespecific pose changes. Many methods employ deferred rendering, NeRFs and implicit methods to represent clothed humans, on the premise that mesh-based representations cannot capture complex clothing and textures from RGB, silhouettes, and keypoints alone. We provide a counter viewpoint to this fundamental premise by optimizing a SMPL+D mesh and an efficient, multi-resolution texture representation using only RGB images, binary silhouettes and sparse 2D keypoints. Experimental results demonstrate that our approach is more capable of capturing geometric details compared to visual hull, mesh-based methods. We show competitive novel view synthesis and improvements in novel pose synthesis compared to NeRF-based methods, which introduce noticeable, unwanted artifacts. By restricting the solution space to the SMPL+D model combined with differentiable rendering, we obtain dramatic speedups in compute, training times (up to 24x) and inference times (up to 192x). Our method therefore can be used as is or as a fast initialization to NeRF-based methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2303.08808" target="_blank" >}}
Paper
{{< /button >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}

#### Performance
{{<badge label="train" message="40mins" color="informational" logo="link" >}}
{{<badge label="render" message="60ms" color="informational" logo="link" >}}
