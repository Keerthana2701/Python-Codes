print('class with multiple instances')

class Student:
    def __init__(self, no, name, mark1, mark2):
        self.no = no
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2

    def studentname(self):
        print(f'Student name: {self.name}')

    def studentmarks(self):
        total = self.mark1 + self.mark2
        print(f"Student total mark: {total}")

    def studentdetails(self):
        print(f"Student details:\n Name: {self.name}\n Number: {self.no}\n Mark1: {self.mark1}\n Mark2: {self.mark2}")

# Create 2 instances
S1 = Student('100', 'Keerthu', 200, 600)
S2 = Student('111', 'Vikee', 500, 500)


# Call methods
S1.studentdetails()
S1.studentmarks()
S2.studentdetails()
S2.studentmarks()
S2.studentname()
