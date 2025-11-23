---
date: 2025-08-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HumanRAM
categories: ["papers"]
tags: ["smplx", "texture", "monocular", "siggraph25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "HumanRAM: Feed-forward Human Reconstruction and Animation Model using Transformers"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 22
---

## `HumanRAM`: Feed-forward Human Reconstruction and Animation Model using Transformers

> Zhiyuan Yu, Zhe Li, Hujun Bao, Can Yang, Xiaowei Zhou

{{< keywordList >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH* 2025 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
3D human reconstruction and animation are long-standing topics in computer graphics and vision. However, existing methods typically rely on sophisticated dense-view capture and/or time-consuming per-subject optimization procedures. To address these limitations, we propose HumanRAM, a novel feed-forward approach for generalizable human reconstruction and animation from monocular or sparse human images. Our approach integrates human reconstruction and animation into a unified framework by introducing explicit pose conditions, parameterized by a shared SMPL-X neural texture, into transformer-based large reconstruction models (LRM). Given monocular or sparse input images with associated camera parameters and SMPL-X poses, our model employs scalable transformers and a DPT-based decoder to synthesize realistic human renderings under novel viewpoints and novel poses. By leveraging the explicit pose conditions, our model simultaneously enables high-quality human reconstruction and high-fidelity pose-controlled animation. Experiments show that HumanRAM significantly surpasses previous methods in terms of reconstruction accuracy, animation fidelity, and generalization performance on real-world datasets.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2506.03118" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.gif"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}


{{< figure
    src="method.jpg"
    alt="Method"
    caption="Method."
    >}}

{{< figure
    src="overview.jpg"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="Human4DiT" color="orchid" style="plastic" logo="github" link="https://human4dit.github.io/" target="_blank">}}
{{<badge label="test" message="ActorsHQ" color="silver" logo="link" link="https://actors-hq.com/#dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="GHG" color="plum" logo="github" link="https://github.com/humansensinglab/Generalizable-Human-Gaussians" target="_blank">}}
{{<badge label="body--NeRF" message="SHERF" color="mediumblue" logo="github" link="https://github.com/skhu101/SHERF" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--NeRF" message="NNA" color="seagreen" logo="github" link="https://github.com/Talegqz/neural_novel_actor" target="_blank">}}

