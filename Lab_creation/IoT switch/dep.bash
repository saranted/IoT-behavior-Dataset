#!/bin/bash
c=0
for ((i=0;i<=19;i++))
do
    echo $c
    docker run -e var=$c -d --network lab-net --name switch$c lab/0.1
    ((c++))
    sleep 30s 
done
