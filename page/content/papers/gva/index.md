---
date: 2024-02-07T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GVA
categories: ["papers"]
tags: ["splats", "smplx", "monocular", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "GVA: Reconstructing Vivid 3D Gaussian Avatars from Monocular Videos"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 39
---

## `GVA`: Reconstructing Vivid 3D Gaussian Avatars from Monocular Videos

> Xinqi Liu, Chenming Wu, Jialun Liu, Xing Liu, Jinbo Wu, Chen Zhao, Haocheng Feng, Errui Ding, Jingdong Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
In this paper, we present a novel method that facilitates the creation of vivid 3D Gaussian avatars from monocular video inputs (GVA). Our innovation lies in addressing the intricate challenges of delivering high-fidelity human body reconstructions and aligning 3D Gaussians with human skin surfaces accurately. The key contributions of this paper are twofold. Firstly, we introduce a pose refinement technique to improve hand and foot pose accuracy by aligning normal maps and silhouettes. Precise pose is crucial for correct shape and appearance reconstruction. Secondly, we address the problems of unbalanced aggregation and initialization bias that previously diminished the quality of 3D Gaussian avatars, through a novel surface-guided re-initialization method that ensures accurate alignment of 3D Gaussian points with avatar surfaces. Experimental results demonstrate that our proposed method achieves high-fidelity and vivid 3D Gaussian avatar reconstruction. Extensive experimental analyses validate the performance qualitatively and quantitatively, demonstrating that it achieves state-of-the-art performance in photo-realistic novel view synthesis while offering fine-grained control over the human body and hand pose.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2402.16607" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="GVA teaser"
    caption="`GVA` teaser."
    >}}

{{< figure
    src="method.png"
    alt="GVA overview"
    caption="`GVA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}
{{<badge label="test" message="GVA--Snapshot" color="floralwhite" logo="link" link="https://3d-aigc.github.io/GEA/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="InstantNVR" color="fuchsia" logo="github" link="https://github.com/zju3dv/instant-nvr" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--Splats" message="GART" color="springgreen" logo="github" link="https://github.com/JiahuiLei/GART" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}

