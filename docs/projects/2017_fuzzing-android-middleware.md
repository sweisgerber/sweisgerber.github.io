---
title: Fuzzing the Android Middleware
key: fuzzart
# date  --iso-8601=seconds   
date: 2017-01-01T00:00:00+01:00
link: 'https://example.org'
draft: false
featured: false
# image: ""
description: >-
  An automated large-scale Android Middleware fuzzer
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
  Instrumenting the Android middleware with ARTist to get feedback when fuzzing the Android-Middleware.
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---

ARTist was enhanced to be able to instrument the Android-Middleware (system server) as an important stepping 
stone that enabled this projects.
With this new capability we now  utilized American Fuzzy Lop (AFL) to generate random fuzzing inputs
and by instrumenting the Android middleware with AFL's required fuzzing feedback code, AFL now worked.
This setup ran in an Android emulator, which was a necessity in order to do this on a larger scale later on.

In order to automate the whole process, we wrote Python automation scripts and were then able
to fully automate the fuzzing of the Android middleware.
The findings of AFL were also verified by reusing them as inputs in order to reproduce the results on an Android emualtor

In order for this whole setup to work, many solutions to problems had to get found, which besides other nice tools,
spawned [dexterous], a tool to merge and sign the code of multiple dex files, while still respecting the dex-file's
method limit.

This work continued in the project [Monkey-Troop].

The results of this project were published together with the [Monkey-Troop] project in the [paper] 
"Towards a Principled Approach for Dynamic Analysis of Android's Middleware".

[paper]: https://arxiv.org/abs/2110.05619
[Monkey-Troop]: ./2018_monkey-troop-fuzzing-android-middleware-large-scale.md
[dexterous]: https://github.com/Project-ARTist/dexterous
