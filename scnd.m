count=0
echo "Enter the list of numbers "
read numbers
for i in ${numbers[@]}
do
        if [$((i % 2)) -eq 0]; then
                count=$((count + i))
        fi
done
echo "The sum of even numbers are  $count"
