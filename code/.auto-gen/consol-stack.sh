#!/bin/bash
rm -f final-cf-resources.dat
input="cf-resources.dat"
while IFS= read -r line
do
  #echo "$line"
  grep $line stack_resources.dat
  if [[ $? -ne 0 ]];then
    echo $line >> final-cf-resources.dat
  fi
done < "$input"
