---
date: 2025-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: TaoAvatar
categories: ["papers"]
tags: ["splats", "smplx", "deformation", "cvpr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "TaoAvatar: Real-Time Lifelike Full-Body Talking Avatars for Augmented Reality via 3D Gaussian Splatting"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 16
---

## `TaoAvatar`: Real-Time Lifelike Full-Body Talking Avatars for Augmented Reality via 3D Gaussian Splatting

> Jianchuan Chen, Jingchuan Hu, GaiGe Wang, Zhonghua Jiang, TianSong Zhou, Zhiwen Chen, Chengfei Lv

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
Realistic 3D full-body talking avatars hold great potential in AR, with applications ranging from e-commerce live streaming to holographic communication. Despite advances in 3D Gaussian Splatting (3DGS) for lifelike avatar creation, existing methods struggle with fine-grained control of facial expressions and body movements in full-body talking tasks. Additionally, they often lack sufficient details and cannot run in real-time on mobile devices.We present TaoAvatar, a high-fidelity, lightweight, 3DGS-based full-body talking avatar driven by various signals. Our approach starts by creating a personalized clothed human parametric template that binds Gaussians to represent appearances. We then pre-train a StyleUnet-based network to handle complex pose-dependent non-rigid deformation, which can capture high-frequency appearance details but is too resource-intensive for mobile devices. To overcome this, we "bake" the non-rigid deformations into a lightweight MLP-based network using a distillation technique and develop blend shapes to compensate for details. Extensive experiments show that TaoAvatar achieves state-of-the-art rendering quality while running in real-time across various devices, maintaining 90 FPS on high-definition stereo devices such as the Apple Vision Pro.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2503.17032" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="pipeline.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="TalkBody4D" color="peachpuff" style="plastic" logo="github" link="https://huggingface.co/datasets/PixelAI-Team/TalkBody4D" target="_blank">}}
{{<badge label="test" message="ActorsHQ" color="silver" logo="link" link="https://actors-hq.com/#dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="AnimatableGaussians" color="darkred" logo="github" link="https://github.com/lizhe00/AnimatableGaussians" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--Splats" message="MeshAvatar" color="limegreen" logo="github" link="https://github.com/shad0wta9/meshavatar" target="_blank">}}


#### Performance

{{<badge label="render" message="6ms" color="informational" logo="link" >}}
{{<badge label="render" message="RTX4090" color="informational" logo="link" >}}
{{<badge label="render" message="1500_x_2000" color="informational" logo="link" >}}
