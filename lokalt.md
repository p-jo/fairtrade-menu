---
layout: local
title: Lokalt
menu: 1
submenu: 1
ingress: "Gräsrotsarbetet inom Djurens Rätt är nyckeln till att nå vårt mål - ett samhälle som inte förtrycker djur. Som medlem har du möjlighet att engagera dig tillsammans med andra i din närhet - samtidigt som du gör en insats för djuren får du chansen att möta trevliga och likasinnade människor."

type: ingang
description: Lokalt
weight: 50

---

<div class="row">
  {% for item in site.data.local %}
    <div class="col-sm-4 col-md-3">
      <h4><a href="/goteborg/">{{item.name}}</a></h4>
    </div>
  {% endfor %}
</div>
