---
layout: landingpage
title: Gallery
permalink: /gallery/
subtitle: Handcrafted instruments from Paul Fremantle
excerpt: 
header_type: hero
header_img: "./assets/images/scroll.jpg"
---

{% assign externalgalleryviolin = "
./assets/images/gallery/violin/back.jpg,
./assets/images/gallery/violin/head.jpg,
./assets/images/gallery/violin/top1.jpg,
./assets/images/gallery/violin/top2.jpg,
./assets/images/gallery/violin/top3.jpg" %}

{% assign externalgalleryterz = "
./assets/images/gallery/terz/back1.jpg,
./assets/images/gallery/terz/back2.jpg,
./assets/images/gallery/terz/front1.jpg,
./assets/images/gallery/terz/front2.jpg,
./assets/images/gallery/terz/head.jpg" %}

{% assign externalgallerygsmini = "
./assets/images/gallery/gsmini/top1.jpg,
./assets/images/gallery/gsmini/top2.jpg,
./assets/images/gallery/gsmini/back1.jpg,
./assets/images/gallery/gsmini/back2.jpg,
./assets/images/gallery/gsmini/head.jpg" %}


# Violin after Stradivari
{% include_cached snippets/masonry.html external=externalgalleryviolin %}



# Terz Guitar after Stauffer
{% include_cached snippets/masonry.html external=externalgalleryterz %}

# Modern Steel String Guitar GS Mini
{% include_cached snippets/masonry.html external=externalgallerygsmini %}
