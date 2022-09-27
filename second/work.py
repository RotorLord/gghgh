'''Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение,
multiplication — умножение, division — деление, subtraction — вычитание.
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.'''
import math



class math():
    def __init__(self,a = 0 ,b = 0):
        self.a = a
        self.b = b

    def choose_a_b(self,math):
        self.a = int(input("a - number"))
        self.b = int(input("b - number"))

    def addition(self,a,b):
        print(f'{a} + {b} = {a  + b }')
    def multiplication(self,a,b) :
        print(f'{a} * {b} = {a  * b }')

    def division(self,a,b):
        print(f'{a} / {b} = {a  / b }')
    def subtraction(self,a,b):
        print(f'{a} - {b} = {a  - b }')














