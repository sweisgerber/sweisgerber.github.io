---
title: Monkey-Troop - Large Scale Automated Android Middleware Fuzzing
key: money-troop
# date  --iso-8601=seconds   
date: 2018-01-01T00:00:00+01:00
link: 'https://github.com/Project-ARTist/monkey-troop'
draft: false
featured: true
# image: ""
description: >-
  Large scale automated Android middleware fuzzing.
tags:
  - Java
  - Python
  - Rust
  - C
  - C++
  - Android
  - Android-Middleware
  - Android-System
  - Android-Art
  - Android-Emulator
  - Compiler-Development
  - Android-Apps
  - AFL 
fact: >-
  Fuzzing like a troop of monkeys
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---

Based on the works in the previous project [Fuzzing the Android Middleware], the automation and general applicability
was taken a step further in this project.

In this project, we argued that in order to steer away from incompatible custom toolchains and towards having comparable 
analyses with reproducible results, a more principled approach to dynamically analyzing the Android system is required. 
As an important first step in this direction, we proposed a unified dynamic analysis platform that provides re-usable 
solutions for common challenges as the building blocks for future analyses.

It enabled us to integrate different fuzzers by providing a plugin interface and also doing it on a larger 
scale than before (30 worker processes with each utilizing an own Android emulator).

The results of this project were published together with the project [Fuzzing the Android Middleware] 
in the [paper]: "Towards a Principled Approach for Dynamic Analysis of Android's Middleware".

[Fuzzing the Android Middleware]: ./2017_fuzzing-android-middleware.md 
[paper]: https://arxiv.org/abs/2110.05619
