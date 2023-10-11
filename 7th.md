#!/usr/bin/env bash
echo "Enter the word to find"
read great
echo "Enter the filename"
read author
grep "$great" "$author" --color=auto

#!/bin/bash
echo "Enter the word you need to change "
read great
echo "Enter the new word to replace "
read Super
echo "Enter the file name "
read Author
sed -i 1,5s/$great/$super/g $author
