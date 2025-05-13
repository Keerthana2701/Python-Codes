print('class with multiple instances')
class student:
    def __init__(self,no,name,mark1,mark2):
        self.no=no
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
    def studentname(self):
        print('student name:{self.name}')
    def studentmarks(self,mark1,mark2):
        print("student total mark:{mark1+mark2}")
    def studentdetails(self,no,name,mark1,mark2):
        print("student details: \n name:{self.name}\n number:{self.no}\n mark1 :{self.mark1} \n mark2:{self.mark2}" )

#create 2 instances
S1=student('100','keerthu',200,600)
S2=student('111','Vikee',500,500)
S1.studentdetails()

