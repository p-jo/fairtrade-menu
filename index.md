---
layout: global
type: ingang
description: Startsida
weight: 0

---

<div class="container-fluid" id="front">

  <div class="row">
    {% for item in site.posts limit:1 %}
      {% include node/teaser.html col=12 %}
    {% endfor %}
  </div>

  <div class="row">
    {% for item in site.posts limit:2 offset:1 %}
      {% include node/teaser.html col=6 %}
    {% endfor %}
  </div>

  <div class="row">
    {% for item in site.posts limit:6 offset:3 %}
      {% include node/teaser.html col=4 %}
    {% endfor %}
  </div>

</div>
<div class="container">
  <div class="row">
    <div class="col-md-8 col-md-offset-2">
      <h2>Aktuellt</h2>
      {% for item in site.categories.type-blogg %}
        {% include node/teaser_list.html %}
      {% endfor %}
    </div>
  </div>
</div>
