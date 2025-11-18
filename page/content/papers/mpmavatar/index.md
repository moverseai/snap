---
date: 2025-11-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: MPMAvatar
categories: ["papers"]
tags: ["splats", "smplx", "clothing", "deformation", "neurips25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust Physics-Based Dynamics"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 9
---

## `MPMAvatar`: Learning 3D Gaussian Avatars with Accurate and Robust Physics-Based Dynamics

> Changmin Lee, Jihyun Lee, Tae-Kyun Kim

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *NeurIPS* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="KAISTChangmin/MPMAvatar" >}}

### Abstract
{{< lead >}}
While there has been significant progress in the field of 3D avatar creation from visual observations, modeling physically plausible dynamics of humans with loose garments remains a challenging problem. Although a few existing works address this problem by leveraging physical simulation, they suffer from limited accuracy or robustness to novel animation inputs. In this work, we present MPMAvatar, a framework for creating 3D human avatars from multi-view videos that supports highly realistic, robust animation, as well as photorealistic rendering from free viewpoints. For accurate and robust dynamics modeling, our key idea is to use a Material Point Method-based simulator, which we carefully tailor to model garments with complex deformations and contact with the underlying body by incorporating an anisotropic constitutive model and a novel collision handling algorithm. We combine this dynamics modeling scheme with our canonical avatar that can be rendered using 3D Gaussian Splatting with quasi-shadowing, enabling high-fidelity rendering for physically realistic animations. In our experiments, we demonstrate that MPMAvatar significantly outperforms the existing state-of-the-art physics-based avatar in terms of (1) dynamics modeling accuracy, (2) rendering accuracy, and (3) robustness and efficiency. Additionally, we present a novel application in which our avatar generalizes to unseen interactions in a zero-shot manner—which was not achievable with previous learning-based methods due to their limited simulation generalizability.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2510.01619" target="_blank" >}}
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

{{<badge label="test" message="ActorsHQ" color="silver" logo="link" link="https://actors-hq.com/#dataset" target="_blank">}}
{{<badge label="test" message="4D--DRESS" color="orange" logo="link" link="https://4d-dress.ait.ethz.ch/" target="_blank">}}


#### Comparisons

{{<badge label="body--NeRF" message="TAVA" color="coral" logo="github" link="facebookresearch/tava" target="_blank">}}
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--Splats" message="PhyAvatar" color="peru" logo="github" link="https://github.com/y-zheng18/PhysAvatar" target="_blank">}}
