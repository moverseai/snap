---
date: 2025-04-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GIGA
categories: ["papers"]
tags: ["splats", "smplx", "generalized", "3dv26"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "GIGA: Generalizable Sparse Image-driven Gaussian Humans"
summary: TODO
keywords: #
type: '2026' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2026"]
series_order: 1
---

## `GIGA`: Generalizable Sparse Image-driven Gaussian Humans

> Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *3DV* 2026 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="antonzub99/giga" >}}

### Abstract
{{< lead >}}
Driving a high-quality and photorealistic full-body virtual human from a few RGB cameras is a challenging problem that has become increasingly relevant with emerging virtual reality technologies. A promising solution to democratize such technology would be a generalizable method that takes sparse multi-view images of any person and then generates photoreal free-view renderings of them. However, the state-of-the-art approaches are not scalable to very large datasets and, thus, lack diversity and photorealism. To address this problem, we propose GIGA, a novel, generalizable full-body model for rendering photoreal humans in free viewpoint, driven by a single-view or sparse multi-view video. Notably, GIGA can scale training to a few thousand subjects while maintaining high photorealism and synthesizing dynamic appearance. At the core, we introduce a MultiHeadUNet architecture, which takes an approximate RGB texture accumulated from a single or multiple sparse views and predicts 3D Gaussian primitives represented as 2D texels on top of a human body mesh. At test time, our method performs novel view synthesis of a virtual 3D Gaussian-based human from 1 to 4 input views and a tracked body template for unseen identities. Our method excels over prior works by a significant margin in terms of identity generalization capability and photorealism.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2504.07144" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.jpg"
    alt="GIGA teaser"
    caption="`GIGA` teaser."
    >}}


{{< figure
    src="overview.webp"
    alt="GIGA overview"
    caption="`GIGA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="DNA--Rendering" color="darkorange" style="plastic" logo="github" link="https://dna-rendering.github.io/" target="_blank">}}
{{<badge label="test" message="THuman2.0" color="olive" logo="github" link="https://github.com/ytrock/THuman2.0-Dataset" target="_blank">}}
{{<badge label="test" message="MVHumanNet" color="thistle" logo="github" link="https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}
{{<badge label="body--Splats" message="GHG" color="plum" logo="github" link="https://github.com/humansensinglab/Generalizable-Human-Gaussians" target="_blank">}}
