echo "Enter the directory path"
read input
find $input -maxdepth 1 -type f | wc -l
