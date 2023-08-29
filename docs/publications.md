---
title: Publications
summary: An overview of the most important publications
date: 
some_url: 
#publications:
#  - name: 2011-09_masters-thesis_design-einer-mobilen-anwendung-zur-verschluesselten-sprackommunikation-auf-android.md
#    date: 2011-09-01
#    internal_url: ./publications/2011-09_masters-thesis_design-einer-mobilen-anwendung-zur-verschluesselten-sprackommunikation-auf-android.md
#  - name: 2014-11_you-can-run-but-you-cant-read.md
#    date: 2014-11-01
#    internal_url: ./publications/2014-11_you-can-run-but-you-cant-read.md
#  - name: 2016-08_on-demystifying-the-android-application-framework.md
#    date: 2016-08-01
#    internal_url: ./publications/2016-08_on-demystifying-the-android-application-framework.md
#  - name: 2017-04_artist-the-android-runtime-instrumentation-and-security-toolkit.md
#    date: 2017-04-01
#    internal_url: ./publications/2017-04_artist-the-android-runtime-instrumentation-and-security-toolkit.md
#  - name: 2021-10_towards-a-principled-approach-for-dynamic-analysis-of-androids-middleware.md
#    date: 2021-10-01
#    internal_url: ./publications/2021-10_towards-a-principled-approach-for-dynamic-analysis-of-androids-middleware.md
---

# Publications

{% set publications_list = [] %}

{% for publication_key in publications %}
    {% set _publication = publications[publication_key] %}
    {{ publications_list.append(_publication) or "" }} 
{% endfor %}

{% for publication in publications_list | sort(attribute='date', reverse = True) %}

!!! abstract "**Topics**: {{ publication.tags | join(', ') }} &nbsp;:material-calendar-outline: _{{ publication.date | string | truncate(4, true, '') }}_"

    ## {{ publication.title }}

    > {{ publication.description }}
  
    [Publication Details]({{ publication.url }}) :material-note-search-outline:

{% endfor %}
