#!/bin/sh

for i in {1..25}; do cp template.py $i.py; done
touch {1..25}.txt
touch {1..25}_temp.txt

