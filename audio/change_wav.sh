for j in *.wav; do echo $j; sox "$j" -e signed -r 16000 -b 16 ${j%%.wav}.new.wav; rm $j; done
for j in *.new.wav; do echo $j; mv $j ${j%%.new.wav}.wav; done

