#!/bin/bash

hdfs dfs -rm -r /user/s/assignment1/task7

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=. \
-D stream.map.output.field.separator=. \
-D stream.num.map.output.key.fields=2 \
-D num.key.fields.for.partition=1 \
-D mapreduce.partition.keypartitioner.options=-k1 \
-D mapreduce.partition.keycomparator.options="-k1,1r -k2,2" \
-input /data/assignments/ex1/uniLarge.txt \
-output /user/s/assignment1/task7 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
