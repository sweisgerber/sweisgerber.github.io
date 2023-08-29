---
title: "Towards a Principled Approach for Dynamic Analysis of Android's Middleware"
key: paper-arxiv-monkey-troop
date: 2021-10-11T13:00:00+0100
draft: false
pubtype: paper
featured: true
description: >-
  A unified dynamic analysis platform that provides re-usable solutions for common challenges as the building blocks for future analyses and allows to compare different approaches under the same assumptions.
tags:
  - Fuzzing
  - Dex2oat
  - Android
  - Android-Middleware
  - Android-System
  - Python
  - C++
  - C
  - Java
  - Java-JNI
image: ""
link: "https://arxiv.org/abs/2110.05619"
fact: >- 
  "Fuzzing like a troop of monkeys"
weight: 400
sitemap:
  priority : 0.8
---

### Abstract

The Android middleware, in particular the so-called systemserver, 
is a crucial and central component to Android's security and robustness. 
To understand whether the systemserver provides the demanded security properties, 
it has to be thoroughly tested and analyzed. A dedicated line of research focuses exclusively on this task. 
While static analysis builds on established tools, dynamic testing approaches lack a common foundation, 
which prevents the community from comparing, reproducing, or even re-using existing results from related work. 
This raises questions about whether the underlying approach of any proposed solution is the only possible or optimal one, 
if it can be re-used as a building block for future analyses, or whether results generalize. 
In this work, we argue that in order to steer away from incompatible custom toolchains and towards having comparable 
analyses with reproducible results, a more principled approach to dynamically analyzing the Android system is required. 
As an important first step in this direction, we propose a unified dynamic analysis platform that provides re-usable 
solutions for common challenges as the building blocks for future analyses and allows to compare different approaches 
under the same assumptions.

- Published in: [arxiv.org][proceedings]

#### Authors

- Oliver Schranz (CISPA Helmholtz Center for Information Security, Saarland Informatics Campus)
- Sebastian Weisgerber (CISPA Helmholtz Center for Information Security, Saarland Informatics Campus)
- Erik Derr (University of Luxembourg)
- Michael Backes (CISPA Helmholtz Center for Information Security, Saarland Informatics Campus)
- and Sven Bugiel (CISPA Helmholtz Center for Information Security, Saarland Informatics Campus)

[proceedings]: https://arxiv.org/abs/2110.05619
