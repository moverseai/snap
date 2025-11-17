---
date: 2025-08-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SqueezeMe
categories: ["papers"]
tags: ["splats", "smpl", "texture", "siggraph25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "SqueezeMe: Mobile-Ready Distillation of Gaussian Full-Body Avatars"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 6
---

## `SqueezeMe`: Mobile-Ready Distillation of Gaussian Full-Body Avatars

> Forrest Iandola, Stanislav Pidhorskyi, Igor Santesteban, Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Frank Yu, Emanuel Garbin, Tomas Simon, Shunsuke Saito

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH* 2025 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
Gaussian-based human avatars have achieved an unprecedented level of visual fidelity. However, existing approaches based on high-capacity neural networks typically require a desktop GPU to achieve real-time performance for a single avatar, and it remains non-trivial to animate and render such avatars on mobile devices including a standalone VR headset due to substantially limited memory and computational bandwidth. In this paper, we present SqueezeMe, a simple and highly effective framework to convert high-fidelity 3D Gaussian full-body avatars into a lightweight representation that supports both animation and rendering with mobile-grade compute. Our key observation is that the decoding of pose-dependent Gaussian attributes from a neural network creates non-negligible memory and computational overhead. Inspired by blendshapes and linear pose correctives widely used in Computer Graphics, we address this by distilling the pose correctives learned with neural networks into linear layers. Moreover, we further reduce the parameters by sharing the correctives among nearby Gaussians. Combining them with a custom splatting pipeline based on Vulkan, we achieve, for the first time, simultaneous animation and rendering of 3 Gaussian avatars in real-time (72 FPS) on a Meta Quest 3 VR headset.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2412.15171" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="method1.png"
    alt="Method overview (1/2)"
    caption="Method overview (1/2)."
    >}}

{{< figure
    src="method2.png"
    alt="Method overview (2/2)"
    caption="Method overview (2/2)."
    >}}
