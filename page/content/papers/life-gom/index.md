---
date: 2025-04-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: LIFe-GoM
categories: ["papers"]
tags: ["splats", "smplx", "generalized", "monocular", "iclr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "LIFe-GoM: Generalizable Human Rendering with Learned Iterative Feedback Over Multi-Resolution Gaussians-on-Mesh"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 26
---

## `LIFe-GoM`: Generalizable Human Rendering with Learned Iterative Feedback Over Multi-Resolution Gaussians-on-Mesh

> Jing Wen, Alexander G. Schwing, Shenlong Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ICLR* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="wenj/LIFe-GoM" >}}

### Abstract
{{< lead >}}
Generalizable rendering of an animatable human avatar from sparse inputs relies on data priors and inductive biases extracted from training on large data to avoid scene-specific optimization and to enable fast reconstruction. This raises two main challenges: First, unlike iterative gradient-based adjustment in scene-specific optimization, generalizable methods must reconstruct the human shape representation in a single pass at inference time. Second, rendering is preferably computationally efficient yet of high resolution. To address both challenges we augment the recently proposed dual shape representation, which combines the benefits of a mesh and Gaussian points, in two ways. To improve reconstruction, we propose an iterative feedback update framework, which successively improves the canonical human shape representation during reconstruction. To achieve computationally efficient yet high-resolution rendering, we study a coupled-multi-resolution Gaussians-on-Mesh representation. We evaluate the proposed approach on the challenging THuman2.0, XHuman and AIST++ data. Our approach reconstructs an animatable representation from sparse inputs in less than 1s, renders views with 95.1FPS at 1024x1024, and achieves PSNR/LPIPS*/FID of 24.65/110.82/51.27 on THuman2.0, outperforming the state-of-the-art in rendering quality.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2502.09617" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="LIFe-GoM teaser"
    caption="`LIFe-GoM` teaser."
    >}}


{{< figure
    src="method.png"
    alt="LIFe-GoM overview"
    caption="`LIFe-GoM` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="X--Humans" color="goldenrod" logo="github" link="https://xhumans.ait.ethz.ch/" target="_blank">}}
{{<badge label="test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}
{{<badge label="test" message="AIST++" color="navy" logo="github" link="https://google.github.io/aistplusplus_dataset/factsfigures.html" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}
{{<badge label="body--Splats" message="GHG" color="plum" logo="github" link="https://github.com/humansensinglab/Generalizable-Human-Gaussians" target="_blank">}}
{{<badge label="body--Splats" message="GoMAvatar" color="bisque" logo="github" link="https://github.com/wenj/GoMAvatar" target="_blank">}}
{{<badge label="body--Splats" message="iHuman" color="crimson" logo="github" link="https://github.com/pramishp/ihuman" target="_blank">}}
{{<badge label="body--NeRF" message="NIA" color="orangered" logo="github" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="ActorsNeRF" color="hotpink" logo="github" link="https://github.com/JitengMu/ActorsNeRF" target="_blank">}}

#### Performance
{{<badge label="render" message="10ms" color="informational" logo="link" >}}
{{<badge label="render" message="1024_x_1024" color="informational" logo="link" >}}
{{<badge label="render" message="A100" color="informational" logo="link" >}}