sound =['iaunn','iáunn','iàunn','iaunnh','iâunn','iáunn','iāunn','ia̍unnh',
        'uainn','uáinn','uàinn','uainnh','uâinn','uáinn','uāinn','ua̍innh',
        'aunn','áunn','àunn','aunnh','âunn','áunn','āunn','a̍unnh',
        'iann','iánn','iànn','iannh','iânn','iánn','iānn','ia̍nnh',
        'iunn','iúnn','iùnn','iunnh','iûnn','iúnn','iūnn','iu̍nnh',
        'iang','iáng','iàng','iak','iâng','iáng','iāng','ia̍k',
        'iong','ióng','iòng','iok','iông','ióng','iōng','io̍k',
        'uang','uáng','uàng','uak','uâng','uáng','uāng','ua̍k',
        'uann','uánn','uànn','uannh','uânn','uánn','uānn','ua̍nnh',
        'uinn','uínn','uìnn','uinnh','uînn','uínn','uīnn','ui̍nnh',
        'ang','áng','àng','ak','âng','áng','āng','a̍k',
        'ann','ánn','ànn','annh','ânn','ánn','ānn','a̍nnh',
        'enn','énn','ènn','ennh','ênn','énn','ēnn','e̍nnh',
        'iam','iám','iàm','iap','iâm','iám','iām','ia̍p',
        'ian','ián','iàn','iat','iân','ián','iān','ia̍t',
        'iau','iáu','iàu','iauh','iâu','iáu','iāu','ia̍uh',
        'ing','íng','ìng','ik','îng','íng','īng','i̍k',
        'inn','ínn','ìnn','innh','înn','ínn','īnn','i̍nnh',
        'ong','óng','òng','ok','ông','óng','ōng','o̍k',
        'onn','ónn','ònn','onnh','ônn','ónn','ōnn','o̍nnh',
        'uai','uái','uài','uaih','uâi','uái','uāi','ua̍ih',
        'uan','uán','uàn','uat','uân','uán','uān','ua̍t',
        'am','ám','àm','ap','âm','ám','ām','a̍p',
        'an','án','àn','at','ân','án','ān','a̍t',
        'au','áu','àu','auh','âu','áu','āu','a̍uh',
        'ia','iá','ià','iah','iâ','iá','iā','ia̍h',
        'im','ím','ìm','ip','îm','ím','īm','i̍p',
        'in','ín','ìn','it','în','ín','īn','i̍t',
        'io','ió','iò','ioh','iô','ió','iō','io̍h',
        'iu','iú','iù','iuh','iû','iú','iū','iu̍h',
        'om','óm','òm','op','ôm','óm','ōm','o̍p',
        'oo','óo','òo','ooh','ôo','óo','ōo','o̍oh',
        'ua','uá','uà','uah','uâ','uá','uā','ua̍h',
        'ue','ué','uè','ueh','uê','ué','uē','ue̍h',
        'ui','uí','uì','uih','uî','uí','uī','ui̍h',
        'un','ún','ùn','ut','ûn','ún','ūn','u̍t',
        'ng','ńg','ǹg','ngh','n̂g','ńg','n̄g','n̍gh',
        'a','á','à','ah','â','á','ā','a̍h',
        'e','é','è','eh','ê','é','ē','e̍h',
        'i','í','ì','ih','î','í','ī','i̍h',
        'o','ó','ò','oh','ô','ó','ō','o̍h',
        'u','ú','ù','uh','û','ú','ū','u̍h',
        'm','ḿ','m̀','mh','m̂','ḿ','m̄','m̍h']
