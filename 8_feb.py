# -*- coding: utf-8 -*-
"""8 feb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E1ui9-uPdz2xekiK1m8OJvBMTTxf3o7F
"""

'''
1.abstraction is the process in which we hide the unnecessary  or irrelevant details for the user'''
import abc
class book:
  @abc.abstractmethod
  def c(self):
    pass
  @abc.abstractmethod
  def java(self):
    pass
  @abc.abstractmethod
  def python(self):
    pass

a=book()

a.c()

class notes(book):
  def c(self,b_name):
    print('this is the c book of',b_name)

n=notes()

n.c('ashraf rizvi')

'''
2:abstraction is the process in which we hide the unnecessary  or irrelevant details from the userbut we can derive it in another class and use it
 whereas in encapsulation this user cant access particular stuff from the code'''
#example for encapsulation
class personaldetails:
  def __init__(self,name,mobile,age):
    self.__name=name
    self.__mobile=mobile
    self.__age=0

  def uname(self):
    print('my name is ',self.__name)

  def umobile(self):
    return self.__mobile

  def uage(self,age):
    return self.__age if age<0 else age

pd=personaldetails('ayushi',8748928,20)

pd._personaldetails__mobile

class personaldetails:
    def __init__(self, name, mobile, age):
        self.__name = name
        self.__mobile = mobile
        self.__age = age

    def uname(self):
        print('My name is', self.__name)

    def umobile(self):
        return self.__mobile

    def uage(self, age):
        return self.__age if age < 0 else age

pd=personaldetails('ayu',7893217,20)

pd._personaldetails__name

pd._personaldetails__age

'''3. abc-abstract base class module which is used to achieve absr=traction in python
4.we use @abc.abstractmethod a decorator function to achieve it
5.No, you cannot create an instance of an abstract class in Python.
An abstract class is meant to be a blueprint for other classes, and it's designed to be subclassed.
Abstract classes cannot be instantiated directly because they often contain incomplete or abstract methods that need to be implemented by their concrete subclasses.'''

