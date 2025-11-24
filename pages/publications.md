---
layout: default
title: Publications
nav_order: 2
permalink: /publications/
has_children: false
search_exclude: true
---

<h1>{{ page.title }}</h1>

<ul>
  {% for publication in site.publications reversed %}
    <li>
      <a href="{{ publication.permalink }}">{{ publication.title }}</a><br/>
      <i>{{ publication.venue }}</i>, {{ publication.date | default: "1900-01-01" | date: "%Y" }}
    </li>
  {% endfor %}
</ul>