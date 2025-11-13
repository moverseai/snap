---
date: 2024-11-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HFGaussian
categories: ["papers"]
tags: ["splats", "generalized", "smplx", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "HFGaussian: Learning Generalizable Gaussian Human with Integrated Human Features"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 11
---

## `HFGaussian`: Learning Generalizable Gaussian Human with Integrated Human Features

> Arnab Dey, Cheng-You Lu, Andrew I. Comport, Srinath Sridhar, Chin-Teng Lin, Jean Martinet

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Recent advancements in radiance field rendering show promising results in 3D scene representation, where Gaussian splatting-based techniques emerge as state-of-the-art due to their quality and efficiency. Gaussian splatting is widely used for various applications, including 3D human representation. However, previous 3D Gaussian splatting methods either use parametric body models as additional information or fail to provide any underlying structure, like human biomechanical features, which are essential for different applications. In this paper, we present a novel approach called HFGaussian that can estimate novel views and human features, such as the 3D skeleton, 3D key points, and dense pose, from sparse input images in real time at 25 FPS. The proposed method leverages generalizable Gaussian splatting technique to represent the human subject and its associated features, enabling efficient and generalizable reconstruction. By incorporating a pose regression network and the feature splatting technique with Gaussian splatting, HFGaussian demonstrates improved capabilities over existing 3D human methods, showcasing the potential of 3D human representations with integrated biomechanics. We thoroughly evaluate our HFGaussian method against the latest state-of-the-art techniques in human Gaussian splatting and pose estimation, demonstrating its real-time, state-of-the-art performance.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2411.03086" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="HFGaussian overview"
    caption="`HFGaussian` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="THuman4" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/THUman4.0-Dataset" target="_blank">}}
{{<badge label="test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="ENeRF" color="lightcoral" logo="github" link="https://github.com/zju3dv/ENeRF" target="_blank">}}
{{<badge label="body--NeRF" message="GHNeRF" color="orchid" logo="github" link="https://github.com/skhu101/SHERF" target="_blank">}}

#### Performance

{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="41ms" color="informational" logo="link" >}}