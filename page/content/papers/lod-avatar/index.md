---
date: 2024-10-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: LoDAvatar
categories: ["papers"]
tags: ["splats", "smpl", "monocular", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "LoDAvatar: Hierarchical Embedding and Adaptive Levels of Detail with Gaussian Splatting for Enhanced Human Avatars"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 16
---

## `LoDAvatar`: Hierarchical Embedding and Adaptive Levels of Detail with Gaussian Splatting for Enhanced Human Avatars

> Xiaonuo Dongye, Hanzhi Guo, Le Luo, Haiyan Jiang, Yihua Bao, Zeyu Tian, Dongdong Weng


{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
With the advancement of virtual reality, the demand for 3D human avatars is increasing. The emergence of Gaussian Splatting technology has enabled the rendering of Gaussian avatars with superior visual quality and reduced computational costs. Despite numerous methods researchers propose for implementing drivable Gaussian avatars, limited attention has been given to balancing visual quality and computational costs. In this paper, we introduce LoDAvatar, a method that introduces levels of detail into Gaussian avatars through hierarchical embedding and selective detail enhancement methods. The key steps of LoDAvatar encompass data preparation, Gaussian embedding, Gaussian optimization, and selective detail enhancement. We conducted experiments involving Gaussian avatars at various levels of detail, employing both objective assessments and subjective evaluations. The outcomes indicate that incorporating levels of detail into Gaussian avatars can decrease computational costs during rendering while upholding commendable visual quality, thereby enhancing runtime frame rates. We advocate adopting LoDAvatar to render multiple dynamic Gaussian avatars or extensive Gaussian scenes to balance visual quality and computational costs.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2410.20789" target="_blank" >}}
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
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--Splats" message="SplattingAvatar" color="lemonchiffon" logo="github" link="https://github.com/initialneil/SplattingAvatar" target="_blank">}}

#### Performance

{{<badge label="render" message="8--18ms" color="informational" logo="link" >}}
{{<badge label="render" message="1080_x_1080" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3080" color="informational" logo="link" >}}