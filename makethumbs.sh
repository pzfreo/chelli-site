#!/bin/bash
cd ~/repos/chelli-site
rm -r thumbnails/
find gallery -type d -exec mkdir -p "thumbnails/{}" \;
find gallery -iname '*.jpg' -exec convert -define jpeg:size=200x200 '{}' -thumbnail 40000@ -gravity center  -extent 200x200  'thumbnails/{}' \;