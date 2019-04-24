---
layout: archive
title: "Publications"
permalink: /publications/type
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<!-- Per TYPE -->

## [Journals](#journals) - [Conferences](#conferences) - [Misc](#misc) - [Communications](#communications) <a name="top"></a>

### [Sort publications per year](/publications)

<!--
<div class="{{ include.type | default: "list" }}__item">
    <h2 class="archive__item-title" itemprop="headline">
        <a name="journals"></a>
        Journals
    </h2>
</div>
-->

## Journals <a name="journals"></a> ([top](#top))
{% for post in site.publications reversed %}
    {% if post.type == "journal" %}
        {% include archive-single-pub.html %}
    {% endif %}
{% endfor %}

## Conferences <a name="conferences"></a> ([top](#top))
{% for post in site.publications reversed %}
    {% if post.type == "conference" %}
        {% include archive-single-pub.html %}
    {% endif %}
{% endfor %}

## Misc <a name="misc"></a> ([top](#top))
{% for post in site.publications reversed %}
    {% if post.type == "misc" %}
        {% include archive-single-pub.html %}
    {% endif %}
{% endfor %}

## Communications <a name="communications"></a> ([top](#top))
{% for post in site.publications reversed %}
    {% if post.type == "communication" %}
        {% include archive-single-pub.html %}
    {% endif %}
{% endfor %}
