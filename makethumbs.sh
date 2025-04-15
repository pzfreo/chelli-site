#!/bin/bash
cd ~/repos/chelli-site
rm -r thumbnails/
find gallery -type d -exec mkdir -p "thumbnails/{}" \;
find gallery -iname '*.jpg' -exec convert -define jpeg:size=300x300 '{}' -thumbnail 90000@ -gravity center  -extent 300x00  'thumbnails/{}' \;
find gallery -iname '*.png' -exec convert -define png:size=300x300 '{}' -thumbnail 90000@ -gravity center  -extent 300x00  'thumbnails/{}' \;