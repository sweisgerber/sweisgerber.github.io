---
title: Headless CMS extension for cispa.de with Jekyll and Netlify
key: website-cispa-de-netlify
# date  --iso-8601=seconds   
date: 2019-01-01T00:00:00+01:00
link: 'https://cispa.saarland'
draft: true
featured: false
# image: ""
description: >-
  Headless CMS for cispa.saarland with Jekyll and Netlify for th non-tech personnel.
tags:
  - Jekyll
  - Netlify
  - Gitlab
  - CI/CD
fact: >-
  A Static Website Generator can be a CMS, too!
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---

As jekyll and our CI/CD-based toolchain required the writing of markdown/yaml pased text files and the usage of git,
we wanted to have a system in place, that enabled non-tech personnel an easier way to write news-posts.
A new website setup was already on the horizon, so we needed a simple and quick solution, to fill the time until then.

After some research we found [netlify CMS](https://www.netlifycms.org/) and integrated it easily in our existing jekyll
setup and the existing CI/CD deployment scheme.

