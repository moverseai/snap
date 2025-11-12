---
date: 2023-12-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Deformable 3D Gaussian Splatting for Animatable Human Avatars
categories: ["papers"]
tags: ["splats", "smpl", "arXiv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Deformable 3D Gaussian Splatting for Animatable Human Avatars"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 23
---

## Deformable 3D Gaussian Splatting for Animatable Human Avatars

> HyunJun Jung, Nikolas Brasch, Jifei Song, Eduardo Perez-Pellitero, Yiren Zhou, Zhihao Li, Nassir Navab, Benjamin Busam

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Recent advances in neural radiance fields enable novel view synthesis of photo-realistic images in dynamic settings, which can be applied to scenarios with human animation. Commonly used implicit backbones to establish accurate models, however, require many input views and additional annotations such as human masks, UV maps and depth maps. In this work, we propose ParDy-Human (Parameterized Dynamic Human Avatar), a fully explicit approach to construct a digital avatar from as little as a single monocular sequence. ParDy-Human introduces parameter-driven dynamics into 3D Gaussian Splatting where 3D Gaussians are deformed by a human pose model to animate the avatar. Our method is composed of two parts: A first module that deforms canonical 3D Gaussians according to SMPL vertices and a consecutive module that further takes their designed joint encodings and predicts per Gaussian deformations to deal with dynamics beyond SMPL vertex deformations. Images are then synthesized by a rasterizer. ParDy-Human constitutes an explicit model for realistic dynamic human avatars which requires significantly fewer training views and images. Our avatars learning is free of additional annotations such as masks and can be trained with variable backgrounds while inferring full-resolution images efficiently even on consumer hardware. We provide experimental evidence to show that ParDy-Human outperforms state-of-the-art methods on ZJU-MoCap and THUman4.0 datasets both quantitatively and visually.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2312.15059" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="feature.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="method.png"
    alt="Method overview"
    caption="Method overview."
    >}}


{{< figure
    src="method2.png"
    alt="Method details"
    caption="Method details."
    >}}


{{< figure
    src="method3.png"
    alt="Method flow"
    caption="Method flow."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="THuman4" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/THUman4.0-Dataset" target="_blank">}}


#### Comparisons
{{<badge label="body--NeRF" message="UV Volumes" color="wheat" logo="github" link="https://github.com/fanegg/UV-Volumes" target="_blank">}}

#### Performance
{{<badge label="render" message="0.3sec" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3080" color="informational" logo="link" >}}
