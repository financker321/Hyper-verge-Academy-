#!/bin/sh
echo "The file names are $@"
mkdir backup
cp $@ backup
tar -cvf backup.tar backup
