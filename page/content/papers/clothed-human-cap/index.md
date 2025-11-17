---
date: 2023-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: ClothedHumanCap
categories: ["papers"]
tags: ["nerf", "smpl", "clothing", "deformation", "monocular", "cvpr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Clothed Human Performance Capture with a Double-layer Neural Radiance Fields"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 29
---

## Clothed Human Performance Capture with a Double-layer Neural Radiance Fields

> Kangkan Wang, Guofeng Zhang, Suxu Cong, Jian Yang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="wangkangkan/ClothedHumanCap" >}}

### Abstract
{{< lead >}}
This paper addresses the challenge of capturing performance for the clothed humans from sparse-view or monocular videos. Previous methods capture the performance of full humans with a personalized template or recover the garments from a single frame with static human poses. However, it is inconvenient to extract cloth semantics and capture clothing motion with one-piece template, while single frame-based methods may suffer from instable tracking across videos. To address these problems, we propose a novel method for human performance capture by tracking clothing and human body motion separately with a doublelayer neural radiance fields (NeRFs). Specifically, we propose a double-layer NeRFs for the body and garments, and track the densely deforming template of the clothing and body by jointly optimizing the deformation fields and the canonical double-layer NeRFs. In the optimization, we introduce a physics-aware cloth simulation network which can help generate physically plausible cloth dynamics and body-cloth interactions. Compared with existing methods, our method is fully differentiable and can capture both the body and clothing motion robustly from dynamic videos. Also, our method represents the clothing with an independent NeRFs, allowing us to model implicit fields of general clothes feasibly. The experimental evaluations validate its effectiveness on real multi-view or monocular videos.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2023/papers/Wang_Clothed_Human_Performance_Capture_With_a_Double-Layer_Neural_Radiance_Fields_CVPR_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach


{{< figure
    src="teaser.png"
    alt="ClothedHumanCap teaser"
    caption="`ClothedHumanCap` teaser."
    >}}

{{< figure
    src="pipeline.png"
    alt="ClothedHumanCap overview"
    caption="`ClothedHumanCap` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="DeepCap" color="cyan" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="test" message="DeepCap" color="lightsalmon" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="NerfCap" color="lightslategray" logo="link" link="https://github.com/wangkangkan/nerfcap" target="_blank">}}

#### Performance
{{<badge label="train" message="12h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX2080Ti" color="informational" logo="link" >}}