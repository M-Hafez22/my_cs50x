'''
def myFun(li):
    li[2] =li[2] + 20

list1 = [0,1,2]
myFun(list1)
print(list1)


for i in range(5):
  print(i)

myString= "I need a vacation"
print(myString[-18])

str = "this is string example....wow!!! this is really string"
print str
print str.replace("is", "was") #
print str.replace("is", "was", 3) #the third parameter is where to start replacement

def s(z,x):
	return z+x


z=1
x=5
print s(z,x)
print z

n = 1
for n in range(6):
  n +=1
else:
  n-=1
print(n)

str1 ="Egy" 
a, b, c = str1 
print(a)


txt= "Hello World" 
txt.split(",") 
print(txt)
list1=[]
def addCoun(par1, *par2):
  for i in par2:
    list1.append(i)
addCoun('Egypt', 'Syria', 'Lebanon', 'Iraq')
print(len(list1))

def figure_it_out(x)
    print(x)

figure_it_out("hello")

def does_it_change(x):
    x = "hello"
    return x

my_str = "koko"
does_it_change(my_str)

print(my_str)


def sum_all(x):
    if x == 0:
        return 0

    return x + sum_all(x-1)

print(sum_all(5))

x = 5
if x = 4:
    print("it is equal")
else:
    print("it is not eqaul")


def my_loop():
    counter = 0
    while counter < 20:
        print(str(counter))
        counter += 2

my_loop()


x = 5
while x < 10:
    if x > 7: break
    print(x)
    x += 1

a = [1, 2, 3]

for x in a:
    x += 1
    print(x)
    
for x in a:
    print(x)
def check_i():
  i =0
  while i < 5:
    i += 1
    return i
print(check_i())


list1 = [None,"World" ,5,0.4 ,None,{},[]]
print(len(list1))

def proc3(mylist):
    mylist += [6,7]

list4 = [1,2,3,4,5]
print (id(list4))
print (list4)
proc3(list4)
print ((list4))
print (id(list4))

   numbers = [-1 ,1,5,4.5]

mySum = sum(numbers)
print(mySum)


for i in range(1):
    print(i)

#for i in range(1,2):
    print(i)

#for i in range(2,4):
    print(i)

    
import os

os.chdir(r"C:\prank\12")
os.rename(athens.jpg , file.translate(None, "0123456789"))


def say_hello():
    return "hello"

def does_it_change(x):
    x = "hello"
    return x

my_str = "koko"
does_it_change(my_str)

print(my_str)


def sum_all(x):
    if x == 0:
        return 0

    return x + sum_all(x-1)

print(sum_all(5))

a = [1, 2, 3]
x = id(a)

a = a + [4]
y = id(a)

if x == y:
    a += [5]

print a
class B:
    def __init__(self):
        self.element_1 = 'can you print me'
        
print(B().element_1)




class A:
    element_1 = 'is it gonna print it'
    
print(A.element_1)





class A:
    element_1 = 'hola'


class B(A):
    def say_hello(self):
        self.element_1 = 'ola'
        print(super().element_1)


class B:
    def __init__(self):
        self.element_1 = 'can you print me'
        
print(B().element_1)

class A:
    element_1 = 'is it gonna print it'
    
print(A.element_1)



class A:
    element_1 = 'hola'
    
    def say_hello(self):
        return self.element_1


class B(A):
    def say_hello(self):
        super().say_hello()
        self.element_1 = 'ola'
        print(self.element_1)


te = B()

print(te.say_hello)


d =range(5)
print d[6]


def check_i():
  i =0
  while i < 5:
    i += 1
    return i
print(check_i())



def get_s(a, b):
  return a[:b]
print(get_s("mySchool",10))


class MyLang:
  def loveLanguage(self, l='Go'):
    return(l)
  
l = MyLang()
#print(l.loveLanguage("JavaScript"))
print (l)
myList = ["a","b","c","d"]
myList.reverse()
print "".join(myList)


x = 2
pr = lambda i : i * x
print pr(4)



def myFunction(): pass
print(type(myFunction()))

print type(type(int))

list1 = [None,"World" ,5,0.4 ,None,{},[]]
print(len(list1))

'''
import math

p=math.ceil(3.4)
print(p)