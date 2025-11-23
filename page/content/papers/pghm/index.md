---
date: 2025-11-20T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: PGHM
categories: ["papers"]
tags: ["splats", "smplx", "generalized", "texture", "monocular", "3dv26"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling"
summary: TODO
keywords: #
type: '2026' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2026"]
series_order: 2
---

## Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling

> Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *3DV* 2026 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="pengc02/pghm/" >}} -->

### Abstract
{{< lead >}}
Photorealistic and animatable human avatars are a key enabler for virtual/augmented reality, telepresence, and digital entertainment. While recent advances in 3D Gaussian Splatting (3DGS) have greatly improved rendering quality and efficiency, existing methods still face fundamental challenges, including time-consuming per-subject optimization and poor generalization under sparse monocular inputs. In this work, we present the Parametric Gaussian Human Model (PGHM), a generalizable and efficient framework that integrates human priors into 3DGS for fast and high-fidelity avatar reconstruction from monocular videos. PGHM introduces two core components: (1) a UV-aligned latent identity map that compactly encodes subject-specific geometry and appearance into a learnable feature tensor; and (2) a Disentangled Multi-Head U-Net that predicts Gaussian attributes by decomposing static, pose-dependent, and view-dependent components via conditioned decoders. This design enables robust rendering quality under challenging poses and viewpoints, while allowing efficient subject adaptation without requiring multi-view capture or long optimization time. Experiments show that PGHM is significantly more efficient than optimization-from-scratch methods, requiring only approximately 20 minutes per subject to produce avatars with comparable visual quality, thereby demonstrating its practical applicability for real-world monocular avatar creation.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2506.06645" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.jpg"
    alt="PGHM teaser"
    caption="`PGHM` teaser."
    >}}

{{< figure
    src="pipeline.jpg"
    alt="PGHM overview"
    caption="`PGHM` overview."
    >}}

### Results

#### Data
{{<badge label="train" message="DNA--Rendering" color="darkorange" style="plastic" logo="github" link="https://dna-rendering.github.io/" target="_blank">}}
{{<badge label="train" message="MVHumanNet" color="thistle" logo="github" link="https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet" target="_blank">}}
{{<badge label="test" message="THuman4" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/THUman4.0-Dataset" target="_blank">}}
{{<badge label="test" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="HumanNeRF" color="blue" logo="github" link="chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--Splats" message="ExAvatar" color="steelblue" logo="github" link="https://github.com/mks0601/ExAvatar_RELEASE" target="_blank">}}


#### Performance
{{<badge label="train" message="20mins" color="informational" logo="link" >}}
{{<badge label="train" message="V100" color="informational" logo="link" >}}
