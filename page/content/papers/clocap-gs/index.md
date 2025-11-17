---
date: 2025-07-30T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: CloCap-GS
categories: ["papers"]
tags: ["splats", "smpl", "clothing", "deformation", "monocular", "tip25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "CloCap-GS: Clothed Human Performance Capture With 3D Gaussian Splatting"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 5
---

## `CloCap-GS`: Clothed Human Performance Capture With 3D Gaussian Splatting


> Kangkan Wang, Chong Wang, Jian Yang, Guofeng Zhang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *TIP* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="wangkangkan/CloCap-GS" >}}

### Abstract
{{< lead >}}
Capturing the human body and clothing from videos has obtained significant progress in recent years, but several challenges remain to be addressed. Previous methods reconstruct the 3D bodies and garments from videos with self-rotating human motions or capture the body and clothing separately based on neural implicit fields. However, the reconstruction methods for self-rotating motions may cause instable tracking on dynamic videos with arbitrary human motions, while implicit fields based methods are limited to inefficient rendering and low quality synthesis. To solve these problems, we propose a new method, called CloCap-GS, for clothed human performance capture with 3D Gaussian Splatting. Specifically, we align 3D Gaussians with the deforming geometries of body and clothing, and leverage photometric constraints formed by matching Gaussians renderings with input video frames to recover temporal deformations of the dense template geometry. The geometry deformations and Gaussians properties of both the body and clothing are optimized jointly, achieving both dense geometry tracking and novel-view synthesis. In addition, we introduce a physics-aware material-varying cloth model to preserve physically-plausible cloth dynamics and body-clothing interactions that is pre-trained in a self-supervised manner without preparing training data. Compared with the existing methods, our method improves the accuracy of dense geometry tracking and quality of novel-view synthesis for a variety of daily garment types (e.g., loose clothes). Extensive experiments in both quantitative and qualitative evaluations demonstrate the effectiveness of CloCap-GS on real sparse-view or monocular videos.
{{< /lead >}}

{{< button href="https://ieeexplore.ieee.org/document/11104970" target="_blank" >}}
Paper
{{< /button >}}

### Approach


{{< figure
    src="teaser.png"
    alt="ClothedHumanCap teaser"
    caption="`CloCap-GS` teaser."
    >}}

{{< figure
    src="overview.jpg"
    alt="ClothedHumanCap overview"
    caption="`CloCap-GS` overview."
    >}}

