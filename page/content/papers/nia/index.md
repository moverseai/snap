---
date: 2023-05-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NIA
categories: ["papers"]
tags: ["nerf", "smpl", "generalized", "iclr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Neural Image-based Avatars Generalizable Radiance Fields for Human Avatar Modeling"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 28
---

## Neural Image-based Avatars Generalizable Radiance Fields for Human Avatar Modeling

> Youngjoong Kwon, Dahun Kim, Duygu Ceylan, Henry Fuchs

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *ICLR* 2023 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="YoungJoongUNC/Neural_Image_Based_Avatars" >}} -->

### Abstract
{{< lead >}}
We present a method that enables synthesizing novel views and novel poses of arbitrary human performers from sparse multi-view images. A key ingredient of our method is a hybrid appearance blending module that combines the advantages of the implicit body NeRF representation and image-based rendering. Existing generalizable human NeRF methods that are conditioned on the body model have shown robustness against the geometric variation of arbitrary human performers. Yet they often exhibit blurry results when generalized onto unseen identities. Meanwhile, image-based rendering shows high-quality results when sufficient observations are available, whereas it suffers artifacts in sparse-view settings. We propose Neural Image-based Avatars (NIA) that exploits the best of those two methods: to maintain robustness under new articulations and self-occlusions while directly leveraging the available (sparse) source view colors to preserve appearance details of new subject identities. Our hybrid design outperforms recent methods on both in-domain identity generalization as well as challenging cross-dataset generalization settings. Also, in terms of the pose generalization, our method outperforms even the per-subject optimized animatable NeRF methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2304.04897" target="_blank" >}}
Paper
{{< /button >}}

### Approach


{{< figure
    src="overview.png"
    alt="NIA overview"
    caption="`NIA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DeepCap" color="cyan" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="Anim--NeRF" color="yellow" logo="github" link="https://github.com/JanaldoChen/Anim-NeRF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}
{{<badge label="body--NeRF" message="GP--NeRF" color="lightgray" logo="github" link="https://github.com/sail-sg/GP-Nerf" target="_blank">}}
{{<badge label="body--NeRF" message="Keypoint--NeRF" color="mistyrose" logo="github" link="https://github.com/facebookresearch/KeypointNeRF" target="_blank">}}

#### Performance
{{<badge label="train" message="1d" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}