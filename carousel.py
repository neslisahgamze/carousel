# -*- coding: utf-8 -*-
import random
import sys
'''
R : of times that machine works at a day
N : of groups that are willing to use machine 
k : max of person who can use the machine for at one time
'''
while True:
    try:
        a,b,c = map(int,input().strip().split(" "))
        break
    except ValueError:
       print("Oops! Please enter 3 values...")

def carousel(R,N,k):
	total, ticket = 0, 0
	a=[]	
	list1 = input()
	for x in list1.split():
		a.append(x)
		
	for i in range(0, int(R)):
		while(total <= int(k)):
			if((total+ int(a[0]))>int(k)):
				break
			else:
				total = total + int(a[0])
				a.append(a[0])
				a.pop(0)
		ticket = ticket +total
		total = 0
	print(ticket)
carousel(a,b,c)