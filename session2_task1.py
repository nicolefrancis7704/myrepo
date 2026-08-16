class student : #Make a class of studets
    def __init__(self,name,id): #get name and id of student
        self.name=name
        self.id=id
        self.grades=[] #prepare list for grades
    def add_grade (self,grade) : #Add new grade
        self.grades.append(grade)
    def average (self):
        if len(self.grades)==0 : #if the list is empty then we need to avoid the division error (0/0)
            return 0
        else :
            return sum(self.grades) / len(self.grades) #return the average of grades
    def display(self):
        print(f"Name:{self.name} - ID:{self.id} - Grades:{self.grades} - Average:{self.average()}") #print all the info of the student

name=input("Enter name:") #print the name
if not name.replace(" ","").isalpha():#Confirm the name
    print("Invalid name")
    exit() 
id=input("Enter ID:")#print ID
if not id.isdecimal():#confirm ID
    print("Invalid ID")
    exit()
s1=student(name,id) #Send name and ID to the class
for i in range(3) :# a loop to get 3 grades and added it to the list
    grade=int(input("Enter grade:"))
    s1.add_grade(grade)      
s1.display() #display info of student