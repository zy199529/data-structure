#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-28 08:52:20
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-28 09:03:36


def InsertSort(k, n):
    for i in range(1, n):
        if k[i-1] > k[i]:
            temp = k[i]
            index = i
            for j in range(i-1, -1, -1):
                if k[j] > temp:
                	k[j+1]=k[j]
                	index = j
                else:
                	break
            k[index]=temp
    return k
if __name__=='__main__':
	k=[1,3,2,5,7,9,0,6,4,8]
	print(InsertSort(k,len(k)))
