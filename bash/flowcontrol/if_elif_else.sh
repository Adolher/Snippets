#!/bin/bash

x=6
y=6

if [ $x -gt $y ]
then
    echo "x > y"
elif [ $x -eq $y ]
then
    echo "x == y"
else
    echo " x < y"
fi
