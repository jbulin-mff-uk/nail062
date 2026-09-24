#!/bin/bash
# Script to compile all .tex files in the current directory and clean up auxiliary files
exceptions=("slides-header.tex")

for f in *.tex; do
    if [ -f "$f" ]; then
        if [[ " ${exceptions[*]} " == *" $f "* ]]; then
            echo "Skipping excluded file $f"
            continue
        fi
        echo "Compiling $f (first pass)..."
        pdflatex -interaction=nonstopmode "$f"
        echo "Compiling $f (second pass)..."
        pdflatex -interaction=nonstopmode "$f"
        echo "Cleaning up auxiliary files for $f..."
        basename="${f%.tex}"
        rm -f "$basename.aux" "$basename.log" "$basename.fls" "$basename.fdb_latexmk" "$basename.synctex.gz" "$basename.out" "$basename.toc" "$basename.nav" "$basename.snm" "$basename.vrb"
        echo "Done with $f"
        echo "---"
    fi
done