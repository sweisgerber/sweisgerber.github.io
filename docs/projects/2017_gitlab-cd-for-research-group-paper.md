---
title: "DebLatex: Gitlab Pipelines for automated Researcher Paper Deployment"
key: cd-research-paper
# date  --iso-8601=seconds   
date: 2017-01-01T00:00:00+01:00
link: 'https://github.com/sweisgerber-dev/DebLatex/'
draft: false
featured: false
# image: ""
description: >-
  Automatic research paper building on CI/CD infrastructure with custom docker image.
tags:
  - Docker
  - Gitlab
  - Latex
  - CI/CD
fact: "Properly maintaining docker images is a time sink."
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---

Another project at CISPA, was the automation of the latex paper compilation in our self-hosted gitlab installation.
As no real suitable and maintained docker images existed at this point in time, I created the [DebLatex] image,
in order to have a customizable and maintained image available.
The image reduced some potential attack vectors by utilizing gosu for dropping privileges.

Besides the creation of the docker image, CI templates for gitlab were provided,
runner's set up and maintained and guidance to colleagues was provided.

[DebLatex]: https://github.com/sweisgerber-dev/DebLatex/
