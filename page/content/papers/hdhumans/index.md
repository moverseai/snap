---
date: 2023-08-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HDHumans
categories: ["papers"]
tags: ["nerf", "skeleton", "texture", "deformation", "sca23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "HDHumans: A Hybrid Approach for High-fidelity Digital Humans"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 12
---

## `HDHumans`: A Hybrid Approach for High-fidelity Digital Humans

> Marc Habermann, Lingjie Liu, Weipeng Xu, Gerard Pons-Moll, Michael Zollhoefer, Christian Theobalt

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *SCA* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Photo-real digital human avatars are of enormous importance in graphics, as they enable immersive communication over the globe, improve gaming and entertainment experiences, and can be particularly beneficial for AR and VR settings. However, current avatar generation approaches either fall short in high-fidelity novel view synthesis, generalization to novel motions, reproduction of loose clothing, or they cannot render characters at the high resolution offered by modern displays. To this end, we propose HDHumans, which is the first method for HD human character synthesis that jointly produces an accurate and temporally coherent 3D deforming surface and highly photo-realistic images of arbitrary novel views and of motions not seen at training time. At the technical core, our method tightly integrates a classical deforming character template with neural radiance fields (NeRF). Our method is carefully designed to achieve a synergy between classical surface deformation and a NeRF. First, the template guides the NeRF, which allows synthesizing novel views of a highly dynamic and articulated character and even enables the synthesis of novel motions. Second, we also leverage the dense pointclouds resulting from the NeRF to further improve the deforming surface via 3D-to-3D supervision. We outperform the state of the art quantitatively and qualitatively in terms of synthesis quality and resolution, as well as the quality of 3D surface reconstruction.
{{< /lead >}}

{{< button href="https://dl.acm.org/doi/pdf/10.1145/3606927" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="HDHumans overview"
    caption="`HDHumans` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="skeleton--NeRF" message="NeuralActor" color="blue" logo="github" link="lingjie0206/Neural_Actor_Main_Code" target="_blank">}}
{{<badge label="body--NeRF" message="A--NeRF" color="orange" logo="github" link="https://github.com/LemonATsu/A-NeRF" target="_blank">}}