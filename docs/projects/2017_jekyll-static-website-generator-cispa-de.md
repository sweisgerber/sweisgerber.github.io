---
title: New Website for cispa.de with Jekyll Static Website Generator
key: website-cispa-de-jekyll
date: 2017-01-01T00:00:00+01:00
link: 'http://cispa.saarland'
draft: false
featured: false
# image: ""
description: >-
  Static Website Generator with dynamic content generation for cispa.de 
  with Jekyll, Bootstrap and automatic data aggregation on gitlab CI/CD
tags:
  - Static-Website-Generator
  - Jekyll
  - Liquid
  - Ruby
  - SCSS
  - HTML
  - Bootstrap
  - JavaScript
  - CI/CD
  - Gitlab
  - Automation
fact: >-
  Dedicated system for specific tasks are great. CI/CD automatic is robust.
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---

The CISPA institute website should get overhauled, and we wanted to get rid of the old WordPress install, due to maintenance
and security reasons.
The publication management had received a dedicated system with [ePrints], so besides the employee data, which resided
in a dedicated account server, this needed to get integrated into the jekyll setup as well.
The interesting parts from an engineering perspective (as building websites with HTML/SCSS/etc is pretty boring),
were:

- Data aggregation from various sources and preparing them for usage in Jekyll
- Dynamic content generation based on the data (publication pages, user pages, etc)
- CI/CD automation with gitlab, including dynamic deployment environments and staging 

[ePrints]: ./2017_publication-management-system-eprints.md
