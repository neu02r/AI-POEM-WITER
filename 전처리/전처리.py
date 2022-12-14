import pandas as pd
import csv
import sys
from webbrowser import Konqueror
from pandas import DataFrame, Series
import re



poem=pd.read_csv('poemss.csv', encoding='utf-8')

for i in range(0, 6611) :
    poem["시"][i] = poem["시"][i].replace(u'\xa0', u' ')  #유니코드 제거
    poem["시"][i] = poem["시"][i].replace('\n \n ', '\n\n')    
    poem["시"][i] = poem["시"][i].replace('\n  \n \n ', '')
    poem["시"][i] = poem["시"][i].replace('    ', '\n\n') 
    poem["시"][i] = poem["시"][i].replace('  ', '\n')  #두칸 띄어쓰기 제거
    poem["시"][i] = poem["시"][i].strip()
    poem["시"][i] = re.sub(r'\([^)]*\)', '', poem["시"][i]) #괄호안 내용 제거
    poem["시인"][i] = re.sub(r'\([^)]*\)', '', poem["시인"][i]) #시인 이름과 한문 같이 되어있는 부분 제거
    poem["제목"][i] = re.sub(r'\([^)]*\)', '', poem["제목"][i]) #제목 이름과 한문 같이 되어있는 부분 제거

df = pd.DataFrame(poem)
df_poem = df.loc[:,"시"]
df_writer = df.loc[:,'시인']
df_title = df.loc[:,'제목']
print(df_writer)

not_korean=[] #본문에 한글 이외의 글자
for line in df_poem:    
    for i in range(0,int(len(line))) :
        char_line = ord(line[i])
        if(int('2E80',16) <= char_line <= int('2EFF',16))  \
        or (3400 <= char_line <= int('4DB5',16)) \
        or (int('4E00',16) <= char_line <= int('9FBF',16)) \
        or (int('0x61',16) <= char_line <= int('0x7A',16)) \
        or '---' in df_poem[i] \
        or df_writer[i] in df_poem[i] \
        or '출처:' in df_poem[i] :
            not_korean.append(line)

not_korea = [] #영문으로 이름이 쓰여진 외국 시인
for line in df_writer: 
    for i in range(0,int(len(line))) :
        if line[i].upper() != line[i].lower() :
            not_korea.append(line)
            print(line)

not_title =[] #제목에 한글 이외의 글자
for line in df_title: 
    for i in range(0,int(len(line))) :
        char_line = ord(line[i])
        if(int('2E80',16) <= char_line <= int('2EFF',16))  \
        or (3400 <= char_line <= int('4DB5',16)) \
        or (int('4E00',16) <= char_line <= int('9FBF',16)) :
            not_title.append(line)
            print(line)


section_index= []
for x in not_korean :
    index = df[df['시']==x].index[0]
    section_index.append(index)

for i in not_korea :
    index3 = df[df['시인']==i].index[0]
    section_index.append(index3)
    print(index3)
for y in not_title :
    index1 = df[df['제목']==y].index[0]
    section_index.append(index1)


new_list = []
for v in section_index:
    if v not in new_list:
        new_list.append(v)
list_idx = list(set(new_list))

print("뺄 인덱스")
print(new_list)
print(len(new_list))
df = df.drop(df.index[new_list])

print(df)

df.to_csv('poemss_processing_final.csv', index=False, encoding='utf-8-sig', mode = 'w')
