---
title: "ARTist: The Android Runtime Instrumentation and Security Toolkit"
key: paper-artist
date: 2017-04-26T13:00:00+0100
draft: false
pubtype: paper
featured: true
description: >-
  ARTist, a compiler-based application instrumentation solution for Android that does not depend on operating system modifications and solely operates on the application layer.
tags: 
  - Android
  - Android-System
  - Application-Instrumentation
  - Java
  - C++
  - C
image: ""
link: "https://ieeexplore.ieee.org/document/7961998"
fact: >- 
  "Since dex2oat was yet uncharted, our approach required first and foremost a thorough study of the compiler suite's internals and in particular of the new default compiler backend called Optimizing."
weight: 400
sitemap:
  priority : 0.8
---

### Abstract

With the introduction of Android 5 Lollipop, the Android Runtime (ART) superseded the 
Dalvik Virtual Machine (DVM) by introducing ahead-of-time compilation and native execution of applications, 
effectively deprecating seminal works such as TaintDroid that hitherto depend on the DVM. In this paper, 
we discuss alternatives to overcome those restrictions and highlight advantages for the security community 
that can be derived from ART's novel on-device compiler dex2oat and its accompanying runtime components. T
o this end, we introduce ARTist, a compiler-based application instrumentation solution for Android that does not depend
on operating system modifications and solely operates on the application layer. Since dex2oat is yet uncharted, 
our approach required first and foremost a thorough study of the compiler suite's internals and in particular of 
the new default compiler backend called Optimizing. We document the results of this study in this paper to facilitate 
independent research on this topic and exemplify the viability of ARTist by realizing two use cases. In particular, 
we conduct a case study on whether taint tracking can be re-instantiated using a compiler-based app instrumentation 
framework. Overall, our results provide compelling arguments for the community to choose compiler-based approaches 
over alternative bytecode or binary rewriting approaches for security solutions on Android.

- Published in: [2017 IEEE European Symposium on Security and Privacy (EuroS&P)][proceedings]
- Alternate Paper Link: [publications.cispa.saarland][paper-cispa]
- Poster (separate publication before the paper, is interpreted as work-in-progress) [EuroSP2016][poster]

#### Authors

- Michael Backes (CISPA, Saarland University & MPI-SWS, Saarland Informatics Campus)
- Sven Bugiel (CISPA, Saarland University, Saarland Informatics Campus)
- Oliver Schranz (CISPA, Saarland University, Saarland Informatics Campus)
- Philipp von Styp-Rekowsky (CISPA, Saarland University, Saarland Informatics Campus)
- Sebastian Weisgerber (CISPA, Saarland University, Saarland Informatics Campus)


[proceedings]: https://ieeexplore.ieee.org/xpl/conhome/7961955/proceeding
[paper-cispa]: https://publications.cispa.saarland/145/
[poster]: https://www.ieee-security.org/TC/EuroSP2016/posters/number15.pdf
