---
title: "Kubernetes Individual Service Monitoring with the PLG stack"
key: centralised-monitoring
# date  --iso-8601=seconds
date: 2023-01-01T00:00:00+01:00
link: 'https://grafana.com'
draft: false
featured: true
# image: ""
description: >-
  Setup of central monitoring and logging server with production-ready monitoring dashboards.
tags:
  - Loki
  - Prometheus
  - Grafana
  - Promtail
  - Netdata
  - Rsyslogd
  - Docker
  - Nginx
  - Kubernetes
  - DevOps
fact: >-
  Promtail's syslog interface only accepts TCP, while nginx' syslog logger only sends UDP.
creator: false
---

Setup of a centralised log and monitoring server, with selected long-termn storage for statistics.
Kubernetes service logging, physical host logging and monitoring data with Prometheus & Loki as database, Promtail as an aggregator and Grafana as the user interface.

Some Dashboards were configured for non-technical personell as well.

rsyslogd and netdata provider additional data & input.

