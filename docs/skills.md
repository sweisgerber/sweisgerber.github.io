---
title: Skills
summary: The skills I collected over the years
skills:
  - grouping: Programming Languages
    skills:
      - Bash
      - C
      - C++
      - Java
      - Javascript
      - Perl
      - Python
      - Typescript
      - PHP
      - SQL

  - grouping: Build systems, etc
      skills:
      - Android OS build system
      - Ant
      - Bazel
      - Cmake
      - Gradle
      - Maven
      - Ninja
      - Parcel
      - Pipenv

  - grouping: Dev(Sec)Ops & Cloud
    skills:
      - Ansible
      - Apache
      - Caddy
      - name: Cockpit
#        url: https://cockpit-project.org
      - name: Docker
      - Github
      - Github Actions
      - Gitlab
      - Gitlab CI/CD
      - Helm
      - Kubernetes
      - NginX
      - NodeRed
      - name: OPNsense
      - name: Podman
      - Portainer

  - grouping: Monitoring
    skills:
      - Grafana
      - Prometheus
      - Loki
      - Promtail
      - Netdata
      - HealthChecks
      - Influx

  - grouping: Data Management
    skills:
      - name: Directus
#        url: https://directus.io
      - name: MariaDB
#        url: https://www.metabase.com
      - name: MetaBase
      - name: Mysql
      - name: NocoDB
      - name: OrientDB
      - name: Postgres
        icon: database

  - grouping: Operating System
    skills:
      - Android
      - Arch Linux
      - Debian Linux
      - Manjaro
      - Windows

  - grouping: Web
    skills:
      - Django
      - Emotion CSS
      - Hugo
      - Jekyll
      - Netlify
      - React
      - Wordpress

  - grouping: Tools
    skills:
      - fish shell
      - git
      - gitea
      - Jetbrains IDEs
      - Linux
      - ssh
      - subversion
---

# Skills

{% for skill in skills %}

## {{ skill.grouping }}

{% for skill_item in skill.skills %}
  {% if skill_item.name %}
    {% if skill_item.url %}
- [{{ skill_item.name }}]({{ skill_item.url }})
    {% else %}
- {{ skill_item.name }}
    {% endif %}
  {% else %}
- {{ skill_item }}
{% endif %}
{% endfor %}

</ul>

{% endfor %}
