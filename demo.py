
#1 Problem

class Rectangle:
    def __init__(self,length,width) -> None:
        self.length = length
        self.width = width
        
    def Perimeter(self):
        return 2*(self.length+self.width)
    def Area(self):
        return self.length*self.width
    def display(self):
        print("Length is", self.length)
        print("Width is", self.width)
        print("Perimeter is", self.Perimeter())
        print("Area is", self.Area())
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height) -> None:
        Rectangle.__init__(self,length, width)
        self.heigth = height
    def volume(self):
        return self.length*self.width*self.heigth
MyRect = Rectangle(2,3)
MyRect.display()
MyPara = Parallelepipede(2,3,4)
print("Volume is",MyPara.volume())


#2 Problem
class person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def display(self):
        print("Name is",self.name)
        print("Age is", self.age)

class student(person):
    def __init__(self, name, age,section):
        person.__init__(self,name, age,)
        self.section= section
    def displayStudent(self):
        print("Name is ", self.name)
        print("Age is ", self.age)
        print("Section is ", self.section)
Student1=person("Reva",27)
Student1.display()
Student2= student("Kartik",22,"A")
Student2.displayStudent()


#3 Problem
class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def deposit(self,d):
        self.balance = self.balance + d 
    def withdrawal(self,w):
        if(self.balance<w):
            print("Insufficient balance")
        else:   
            self.balance = self.balance - w
    def display(self):
        print("Acc. No. = ", self.accountNumber)
        print("Acc. Name = ", self.name)
        print("Acc. Balance = ", self.balance) 
Account1 = BankAccount(201938408,"Reva",3000)
Account1.withdrawal(100)
Account1.deposit(200)
Account1.display()
        
#4 Problem
class Circle:
    def __init__(self,a,b,r):
        self.a = a         
        self.b = b         
        self.r = r
    def Perimeter(self):
        return 2 * 3.14 * self.r
    def Area(self):
        return 3.14 * self.r * self.r
    def formEquation (self, x, y):
        return (x-self.a)**2 + (y-self.b)**2 - self.r**2
    def test_belong (self, x, y):
        if self.formEquation (x, y) == 0:
            print ("the point: (", x, y, ") belongs to the circle C")
        else:
            print ("the point: (", x, y, ") does not belong to the circle C")
Circle1= Circle(1,2,1)
print("Perimeter = ", Circle1.Perimeter())
print("Area = ", Circle1.Area())
Circle1.test_belong(1,1)


#5 Problem
class Computation:
    def __init__(self):
        pass
    def Factorial(self,n):
        i = 1
        for j in range(1,n+1):
            i *= j
        return i
        
    def sum(self,n):
        i = 1
        for j in range(1,n+1):
            i+=j
        return i
    
    def Prime(self, n):
        j = 0
        for i in range (1, n + 1):
            if (n% i == 0):
                j = j + 1
        if (j == 2):
            return True
        else:
            return False
    
    def table(self, m):
        for i in range (1,10):
            print (i, "x", m, "=", i * m)
    def allTable(self):
        for k in range (1,10):
            print ("Multiplication table of", k, "is:")
            for i in range (1,10):
                print (i, "x", k, "=", i * k)
    def Div(self,n):
        Dlist=[]
        for i in range(1,n+1):
            if(n%i==0):
             Dlist.append(i)
        return Dlist
Comp = Computation()
n = 3
print(Comp.sum(n))

# 6 Problem

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def displey(self):
        print("Title = ", self.title)
        print("Author =", self.author)
        print("Price =", self.price)

Book1 = Book("Two Ststes","Chetan Bhagat", "$ 400")
print(Book1.displey())

#7 Problem
class Geometry:
    def __init__(self) :
        pass
    def distance(self,A,B):
        a1,a2 = A
        b1,b2 = B
        return ((b1-a1)**2 + (b2-a2)**2)**0.5
    def middle(self, A, B):
        a1, a2 = A
        b1, b2 = B
        return ((a1+b1)/2, (a2+b2)/2)
    def trianglePerimeter(self, A, B, C):
        return self.distance(A,B) + self.distance(B,C) + self.distance(C,A)
    def triangleIsoscel(self, A, B, C):
        AB = self.distance(A,B)
        AC = self.distance(A,C)
        BC = self.distance(B,C)
        return AB == AC or AB == BC or AC == BC
geometry = Geometry()
A = (0, 0)
B = (3, 4)
C = (6, 0)

print(geometry.triangleIsoscel(A, B, C))

#8 Problem

class MyString(str):
    def __init__(self,string):
        
        self.String = string
    def append(self,char):
        self.String += char
    def pop(self):
        self.String = self.String[:-1]
    def __str__(self):
        return self.String
Word = MyString("Reva")
Word.append(" K")
print(Word)
Word.pop()
print(Word)