number=['iaunn1','iaunn2','iaunn3','iaunnh4','iaunn5','iaunn6','iaunn7','iaunnh8',
        'uainn1','uainn2','uainn3','uainnh4','uainn5','uainn6','uainn7','uainnh8',
        'aunn1','aunn2','aunn3','aunnh4','aunn5','aunn6','aunn7','aunnh8',
        'iann1','iann2','iann3','iannh4','iann5','iann6','iann7','iannh8',
        'iunn1','iunn2','iunn3','iunnh4','iunn5','iunn6','iunn7','iunnh8',
        'iang1','iang2','iang3','iak4','iang5','iang6','iang7','iak8',
        'iong1','iong2','iong3','iok4','iong5','iong6','iong7','iok8',
        'uang1','uang2','uang3','uak4','uang5','uang6','uang7','uak8',
        'uann1','uann2','uann3','uannh4','uann5','uann6','uann7','uannh8',
        'uinn1','uinn2','uinn3','uinnh4','uinn5','uinn6','uinn7','uinnh8',
        'ang1','ang2','ang3','ak4','ang5','ang6','ang7','ak8',
        'ann1','ann2','ann3','annh4','ann5','ann6','ann7','annh8',
        'enn1','enn2','enn3','ennh4','enn5','enn6','enn7','ennh8',
        'iam1','iam2','iam3','iap4','iam5','iam6','iam7','iap8',
        'ian1','ian2','ian3','iat4','ian5','ian6','ian7','iat8',
        'iau1','iau2','iau3','iauh4','iau5','iau6','iau7','iauh8',
        'ing1','ing2','ing3','ik4','ing5','ing6','ing7','ik8',
        'inn1','inn2','inn3','innh4','inn5','inn6','inn7','innh8',
        'ong1','ong2','ong3','ok4','ong5','ong6','ong7','ok8',
        'onn1','onn2','onn3','onnh4','onn5','onn6','onn7','onnh8',
        'uai1','uai2','uai3','uaih4','uai5','uai6','uai7','uaih8',
        'uan1','uan2','uan3','uat4','uan5','uan6','uan7','uat8',
        'am1','am2','am3','ap4','am5','am6','am7','ap8',
        'an1','an2','an3','at4','an5','an6','an7','at8',
        'au1','au2','au3','auh4','au5','au6','au7','auh8',
        'ia1','ia2','ia3','iah4','ia5','ia6','ia7','iah8',
        'im1','im2','im3','ip4','im5','im6','im7','ip8',
        'in1','in2','in3','it4','in5','in6','in7','it8',
        'io1','io2','io3','ioh4','io5','io6','io7','ioh8',
        'iu1','iu2','iu3','iuh4','iu5','iu6','iu7','iuh8',
        'om1','om2','om3','op4','om5','om6','om7','op8',
        'oo1','oo2','oo3','ooh4','oo5','oo6','oo7','ooh8',
        'ua1','ua2','ua3','uah4','ua5','ua6','ua7','uah8',
        'ue1','ue2','ue3','ueh4','ue5','ue6','ue7','ueh8',
        'ui1','ui2','ui3','uih4','ui5','ui6','ui7','uih8',
        'un1','un2','un3','ut4','un5','un6','un7','ut8',
        'ng1','ng2','ng3','ngh4','ng5','ng6','ng7','ngh8',
        'a1','a2','a3','ah4','a5','a6','a7','ah8',
        'e1','e2','e3','eh4','e5','e6','e7','eh8',
        'i1','i2','i3','ih4','i5','i6','i7','ih8',
        'o1','o2','o3','oh4','o5','o6','o7','oh8',
        'u1','u2','u3','uh4','u5','u6','u7','uh8',
        'm1','m2','m3','mh4','m5','m6','m7','mh8']

for i in range(len(sound)):
        for j in range(0,len(sound)-1):
                if(len(sound[j])<len(sound[j+1])):
                        temp = sound[j]
                        sound[j]=sound[j+1]
                        sound[j+1]=temp
                        temp = number[j]
                        number[j]=number[j+1]
                        number[j+1]=temp
print(sound)
print(number)
print(len('iâm'))




# def change_to_number(s):
#     for c in range(len(sound)):
#         if s.find(sound[c])!=-1:
#             print(c)
#             print(s)
#             s = s.replace(sound[c],number[c])
#             print(s)
#             return s
#     return 'no_sound'

# print(change_to_number('uainnh'))