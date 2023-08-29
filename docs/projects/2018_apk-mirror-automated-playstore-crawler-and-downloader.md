---
title: PlayGround - Automated Google Playstore Crawler and downloader (APK-Mirror)
key: playground
# date  --iso-8601=seconds   
date: 2018-01-01T00:00:00+01:00
link: 'https://example.org'
draft: false
featured: false
# image: ""
description: >-
  Automated Google Playstore Crawler, Downloader and Sorter
tags:
  - Python
  - Playstore
  - Android-Apk
fact: >-
  Putting 100k+ files in a single folder is not a good idea
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---

A good deal of research paper at CISPA needed Android applications APKs for static analysis, for doing statistical evaluations
and more.
In order to provide this as a central piece of infrastructure, I worked on a project that automatically crawled the
Google PlayStore by utilizing the category pages as entry for the crawling and crawling forward from there on, 
by parsing the "Similar Apps" section. 

This created an enormous (deduplicated) list of applications and games which were then downloaded and stored on disk.

A small CLI toolkit was provided for querying and retrieving from the storage as well.  
