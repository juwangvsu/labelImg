#!/bin/bash
cd "/home/student/labelImg"
python udpsnd.py $1
sleep 0.1
cp /media/student/code1/darknet/predictions.jpg /home/student/labelImg/
