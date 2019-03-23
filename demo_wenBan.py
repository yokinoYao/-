#!/usr/bin/ruby

import CRFPP
import sys
import nltk
import re

tagger = CRFPP.Tagger("-m model5 -v 3 -n2")
sen_file = open('/Users/yao/Desktop/Test/project/test.txt','r')
rule_file = open('/Users/yao/Desktop/Test/project/rule.txt','r')

tagger.clear()
sentence = sen_file.readline()
sentence_list = sentence.split(' ')

#tag
tokens = nltk.word_tokenize(sentence)
#ci ji ci xing biao
tag_sent = nltk.pos_tag(tokens)
#ci xing ju
tag_sentence = ''
for x in tag_sent:
    tag_sentence += x[1] + ' '
#print(tag_sentence)


for rule in rule_file.readlines():
    tag_sen_list = re.findall(rule,tag_sentence)
    #print(tag_sen_list)
    #zheng li you yong de jie guo
    select_sen_list = []
    for i in tag_sen_list:
        exist = re.search('VB[ZP]', i)
        if exist == None:
            continue
        i_list = i.strip().split(' ')
        if len(i_list[0]) < 2:
            del i_list[0]
        if len(i_list[len(i_list) - 1]) < 2:
            i_list.pop()
        if len(i_list) < 3:
            continue
        s = ''
        for x in i_list:
            s += x +' '
        select_sen_list.append(s)
    #print(select_sen_list)

    position_list = []
    for s in select_sen_list:
        s_list = s.strip().split(' ')
        t_list = tag_sentence.split(' ')
        t_len = len(t_list)
        s_len = len(s_list)
        for i in range(t_len):
            for j in range(s_len):
                temp = s_len - 1
                if s_list[j] != t_list[i+j]:
                    break
                if j == s_len-1:
                    position_list.append(str(i)+' '+str(i+j+1))
    #print(position_list)



    #model test
    for i in tag_sent:
        #print(i[0] + ' '+ i[1])
        tagger.add(i[0] + ' '+ i[1])
    ysize = tagger.ysize()
    tagger.parse()
    #ce shi jie guo biao
    tagger_sent = []
    size = tagger.size()
    xsize = tagger.xsize()
    for i in range(0, (size - 1)):
        l = ''
        for j in range(0, (xsize-1)):
            #print tagger.x(i, j) , "\t",
            l += tagger.x(i, j)+ ' '
        #print tagger.y2(i) , "\n",
        l += tagger.y2(i)
        tagger_sent.append(l)
    #print(tagger_sent)


    #shi ti
    word_list = []
    #shi ti de biao ji
    pos_list = []
    #shi ti de wei zhi
    wrod_vec = []
    words_line = ''
    for t in range(len(tagger_sent)):
        tlist = tagger_sent[t].split(' ')
        if tlist[1].startswith('B-'):
            words_line += str(t) + ' '
            continue
        if tlist[1].startswith('E-'):
            words_line += str(t) + ' '
            wrod_vec.append(words_line)
            words_line = ''
            continue
        if tlist[1].startswith('S-'):
            words_line += str(t) + ' '
            wrod_vec.append(words_line)
            words_line = ''
            continue
    #print(wrod_vec)


    #shi jian shu chu
    #shi jian bu cun zai shu chu shi ti
    if len(position_list) == 0:
        print('Even is not existence.')
        if len(wrod_vec) != 0:
            print('entity:')
            for x in wrod_vec:
                w_of_words_vec = x.strip().split(' ')
                line = ''
                left_pos = int(w_of_words_vec[0])
                if len(w_of_words_vec) == 1:
                    right_pos = int(w_of_words_vec[0]) + 1
                else:
                    right_pos = int(w_of_words_vec[1]) + 1
                for l in range(left_pos,right_pos):
                    line += sentence_list[l] + ' '
                print(line)
    #shi jian cun zai shu chu shi jian
    else:
        print('Event is existence:')
        for x in position_list:
            p_position_list = x.strip().split(' ')
            left_pos = int(p_position_list[0])
            right_pos = int(p_position_list[1])

            #bao zheng shi ti zai shi jian zhong
            count = 0
            for y in wrod_vec:
                w_of_words_vec = y.strip().split(' ')
                w_left_pos = int(w_of_words_vec[0])
                if len(w_of_words_vec) == 1:
                    w_right_pos = int(w_of_words_vec[0])
                else:
                    w_right_pos = int(w_of_words_vec[1])
                if w_left_pos >= left_pos and w_right_pos<= right_pos:
                    count  = count + 1
            #gen ju shi ti cun zai jie guo shu chu
            if count >= 1:
                event_line = ''
                for l in range(left_pos,right_pos):
                    event_line += sentence_list[l] + ' '
                print(event_line)













