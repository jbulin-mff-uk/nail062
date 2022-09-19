#!/bin/bash

mkdir -p output

# Lecture notes
cp lecture-notes.pdf output/lecture-notes.pdf

# Chapters
pdftk lecture-notes.pdf cat 8-17 output output/chapter1.pdf
pdftk lecture-notes.pdf cat 19-37 output output/chapter2.pdf
pdftk lecture-notes.pdf cat 38-44 output output/chapter3.pdf