---
title: "Kubernetes Cluster Setup, Proxmox Management & Automated DevOps Deployment"
key: gitlab-kubernetes-automatisation
# date  --iso-8601=seconds   
date: 2023-01-01T00:00:00+01:00
link: 'https://k3s.io'
draft: false
featured: true
# image: ""
description: >-
  Setup and integration of a k3s based kubernetes cluster into gitlab for AutoDevOps integration.
tags:
  - Kubernetes
  - DevOps
  - K3S
  - Gitlab
  - Helm
fact: >-
  k3s' helm controller is a time-saver, especially for small teams.
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---

Setup and integration of a k3s based kubernetes cluster into gitlab for AutoDevOps integration.
Initially a manual kubernetes setup was implemented, but for easier maintenance through the development team,
we switched to k3s.

The k3s cluster itself runs on a Proxmox VE.
