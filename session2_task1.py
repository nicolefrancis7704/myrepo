class student :
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.grade=[]
    def add_grade (self,grade) :
        self.grade.append(grade)
    def average(self):
        if len(self.grade) == 0:
            return 0
        return sum(self.grade) / len(self.grade) 
    def display_info (self) :
        print(f"Name:{self.name} - ID:{self.id} - Average:{self.average( )} ")        
    
name=input("Enter name:")
id = input("Enter ID :")
stu=student(name,id)
for i in range(3) :
    grade=int(input("Enter grade:"))
    stu.add_grade(grade)

stu.display_info( )