#imp
#finding the index for diplicate eliments
l  = [1,2,3,3,1,0,1]
count = 0
s = set()
v = []
for indx,value in enumerate(l):
    if value not in s:
        s.add(value)
    else:
        v.append([value,indx])        
print(v)

#lambda exampple
a = lambda x,y : x+y
print(a(5, 6))
Output: 11
#reverse
for i in range(5,-1,-2):
    print(i)

#bubble sort algoritham
l =  [3,5,3,42,32,7932,1241,13,1,0]
for i in range(len(l)-1):
    for v in range(0,len(l)-1):
        if l[v] > l[v+1]:
            l[v],l[v+1] = l[v+1],l[v]
print(l)


#  Bubble Sort 
def bubbleSort(arr): 
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
#sorting of list using min()
l = [56,0,2,2,6,0]

for i in range(len(l)-1):
    min_v  =  min(l[i:])
    min_ind = l.index(min_v,i)
    l[i],l[min_ind] = l[min_ind],l[i]
print(l)
    
#Palendrome number
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

#Palendrome string
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")


# factorial
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


#prime number 
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")



#*args
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  

#**kwargs
def myFun(arg1, arg2, arg3): 
	print("arg1:", arg1) 
	print("arg2:", arg2) 
	print("arg3:", arg3) 
	
# Now we can use *args or **kwargs to 
# pass arguments to this function : 
args = ("Geeks", "for", "Geeks") 
myFun(*args) 

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun(**kwargs) 

#class
class Employee:
    def __init__(self, name):
    self.name = name
    E1=Employee("abc")
    print(E1.name)


#to create empty class
class a:
    pass
    obj=a()
    obj.name="xyz"
    print("Name = ",obj.name)

def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

# decorator function to split words
def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    return wrapper

@splitter_decorator	# this is executed next
@lowercase_decorator	# this is executed first
def hello():
    return 'Hello World'

hello() 	

#array creation
import array

a = array.array('i', [1, 2, 3])

for i in a:
     print(i, end=' ')


#decorators
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result


#shallow copy
#one way 
import copy
l = [1,2,3,4]
l2 = copy.copy(l)
l2[0] = 7
print(l)
print(l2)
#second way
l = [1,2,3,4]
l2 = list(l)
l2[0] = 7
print(l)
#deep copy
import copy
l = [1,2,3,4]
l2 = copy.deepcopy(l)

#amstrong number
n = input()
if int(n) < 10 & int(n) > 0:
    print('it is amstromg number')
def ams(n):
    u = 0
    l = list(n)

    v = [int(i) for i in l ]

    for i in v:
        u = u + i**len(v)
    return u
f = ams(n)
if f == int(n):
    print('it is amstrong nummber')
else:
    print('it is not amstrong')

# fibonacci series
n = int(input())
first = 0 
second = 1
for i in range (n):
    print(first)
    temp = first 
    first = second
    second = temp +second
#closure
def outer():
    f = 'message'
    def inner():
        print(f)
    return inner

e = outer()
e()
#decorator
v = [1,2,4,'eswar',23,5]
def outer(f):
    def inner(l):
        for i in l:
            if str(i).isalpha(): #altering the funtionality by checking weather the list has aplha 
                l.remove(i)
        return f(l)
    return inner
@outer #decorator call
def fun(list):
    list.sort()
    return list
print(fun(v))
#program to find missing number in series
l = [1,2,3,4,100]
def v(l):
    return [i for i in range(l[0],l[-1]+1) if i not in l]
print(v(l))

#counting ovels in string

a = ['a','e','i','o','u']
l = []
count = 0
c = input()
for i in c:
    if i in a:
        l.append((i,c.index(i)))
print(l)
 

	
###############################

#print 5 decimal points

 print("%.5f" % (equalCount(arr)/l))  # use this formatting for Zero divdable 

print(float("{0:.5f}".format(lessCount(arr)/l)))
print(float("{0:.5f}".format(greaterCount(arr)/l))) 
