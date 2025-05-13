print('class with methods \n')
print('class with multiple instances')
class employee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
    def printinfo(self):
        print(f"Name: {self.ename}, No: {self.eno}")


# creating multiple instance for class employee
# like employee1, employee2, employee3 etc

employee1=employee("100","keerthu")
employee2=employee("200","vikee")
employee1.printinfo()
employee2.printinfo()
