# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:01:56 2021
@author: ELTARON
elsgha_lamba
"""
a = input("Enter your value: ")
k = a.split()
m= len(k)-1
for b , n in enumerate(k):
    if n[0] == 'ا' and n[1] == 'ل':
        l=k[b+1][0]
        a = n[0:2] + k[b+1][0] + n[3:] + " "
    else:
        a = k[b+1][0] + n[1:] + " "
    k.pop(b)
    for i in a:
      print(i, end='')

