---
title: Skills
summary: The skills I collected over the years
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
