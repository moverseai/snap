---
date: 2022-12-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NeuralAM
categories: ["papers"]
tags: ["sdf", "deformation", "siggraph_asia22"]
layout: simple # single # 
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Human Performance Modeling and Rendering via Neural Animated Mesh"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 4
---

## `NeuralAM`: Human Performance Modeling and Rendering via Neural Animated Mesh

> Fuqiang Zhao, Yuheng Jiang, Kaixin Yao, Jiakai Zhang, Liao Wang, Haizhao Dai, Yuhui Zhong, Yingliang Zhang, Minye Wu, Lan Xu, Jingyi Yu

{{< keywordList >}}
{{< keyword icon="tag" >}} SDF {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH Asia* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="zhaofuq/Instant-NSR" >}}

### Abstract
{{< lead >}}
We have recently seen tremendous progress in the neural advances for photo-real human modeling and rendering. However, it's still challenging to integrate them into an existing mesh-based pipeline for downstream applications. In this paper, we present a comprehensive neural approach for high-quality reconstruction, compression, and rendering of human performances from dense multi-view videos. Our core intuition is to bridge the traditional animated mesh workflow with a new class of highly efficient neural techniques. We first introduce a neural surface reconstructor for high-quality surface generation in minutes. It marries the implicit volumetric rendering of the truncated signed distance field (TSDF) with multi-resolution hash encoding. We further propose a hybrid neural tracker to generate animated meshes, which combines explicit non-rigid tracking with implicit dynamic deformation in a self-supervised framework. The former provides the coarse warping back into the canonical space, while the latter implicit one further predicts the displacements using the 4D hash encoding as in our reconstructor. Then, we discuss the rendering schemes using the obtained animated meshes, ranging from dynamic texturing to lumigraph rendering under various bandwidth settings. To strike an intricate balance between quality and bandwidth, we propose a hierarchical solution by first rendering 6 virtual views covering the performer and then conducting occlusion-aware neural texture blending. We demonstrate the efficacy of our approach in a variety of mesh-based applications and photo-realistic free-view experiences on various platforms, i.e., inserting virtual human performances into real environments through mobile AR or immersively watching talent shows with VR headsets.
{{< /lead >}}

{{< button href="https://dl.acm.org/doi/pdf/10.1145/3550454.3555451" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="NeuralAM overview"
    caption="`NeuralAM` overview."
    >}}

{{< figure
    src="method1.png"
    alt="NeuralAM tracking"
    caption="`NeuralAM` tracking."
    >}}

{{< figure
    src="method2.png"
    alt="NeuralAM rendering"
    caption="`NeuralAM` rendering."
    >}}

### Results

#### Data
{{<badge label="test" message="NeuralAM" color="lightblue" logo="google" logoColor="white" link="https://drive.google.com/drive/folders/1QhEXw9vrqRW5jUNqPGuxOwqbNC9r0Uay" target="_blank">}}

#### Performance
{{<badge label="train" message="15min/frame" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="render" message="2048_x_1536" color="informational" logo="link" >}}
{{<badge label="render" message="100ms" color="informational" logo="link" >}}