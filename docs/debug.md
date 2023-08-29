---
title: My Document
summary: A brief description of my document.
authors:
    - Waylan Limberg
    - Tom Christie
date: 2018-07-10
some_url: https://example.com
extra:
  dingsi: hoho
projects:
  - name: Projekt One
    tag: 
      - täg one
      - tag 2
  - name: Projekt Two
    tag: 
      - täg three
      - tag 44
---

This is the first paragraph of the document. {{ some_url }}  {{ extra.dingsi }}


{% for project in projects %}

<h5>{{ project.name }}</h5>

<ul>
{% for tag in project.tag %}
<li>{{ tag }}</li>
{% endfor %}
</ul>


{% endfor %}

---

{{ macros_info() }}{: style="color: black;"}

---

# Files

{% for file in files %}


- `{{ file }}`


{% endfor %}

---

# Pages

{% for page in pages %}


- `{{ page }}`


{% endfor %}
