thumbsup --input gallery-photos/ --output gallery/ --index noyaml.html --theme cards --title "" --thumb-size 360 --photo-quality 100 --home-album-name "Chelli Strings Gallery"
cat gallery/index.yml > gallery/index.html
cat gallery/noyaml.html >> gallery/index.html