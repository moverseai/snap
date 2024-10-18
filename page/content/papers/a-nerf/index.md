---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: A-NeRF
categories: ["papers"]
tags: ["nerf", "skeleton", "neurips21"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Animatable Neural Radiance Fields for Modeling Dynamic Human Bodies"
summary: TODO
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 1
---

## `A-NeRF`: Animatable Neural Radiance Fields for Modeling Dynamic Human Bodies

> Shih-Yang Su, Frank Yu, Michael Zollhöfer, Helge Rhodin

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="email" >}} *NeurIPS* 2021 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="LemonATsu/A-NeRF" >}}

### Abstract
{{< lead >}}
While deep learning reshaped the classical motion capture pipeline with feedforward networks, generative models are required to recover fine alignment via iterative refinement. Unfortunately, the existing models are usually hand-crafted or learned in controlled conditions, only applicable to limited domains. We propose a method to learn a generative neural body model from unlabelled monocular videos by extending Neural Radiance Fields (NeRFs). We equip them with a skeleton to apply to time-varying and articulated motion. A key insight is that implicit models require the inverse of the forward kinematics used in explicit surface models. Our reparameterization defines spatial latent variables relative to the pose of body parts and thereby overcomes ill-posed inverse operations with an overparameterization. This enables learning volumetric body shape and appearance from scratch while jointly refining the articulated pose; all without ground truth labels for appearance, pose, or 3D shape on the input videos. When used for novel-view-synthesis and motion capture, our neural model improves accuracy on diverse datasets.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2102.06199" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="A-NeRF overview"
    caption="`A-NeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="MPI--INF--3DHP" color="squamarine" logo="link" link="https://vcai.mpi-inf.mpg.de/3dhp-dataset/" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}
{{<badge label="test" message="MonoPerfCap" color="coral" logo="link" link="https://vcai.mpi-inf.mpg.de/projects/wxu/MonoPerfCap/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="60h" color="informational" logo="link" >}}
{{<badge label="train" message="2_x_V100" color="informational" logo="link" >}}
{{<badge label="render" message="1-4sec" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="V100" color="informational" logo="link" >}}
