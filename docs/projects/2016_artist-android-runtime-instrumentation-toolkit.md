---
title: ARTist - the flexible Android Instrumentation Framework
key: artist
date: 2016-01-01T00:00:00+01:00
link: "https://artist.cispa.saarland/"
# image: "/img/deploysonly.webp"
description: > 
    ARTist is a flexible Android instrumentation framework for security researchers 
    and developers based on the Android Runtime’s dex2oat on-device compiler.
featured: true
tags:
  - Java
  - Android
  - Android-Middleware
  - Android-System
  - Android-Art
  - Compiler-Development
  - Dex2oat
  - Android-Apps
  - Mobile-Development
fact: "Application instrumentation works and is useful."
creator: true
weight: 100
sitemap: 
    priority : 0.8
---

ARTist is a flexible open source instrumentation and hybrid analysis framework for Android apps and Android’s 
Java middleware. It is based on the Android Runtime’s (ART) compiler and modifies code during on-device compilation.

ARTist blends particularly well into the Android app install mechanism because it does not change the 
app’s package (APK) file but just replaces the compiled native version, hence it preserves the package 
signature so that modified apps still receive updates.

ARTist can be used to instrument arbitrary third party apps and Androids Java middleware layer (e.g., system server).

To find out more about ARTist, please visit the [website](https://artist.cispa.saarland/), where you read the [paper](https://artist.cispa.saarland/publications/) and
get a better overview of what [ARTist is doing](https://artist.cispa.saarland/docs/overview/).
