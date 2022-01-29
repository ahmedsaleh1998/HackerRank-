#////////////////task2//////////
# import sys   
# N = int(input())
# if N%2!=0 and N>=1 and N<=100:
#         print('Weird')
# elif N%2==0 and N>=1 and N<=100:
         
#         if N>=2 and N <=5:
#             print('Not Weird') 
#         elif  N>=6 and N <=20 :
#             print('Weird')
#         else :
#              print('Not Weird')    
 
 #////////////////task3//////////
# a = int(input())
# b = int(input())
# if a>=1 and a<=10**10 and b>=1 and b<=10**10:
#     print(a+b)
#     print(a-b)
#     print(a*b)
 #////////////////task4//////////
# a = int(input())
# b = int(input())
# print(a//b)
# print(float(a)/float(b))
 #////////////////task5//////////
# number = int(input())
# if number>=1 and number<=20:
#     for i in range(number):
#         print (i**2)
# else:
#     print('wrong! range fron 1 to 20 ')

#////////////////task6//////////
# def is_leap (year):
#     if year>=1900 and year<=10**5:
#         if year%4==0 and year%100!=0 or year%400==0:
#             return True
#         else :
#             return False    
#////////////////task7//////////
# def concatNumbers (number):
#     myStr=''
#     if number>=1 and number<=150:
#         for i in range(1,number+1):
#             myStr+=str(i)
#     print(myStr)        
# concatNumbers (5)
#////////////////task8//////////
# import calendar
# from posixpath import split
# def viewday():
#          myDate=input()
#          MyNewDate=myDate.split(' ')
#          if int(MyNewDate[2]) >2000 and int(MyNewDate[2])<3000 :
#              dayNumber=calendar.weekday(int(MyNewDate[2]),int(MyNewDate[0]),int(MyNewDate[1]))
#              print(calendar.day_name[dayNumber].upper())
#          else :
#              print('enter year in range from 2000 ton 3000')  
 #/////another sol
 
# import calendar
# m, d, y = map(int, input().strip().split())
# print(calendar.day_name[calendar.weekday(y, m, d)].upper())

#////////////////task9//////////
# import math
# import os
# import random
# import re
# import sys
# from datetime import datetime
# def time_delta(t1, t2):
#     t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
#     t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
#     return str(int(abs((t1-t2).total_seconds())))
# # Time Delta in Python - Hacker Rank Solution END

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         delta = time_delta(t1, t2)

#         fptr.write(delta + '\n')

#     fptr.close()

#//////////////////////task10/////////////