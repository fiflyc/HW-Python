#!/bin/bash

python3 src/tabular.py in.csv
python3 src/graphics.py in.csv

rm artifacts/*.{toc,out,aux,log}
pdflatex -output-directory=artifacts/ artifacts/out_medium.tex
rm artifacts/*.{toc,out,aux,log}
rm artifacts/out_medium.tex
