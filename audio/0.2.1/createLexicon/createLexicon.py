from cmath import exp
import csv
from re import S
from function import *
import random
import shutil
file = open('SuiSiannUTF8.csv', newline='', encoding='utf-8')
Lexicon = []
Sentence = []
rows = list(csv.reader(file, delimiter=','))
file.close()
rows.pop(0)

# read file
print('Read File')
# for rrr in range(5,6):
for rrr in range(len(rows)):
    if rrr%100==0:
        print(rrr)
    row = rows[rrr]


    if row[0].split('/')[1].split('.')[0]=='SuiSiann_2266':
        continue

    #把中文字標點符號拿掉
    for w in row[2]:#把所有標點符號拿掉
        if check_punctuation(w):#檢查是不是標點符號
            row[2] = row[2].replace(w,'')#把標點符號移除

    #檢查有沒有英文字
    if check_have_english(row[2]):
        continue

    #整句英文字轉小寫
    row[3]=sentence_to_lower(row[3])
    

    #切音成詞
    sound=[]
    nowSound=''
    for r in range(len(row[3])):
        #確認是不是符號
        if check_punctuation(row[3][r]):#如果是符號
            #檢查是不是連字號
            if check_hyphen(row[3][r]) and nowSound!='':#是連字號
                nowSound=nowSound+'-'#加上連字號
            else:#不是連字號
                if nowSound!='':#當前音存在
                    sound.append(nowSound)#把當前音放入到音清單裡面
                    nowSound=''#清空當前音
        else:#如果不是符號
            nowSound=nowSound+row[3][r]#把字母放入到當前音後面

    #所有字轉數字調
    for s in range(len(sound)):
        # print(sound[s])
        sound[s]=change_to_number(sound[s])

    #儲存整句數字調
    nowSentence=''
    for s in sound:
        if nowSentence!='':
            nowSentence=nowSentence+' '+s
        else:
            nowSentence=s
    
    #把中文字切成詞清單
    word=[]
    wordidx=0
    for s in sound:#切字
        nowWord=''
        for i in range(word_count(s)):
            nowWord=nowWord+row[2][wordidx]
            wordidx=wordidx+1
        word.append(nowWord)

    #整句英文數字調放入清單，來建立corpus和text
    Sentence.append([row[0].split('/')[1].split('.')[0],nowSentence])

    #辭典，建立lexicon用
    for w in range(len(word)):
        chkWord=True
        for i in range(len(Lexicon)):
            if word[w]==Lexicon[i][0]:
                chkWord=False
                chkSound=True
                for l in Lexicon[i][1]:#如果音出現過則跳過
                    if sound[w].lower()==l:
                        chkSound=False
                        break
                if chkSound:#如果音沒出現過則要建立
                    Lexicon[i][1].append(sound[w])
        if chkWord:#如果沒出現過則要建立
            Lexicon.append([word[w],[sound[w]]])

# print(word)
# print(sound)
# print(Sentence)

# export corpus.txt
print('export corpus.txt')
export = open('corpus.txt', 'w', newline='', encoding='utf-8-sig')
for L in Sentence:
    export.write(L[1]+'\n')
export.close()
shutil.copyfile('./corpus.txt','../../../data/local/corpus.txt')

# export text_test
p=0.2 #比例
print('export text_test and text_train')
export = open('text_train', 'w', newline='', encoding='utf-8-sig')
export2 = open('text_test', 'w', newline='', encoding='utf-8-sig')
try:
    for L in range(len(Sentence)):
        if random.random()>=p:
            export.write(Sentence[L][0]+' '+Sentence[L][1]+'\n')
            shutil.copyfile('../ImTong/'+Sentence[L][0]+'.wav','../../train/'+Sentence[L][0]+'.wav')
        else:
            export2.write(Sentence[L][0]+' '+Sentence[L][1]+'\n')
            shutil.copyfile('../ImTong/'+Sentence[L][0]+'.wav','../../test/'+Sentence[L][0]+'.wav')
except:
    print('export text')
export.close()
export2.close()
shutil.copyfile('./text_train','../../../data/train/text')
shutil.copyfile('./text_test','../../../data/test/text')


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


noSameLexicon=[]
export = open('lexicon_haveSame.txt', 'w', newline='', encoding='utf-8-sig')
for L in Lexicon:
    #把連字號拿掉
    for s in L[1]:
        now = ''
        for l in range(len(s)):
            if s[l] == '-':
                if s[l+1]!='-':
                    now = now + ' '
            else:
                now = now+s[l]
    export.write(s+' '+to_tone(now)+'\n')

    #檢查有沒有出現過
    wordChk=True
    for n in noSameLexicon:
        try:
            if n[0]==s:
                wordChk=False
                break
        except:
            a=1
    #如果重複出現過就不存
    if wordChk:
        noSameLexicon.append([s,now])
export.close()

export = open('lexicon.txt', 'w', newline='', encoding='utf-8-sig')
for L in noSameLexicon:
    export.write(L[0]+' '+to_tone(L[1])+'\n')
export.close()


print('nonsilence_phones.txt')
tone=[]
for L in noSameLexicon:
    for w in to_tone(L[1]).split(' '):
        toneCheck=True
        for t in tone:
            if w==t:
                toneCheck=False
        if toneCheck:
            tone.append(w)
tone.sort()
tone.pop(0)
# print(tone)
export = open('nonsilence_phones.txt', 'w', newline='', encoding='utf-8-sig')
for L in tone:
    export.write(L+'\n')
export.close()