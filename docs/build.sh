#!/bin/bash

if [ -e dist/ ]; then
    rm dist/*
else
    mkdir dist/
fi

cp src/index.html dist/index.html
cp src/interactive.js dist/interactive.js
cp src/waldoheader.jpg dist/waldoheader.jpg
sass --no-source-map src/emerson-styles.scss dist/emerson-styles.css
