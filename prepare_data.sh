#!/bin/bash

. ./path.sh

echo 'Preparing wav.scp'
python3 wav_prepare.py

echo 'Preparing utt2spk'
python3 utt2spk_prepare.py

echo 'Preparing text and corpus'
python3 text_corpus_prepare.py

cp data/test/text data/local/train
