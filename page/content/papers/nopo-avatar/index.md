---
date: 2025-11-28T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NoPo-Avatar
categories: ["papers"]
tags: ["splats", "smplx", "generalized", "neurips25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "NoPo-Avatar: Generalizable and Animatable Avatars from Sparse Inputs without Human Poses"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 27
---

## `NoPo-Avatar`: Generalizable and Animatable Avatars from Sparse Inputs without Human Poses

> Jing Wen, Alexander G. Schwing, Shenlong Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *NeurIPS* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="wenj/NoPo-Avatar" >}}

### Abstract
{{< lead >}}
We tackle the task of recovering an animatable 3D human avatar from a single or a sparse set of images. For this task, beyond a set of images, many prior state-of-theart methods use accurate “ground-truth” camera poses and human poses as input to guide reconstruction at test-time. We show that pose-dependent reconstruction degrades results significantly if pose estimates are noisy. To overcome this, we introduce NoPo-Avatar, which reconstructs avatars solely from images, without any pose input. By removing the dependence of test-time reconstruction on human poses, NoPo-Avatar is not affected by noisy human pose estimates, making it more widely applicable. Experiments on challenging THuman2.0, XHuman, and HuGe100K data show that NoPo-Avatar outperforms existing baselines in practical settings (without ground-truth poses) and delivers comparable results in lab settings (with ground-truth poses).
{{< /lead >}}

{{< button href="https://openreview.net/pdf/c8754d674e28813a83529ce78d5a8e8e6637fff5.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="NoPo-Avatar teaser"
    caption="`NoPo-Avatar` teaser."
    >}}


{{< figure
    src="method.png"
    alt="NoPo-Avatar overview"
    caption="`NoPo-Avatar` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="X--Humans" color="goldenrod" logo="github" link="https://xhumans.ait.ethz.ch/" target="_blank">}}
{{<badge label="train--test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}
{{<badge label="train--test" message="HuGe100K" color="khaki" logo="github" link="https://yiyuzhuang.github.io/IDOL/#dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}
{{<badge label="body--Splats" message="GHG" color="plum" logo="github" link="https://github.com/humansensinglab/Generalizable-Human-Gaussians" target="_blank">}}
{{<badge label="body--Splats" message="GoMAvatar" color="bisque" logo="github" link="https://github.com/wenj/GoMAvatar" target="_blank">}}
{{<badge label="body--Splats" message="iHuman" color="crimson" logo="github" link="https://github.com/pramishp/ihuman" target="_blank">}}
{{<badge label="body--NeRF" message="NIA" color="orangered" logo="github" target="_blank">}}
{{<badge label="body--NeRF" message="LIFe--GoM" color="khaki" logo="github" link="https://github.com/wenj/LIFe-GoM" target="_blank">}}