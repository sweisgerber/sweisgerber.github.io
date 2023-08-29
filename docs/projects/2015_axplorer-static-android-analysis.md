---
title: "Axplorer - Static Software Analysis of the Android Middleware"
key: axplorer
date: 2015-01-01T00:00:00+01:00
link: "https://github.com/reddr/axplorer"
# image: "/img/deploysonly.webp"
description: "Static Software Analysis of the Android Middleware with wala/joana (& soot exploration)"
featured: true
tags:
  - Java
  - Android
  - Android-Middleware
  - Wala
  - Joana
  - Soot
fact: "The Android middleware is not so hidden after all."
creator: true
weight: 100
sitemap: 
    priority : 0.8
---

[axplorer (Android explorer)](https://github.com/reddr/axplorer) is a static analysis tool to study Android's 
application framework's internals. 
It generates high-precision call-graphs for middleware services that are subsequently analyzed via 
control-flow slicing. As one of the results, axplorer can generate very accurate Android API to permission mappings.
