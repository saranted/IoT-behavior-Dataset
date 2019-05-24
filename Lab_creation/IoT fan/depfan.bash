#!/bin/bash
c=0
for ((i=0;i<=19;i++))
do
    echo $c
    docker run -e var=$c -d --network lab-net --name fan$c lab/0.2
    ((c++))
    sleep 30s 
done
