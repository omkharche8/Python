# I will use my Example to show this (Classroom)
class College:
    def name(self,name):
        return name


class Classroom(College):
    def number(self,num):
        return num


class Student(Classroom):
    def details(self,sname, sheight, syear):
        print(sname + "\n" + str(sheight) + "\n" +  syear)


obj1 = Student()
obj1.details("Om", 6, "3rd")
print(obj1.number(6))
print(obj1.name("Test"))