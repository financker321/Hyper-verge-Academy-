#!/bin/bash
echo "Type the directory path"
read input
find $input -name "*.txt" -type f 
for i in *.txt
do
        cp $i ${i%.*}.bak
        sed -i 's/foo/bar/g' ${i%.*}.bak
done
