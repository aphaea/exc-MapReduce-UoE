hdfs dfs -rm -r /user/s/assignment2/task1

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=:@ \
-D num.key.fields.for.partition=1 \
-input /data/assignments/ex2/part1/large/ \
-output /user/s/assignment2/task1 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py \
-combiner combiner.py \
-file combiner.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
