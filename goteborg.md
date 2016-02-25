---
layout: local
title: Göteborg
menu: 9
ingress: "Djurens Rätt Göteborg har över 3900 medlemmar varav många är ideellt engagerade för djurs rättigheter. Vi arbetar genom att sprida information på stan, bjuda på veganmat, arrangera utställningar, vegomässa, föredrag och mycket mer. Vem som helst som är intresserad är välkommen att besöka våra aktiviteter och komma med egna idéer."

type: ingang
description: Lokalorganisation
weight: 60

---

<div class="row">
  <div class="col-md-8 col-md-offset-1">


    <h2>Kontakta oss</h2>
    <div class="row">
      <div class="col-md-6">
        <p>
          Djurens Rätt Göteborg<br>
          Fjärde Långgatan 18<br>
          413 27 Göteborg<br>
          goteborg@djurensratt.se
        </p>
        <p>
          Ge gärna ett bidrag till vår verksamhet på PG 409 47-4.
        </p>
      </div>
      <div class="col-md-6">
        <p>
          <strong>Ordförande</strong><br>
          Moa Ranum<br>
          ordforandegbg@djurensratt.se
        </p>
        <p>
          <strong>Medlemsservice</strong><br>
          08-555 914 40<br>
          medlemsservice@djurensratt.se
        </p>

      </div>
    </div>
    <ul class="nav nav-pills">
      <li class="disabled"><a>Följ oss:</a></li>
      <li><a href="#">Facebook</a></li>
      <li><a href="#">Twitter</a></li>
    </ul>


    <hr>

    <h2>Nyheter</h2>
    {% for item in site.posts limit:5 %}
      {% include node/teaser_list.html %}
    {% endfor %}
    <p><a href="#" class="btn btn-default">Visa fler</a></p>

    <hr>


    <h2>Kalender</h2>
    {% for item in site.posts limit:5 %}
      {% include node/teaser_calendar.html %}
    {% endfor %}
    <p><a href="#" class="btn btn-default">Visa fler</a></p>

  </div>
</div>
