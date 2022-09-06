from cmath import exp
import csv
import change_to_number
file = open('SuiSiannUTF8.csv', newline='', encoding='utf-8')
Lexicon = []
Sentence = []
rows = list(csv.reader(file, delimiter=','))
file.close()
rows.pop(0)

punctuation = ['-','.',' ',' ','，','。','?','？','「','」','…','！','!','"','、',',','：','；','─',';','）','（','〈','〉','《','》','“','”','(',')','『','』',':']
special_word=['㧌','𩛩','䆀','𤲍','𪜶','𨑨','𠕇','㽎']

def is_Chinese(c):
    if c >= u'\u4e00' and c <= u'\u9fa5':
        return True
    for word in special_word:
        if word == c:
            return True
    return False

# read file
print('Read File')
# for row in rows:
for rrr in range(0,len(rows)):
    if rrr%100==0:
        print(rrr)
    row = rows[rrr]
    wordCount=0
    word=[]
    sound=[]
    nowWord=''
    nowSound=''
    nowSentence=''
    for r in range(len(row[3])):
        chkSound=True
        for p in punctuation:
            if row[3][r]==p:
                chkSound=False
                if row[3][r]=='-':
                    nowSound=nowSound+row[3][r]
                    if row[3][r+1]!='-':
                        chkWord=True
                        while chkWord and wordCount<len(row[2])-1:
                            chkWord=False
                            for p2 in punctuation:
                                if p2==row[2][wordCount] and wordCount<len(row[2])-1:
                                    chkWord=True
                                    wordCount+=1
                        if wordCount<len(row[2])-1:
                            nowWord=nowWord+row[2][wordCount]
                            wordCount+=1
                elif nowSound!='':
                    nowSound=change_to_number.change_to_number(nowSound)
                    if nowSentence=='':
                        nowSentence=nowSound
                    else:
                        nowSentence=nowSentence+' '+nowSound
                    word.append(nowWord)
                    nowWord=''
                    sound.append(nowSound)
                    nowSound=''
        if chkSound:
            nowSound=nowSound+row[3][r]
            if nowWord=='' or (wordCount<len(row[2])-1 and not is_Chinese(row[2][wordCount]) and not is_Chinese(nowWord[-1])):
                chkWord=True
                while chkWord and wordCount<len(row[2])-1:
                    chkWord=False
                    for p2 in punctuation:
                        if p2==row[2][wordCount] and wordCount<len(row[2])-1:
                            chkWord=True
                            wordCount+=1
                if wordCount<len(row[2])-1:
                    nowWord=nowWord+row[2][wordCount]
                    wordCount+=1
    if nowSound!='':
        nowSound=change_to_number.change_to_number(nowSound)
        if nowSentence=='':
            nowSentence=nowSound
        else:
            nowSentence=nowSentence+' '+nowSound
        word.append(nowWord)
        nowWord=''
        sound.append(nowSound)
        nowSound=''

    Sentence.append([row[0].split('/')[1].split('.')[0],nowSentence])

    for w in range(len(word)):
        chkWord=True
        for i in range(len(Lexicon)):
            if word[w]==Lexicon[i][0]:
                chkWord=False
                chkSound=True
                for l in Lexicon[i][1]:
                    if sound[w].lower()==l:
                        chkSound=False
                        break
                if chkSound:
                    Lexicon[i][1].append(sound[w].lower())
        if chkWord:
            Lexicon.append([word[w],[sound[w].lower()]])

# print(Sentence)

# export corpus.txt
print('export corpus.txt')
export = open('corpus.txt', 'w', newline='', encoding='utf-8-sig')
for L in Sentence:
    export.write(L[1]+'\n')
export.close()

# export text_test
print('export text_test')
export = open('text_test', 'w', newline='', encoding='utf-8-sig')
for L in range(0,1000):
    export.write(Sentence[L][0]+' '+Sentence[L][1]+'\n')
export.close()

# export text_train
print('export text_train')
export = open('text_train', 'w', newline='', encoding='utf-8-sig')
for L in range(1000,3000):
    export.write(Sentence[L][0]+' '+Sentence[L][1]+'\n')
export.close()

# export Lexicon
print('export Lexicon')
export = open('export_n.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(export, delimiter=',')
for L in Lexicon:
    temp=[L[0]]
    for s in L[1]:
        temp.append(s)
    writer.writerow(temp)
export.close()

export = open('lexicon.txt', 'w', newline='', encoding='utf-8-sig')
for L in Lexicon:
    for s in L[1]:
        now = s+' '
        for l in range(len(s)):
            if s[l] == '-':
                if s[l+1]!='-':
                    now = now + ' '
            else:
                now = now+s[l]
    export.write(now+'\n')
export.close()