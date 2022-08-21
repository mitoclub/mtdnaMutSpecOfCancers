#!/bin/bash

ACC_LIST=data/external/human_mt_acc.txt
GB_FILE=data/external/human_mt_seqs.gb
LAG=0.4

touch $GB_FILE
for acc in `cat $ACC_LIST`; do
    cnt=`grep -c $acc $GB_FILE`
    if [ $cnt == 0 ]; then
        echo "Downloading $acc"
        efetch -db nuccore -format gb -id $acc >> $GB_FILE
        sleep $LAG
    else
        echo "Passing $acc"
    fi
done
