#!/bin/bash

hdfs dfs -rm -r /user/s/assignment2/task4
hdfs dfs -rm -r /user/s/temp1_task4
hdfs dfs -rm -r /user/s/temp2_task4

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=@ \
-D num.key.fields.for.partition=1 \
-D mapreduce.partition.keypartitioner.options=-k1 \
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/s/temp1_task4 \
-mapper mapper1.py \
-file mapper1.py \
-reducer reducer1.py \
-file reducer1.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=@ \
-D num.key.fields.for.partition=1 \
-D mapreduce.partition.keypartitioner.options=-k1 \
-input /user/s/temp1_task4 \
-output /user/s/temp2_task4 \
-mapper mapper2.py \
-file mapper2.py \
-reducer reducer2.py \
-file reducer2.py \
-combiner combiner2.py \
-file combiner2.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=@ \
-D stream.map.output.field.separator=@ \
-D stream.num.map.output.key.fields=3 \
-D mapreduce.partition.keycomparator.options="-k1,1nr" \
-D mapred.reduce.tasks=1 \
-input /user/s/temp2_task4 \
-output /user/s/assignment2/task4 \
-mapper mapper3.py \
-file mapper3.py \
-reducer reducer3.py \
-file reducer3.py
