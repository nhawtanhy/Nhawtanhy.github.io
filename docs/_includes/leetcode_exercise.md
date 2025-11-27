###  {{ include.number }}. {{ include.title }}
**Difficulty:** {{ include.difficulty }}  
**Status:** {{ include.status }}

{% if include.description %}
### 🔍 Problem Description
{{ include.description }}
{% endif %}

### Solution ({{ include.language | default: "Python" }})

```{{ include.language | default: "python" }}
{{ include.solution }}
