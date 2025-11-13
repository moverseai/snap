---
date: 2025-01-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: BAGA
categories: ["papers"]
tags: ["splats", "smpl", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Bundle Adjusted Gaussian Avatars Deblurring"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 20
---

## Bundle Adjusted Gaussian Avatars Deblurring

> Muyao Niu, Yifan Zhan, Qingtian Zhu, Zhuoxiao Li, Wei Wang, Zhihang Zhong, Xiao Sun, Yinqiang Zheng

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
The development of 3D human avatars from multiview videos represents a significant yet challenging task in the field. Recent advancements, including 3D Gaussian Splattings (3DGS), have markedly progressed this domain. Nonetheless, existing techniques necessitate the use of high-quality sharp images, which are often impractical to obtain in real-world settings due to variations in human motion speed and intensity. In this study, we attempt to explore deriving sharp intrinsic 3D human Gaussian avatars from blurry video footage in an end-to-end manner. Our approach encompasses a 3D-aware, physics-oriented model of blur formation attributable to human movement, coupled with a 3D human motion model to clarify ambiguities found in motion-induced blurry images. This methodology facilitates the concurrent learning of avatar model parameters and the refinement of sub-frame motion parameters from a coarse initialization. We have established benchmarks for this task through a synthetic dataset derived from existing multi-view captures, alongside a real-captured dataset acquired through a 360-degree synchronous hybrid-exposure camera system. Comprehensive evaluations demonstrate that our model surpasses existing baselines.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2411.16758" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="BAGA overview"
    caption="`BAGA` overview."
    >}}

{{< figure
    src="method.png"
    alt="BAGA details"
    caption="`BAGA` details."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="BSHuman" color="moccasin" logo="link" link="https://github.com/MyNiuuu/BAGA" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}

#### Performance
{{<badge label="train" message="RTX4090" color="informational" logo="link" >}}

{{<badge label="render" message="612_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="RTX4090" color="informational" logo="link" >}}