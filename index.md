---
layout: landingpage
title: <span class="font-weight-bold">Chelli Strings</span> #'<span class="chulapa">Chelli Strings</span>'
subtitle: <span style="color:#acacad">Handcrafted stringed instruments made in Sussex, UK</span>
excerpt: 
# header_type: splash
# header_img: "./assets/images/scroll.jpg"
# og_image: "./assets/images/scroll.jpg"
include_on_search: true
show_sociallinks: false
show_tags: false
project_links:
    - url: https://instagram.com/paulfremantleluthier
      icon: fab fa-instagram fa-lg
      label: Follow
---
<script src="/assets/public/masonry.pkgd.min.js"></script>
<script src="/assets/public/imagesloaded.pkgd.min.js"></script>


<!-- <img height="1000" style="margin-bottom: 5px;" src="gallery/fiddle/hero.png"/> -->
<div id="masonry">
    <div class="image-item">
        <img src="gallery/fiddle/oldhero.png"/>
        <p style="text-align:center;">Fiddle after Matthew Hardie c.1800</p>
    </div>
</div>

<br/>
<p style="text-align:center;font-size:150%" >
<a href="/about">about</a>  / <a href="/gallery">gallery</a> /  <a href="https://paulfremantleluthier.substack.com/archive">blog</a>
</p>

<script type="text/javascript">

  
    
    var elem = document.getElementById('masonry');
    var msnry = new Masonry( elem, {
        itemSelector: '.image-item',
        columnWidth: 2000
    });

    imagesLoaded(elem, () => msnry.layout());
    
</script>

