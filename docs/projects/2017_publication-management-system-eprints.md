---
title: Publication Management System Implementation with ePrints
key: eprints
# date  --iso-8601=seconds   
date: 2017-01-01T00:00:00+01:00
link: 'https://publications.cispa.saarland'
draft: false
featured: false
# image: ""
description: >-
  Evaluation, Setup, Migration and Extension of new Publication Management System
tags:
  - Publication-Management
  - Eprints
  - Perl
  - SQL
  - JSON
fact: >-
  Old software has its Pros.
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---

The CISPA institute website should get overhauled, and we wanted to get rid of the old WordPress install,
due to maintenance and security reasons.
A dedicated system should get used instead of an all-in-one system, so different Publication Management System 
were compared and ePrints was set up.
The old data from the WordPress/TeachPress setup needed to get migrated to the new ePrints data model which I did as well.
As ePrints provides lots of sane defaults, one could use a lot out of the box, but some Institute specific fields 
and customizations had to get implemented via Perl and ePrints xPages template format.
