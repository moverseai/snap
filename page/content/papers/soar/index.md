---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SOAR
categories: ["papers"]
tags: ["splats", "smplx", "monocular", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "SOAR: Self-Occluded Avatar Recovery from a Single Video In the Wild"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 9
---

## `SOAR`: Self-Occluded Avatar Recovery from a Single Video In the Wild

> Zhuoyang Pan, Angjoo Kanazawa, Hang Gao

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="hangg7/soar" >}}

### Abstract
{{< lead >}}
Self-occlusion is common when capturing people in the
wild, where the performer do not follow predefined motion
scripts. This challenges existing monocular human reconstruction systems that assume full body visibility. We introduce Self-Occluded Avatar Recovery (SOAR), a method for
complete human reconstruction from partial observations
where parts of the body are entirely unobserved. SOAR
leverages structural normal prior and generative diffusion
prior to address such an ill-posed reconstruction problem.
For structural normal prior, we model human with an reposable surfel model with well-defined and easily readable shapes. For generative diffusion prior, we perform
an initial reconstruction and refine it using score distillation. On various benchmarks, we show that SOAR performs favorably than state-of-the-art reconstruction and
generation methods, and on-par comparing to concurrent
works. 
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2410.23800" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="system.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="X--Humans" color="goldenrod" logo="github" link="https://xhumans.ait.ethz.ch/" target="_blank">}}
{{<badge label="test" message="DNA--Rendering" color="darkorange" style="plastic" logo="github" link="https://dna-rendering.github.io/" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}

