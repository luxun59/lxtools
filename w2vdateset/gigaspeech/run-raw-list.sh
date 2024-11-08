
train_set=train_XL
shards_dir=giga_shards_raw

for x in $train_set ; do
    dst=$shards_dir/$x
    mkdir -p $dst
    make_shard_raw_list.py --resample 16000 --num_utts_per_shard 1000 \
      --num_threads 32 --segments data/$x/segments \
      data/$x/wav.scp data/$x/text \
      $(realpath $dst) data/$x/data.list
done







