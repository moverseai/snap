---
date: 2025-08-28T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Snap-Snap
categories: ["papers"]
tags: ["splats", "smplx", "generalized", "arxiv25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "Snap-Snap: Taking Two Views to Reconstruct Human 3D Gaussians in Milliseconds"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 32
---

## `Snap-Snap`: Taking Two Views to Reconstruct Human 3D Gaussians in Milliseconds

> Jia Lu, Taoran Yi, Jiemin Fang, Chen Yang, Chuiyun Wu, Wei Shen, Wenyu Liu, Qi Tian, Xinggang Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="hustvl/Snap-Snap" >}}

### Abstract
{{< lead >}}
Reconstructing 3D human bodies from sparse views has been an appealing topic, which is crucial to broader the related applications. In this paper, we propose a quite challenging but valuable task to reconstruct the human body from only two images, i.e., the front and back view, which can largely lower the barrier for users to create their own 3D digital humans. The main challenges lie in the difficulty of building 3D consistency and recovering missing information from the highly sparse input. We redesign a geometry reconstruction model based on foundation reconstruction models to predict consistent point clouds even input images have scarce overlaps with extensive human data training. Furthermore, an enhancement algorithm is applied to supplement the missing color information, and then the complete human point clouds with colors can be obtained, which are directly transformed into 3D Gaussians for better rendering quality. Experiments show that our method can reconstruct the entire human in 190 ms on a single NVIDIA RTX 4090, with two images at a resolution of 1024×1024, demonstrating state-of-the-art performance on the THuman2.0 and cross-domain datasets. Additionally, our method can complete human reconstruction even with images captured by low-cost mobile devices, reducing the requirements for data collection.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2508.14892" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="SNAP-SNAP teaser"
    caption="`SNAP-SNAP` teaser."
    >}}


{{< figure
    src="method.png"
    alt="SNAP-SNAP overview"
    caption="`SNAP-SNAP` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="2K2K" color="lawngreen" logo="github" link="https://github.com/SangHunHan92/2K2K" target="_blank">}}
{{<badge label="test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}
{{<badge label="test" message="4D--DRESS" color="orange" logo="link" link="https://4d-dress.ait.ethz.ch/" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="GHG" color="plum" logo="github" link="https://github.com/humansensinglab/Generalizable-Human-Gaussians" target="_blank">}}

#### Performance
{{<badge label="train" message="RTX4090" color="informational" logo="link" >}}
{{<badge label="train" message="19h" color="informational" logo="link" >}}

{{<badge label="inference" message="RTX4090" color="informational" logo="link" >}}
{{<badge label="inference" message="190ms" color="informational" logo="link" >}}