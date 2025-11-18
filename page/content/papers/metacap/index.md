---
date: 2024-10-23T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: MetaCap
categories: ["papers"]
tags: ["nerf", "smpl", "generalized", "eccv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "MetaCap: Meta-learning Priors from Multi-View Imagery for Sparse-view Human Performance Capture and Rendering"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 33
---

## `MetaCap`: Meta-learning Priors from Multi-View Imagery for Sparse-view Human Performance Capture and Rendering

> Guoxing Sun, Rishabh Dabral, Pascal Fua, Christian Theobalt, Marc Habermann

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="sunshinnnn/metacap" >}}

### Abstract
{{< lead >}}
Faithful human performance capture and free-view rendering from sparse RGB observations is a long-standing problem in Vision and Graphics. The main challenges are the lack of observations and the inherent ambiguities of the setting, e.g. occlusions and depth ambiguity. As a result, radiance fields, which have shown great promise in capturing high-frequency appearance and geometry details in dense setups, perform poorly when naïvely supervising them on sparse camera views, as the field simply overfits to the sparse-view inputs. To address this, we propose MetaCap, a method for efficient and high-quality geometry recovery and novel view synthesis given very sparse or even a single view of the human. Our key idea is to meta-learn the radiance field weights solely from potentially sparse multi-view videos, which can serve as a prior when fine-tuning them on sparse imagery depicting the human. This prior provides a good network weight initialization, thereby effectively addressing ambiguities in sparse-view capture. Due to the articulated structure of the human body and motion-induced surface deformations, learning such a prior is non-trivial. Therefore, we propose to meta-learn the field weights in a pose-canonicalized space, which reduces the spatial feature range and makes feature learning more effective. Consequently, one can fine-tune our field parameters to quickly generalize to unseen poses, novel illumination conditions as well as novel and sparse (even monocular) camera views. For evaluating our method under different scenarios, we collect a new dataset, WildDynaCap, which contains subjects captured in, both, a dense camera dome and in-the-wild sparse camera rigs, and demonstrate superior results compared to recent state-of-the-art methods on both public and WildDynaCap dataset.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2403.18820" target="_blank" >}}
Paper
{{< /button >}}

### Approach


{{< figure
    src="teaser.png"
    alt="MetaCap teaser"
    caption="`MetaCap` teaser."
    >}}

{{< figure
    src="overview.png"
    alt="MetaCap overview"
    caption="`MetaCap` overview."
    >}}

### Results

#### Data

{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="WildDynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/MetaCap" target="_blank">}}

#### Comparisons

{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}