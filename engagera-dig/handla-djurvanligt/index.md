---
layout: portal
title: Handla djurvänligt
ingress: "Vi vet att det inte alltid är det enklaste att vara en medveten konsument. Vi har alla stått i butiken och kisat mot den kryptiska innehållsförteckningen "

type: ingang
description: Handla djurvänligt
weight: 40
---

<div class="container">
  <p>&nbsp;</p>
  <div class="row">
    <div class="col-md-12">
      <h3>Kampanjer och blixtaktioner</h3>
      <br>
      {% for item in site.categories.type-blixtaktion %}
        {% include node/teaser_action_small.html %}
      {% endfor %}
      <p><a href="/engagera-dig/kampanjer/" class="btn btn-default">Alla kampanjer</a></p>
    </div>

    <!--
    <div class="col-sm-6">
      <h3>Kampanjer</h3>
      <br>
      {% for item in site.categories.kampanj %}
        {% include node/teaser_list_simple.html %}
      {% endfor %}
      <p><a href="/engagera-dig/kampanjer/" class="btn btn-default">Alla kampanjer</a></p>
    </div>
    -->
  </div>
</div>
