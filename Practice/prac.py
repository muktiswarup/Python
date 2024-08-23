""" . 
 1. Printnumbersfrom1to10usingaforloop?
 2. Printnumbersfrom1to10usingawhileloop?
 3. Programtocalculatethesumofthefirst10naturalnumbersusingforLoop-for
    loopandWhileloop?
 4. Programtoprint15to10numbersusingfor loopandwhileloop?
 5. Programtoprint15to10numbersusingawhileloop?
 6. Programtoprintthefirst10evennumbersusingawhileloop?
 7. Programtoprintthefirst5evennumbersusingafor loop?
 8. Programtoprintthefirst10oddnumbersusingawhileloop? 
 
 """

"""
#question no. 1 

for i in range(1,11):
    print( 'One to 10 number is : ' ,i)  """

#..............................................

#question number 2.

""" n= int(input("Enter A number:"))
i= 1
while(i<=n):
    print(i)
    i=i+1 """

#................................................

#Question number 3
""" sum=0
for i in range(1,11):
    sum= sum+i
print("Sum of th 10 natural number:",sum) """

#Question number 3 in while loop

""" n= int(input("Enter a number : "))
sum =0
i=1
while(i<=n):
   sum= sum+i
   print(sum)
   i=i+1 """
 

#.......................................
""" for i in range(15,9,-1):
    print(i) """

""" i=15
while(i>=10):
    print(i)
    i=i-1
 """

#..........................

""" i=2
while(i<=20):
    print(i)
    i=i+2

for i in range(2,11,2):
    print(i) """

#print good mrning 10 times 

""" name=input("Enter your name")
for i in range(1,11):
    print(f"Good Morning Mr.{name}") """


#print 10 to 1
""" for i in range(10,0,-1):
    print(i) """


""" for i in range(11,30,2):
    print(i) """


""" for i in range(4,21,4):
    print(i) """


""" i=5
while(i<=25):
    print(i)
    i=i+5 """

""" num=6
for i in range(1,11):
    print(num,"*",i,"=",num*i)

num=6
i=1
while(i<=10):
    print(num,'*',i,'=',num*i)
    i=i+1 """


""" n=int(input("Enter a number: "))
i=1
while(i<=n):
    if(n%i==0):
        print(f'The divisor of {n} is ',i)
    i=i+1 """

""" n=int(input('Enter your number: '))
factor=[]
i=1
while(i<=n):
    if(n%i==0):
        factor.append(i)
    i=i+1
print(f"Factor of {n} is : ", factor) """


