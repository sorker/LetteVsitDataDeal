# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/23 19:53
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""

file1 = open('../data/中文停用词表.txt', 'r', encoding='utf-8')
file2 = open('../data/哈工大停用词表.txt', 'r', encoding='utf-8')
file3 = open('../data/四川大学机器智能实验室停用词库.txt', 'r', encoding='utf-8')
file5 = open('../data/2.txt', 'r', encoding='utf-8')
file4 = open('../data/停用词表.txt', 'w+', encoding='utf-8')
words1 = file1.readlines()
words2 = file2.readlines()
words3 = file3.readlines()
words5 = file5.readlines()
words4 = []
for word in words1:
    if word not in words2 and word not in words3:
        words4.append(word)
for word in words2:
    if word not in words4:
        words4.append(word)
for word in words3:
    if word not in words4:
        words4.append(word)
for word in words5:
    if word not in words4:
        words4.append(word)
for word in words4:
    file4.writelines(word)
# for word in words:
#     print(word)
