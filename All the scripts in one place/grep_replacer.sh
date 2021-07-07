#!/bin/bash
PATTERN=$1
FILE=$2
while IFS= read -r line; do
	#echo "'$line'"
	grep "$line" $FILE
done < $1
