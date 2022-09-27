'''Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
По умолчанию name = Ivan, age = 18, groupNumber = 10A.
Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о номере группы конкретного студента.
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student,
установить им разные имена, возраст и номер группы.'''

class Student():
    def __init__(self, name = "Ivan", age = "18", groupNumber = "10A" ):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber




    def Name(self, Student):
            print(f'{self.name}')

    def Age(self, Student):
            print(f'{self.age}')

    def groupe(self, Student):
            print(f'{self.groupNumber}')

    def Setgroupe(self, Student, groupNumber = ""):
            self.groupNumber = input("set new groupe")

    def setName_Age(self,Student,age ="",name= ""):
        self.age = input("set new age")
        self.name = input("set new name")



while True:
    try:
        studentWhich = int(input("choose student"))
        if (studentWhich == 1):
            Student1 = Student(name = "ivam",age = "13",groupNumber = "10A")
            Student1.Name(Student)
            Student1.groupe(Student)
            Student1.Age(Student)
            Student1.Setgroupe(Student,groupNumber = "")
            Student1.groupe(Student)
            Student1.setName_Age(Student)
            Student1.Age(Student)
            Student1.Name(Student)
        if (studentWhich == 2):
            Student2 = Student(name="ivam", age="13", groupNumber="10A")
            Student2.Name(Student)
            Student2.groupe(Student)
            Student2.Age(Student)
            Student2.Setgroupe(Student, groupNumber="")
            Student2.groupe(Student)
            Student2.setName_Age(Student)
            Student2.Age(Student)
            Student2.Name(Student)
        if (studentWhich == 3):
            Student3 = Student(name="ivam", age="13", groupNumber="10A")
            Student3.Name(Student)
            Student3.groupe(Student)
            Student3.Age(Student)
            Student3.Setgroupe(Student, groupNumber="")
            Student3.groupe(Student)
            Student3.setName_Age(Student)
            Student3.Age(Student)
            Student3.Name(Student)
        if (studentWhich == 4):
            Student4 = Student(name="ivam", age="13", groupNumber="10A")
            Student4.Name(Student)
            Student4.groupe(Student)
            Student4.Age(Student)
            Student4.Setgroupe(Student, groupNumber="")
            Student4.groupe(Student)
            Student4.setName_Age(Student)
            Student4.Age(Student)
            Student4.Name(Student)
        if (studentWhich == 5):
            Student5 = Student(name="ivam", age="13", groupNumber="10A")
            Student5.Name(Student)
            Student5.groupe(Student)
            Student5.Age(Student)
            Student5.Setgroupe(Student, groupNumber="")
            Student5.groupe(Student)
            Student5.setName_Age(Student)
            Student5.Age(Student)
            Student5.Name(Student)
    except Exception as er:
            print("number")









