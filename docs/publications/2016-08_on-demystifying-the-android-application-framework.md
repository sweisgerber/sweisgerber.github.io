---
title: "On Demystifying the Android Application Framework: Re-Visiting Android Permission Specification Analysis"
key: paper-axplorer
date: 2016-08-10T13:00:00+0100
draft: false
pubtype: paper
featured: true
description: >-
  "The Android middleware is not so hidden after all."
tags: 
  - Java
  - Android
  - Wala
  - Joana
  - Soot
image: ""
link: "https://paper.url"
fact: >- 
  ""
weight: 400
sitemap:
  priority : 0.8
---

### Abstract

In contrast to the Android application layer, Android’s application framework’s internals and their influence on the platform security and user privacy are still largely a black box for us. In this paper, we establish a static runtime model of the application framework in order to study its internals and provide the first high-level classification of the framework’s protected resources. We thereby uncover design patterns that differ highly from the runtime model at the application layer. We demonstrate the benefits of our insights for security-focused analysis of the framework by re-visiting the important use-case of mapping Android permissions to framework/SDK API methods. We, in particular, present a novel mapping based on our findings that significantly improves on prior results in this area that were established based on insufficient knowledge about the framework’s internals. Moreover, we introduce the concept of permission locality to show that although framework services follow the principle of separation of duty, the accompanying permission checks to guard sensitive operations violate it.

- Published in: [Proceedings of 25th USENIX security symposium (USENIX security 16)][proceedings]
- Alternate Paper Link: [publications.cispa.saarland][paper-cispa]
- Project Link: [github.com/reddr/axplorer][project-url]
- Poster (separate publication before the paper, is interpreted as work-in-progress) [EuroSP2016][poster]


#### Authors

- Michael Backes, Saarland University and Max Planck Institute for Software Systems (MPI-SWS)
- Sven Bugiel and Erik Derr, Saarland University
- Patrick McDaniel, The Pennsylvania State University
- Damien Octeau, The Pennsylvania State University and University of Wisconsin—Madison
- Sebastian Weisgerber, Saarland University

[proceedings]: https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_backes-android.pdf
[paper-cispa]: https://publications.cispa.saarland/657/
[project-url]: https://github.com/reddr/axplorer
[poster]: https://www.ieee-security.org/TC/EuroSP2016/posters/number13.pdf
