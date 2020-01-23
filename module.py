# # # # # # # # # # # # # # # # # # # # # # # # # # # # import gb
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(__name__)
# # # # # # # # # # # # # # # # # # # # # # # # # # # import sys as s
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(s.getrecursionlimit())
# # # # # # # # # # # # # # # # # # # # # # # # # # def gb(n):
# # # # # # # # # # # # # # # # # # # # # # # # # #     if n==1:
# # # # # # # # # # # # # # # # # # # # # # # # # #         return 1
# # # # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # # # #         return n*(gb(n-1))
# # # # # # # # # # # # # # # # # # # # # # # # # # a=int(input('Any number:'))
# # # # # # # # # # # # # # # # # # # # # # # # # # b=gb(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # # # # # # # # # # a=12
# # # # # # # # # # # # # # # # # # # # # # # # # b=8
# # # # # # # # # # # # # # # # # # # # # # # # # while True:
# # # # # # # # # # # # # # # # # # # # # # # # #     rem=a%b
# # # # # # # # # # # # # # # # # # # # # # # # #     b=rem
# # # # # # # # # # # # # # # # # # # # # # # # #     a=b
# # # # # # # # # # # # # # # # # # # # # # # # #     if a%b == 0:
# # # # # # # # # # # # # # # # # # # # # # # # #         print(b)
# # # # # # # # # # # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #     # else:
# # # # # # # # # # # # # # # # # # # # # # # # #     #     rem=b
# # # # # # # # # # # # # # # # # # # # # # # # #     #     b=a
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # #print(gb(12,8))
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # def gb(a,b):
# # # # # # # # # # # # # # # # # # # # # # # #     rem=a/b
# # # # # # # # # # # # # # # # # # # # # # # #     if a%b==0:
# # # # # # # # # # # # # # # # # # # # # # # #         return b
# # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # #         a=b
# # # # # # # # # # # # # # # # # # # # # # # #         b=rem
# # # # # # # # # # # # # # # # # # # # # # # #         return gb(a,b)
# # # # # # # # # # # # # # # # # # # # # # # # print(gb(15,5))
# # # # # # # # # # # # # # # # # # # # # # # def gb(n):
# # # # # # # # # # # # # # # # # # # # # # #     if n==1:
# # # # # # # # # # # # # # # # # # # # # # #         return n**2
# # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # #         return n**2+gb(n-1)
# # # # # # # # # # # # # # # # # # # # # # # b=int(input('Enter any number:'))
# # # # # # # # # # # # # # # # # # # # # # # print(gb(b))
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # def gb(l):
# # # # # # # # # # # # # # # # # # # # # # #     for i in l:
# # # # # # # # # # # # # # # # # # # # # # #         if i/2==0.0:
# # # # # # # # # # # # # # # # # # # # # # #             print(i,end='')
# # # # # # # # # # # # # # # # # # # # # # # gb([1,2,3,4,5,6])
# # # # # # # # # # # # # # # # # # # # # # s={1,2,3,1,2,7,1,6}
# # # # # # # # # # # # # # # # # # # # # # s1={2,6,3,9}
# # # # # # # # # # # # # # # # # # # # # # print(s.intersection(s1))
# # # # # # # # # # # # # # # # # # # # # # print(s.union(s1))
# # # # # # # # # # # # # # # # # # # # # from array import *
# # # # # # # # # # # # # # # # # # # # # gb=array('i',[1,2,3,4,5,6])
# # # # # # # # # # # # # # # # # # # # # for h in gb:
# # # # # # # # # # # # # # # # # # # # #     print(h)
# # # # # # # # # # # # # # # # # # # def gb(n1):
# # # # # # # # # # # # # # # # # # #     a=0
# # # # # # # # # # # # # # # # # # #     b=1
# # # # # # # # # # # # # # # # # # #     if n==1:
# # # # # # # # # # # # # # # # # # #         print(a)
# # # # # # # # # # # # # # # # # # #     elif n==2:
# # # # # # # # # # # # # # # # # # #         print(b)
# # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # #         print(a,b,end=' ')
# # # # # # # # # # # # # # # # # # #         for i in range(n-2):
# # # # # # # # # # # # # # # # # # #             c=a+b
# # # # # # # # # # # # # # # # # # #             a=b
# # # # # # # # # # # # # # # # # # #             b=c
# # # # # # # # # # # # # # # # # # #             print(c,end=' ')
# # # # # # # # # # # # # # # # # # # n=int(input('How many numbers do you want to print of FEbonacci:'))
# # # # # # # # # # # # # # # # # # # gb(n)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # n=int(input('first'))
# # # # # # # # # # # # # # # # # # print(n,end=' ')
# # # # # # # # # # # # # # # # # # # # p=int(input('second'))
# # # # # # # # # # # # # # # # # # print(21)
# # # # # # # # # # # # # # # # # for i in range(6):
# # # # # # # # # # # # # # # # #     print(i*'*')
# # # # # # # # # # # # # # # # s='I love my jaan'
# # # # # # # # # # # # # # # # s=s.split()
# # # # # # # # # # # # # # # # l=[]
# # # # # # # # # # # # # # # # # print(s[0])
# # # # # # # # # # # # # # # # for i in s:
# # # # # # # # # # # # # # # #     l.append(i[::-1])
# # # # # # # # # # # # # # # # print(l)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # s='i love my jaan'
# # # # # # # # # # # # # # # s=s.split()
# # # # # # # # # # # # # # # l=[]
# # # # # # # # # # # # # # # # print(s[::-1])
# # # # # # # # # # # # # # # for i in s:
# # # # # # # # # # # # # # #     i=i[::-1]
# # # # # # # # # # # # # # #     l.append(i)
# # # # # # # # # # # # # # # print(l)
# # # # # # # # # # # # # # s='GAURAV'
# # # # # # # # # # # # # # print(s[::-1])
# # # # # # # # # # # # # # t=12,11,21
# # # # # # # # # # # # # # a,b,c=t
# # # # # # # # # # # # # # print(a,b,c)
# # # # # # # # # # # # # a,b,c=21,50,43
# # # # # # # # # # # # # t=a,b,c
# # # # # # # # # # # # # print(t)
# # # # # # # # # # # # # zip
# # # # # # # # # # # # a=5
# # # # # # # # # # # # b=a
# # # # # # # # # # # # print(id(a),id(b))
# # # # # # # # # # # # l=[1,2,3]
# # # # # # # # # # # # l1=l
# # # # # # # # # # # # l1.append(21)
# # # # # # # # # # # # print(l,id(l))
# # # # # # # # # # # # print(l1,id(l1))
# # # # # # # # # # # # import copy
# # # # # # # # # # # a=[1,2,3,4]
# # # # # # # # # # # # a2=copy.copy(a)
# # # # # # # # # # # # print(a,id(a),a2,id(a2))
# # # # # # # # # # # a[1][1]='aa'
# # # # # # # # # # # print(a)
# # # # # # # # # # l=[1,2,3]
# # # # # # # # # # l2=l.copy()
# # # # # # # # # # print(id(l),id(l2))
# # # # # # # # # # l2.append(21)
# # # # # # # # # # print(l,l2)
# # # # # # # # # class Game:
# # # # # # # # #     def __init__(self,name):
# # # # # # # # #         self.a=name
# # # # # # # # # g=Game('Cricket')
# # # # # # # # # class Bike:
# # # # # # # # #     def __init__(self,name):
# # # # # # # # #         self.a=name
# # # # # # # # # b=Bike('APACHE')
# # # # # # # # # print(b.a)
# # # # # # # # l=[1,2,3,4]
# # # # # # # # l2=list(l)
# # # # # # # # print(id(l),id(l2))
# # # # # # # # l2.append('PUSHPA')
# # # # # # # # print(l2,l)
# # # # # # # # a=[1,2,3]
# # # # # # # # a2=a
# # # # # # # # a2.append('GAURAV')
# # # # # # # # print(a,a2)
# # # # # # # import copy
# # # # # # # l=[1,2,3]
# # # # # # # l2=copy.copy(l)
# # # # # # # print(id(l),id(l2))
# # # # # # # l2[2]=21
# # # # # # # print(l2,l)
# # # # # # l=[1,2,3,4,[5,6,7]]     #Deep copy#
# # # # # # import copy
# # # # # # l2=copy.deepcopy(l)
# # # # # # l2[4][0]='jaan'
# # # # # # print(l2,l)
# # # # # name,address,city,pin=input('Enter your name,address,city,pin code:').split()
# # # # # l=name,address,city,pin
# # # # # print(l)
# # # # # # print(f'My name is {name},i live in {address} in {city} and pin code is {pin}')
# # # # total_sales=eval(input('Enter your amount:'))
# # # # profit=(total_sales-(total_sales*23)/100)
# # # # print(profit)
# # # sugar=1.5
# # # flour=2.75
# # # butter=1
# # # cookies=48
# # # a=int(input('How many cookies you want to made:'))
# # # sugar=(sugar/cookies)*a
# # # flour=(flour/cookies)*a
# # # butter=(butter/cookies)*a
# # # print(f'you need {sugar} cups of sugar,{flour} cups of flour and {butter} cups of butter')
# # students=int(input('Enter total numbers of students in class:'))
# # males=int(input('Enter total numbers of males in class:'))
# # females=int(input('Enter total numbers of females in class:'))
# # males=(males/students)*100
# # females=(females/students)*100
# # print(f'Percentage of males in a class is {males}% and percentage of females is {females}%')
#
# # for i in range(1,8):
# # b=1
# # while b<=7:
# a = int(input('Enter a number from 1 to 7:'))
# if a==1:
#     print('Monday')
# elif a==2:
#     print('Tuesday')
# elif a==3:
#     print('Wednesday')
# elif a==4:
#     print('Thursday')
# elif a==5:
#     print('Friday')
# elif a==6:
#     print('Saturday')
# elif a==7:
#     print('Sunday')
# else:
#     print('You have entered wrong digit!!')
# while True:
#     b=0
#     a=input('Enter rupees denomination to be 100 rupees:').split()
#     for i in a:
#         i=int(i)
#         b=b+i
#     print(b)
#     if b==100:
#         print('You have won!!')
#         break
# w=float(input('Enter your weight:'))
# h=float(input('Enter your hight'))
# BMI=w/h**2
# if BMI>=18.5 and BMI<=25:
#     print('Your weight is ok and you r fit!!')
# elif BMI<18.5:
#     print('You are underweight!!')
# else:
#     print('You are overweight!!')
# cal=4.2
# for i in range(4):
#     a=int(input('Enter time you spend on treadmil to count burnt calories:'))
#     total=a*cal
#     print(f'Total number of callories burnt after {a} time is {total}')
# budget=int(input('Enter the amount of whole month budget:'))
# total=0
# for i in range(4):
#     exp=int(input('Enter the materials cost for one month:'))
#     total+=exp
print(total)
# if total<=budget:
#     print('You have made your monthly expenditure very well!!')
# elif total>budget:
#     print('You have crossed your budget limit,please cut some cost!!')
# speed=int(input('Enter the speed of your vehicle in km/h:'))
# hours=int(input('How many hours it has traveled so far:'))
# for i in range(1,hours+1):
#     distance=speed*i
#     print(f'Distance traveled in {i} hour is {distance}')
# no=input('Enter a positive no or a negatvive to quit:').split()
# total=0
# for i in no:
#     i=int(i)
#     if i<=-1:
#         break
#     else:
#         total+=i
# print(total)
# total=0
# tuition_fee_per_sem=8000
# course_duration=5
# per_year_fee=2*tuition_fee_per_sem
# print(per_year_fee)
# per_year_hike=per_year_fee*3/100
# print(per_year_hike)
# for i in range (1,course_duration+1):
#     print(f'per year hike in fee is {per_year_hike}')
#     total+=per_year_hike
# print(f'You have to pay Rs. {total} in 5 years')
# a=int(input('Enter a number to calculate factorial:'))
# b=1
# for i in range(1,a+1):
#     b=b*a
#     a-=1
# print(f'Factorial is {b}')
# a=int(input('Enter a number:'))
# total=0
# for i in range(1,a+1):
#     total+=i
# average=total/a
# print('Average is',average)
# def gb(a,b):
#     return a+b
# a=int(input(':'))
# b=int(input(':'))
# c=gb(a,b)
# print(c)
# def string(s):
#     count=0
#     for i in s:
#         count+=1
#     print(f'String length is {count}')
# st=input('Enter any string:')
# string(st)
# def gb(s):
#     return s[-1]
# print(gb('GAURAV'))
# def ab(x,y):
#     return x if x>y else y
# def gb(x,y,z):
#     return ab(ab(x,y),z)
# print(gb(25,50,17))
# def sleep_in(weekday, vacation):
#   if not weekday or vacation:
#     return True
#   else:
#     return False
# print(sleep_in('sunday','sunday'))
def parrot_trouble(talking, hour):
    return talking and hour<7 or hour>20
print(parrot_trouble(True,21))














