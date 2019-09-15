
#question 1 part 1
# Iterative version
def triangleiter(n):
    result = 0
    for x in range(n+1):
        result = result + x
    return result

print(triangleiter(3))

# Recursive version
def trianglerec(n):
    if(n==0):
        return 0
    else:
        return n + trianglerec(n - 1)
    
trianglerec(3)


#copy from internet 

def myflatten(l):
    if len(l) == 0 :
        return ()
    elif isinstance(l[0], tuple):
        return myflatten(l[0]) + myflatten(l[1:])
    else:
        return l[:1] + myflatten(l[1:])

myflatten((1, (2), 3, (4, 5, (6), 7), 8))



#question 2
#2.1
from functools import reduce

def mysum(l):
    r = reduce((lambda x, y: x + y), l)
    return r

mysum((4, 7, 1))




2.2
def mylength(l):
    return reduce(lambda count, b: count + 1, map(lambda x: x , l) , 0)
    
print(mylength((4, 2, 5, 2, 5)))
print(mylength("test"))

#2.3
def mylength2(l):
    return reduce(lambda count, r:  count + 1 ,l,0)

print(mylength2((4, 2, 5, 2, 5)))
print(mylength2("test"))




#2.4

#def mysieve(n):
#   def inner(l):
#       return tuple(filter(lambda x: x % l( != 0 , l))
#   return inner(tuple(range(2, n+1)))


#print(mysieve(100))
#def mysieve(n):
 #  def inner(l):
  #     return tuple(filter(lambda x: x == i or x % i, l))
   #return inner(tuple(range(2, n+1)))

#print(mysieve(100))


#l =tuple(range(2, 100+1))


#tuple(filter(lambda x: x == i or x % i, l))


#2.5
def mysieve2(n):
    def inner(l):
       l = ([x for x in l if all(x % y != 0 for y in range(2, x))])
       return l
    return inner(tuple(range(2, n+1)))

mysieve2(100)





#question 3
def mymap(fun, l):
    if not l:
        return None
    
    return mymap(fun, l[1:])
    

l = mymap(lambda x:x**2, tuple(range(10)))
l


#3.1


def mymap(fun, l):
    if not l:
        return []
    else:
        return [fun(l[0])] + mappp(fun, l[1:])

mymap(lambda x:x**2, tuple(range(10)))

#3.2


def myfilter(fun, l):
    if not l:
        return []
    elif fun(l[0]):
        return [ l[0] ] + myfilter(fun, l[1:])
    else:
        return  myfilter(fun, l[1:])  

myfilter(lambda x:x%2==0, tuple(range(10)))


#3.3

def myreduce(fun ,l):
    if not l:
        return []
    
    return [fun(l[0],l[0])] + myreduce(fun, l[1:])

myreduce(lambda x, y: x*y, tuple(range(1,5)))







#5.1
def make_counter(n):    
    def counter():
        nonlocal x
        x = x+ 1
        return x
    x = n
    return counter

c = make_counter(0)
print(c())




#5.2
def make_counter2(n):
    
    def counter(message="nochange"):
        nonlocal x
        if(message == "increment"):
            x += 1
        elif (message == "decrement"):
           x -= 1 
        else:
            return x   
        return x
    x= n
    return counter
    


c = make_counter2(0)
print(c())
print(c("increment"))
print(c("increment"))
print(c("increment"))
print(c("decrement"))
print(c())






#6.1
from random import sample, choice

def quicksort(a):
    if not a:
        return []
    else:
        pivot = a[0]
        low = [x for x in a     if x <  pivot]
        high = [x for x in a[1:] if x >= pivot]
        return quicksort(low) + [pivot] + quicksort(high)
    
a = tuple(sample(range(1000), 1000))
print(a)
b = quicksort(a)
print(b)





#6.2
from random import random
import math
# Write quicksort2 here:
def quicksort2(lst, fun):
   if not lst:
       return []
   else:
       piv = math.floor(len(lst)/2)
       A = [i for i in lst if fun(i) > fun(lst[piv])]
       B = [i for i in lst if fun(i) < fun(lst[piv])]
       
       return quicksort2(A, fun) + [lst[piv]] + quicksort2(B, fun) 


a = tuple(tuple(random() for i in range(3)) for j in range(10))
#print(a)
b = quicksort2(a, sum)
print(b)



#6.3

from math import exp, sqrt, pi
from random import uniform

def gausspdf(x, loc, scale):
   return (exp(-((x - loc) / scale)**2/2)/sqrt(2*pi))/scale


def quicksort3(a, fun, **kwargs):
   if not a:
       return []
   else:
       pivot = math.floor(len(a)/2)
       low = [i for i in a if fun(i, **kwargs) > fun(a[pivot], **kwargs)]
       high = [i for i in a if fun(i, **kwargs) < fun(a[pivot], **kwargs)]
       
       return quicksort3(low, fun, **kwargs) + [a[pivot]] + quicksort3(high, fun, **kwargs) 

   
a = tuple(uniform(-1,1) for i in range(10))
#print(a)
b = quicksort3(a, gausspdf, loc=0, scale=1)
print(b)



#6.4

from math import exp, sqrt, pi
from random import uniform

def gausspdf(x, loc, scale):
   return (exp(-((x - loc) / scale)**2/2)/sqrt(2*pi))/scale

# Write quicksort4 here:
def quicksort4(a, typ, key, **kwargs):
   return(typ(quicksort3(a, key, **kwargs)))

a = tuple(uniform(-1,1) for i in range(10))
#print(a)
b = quicksort4(a, tuple, key=gausspdf, loc=0, scale=1)
print(b)

a = [uniform(-1,1) for i in range(10)]
#print(a)
b = quicksort4(a, list, key=gausspdf, loc=0, scale=1)
print(b)