#!/bin/bash

declare -i repetitions=3
declare -i maxValue=1000
declare -i iterations=70

rm ./PythonPlottingTool/*.csv

for ((rep=1; rep<=repetitions; rep++))
do
    printf "\n"
    echo "Repetition: $rep"
    filename="./res"

    test -f "$filename*.csv" && rm $filename

    ./TesinaAlgoritmi $rep $iterations $maxValue $filename
    mv $filename*.csv ./PythonPlottingTool
    
done

cd PythonPlottingTool
python plot.py $repetitions

echo "Done!"
