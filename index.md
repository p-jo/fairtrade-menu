---
layout: global
type: ingang
description: Startsida
weight: 0

---

<div class="container">
  <div class="row">
    <div class="col-sm-12">
      <div class="alert alert-info alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          Nu är det riksstämma, <a href="#">anmäl dig här</a>
      </div>
      <p>&nbsp;</p>
    </div>
  </div>
</div>

<div class="container-fluid" id="front">

  <div class="row">
    {% for item in site.categories.front limit:1 %}
      {% include node/teaser.html col=12 %}
    {% endfor %}
  </div>

  <div class="row">
    {% for item in site.categories.front limit:2 offset:1 %}
      {% include node/teaser.html col=6 %}
    {% endfor %}
  </div>

  <div class="row">
    {% for item in site.categories.front limit:6 offset:3 %}
      {% include node/teaser.html col=4 %}
    {% endfor %}
  </div>

</div>
<div class="container">
  <div class="row">
    <div class="col-md-8 col-md-offset-2">
      <h3>Senaste nytt</h3>
      <br>
      {% for item in site.categories.type-blogg limit:4 %}
        {% include node/teaser_list.html %}
      {% endfor %}

      <p><a href="blogg" class="btn btn-default">Djurens Rätts blogg</a></p>
    </div>
  </div>
</div>
