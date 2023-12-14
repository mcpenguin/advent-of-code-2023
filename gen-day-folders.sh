#!/bin/bash

# Bash Script to automatically generate folders for the days
# Usage: ./gen-day-folder.sh <year>

year=$1

for i in {22}
do
    problems_folder="./${year}/problems/day${i}"
    # init problem folder
    mkdir $problems_folder
    # init inputs folder and files
    mkdir "${problems_folder}/inputs"
    touch "${problems_folder}/inputs/test.txt"
    touch "${problems_folder}/inputs/real.txt"
    # init python files
    cp "./template/template.py" "${problems_folder}/day${i}-problem1.py"
    cp "./template/template.py" "${problems_folder}/day${i}-problem2.py"
done


