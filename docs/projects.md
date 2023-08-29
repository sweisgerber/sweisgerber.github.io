---
title: Projects
summary: An overview of th emost important projects
date: 
some_url: 

---

# Projects

{% set projects_list = [] %}

{% for projects_key in projects %}
    {% set _project = projects[projects_key] %}
    {{ projects_list.append(_project) or "" }} 
{% endfor %}

{% for project in projects_list | sort(attribute='date', reverse = True) %}

!!! note "**Topics**: {{ project.tags | join(', ') }} &nbsp;:material-calendar-outline: _{{ project.date | string | truncate(4, true, '') }}_" 
    ## {{ project.title }}

    {{ project.description }}    

    > :material-message-outline: &nbsp;&nbsp;{{ project.fact }}

    _ :material-firework: [Project Details]({{ project.url }}) 


{% endfor %}