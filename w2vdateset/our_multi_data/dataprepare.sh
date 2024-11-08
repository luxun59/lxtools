#!/bin/bash
# use your own data path
datadir=/data/home/luxun/mmsdataset/jap
subsetdatadir=evlWAV_16k
destdir=/data/home/luxun/mmsdataset/dest

myreffile=/data/home/luxun/mmsdataset/jap/evltest_8k_split_ref.txt

language=jpn

stage=0 # start from 0 if you need to start from data preparation
stop_stage=1


# local/data_prep_torchaudio.sh ${datadir}/LibriSpeech/${part} $wave_data/${part//-/_}
if [ ${stage} -le 0 ] && [ ${stop_stage} -ge 0 ]; then
    echo "prepare tsv"

    outname=test-${language}
    outdir=$destdir/$outname
    mkdir -p $outdir
    for part in $subsetdatadir;do
        python wav2vec_manifest.py ${datadir}/${part}/ --ext wav --dest ${outdir}  --valid-percent 0 --file-name ${outname}
    done

fi


if [ ${stage} -le 1 ] && [ ${stop_stage} -ge 1 ]; then
    echo "prepare ltr"
    for part in test-${language};do
    outname=$part
        outdir=$destdir/$outname
        echo $outdir
        python libri_labels.py ${outdir}/${outname}.tsv --read-ref-file ${myreffile} --output-dir $outdir --output-name $outname
    done

fi



