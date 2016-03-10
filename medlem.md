---
layout: member
title: Medlem
ingress: 'Har du frågor om ditt medlemskap? Saknar du ditt medlemsnummer eller medlemskort?
Vill du höja ditt stöd via autogiro? <a href="">Här kan du kontakta medlemsservice</a>. Det går också att ringa på 08-555 914 40.<br>
Inte medlem än? <a>Bli medlem här</a>.'

type: ingang
description: Medlemssidor
weight: 20

---

<div class="row">
  {% for item in site.data.member %}
    <div class="col-sm-6 col-md-4">
      <a href=""><h3>{{item.cat}} <span class="{{item.icon}}"></span></h3></a>
      <div class="list-group">
        {% for item in item.items %}
          <a href="#" class="list-group-item">{{item}}</a>
        {% endfor %}
      </div>
    </div>
    {% cycle '', '', '<div class="clearfix"></div>' %}
  {% endfor %}
</div>

<hr>

<div class="row">
  <div class="col-sm-6">
    <a href=""><h3>Mest läst</span></h3></a>
    <div class="list-group">
      {% for item in site.data.member[0].items limit:5 %}
        <a href="#" class="list-group-item">{{item}}</a>
      {% endfor %}
    </div>
  </div>
  <div class="col-sm-6">
    <a href=""><h3>Senast uppdaterat</span></h3></a>
    <div class="list-group">
      {% for item in site.data.member[0].items limit:5 %}
        <a href="#" class="list-group-item">{{item}}</a>
      {% endfor %}
    </div>
  </div>
</div>
