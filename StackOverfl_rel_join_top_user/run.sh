#!/bin/bash


hdfs dfs -rm -r /user/s/assignment2/task3
hdfs dfs -rm -r /user/s/temp_task3


hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=@ \
-D stream.map.output.field.separator=@ \
-D stream.num.map.output.key.fields=3 \
-D num.key.fields.for.partition=1 \
-D mapreduce.partition.keypartitioner.options=-k1 \
-D mapreduce.partition.keycomparator.options="-k1,1 -k3,3" \
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/s/temp_task3 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py \
-combiner combiner.py \
-file combiner.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=@ \
-D stream.map.output.field.separator=@ \
-D stream.num.map.output.key.fields=3 \
-D mapreduce.partition.keycomparator.options="-k1,1nr" \
-D mapred.reduce.tasks=1 \
-input /user/s/temp_task3 \
-output /user/s/assignment2/task3 \
-mapper mapper2.py \
-file mapper2.py \
-reducer reducer2.py \
-file reducer2.py
