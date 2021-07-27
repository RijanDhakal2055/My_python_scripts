#!/bin/bash

cd /home/opensourceferns/Desktop/Script_atoll/Muscle

for file in Muscle_test/*.fa
do
    muscle -in file -out file.afa
done