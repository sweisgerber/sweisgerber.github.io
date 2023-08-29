---
title: Memory Management Library for MDC architecture and Memory Driven Computing Research Evaluation
key: mdc
# date  --iso-8601=seconds   
date: 2019-01-01T00:00:00+01:00
link: 'https://github.com/FabricAttachedMemory'
draft: false
featured: true
# image: ""
description: >-
  The project implemented a prototypical memory-management library, that made applications benefit from MDC hardware without changing their source code. 
tags:
  - Memory-Driven-Computing
  - Application-Manipulation
  - Docker
  - LD_PRELOAD
  - Vagrant
  - Virtualbox
  - Singularity
  - QEMU
fact: >-
  LD_PRELOAD and modifying shared libraries is an awesome mechanism to modify and enhance applications without touching their source code.
creator: false
weight: 999
sitemap:
  priority: 0.8
  weight: 0.1
---
This project needs a short explanation of a not commonly known technology with the name MDC.
MDC stands for Memory-Driven Computing and is a project, initiated by HPE, to tackle the slowing of Moore's law with a new computer architecture.

The main concept is fast load/store access to large shared pool of fabric-attached non-volatile memory.
The memory in this case is NVRAM (non-volatile RAM), which is persistent fast RAM storage where the data contents of
the RAM survives reboots, thus converging memory and storage -> Byte-addressable NVRAM replaces hard drives and SSDs.
All NVRAM modules on one node (physical machine) are addressable and connected and other nodes with their NVRAMs as well.
The prototypical implementation by HPE was called "[The Machine]" and was a computer cluster that connected many MDC nodes over a "memory fabric bus".
This fabric-attached memory pool is accessible by all compute resources, even remote via Optical networking provides near-uniform low latency which resulted in direct, unmediated  access to all fabric-attached NVM across the memory fabric.

The project itself implemented a prototypical memory-management library, that made applications, which currently were not MDC aware and couldn't use the MDC architecture's benefits, compatible.
On a linux system, this library was preloaded via `LD_PRELOAD` and replaced the `malloc*` calls of the applications with MDC aware memory allocation, so that legacy applications benefited from it, without further implementation efforts.
The project utilized `tm-librarian` and the emulation layer of [FabricAttachedMemory].

> No source-code has been published, the link goes to the parent project's page

[FabricAttachedMemory]: https://github.com/FabricAttachedMemory
