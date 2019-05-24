#!/bin/bash
c=0
for ((i=0;i<=20;i++))
do
    echo $c
    docker container kill switch$c
    docker rm switch$c
    ((c++))
done
