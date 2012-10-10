#!/usr/bin/python

#first comment: This program prints the ten first numbers

def printNumbers(n):
   i = 0
   while i < n:
      if i%2==0:
         print i
      i+=1   

printNumbers(1000)   
