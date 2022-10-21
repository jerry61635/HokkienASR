from cmath import exp
import csv
from turtle import tracer
from function import *

file = open('SuiSiannUTF8.csv', newline='', encoding='utf-8')
Lexicon = []
Sentence = []
Words = []
rows = list(csv.reader(file, delimiter=','))
file.close()
rows.pop(0)
no_use = ['SuiSiann_2266','SuiSiann_1550']

# read file
print('Read File')
# for rrr in range(20):
for rrr in range(len(rows)):
    if rrr%100==0:
        print(rrr)
    row = rows[rrr]
    # print(row[0])

    chk=False
    for s in no_use:
        if row[0].split('/')[1].split('.')[0]==s:
            chk=True
    if chk:
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
            # if nowSound!='':#當前音存在
            #     sound.append(nowSound)#把當前音放入到音清單裡面
            #     nowSound=''#清空當前音
        else:#如果不是符號
            nowSound=nowSound+row[3][r]#把字母放入到當前音後面

    #所有字轉數字調
    for s in range(len(sound)):
        sound[s]=change_to_number(sound[s])
        # print(sound[s])

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
    Words.append(word)
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

print('export corpus.txt')
export = open('./output/corpus.txt', 'w', newline='', encoding='utf-8-sig')
for W in Words:
    output=''
    for w in W:
        if output == '':
            output = w
        else:
            output = output+' '+w
    export.write(output+'\n')
export.close()

# print(Sentence)
# print(Words)
# print(Lexicon)

# export text_test
print('export text_test and text_train')
train_count=0
test_count=0
text_train = open('./output/text_train', 'w', newline='', encoding='utf-8-sig')
text_test = open('./output/text_test', 'w', newline='', encoding='utf-8-sig')
text_train_old = open('text_train', 'r', newline='', encoding='utf-8-sig')
text_test_old = open('text_test', 'r', newline='', encoding='utf-8-sig')
train=[]
test=[]
for n in text_train_old.readlines():
    train.append(n.split(' ')[0])
for n in text_test_old.readlines():
    test.append(n.split(' ')[0])

print(train)
print(test)
print(len(test))
for s in range(len(Sentence)):
    if train_count==len(train):
        break
    if train[train_count]==Sentence[s][0]:
        output=Sentence[s][0]
        for w in Words[s]:
            output = output+' '+w
        text_train.write(output+'\n')
        train_count=train_count+1

for s in range(len(Sentence)):
    if test_count==len(test):
        break
    if test[test_count]==Sentence[s][0]:
        output=Sentence[s][0]
        for w in Words[s]:
            output = output+' '+w
        text_test.write(output+'\n')
        test_count=test_count+1

text_train_old.close()
text_test_old.close()
text_train.close()
text_test.close()

print('export text.no_oov')
export = open('./output/text.no_oov', 'w', newline='', encoding='utf-8-sig')
text_train = open('./output/text_train', 'r', newline='', encoding='utf-8-sig')
for n in text_train.readlines():
    output='<SPOKEN_NOISE>'
    for w in n.split(' ')[1:]:
        output=output+' '+w
    export.write(output)
export.close()

# export Lexicon
print('export Lexicon')
export = open('./output/lexicon.txt', 'w', newline='', encoding='utf-8-sig')
for L in Lexicon:
    for w in L[1]:
        export.write(L[0]+' '+w+'\n')

export.close()

