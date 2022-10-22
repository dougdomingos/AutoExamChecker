#!/bin/bash
# receives input from user
echo -n "Prova: "
read test_name;

# run the check script
python3 script/check.py $test_name

if [ $? -eq 2 ]; then
    echo "Provas disponíveis:"
    ls -w 10 gabaritos

else
    cat "results_$test_name.txt"

fi