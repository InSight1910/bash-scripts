#!/bin/bash
timeSleep=$(echo '2.5' | bc -l) 
sudo service docker start
sleep 1
sudo docker container start mongo

sleep $timeSleep

mongo --host localhost -port 27017
