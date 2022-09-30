import csv
f = open('per_utt','r')
export = open('export.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(export, delimiter=',')
writer.writerow([])
for line in f.readlines():
    l = line.split(' ')
    l[-1]=l[-1][:-1]
    while '' in l:
        l.remove('')
    writer.writerow(l)
export.close()
f.close()