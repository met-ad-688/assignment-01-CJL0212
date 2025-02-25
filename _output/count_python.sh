#!/bin/bash
count=$(grep -i "python"  stackoverflow_data/question_tags.csv| wc -l)
echo "Number of lines containing 'python' in CSV files: $count"


