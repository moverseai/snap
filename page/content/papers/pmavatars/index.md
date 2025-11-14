---
date: 2024-05-07T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: PMAvatars
categories: ["papers"]
tags: ["nerf", "skeleton", "iclr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "Pose Modulated Avatars from Video"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 29
---

## Pose Modulated Avatars from Video

> Chunjin Song, Bastian Wandt, Helge Rhodin

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="email" >}} *ICLR* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="ChunjinSong/pmavatar" >}}

### Abstract
{{< lead >}}
It is now possible to reconstruct dynamic human motion and shape from a sparse set of cameras using Neural Radiance Fields (NeRF) driven by an underlying skeleton. However, a challenge remains to model the deformation of cloth and skin in relation to skeleton pose. Unlike existing avatar models that are learned implicitly or rely on a proxy surface, our approach is motivated by the observation that different poses necessitate unique frequency assignments. Neglecting this distinction yields noisy artifacts in smooth areas or blurs fine-grained texture and shape details in sharp regions. We develop a two-branch neural network that is adaptive and explicit in the frequency domain. The first branch is a graph neural network that models correlations among body parts locally, taking skeleton pose as input. The second branch combines these correlation features to a set of global frequencies and then modulates the feature encoding. Our experiments demonstrate that our network outperforms state-of-the-art methods in terms of preserving details and generalization capabilities.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2308.11951" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="PMAvatars overview"
    caption="`PMAvatars` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="TAVA" color="coral" logo="github" link="facebookresearch/tava" target="_blank">}}
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}
{{<badge label="body--NeRF" message="DANBO" color="pink" logo="github" link="LemonATsu/DANBO-pytorch" target="_blank">}}
{{<badge label="body--NeRF" message="A--NeRF" color="orange" logo="github" link="https://github.com/LemonATsu/A-NeRF" target="_blank">}}
