#!/bin/bash

INFILE="$1"

while IFS= read -ra arr; do
    #echo wget -O "${arr[0]}" "${arr[1]}"
    wget -O ${arr[0]} ${arr[1]}
done < $INFILE
