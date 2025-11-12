---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: ASH
categories: ["papers"]
tags: ["splats", "skeleton", "texture", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "ASH: Animatable Gaussian Splats for Efficient and Photoreal Human Rendering"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 5
---

## `ASH`: Animatable Gaussian Splats for Efficient and Photoreal Human Rendering

> Haokai Pang, Heming Zhu, Adam Kortylewski, Christian Theobalt, Marc Habermann

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="kv2000/ASH" >}}

### Abstract
{{< lead >}}
Real-time rendering of photorealistic and controllable human avatars stands as a cornerstone in Computer Vision and Graphics. While recent advances in neural implicit rendering have unlocked unprecedented photorealism for digital avatars, real-time performance has mostly been demonstrated for static scenes only. To address this, we propose ASH, an Animatable Gaussian Splatting approach for photorealistic rendering of dynamic Humans in real time. We parameterize the clothed human as animatable 3D Gaussians, which can be efficiently splatted into image space to generate the final rendering. However, naively learning the Gaussian parameters in 3D space poses a severe challenge in terms of compute. Instead, we attach the Gaussians onto a deformable character model, and learn their parameters in 2D texture space, which allows leveraging efficient 2D convolutional architectures that easily scale with the required number of Gaussians. We benchmark ASH with competing methods on pose-controllable avatars, demonstrating that our method outperforms existing real-time methods by a large margin and shows comparable or even better results than offline methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2312.05941" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="ASH teaser"
    caption="`ASH` teaser."
    >}}

{{< figure
    src="method.jpg"
    alt="ASH method"
    caption="`ASH` method."
    >}}

### Results

#### Data
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="TAVA" color="coral" logo="github" link="facebookresearch/tava" target="_blank">}}
{{<badge label="skeleton--NeRF" message="NeuralActor" color="blue" logo="github" link="lingjie0206/Neural_Actor_Main_Code" target="_blank">}}
{{<badge label="skeleton--NeRF" message="HDHumans" color="cyan" logo="link" target="_blank">}}

#### Performance
{{<badge label="render" message="33ms" color="informational" logo="link" >}}
{{<badge label="render" message="A100" color="informational" logo="link" >}}
{{<badge label="render" message="1285_×_940" color="informational" logo="link" >}}