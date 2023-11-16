cd gallery
find gallery -iname '*.jpg' -exec convert -define jpeg:size=200x200 '{}' -thumbnail 40000@ -gravity center  -extent 200x200  'thumbnails/{}' \;