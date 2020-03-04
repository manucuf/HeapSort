#!/bin/bash

declare -i repetitions=10
declare -i maxValue=1000
declare -i iterations=100

for ((rep=1; rep<=repetitions; rep++))
do
    printf "\n"
    echo "Repetition: $rep"
    filename="./res"

    if test -f "$filename*.csv"; then
      rm $filename
    fi
    
    ./TesinaAlgoritmi $rep $iterations $maxValue $filename

mv $filename*.csv ./PythonPlottingTool
cd PythonPlottingTool
python plot.py

echo 'Done!'
