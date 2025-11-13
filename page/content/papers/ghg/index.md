---
date: 2024-10-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GHG
categories: ["papers"]
tags: ["splats", "smplx", "generalized", "eccv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "Generalizable Human Gaussians (GHG) for Sparse View Synthesis"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 22
---

## Generalizable Human Gaussians (GHG) for Sparse View Synthesis

> Youngjoong Kwon, Baole Fang, Yixing Lu, Haoye Dong, Cheng Zhang, Francisco Vicente Carrasco, Albert Mosella-Montoro, Jianjin Xu, Shingo Takagi, Daeil Kim, Aayush Prakash, Fernando de la Torre

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="humansensinglab/Generalizable-Human-Gaussians" >}}

### Abstract
{{< lead >}}
Recent progress in neural rendering have brought forth pioneering methods, such as NeRF and Gaussian Splatting, which revolutionize view rendering across various domains like AR/VR, gaming, and content creation. While these methods excel at interpolating within the training data, the challenge of generalizing to new scenes and objects from very sparse views persists. Specifically, modeling 3D humans from sparse views presents formidable hurdles due to the inherent complexity of human geometry, resulting in inaccurate reconstructions of geometry and textures. To tackle this challenge, this paper leverages recent advancements in Gaussian splatting and introduces a new method to learn generalizable human Gaussians that allows photorealistic and accurate view-rendering of a new human subject from a limited set of sparse views in a feed-forward manner. A pivotal innovation of our approach involves reformulating the learning of 3D Gaussian parameters into a regression process defined on the 2D UV space of a human template, which allows leveraging the strong geometry prior and the advantages of 2D convolutions. Our method outperforms recent methods on both within-dataset generalization as well as cross-dataset generalization settings.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2407.12777" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="GHG teaser"
    caption="`GHG` teaser."
    >}}


{{< figure
    src="overview.png"
    alt="GHG overview"
    caption="`GHG` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}
{{<badge label="test" message="THuman" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/DeepHuman/tree/master/THUmanDataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NIA" color="orangered" logo="github" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}

#### Performance

{{<badge label="train" message="4h" color="informational" logo="link" >}}

{{<badge label="render" message="1024_x_1024" color="informational" logo="link" >}}