#!/bin/bash

cd /home/rijandhakal/Desktop

for file in Muscle_test/*.fa
do  
    out_name="$(basename $file .fa)"
    ext=".afa"
    out_file="$out_name$ext"
    echo out_file
    muscle -in $file -out $out_file
done
