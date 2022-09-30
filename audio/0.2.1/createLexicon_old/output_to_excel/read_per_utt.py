import csv
f = open('per_utt','r')
export = open('export.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(export, delimiter=',')
writer.writerow(['Correct正確，Substitution錯誤(替換)，Insertiton插入，Deletion刪除'])
writer.writerow([])
i=1
for line in f.readlines():
    l = line.split(' ')
    l[-1]=l[-1][:-1]
    while '' in l:
        l.remove('')
    writer.writerow(l)
    if i%4==0:
        writer.writerow([])
        i=i/4-1
    i=i+1
export.close()
f.close()