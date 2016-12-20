#!/bin/bash

hdfs dfs -rm -r /user/s/assignment1/task2

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input /user/s/assignment1/task1 \
-output /user/s/assignment1/task2 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py
