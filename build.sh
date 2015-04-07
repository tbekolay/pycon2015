#!/usr/bin/env bash
if [[ ! -e 'reveal.js' ]]; then
    wget https://github.com/hakimel/reveal.js/archive/2.6.2.zip -O reveal.js.zip
    unzip reveal.js.zip
    mv reveal.js-* reveal.js
    rm -f reveal.js.zip
fi
ipython nbconvert source.ipynb --to slides
mv source.slides.html index.html
echo "Now serve this directory with"
echo "  python -m SimpleHTTPServer"
