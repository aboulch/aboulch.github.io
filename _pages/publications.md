---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<!-- ORIGINAL -->
<!-- {% for post in site.publications reversed %}
  {% include archive-single-pub.html %}
{% endfor %} -->

<!-- with YEAR -->
<!-- {% for post in site.publications reversed %}
    {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
    {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}

    {% if forloop.first %}
    {% include this_year.html %}

    {% endif %}

    {% include archive-single-pub.html %}

    {% if forloop.last %}

    {% else %}
        {% if this_year != next_year %}
        {% include next_year.html %}

        {% endif %}
    {% endif %}
{% endfor %} -->

<!-- Per TYPE -->

{% include pub_head.html %}


{% include pub_journal.html %}
{% for post in site.publications reversed %}
    {% if post.type == "journal" %}
        {% include archive-single-pub.html %}
    {% endif %}
{% endfor %}

{% include pub_conference.html %}
{% for post in site.publications reversed %}
    {% if post.type == "conference" %}
        {% include archive-single-pub.html %}
    {% endif %}
{% endfor %}

{% include pub_misc.html %}
{% for post in site.publications reversed %}
    {% if post.type == "misc" %}
        {% include archive-single-pub.html %}
    {% endif %}
{% endfor %}

{% include pub_communication.html %}
{% for post in site.publications reversed %}
    {% if post.type == "communication" %}
        {% include archive-single-pub.html %}
    {% endif %}
{% endfor %}
