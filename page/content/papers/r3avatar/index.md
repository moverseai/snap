---
date: 2025-03-10T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: R3-Avatar
categories: ["papers"]
tags: ["splats", "smplx", "deformation", "arxiv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "R3-Avatar: Record and Retrieve Temporal Codebook for Reconstructing Photorealistic Human Avatars"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 11
---

## `R3-Avatar`: Record and Retrieve Temporal Codebook for Reconstructing Photorealistic Human Avatars

> Yifan Zhan, Wangze Xu, Qingtian Zhu, Muyao Niu, Mingze Ma, Yifei Liu, Zhihang Zhong, Xiao Sun, Yinqiang Zheng

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="Yifever20002/R3Avatars" >}}

### Abstract
{{< lead >}}
We present R3-Avatar, incorporating a temporal codebook, to overcome the inability of human avatars to be both animatable and of high-fidelity rendering quality. Existing video-based reconstruction of 3D human avatars either focuses solely on rendering, lacking animation support, or learns a pose-appearance mapping for animating, which degrades under limited training poses or complex clothing. In this paper, we adopt a “record-retrieve-reconstruct” strategy that ensures high-quality rendering from novel views while mitigating degradation in novel poses. Specifically, disambiguating timestamps record temporal appearance variations in a codebook, ensuring high-fidelity novel-view rendering, while novel poses retrieve corresponding timestamps by matching the most similar training poses for augmented appearance. Our R3-Avatar outperforms cutting-edge video-based human avatar reconstruction, particularly in overcoming visual quality degradation in extreme scenarios with limited training human poses and complex clothing.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2503.12751" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="method.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="HiFi4G" color="lightpink" logo="github" link="https://github.com/moqiyinlun/HiFi4G_Dataset" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DNA--Rendering" color="darkorange" style="plastic" logo="github" link="https://dna-rendering.github.io/" target="_blank">}}
{{<badge label="test" message="MVHumanNet" color="thistle" logo="github" link="https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="SplattingAvatar" color="lemonchiffon" logo="github" link="https://github.com/initialneil/SplattingAvatar" target="_blank">}}
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}
{{<badge label="body--Splats" message="DyCo" color="lightpink" logo="github" link="https://github.com/Yifever20002/Dyco" target="_blank">}}

#### Performance

{{<badge label="train" message="90mins" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}

{{<badge label="render" message="16ms" color="informational" logo="link" >}}
