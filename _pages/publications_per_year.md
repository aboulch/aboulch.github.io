---
layout: archive
title: "Publications"
permalink: /publications/year/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<a name="top"></a>

### [Sort publications by type](/publications/)


<!-- with YEAR -->
{% for post in site.publications reversed %}
    {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
    {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}
    
    {% if forloop.first %}

<div class="{{ include.type | default: "list" }}__item">
<article class="archive__item" itemscope itemtype="http://schema.org/CreativeWork">
    <h2 class="archive__item-title" itemprop="headline">
        {{ this_year }} (<a href="#top">top</a>) </h2>
</article>
</div>


    {% endif %}



    {% include archive-single-pub.html %}

    {% if forloop.last %}

    {% else %}
        {% if this_year != next_year %}

<div class="{{ include.type | default: "list" }}__item">
  <article class="archive__item" itemscope itemtype="http://schema.org/CreativeWork">
    <h2 class="archive__item-title" itemprop="headline">
        {{ next_year }} (<a href="#top">top</a>) </h2> 
  </article>
</div>


        {% endif %}
    {% endif %}
{% endfor %}

