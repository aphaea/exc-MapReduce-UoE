#!/bin/bash


hdfs dfs -rm -r /user/s/assignment2/task5

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.reduce.tasks=1 \
-input /data/assignments/ex2/part3/webLarge.txt \
-output /user/s/assignment2/task5 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
