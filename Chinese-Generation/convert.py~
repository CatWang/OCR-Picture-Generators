#coding:utf-8

#This file is used to convert string of characters into character array version
#For example:
#Input: '一二三四‘
#Output: '一','二','三','四'

import codecs
with codecs.open("characters",encoding='utf-8') as fp:
    data = fp.read()
    len = len(data)
    print(len)
    i=0
    print(data[0])
    with codecs.open('characters-covert', 'w', encoding='utf-8') as of:
        while(i < len):
            print(data[i])
            print(i)
            if(i < len - 1):
                of.write('\'' + data[i] + '\'' + ',')
            else:
                of.write('\'' + data[i] + '\'')
            i = i + 1
