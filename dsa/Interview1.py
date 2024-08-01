a = 4.001
print("{:.6f}".format(a)) #float, double
# t1 = ((5,6), (7,8))
# print(type(t1))
# print(t1[0][0])   #it's one dimensional because outer tuple is still one-dimensional and each element of outer tuple is a tuple itself
# l1 = [5,6,7,8]
# t2 = (5,6,7,8,l1)  #search
# print(type(l1))
# print(type(t2))
# d1 = {None:'Rashika'}
# d2 = {t2:'Kh'}
# print(d1)
# print(type(t2))
# print(d2) #coz the list in inside the tuple t2 is unhashable and key in dict is expected to be hashable

# a=[4,5,6]
# b=[4,5,6]
# c= a
# print(id(a))  #memory ref
# print(id(b))


# class Calculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self):
#        return self.x + self.y
#
#     def subtract(self):
#         return self.x-self.y
#
# ob1 = Calculator(5,2)
# print(ob1.add())
# print(ob1.subtract())

#Shallow copy : it reflect the changes in the original copy
#Deep copy: it reflect the changes in the independent copy and do not affect the original copy

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")

# print(say_hello())

# def divide(a,b):
#     try:
#         result = a/b
#         print(result)
#     except (ZeroDivisionError) as e:
#         print(e)
#
# divide(6,2)
# divide(5,0)


# class a:
#     def display(self):
#         print('class a')

# class b:
#     super
#     def display(self):
#         print('class b')

# class c:
#     def display(self):
#         print('class c')

# class d:
#     def display(self):
#         print('class d')

# a1 = a()
# a1.display()
# b1 = b()
# b1.super()

# def my_decorator(func):
#         def wrapper():
#             if y == 0:
#                  print('Non divisible by y')
#             else:
#                  return x/y
#         # return wrapper
#
#
# @my_decorator  #nested func
# def func(x, y):
#     return x/y
#
#
# print(func())


# class MyModel(models.Model):  #Model , ORM model , relationship, 1:Many , read
#     field1 = models.CharField(max_length=50)
#     field2 = models.CharField(max_length=50)
#
#     class Meta:
#         unique_together = ('field1', 'field2')
#
#
# class MyModel(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other')
#     ]
#
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#
#
# class MyModel(models.Model):
#     field1 = models.CharField(max_length=50)
#     field2 = models.CharField(max_length=50)
#
#     class Meta:
#         unique_together = ('field1', 'field2')

# list1 = [i for i in range(1, 1001) if i%2 != 0]
# print(list1)

# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]
#
# dict1 = {key:value for key , value in zip(keys, values)}
# print(dict1)

# replace am with _
# str = "I am pritram"
# s1 = str.replace("am", "_")
# print(s1)

# import re

# str = "I am pritram"
# modified_str = re.sub(r'\bam\b', "_", str)
# print(modified_str)

# a=1
# b=2
# c=3
# addTen = lambda x: x+10
# print(addTen(a))
# print(addTen(b))
# print(addTen(c))

# use map
# list1 = [1, 4, 5, 6, 2, 3]
#
# def double(x):
#     return x*2
#
# doubled_numbers = map(double, list1)
# print(list(doubled_numbers))

# use filter to print even no

# def even(x):
#     return x%2==0
#
# even_numbers=filter(even,list1)
# print(list(even_numbers))


# op="a3b2c2a1"

# def generate_str(input):
#     left = 0
#     right = left +1
#     count = 0
#     result = []
#     new_str = ""

#     while right < len(input):
#         if input[left] == input[right]:
#             right +=1
#         else:
#             count = right - left
#             result.append(input[left])
#             result.append(str(count))
#             left = right
#             right +=1

#         if right == len(input):
#             count = right - left
#             result.append(input[left])
#             result.append(str(count))

#     new_str += "".join(result)
#     return new_str

# input= "aaabbcca"
# print(generate_str(input))

print(set('Banana'))

