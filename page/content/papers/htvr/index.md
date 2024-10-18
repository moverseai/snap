---
date: 2022-09-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HTVR
categories: ["papers"]
tags: ["nerf", "texture", "smpl", "3dv22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "HVTR: Hybrid Volumetric-Textural Rendering for Human Avatars"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 9
---

## `HVTR`: Hybrid Volumetric-Textural Rendering for Human Avatars

> Tao Hu, Tao Yu, Zerong Zheng, He Zhang, Yebin Liu, Matthias Zwicker

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *3DV* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="TaoHuUMD/SurMo" >}}

### Abstract
{{< lead >}}
We propose a novel neural rendering pipeline, Hybrid Volumetric-Textural Rendering (HVTR), which synthesizes virtual human avatars from arbitrary poses efficiently and at high quality. First, we learn to encode articulated human motions on a dense UV manifold of the human body surface. To handle complicated motions (e.g., self-occlusions), we then leverage the encoded information on the UV manifold to construct a 3D volumetric representation based on a dynamic pose-conditioned neural radiance field. While this allows us to represent 3D geometry with changing topology, volumetric rendering is computationally heavy. Hence we employ only a rough volumetric representation using a pose-conditioned downsampled neural radiance field (PDNeRF), which we can render efficiently at low resolutions. In addition, we learn 2D textural features that are fused with rendered volumetric features in image space. The key advantage of our approach is that we can then convert the fused features into a high-resolution, high-quality avatar by a fast GAN-based textural renderer. We demonstrate that hybrid rendering enables HVTR to handle complicated motions, render high-quality avatars under usercontrolled poses/shapes and even loose clothing, and most importantly, be efficient at inference time. Our experimental results also demonstrate state-of-the-art quantitative results
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2112.10203" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="HTVR overview"
    caption="`HTVR` overview."
    >}}

{{< figure
    src="method.png"
    alt="HTVR details"
    caption="`HTVR` details."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="40h" color="informational" logo="link" >}}
{{<badge label="train" message="P6000" color="informational" logo="link" >}}
