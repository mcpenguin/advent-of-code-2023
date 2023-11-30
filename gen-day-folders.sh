#!/bin/bash

# Bash Script to automatically generate folders for the days
# Usage: ./gen-day-folder.sh

for i in {1..1}
do
    problems_folder="./problems/day${i}"
    # init problem folder
    mkdir $problems_folder
    # init inputs folder and files
    mkdir "${problems_folder}/inputs"
    touch "${problems_folder}/inputs/test.txt"
    touch "${problems_folder}/inputs/real.txt"
    # init python files
    cp "./problems/template/template.py" "${problems_folder}/day${i}-problem1.py"
    cp "./problems/template/template.py" "${problems_folder}/day${i}-problem2.py"
done


