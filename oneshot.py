"""print("hello world")

#variable 
name="kashish"
age=22
is_adult=False
print(name)                  #if we write in "" then it will print name so we don't give double inverted comma
print(age)

#exercise-1
name="tony stark"
age=51
print(name)
print(age)



#concatenation
#take no from user 
names=input("what is your name?")
print(names)
print("hello"+names)         

#exercise-2
b=input("what is your superhero name")
print("tony is a superhero and his super hero name is:"+b)

#type conversion
number=18
print(float(18))
old_age=input("enter your old age:")
new_age=int(old_age)+2
print(new_age)

#print sum of 2 no
first=input("enter first no")
second=input("enter second no")
sum=int(first)+int(second)
print("the sum is:"+str(sum))

#strings
name="tony stark"
     #0,1,2,3,4,5-position (start from index 0)
print(name.upper())
print(name.lower())

print(name.find('s'))
print(name.find('e'))
print(name.find('stark'))
print(name.replace("stark","Ironman"))
print(name)
print(name.replace("t","m"))

#keywords
name="tony stark"
print('t' in name)
print('m' in name)

#arithematic operation (ans in no & decimal)
print(5-2)
print(9+8)
print(9*2)
print(5/3)  
print(5//3)                         #if we dont want in float
print(70%4)                         #remainder or modulus opr
print(5**2)                         #for power 


#shortcuts
i=5
i=i+2                               #this and
print(i)
i+=2                                #this have same meaning
i-=2
i*=2

#operator precedence(more pred to * /)
result=2+3*5
print(result)
results=(2+3)*5
print(results)

#comparison operator   (give boolean value)
print(3>2)
print(3<2)
print(3==2)
print(3==3)
print(3!=3)
print(2!=5)

#logical operator
print(2>3 or 2>1)               #1 bhi true toh true
print(5<2 or 5<3)
print(3>2 and 2>1)              # 1 bhi false toh false
print(not 3>2)                  # not--true ko false and f ko t banata hai

#if-else statement
age=2
if age>=18:
    print("u are an adult")
    print("you can vote")
elif age<18 and age>3:
    print("u are in school")
else:
    print("u are a child")

print("thank u")

#MINIPROJECT---3   (calculator)
first=input("enter first no")
operator=input("enter operator(+,-,%,*,/):")
second=input("enter second no")
first=int(first)
second=int(second)
if operator == "+":
            print(first + second)
elif operator == "-":
            print(first - second)
elif operator == "*":
            print(first * second)
elif operator == "%":
            print(first % second)
elif operator == "/":
            print(first / second)
else:
            print("invalid operation")

#range
#range(5) #0,1,2,3,4
num=range(5)
print(num)"""

#loops (while loop)
"""i=1
while i<=100:
    print(i)
    i=i+1"""
"""i=1
while i<=10:
    print(i *'*')
    i=i+1"""
"""i=5
while i>=0:
    print(i *'*')
    i=i-1"""
"""# loop (for loop)
item=1
for item in range(5):
print(item+1)

#list (collection of item)
marks=[23,67,89]
print(marks)
marks=[23,67,89]
print(marks[1])
marks=[23,67,89]
print(marks[-1])
marks=[23,67,89]
print(marks[-2])

marks=[23,67,89]
print(marks[0:2])
marks=[23,67,89]
print(marks[1:3])

marks.append(99)
print(marks)
marks.insert(0,99)
print(marks)

print(99 in marks)
print(93 in marks)
print(len(marks))

# for loop in list
marks=[95,98,97]
i=0
while i < len(marks):
    print(marks[i])
i=i+1"""

"""marks=[95,98,97]
i=0
while i < len(marks):
    print(marks[i])
i=i+1
marks.clear()
print(marks)

#continue and break

students=["kashish","priya","riya","jay","tuna"]                    #to break the statement at riya
for student in students:
    if student == "riya":
        continue;
print(student)

students=["kashish","priya","riya","jay","tuna"]                     #except jay all name will print
for student in students:
    if student == "jay":
        break;
print(student)

#tuple
marks=(95,96,97,97,97,98)
print(marks.count(97))
print(marks.index(97))

#set                   (not compulsory to give parenthesis)(only unquie value will store)
person="ram","abhi","kashish"
print(person)
marks={95,96,97,97,97,98}
print(marks)
for score in marks:
    print(score)

#dictionary       (store key & value)
marks={"english":95,"chemistry":98}
print(marks["chemistry"])

marks["physics"]=97;
print(marks)

marks["physics"]=99;
print(marks)

#functions
#1 in-built function
int()
str()
bool()

#2module function
import math 
print(dir(math))

from math import sqrt
print(sqrt(4))

from math import *
print(sqrt(16))

#3user-defined function
#def function_(parameter):
def print_sum(first,second):
    print(first+second)
print_sum(1,8)
def print_sum(first,second=4):
    print(first+second)
print_sum(1)"""

