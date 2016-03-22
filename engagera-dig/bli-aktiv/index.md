---
layout: portal
title: Bli aktiv
ingress: "Vill du också göra en skillnad för djuren? Utvecklas som människa? Diskutera djurrätt och sprida information till mängder av människor?"

type: ingang
description: Bli aktiv
weight: 40
---

<div class="container">
  <p>&nbsp;</p>
  <div class="row">
    <div class="col-sm-6">
      <h3>Blixtaktioner</h3>
      <br>
      {% for item in site.categories.type-blixtaktion %}
        {% include node/teaser_list_simple.html %}
      {% endfor %}
      <p><a href="/engagera-dig/blixtaktioner/" class="btn btn-default">Alla blixtaktioner</a></p>
    </div>
    <div class="col-sm-6">
      <h3>Kampanjer</h3>
      <br>
      {% for item in site.categories.kampanj %}
        {% include node/teaser_list_simple.html %}
      {% endfor %}
      <p><a href="/engagera-dig/kampanjer/" class="btn btn-default">Alla kampanjer</a></p>
    </div>
  </div>
</div>
