---
date: 2025-08-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: EVA
categories: ["papers"]
tags: ["skeleton", "texture", "deformation", "siggraph25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "EVA: Expressive Virtual Avatars from Multi-view Videos"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 8
---

## `EVA`: Expressive Virtual Avatars from Multi-view Videos

> Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann

{{< keywordList >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH* 2025 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
With recent advancements in neural rendering and motion capture algorithms, remarkable progress has been made in photorealistic human avatar modeling, unlocking immense potential for applications in virtual reality, augmented reality, remote communication, and industries such as gaming, film, and medicine. However, existing methods fail to provide complete, faithful, and expressive control over human avatars due to their entangled representation of facial expressions and body movements. In this work, we introduce Expressive Virtual Avatars (EVA), an actor-specific, fully controllable, and expressive human avatar framework that achieves high-fidelity, lifelike renderings in real time while enabling independent control of facial expressions, body movements, and hand gestures. Specifically, our approach designs the human avatar as a two-layer model: an expressive template geometry layer and a 3D Gaussian appearance layer. First, we present an expressive template tracking algorithm that leverages coarse-to-fine optimization to accurately recover body motions, facial expressions, and non-rigid deformation parameters from multi-view videos. Next, we propose a novel decoupled 3D Gaussian appearance model designed to effectively disentangle body and facial appearance. Unlike unified Gaussian estimation approaches, our method employs two specialized and independent modules to model the body and face separately. Experimental results demonstrate that EVA surpasses state-of-the-art methods in terms of rendering quality and expressiveness, validating its effectiveness in creating full-body avatars. This work represents a significant advancement towards fully drivable digital human models, enabling the creation of lifelike digital avatars that faithfully replicate human geometry and appearance.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2505.15385" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="EVA teaser"
    caption="`EVA` teaser."
    >}}

{{< figure
    src="overview.png"
    alt="EVA overview"
    caption="`EVA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="EVA" color="springgreen" logo="github" link="https://vcai.mpi-inf.mpg.de/projects/EVA/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="ENeRF" color="lightcoral" logo="github" link="https://github.com/zju3dv/ENeRF" target="_blank">}}

#### Performance
{{<badge label="train--mesh" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="train--mesh" message="45min" color="informational" logo="link" >}}
{{<badge label="train--splats" message="A100" color="informational" logo="link" >}}
{{<badge label="train--splats" message="600_x_800" color="informational" logo="link" >}}

{{<badge label="render" message="2K" color="informational" logo="link" >}}
{{<badge label="render" message="2_x_A40" color="informational" logo="link" >}}
{{<badge label="render" message="30ms" color="informational" logo="link" >}}