---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HumanAvatar
categories: ["papers"]
tags: ["splats", "smpl", "monocular", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Efficient Neural Implicit Representation for 3D Human Reconstruction"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 32
---

## Efficient Neural Implicit Representation for 3D Human Reconstruction

> Zexu Huanga, Sarah Monazam Erfania, Siying Lua, Mingming Gongb

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="HZXu-526/Human-Avatar" >}}

### Abstract
{{< lead >}}
High-fidelity digital human representations are increasingly in demand in the digital world, particularly for interactive telepresence, AR/VR, 3D graphics, and the rapidly evolving  etaverse. Even though they work well in small spaces, conventional methods for reconstructing 3D human motion frequently require the use of expensive hardware and have high processing costs. This study presents HumanAvatar, an innovative approach that efficiently reconstructs precise human avatars from monocular video sources. At the core of our methodology, we integrate the pre-trained HuMoR, a model celebrated for its proficiency in human motion estimation. This is adeptly fused with the cutting-edge neural radiance field technology, Instant-NGP, and the state-of-the-art articulated model, Fast-SNARF, to enhance the reconstruction fidelity and speed. By combining these two technologies, a system is created that can render quickly and effectively while also providing estimation of human pose parameters that are unmatched in accuracy. We have enhanced our system with an advanced posture-sensitive space reduction technique, which optimally balances rendering quality with computational efficiency. In our detailed experimental analysis using both artificial and real-world monocular videos, we establish the advanced performance of our approach. HumanAvatar consistently equals or surpasses contemporary leading-edge reconstruction techniques in quality. Furthermore, it achieves these complex reconstructions in minutes, a fraction of the time typically required by existing methods. Our models achieve a training speed that is 110X faster than that of State-of-The-Art (SoTA) NeRF-based models. Our technique performs noticeably better than SoTA dynamic human NeRF methods if given an identical runtime limit. HumanAvatar can provide effective visuals after only 30 seconds of training. 
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2410.17741" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Human Avatar teaser"
    caption="`Human Avatar` teaser."
    >}}

{{< figure
    src="method.png"
    alt="Human Avatar overview"
    caption="`Human Avatar` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}
{{<badge label="test" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="2min" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}

{{<badge label="render" message="66ms" color="informational" logo="link" >}}
{{<badge label="render" message="540_x_540" color="informational" logo="link" >}}