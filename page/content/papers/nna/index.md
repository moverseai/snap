---
date: 2023-01-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NNA
categories: ["papers"]
tags: ["nerf", "smpl", "tvcg23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Neural Novel Actor: Learning a Generalized Animatable Neural Representation for Human Actors."
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 30
---

## Neural Novel Actor: Learning a Generalized Animatable Neural Representation for Human Actors

> Qingzhe Gao, Yiming Wang, Libin Liu, Lingjie Liu, Christian Theobalt, Baoquan Chen

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *TVCG* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="Talegqz/neural_novel_actor" >}}

### Abstract
{{< lead >}}
We propose a new method for learning a generalized ani- matable neural human representation from a sparse set of multi-view imagery of multiple persons. The learned repre- sentation can be used to synthesize novel view images of an arbitrary person from a sparse set of cameras, and further animate them with the user’s pose control. While existing methods can either generalize to new persons or synthesize animations with user control, none of them can achieve both at the same time. We attribute this accomplishment to the employment of a 3D proxy for a shared multi-person human model, and further the warping of the spaces of different poses to a shared canonical pose space, in which we learn a neural field and predict the person- and pose-dependent deforma- tions, as well as appearance with the features extracted from input images. To cope with the complexity of the large vari- ations in body shapes, poses, and clothing deformations, we design our neural human model with disentangled geometry and appearance. Furthermore, we utilize the image features both at the spatial point and on the surface points of the 3D proxy for predicting person- and pose-dependent properties. Experiments show that our method significantly outperforms the state-of-the-arts on both task.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2208.11905" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="NNA teaser"
    caption="`NNA` teaser."
    >}}

{{< figure
    src="method.png"
    alt="NNA overview"
    caption="`NNA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DeepCap" color="cyan" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="Keypoint--NeRF" color="mistyrose" logo="github" link="https://github.com/facebookresearch/KeypointNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}
{{<badge label="body--NeRF" message="MPS-NeRF" color="gold" logo="github" link="gaoxiangjun/MPS-NeRF" target="_blank">}}

#### Performance
{{<badge label="train" message="56h" color="informational" logo="link" >}}
{{<badge label="train" message="4_x_V100" color="informational" logo="link" >}}
