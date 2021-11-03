#!/usr/bin/env bash

#this script is to help clean up images and containers all at once.

docker ps -a 
docker images
read -p 'container id: ' con
read -p 'image id: ' img
docker rm -f $con
docker image rm -f $img
echo deleted $con and $img
docker ps -a 
docker images