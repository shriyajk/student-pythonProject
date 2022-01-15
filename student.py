class Student:
    def __init__(self,name,USN,m1,m2,m3,m4,m5):
        self.name = name
        self.USN = USN
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
    def __str__(self) -> str:
        return self.name + " " + str(self.USN)
    
    def average(self):
        return (self.m1 + self.m2 + self.m3 + self.m4 + self.m5)/5
        
def createStudent(name,USN,m1,m2,m3,m4,m5):
    student = Student(name,USN,m1,m2,m3,m4,m5)
    return student

    
    
    
    