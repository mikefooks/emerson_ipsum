#!/bin/bash

if [ -e dist/ ]; then
    rm dist/*
else
    mkdir dist/
fi

cp src/index.html dist/index.html
cp src/waldo.jpg dist/waldo.jpg
sass src/main.scss dist/main.css
