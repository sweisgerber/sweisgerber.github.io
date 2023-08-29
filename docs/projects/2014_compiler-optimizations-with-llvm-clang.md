---
title: LLVM-Clang Compiler Optimizations & Linker Manipulations
key: llvm-clang
date: 2014-01-01T00:00:00+01:00
featured: true
link: ''
# image: /img/schema-org.webp
description: >-
  Loading code in special permission memory regions, by redirecting function callsand utilizing
  the linker and custom clang optimization passes.
tags:
  - LLVM
  - Clang
  - Linker-Manipulation
  - C
  - C++
fact: >-
  A research idea, that didn't come to fruition, but "Writing clang optimization passes is not that hard after all"
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---
Worked on a side project during the paper: [You can run but you can't read: Preventing disclosure exploits in executable code](https://dl.acm.org/doi/abs/10.1145/2660267.2660378), 
but wasn't used in the paper after all.

Loading code in memory regions with specific permissions (read-only, execute-only), redirecting function calls to 
execute-only memory regions by utilizing the linker and custom clang optimization passes.
