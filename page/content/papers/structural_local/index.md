---
date: 2022-06-21T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: StructuredLocal
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "cvpr22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: Structured Local Radiance Fields for Human Avatar Modeling
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 22
---

## Structured Local Radiance Fields for Human Avatar Modeling

> Zerong Zheng, Han Huang, Tao Yu, Hongwen Zhang, Yandong Guo, Yebin Liu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL  {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2022 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
It is extremely challenging to create an animatable clothed human avatar from RGB videos, especially for loose clothes due to the diffculties in motion modeling. To address this problem, we introduce a novel representation on the basis of recent neural scene rendering techniques. The core of our representation is a set of structured local radiance felds, which are anchored to the pre-defned nodes sampled on a statistical human body template. These local radiance felds not only leverage the fexibility of implicit representation in shape and appearance modeling, but also factorize cloth deformations into skeleton motions, node residual translations and the dynamic detail variations inside each individual radiance feld. To learn our representation from RGB data and facilitate pose generalization, we propose to learn the node translations and the detail variations in a conditional generative latent space. Overall, our method enables automatic construction of animatable human avatars for various types of clothes without the need
for scanning subject-specifc templates, and can generate realistic images with dynamic details for novel poses. Experiment show that our method outperforms state-of-the-art methods both qualitatively and quantitatively.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2022/papers/Zheng_Structured_Local_Radiance_Fields_for_Human_Avatar_Modeling_CVPR_2022_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.jpg"
    alt="StructuredLocal overview"
    caption="`StructuredLocal` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}

#### Performance
{{<badge label="train" message="25h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="render" message="5sec" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}