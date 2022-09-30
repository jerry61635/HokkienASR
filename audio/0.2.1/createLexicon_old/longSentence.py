import csv
import os
import shutil
file = open('SuiSiannUTF8.csv', newline='', encoding='utf-8')
sentence=[[],[],[],[]]
rows = list(csv.reader(file, delimiter=','))
file.close()
rows.pop(0)
count=0

for row in rows:
    if eval(row[4])>=10:
        sentence[count].append(row)
        count=(count+1)%4
        print(row)

export = open('longSentence/蔡濟謙.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(export, delimiter=',')
for L in sentence[0]:
    writer.writerow(L)
    if not os.path.exists('longSentence/蔡濟謙/'+L[0].split('/')[1].split('.')[0]):
        os.mkdir('longSentence/蔡濟謙/'+L[0].split('/')[1].split('.')[0])
    shutil.copyfile('0.2.1/'+L[0], 'longSentence/蔡濟謙/'+L[0].split('/')[1].split('.')[0]+'/'+L[0].split('/')[1])
    f = open('longSentence/蔡濟謙/'+L[0].split('/')[1].split('.')[0]+'/text.txt', 'w',encoding='utf-8-sig')
    f.write(L[2])
    f.write('\n')
    f.close()
export.close()
export = open('longSentence/鄭亦鈞.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(export, delimiter=',')
for L in sentence[1]:
    writer.writerow(L)
    if not os.path.exists('longSentence/鄭亦鈞/'+L[0].split('/')[1].split('.')[0]):
        os.mkdir('longSentence/鄭亦鈞/'+L[0].split('/')[1].split('.')[0])
    shutil.copyfile('0.2.1/'+L[0], 'longSentence/鄭亦鈞/'+L[0].split('/')[1].split('.')[0]+'/'+L[0].split('/')[1])
    f = open('longSentence/鄭亦鈞/'+L[0].split('/')[1].split('.')[0]+'/text.txt', 'w',encoding='utf-8-sig')
    f.write(L[2])
    f.write('\n')
    f.close()
export.close()
export = open('longSentence/張佳渝.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(export, delimiter=',')
for L in sentence[2]:
    writer.writerow(L)
    if not os.path.exists('longSentence/張佳渝/'+L[0].split('/')[1].split('.')[0]):
        os.mkdir('longSentence/張佳渝/'+L[0].split('/')[1].split('.')[0])
    shutil.copyfile('0.2.1/'+L[0], 'longSentence/張佳渝/'+L[0].split('/')[1].split('.')[0]+'/'+L[0].split('/')[1])
    f = open('longSentence/張佳渝/'+L[0].split('/')[1].split('.')[0]+'/text.txt', 'w',encoding='utf-8-sig')
    f.write(L[2])
    f.write('\n')
    f.close()
export.close()
export = open('longSentence/郭晏瑜.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(export, delimiter=',')
for L in sentence[3]:
    writer.writerow(L)
    if not os.path.exists('longSentence/郭晏瑜/'+L[0].split('/')[1].split('.')[0]):
        os.mkdir('longSentence/郭晏瑜/'+L[0].split('/')[1].split('.')[0])
    shutil.copyfile('0.2.1/'+L[0], 'longSentence/郭晏瑜/'+L[0].split('/')[1].split('.')[0]+'/'+L[0].split('/')[1])
    f = open('longSentence/郭晏瑜/'+L[0].split('/')[1].split('.')[0]+'/text.txt', 'w',encoding='utf-8-sig')
    f.write(L[2])
    f.write('\n')
    f.close()
export.close()