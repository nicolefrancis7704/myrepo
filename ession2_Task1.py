class student :
    def __init__(self,name,id): # initialize function , self → parameter that refers to the current object.
        self.name=name
        self.id=id
        self.grade=[] # a list of arrays to get all the grades of a student
    def add_grade (self,grade) :
        self.grade.append(grade) #add grade to the list
    def average(self): #function to get the average of grades
        if len(self.grade) == 0: # if list of grades is empty to avoid the division by zero
            return 0
        return sum(self.grade) / len(self.grade) # return the sum of all grades in the list then divide it by the lenght of list
    def display_info (self) : #dispaly function
        print(f"Name:{self.name} - ID:{self.id} - Grades:{self.grade} - Average:{self.average( )} ") #print name,id,grades and average       
    
name = input("Enter name: ") #print the name
if not name.replace(" ", "").isalpha(): # if name isn't consist of alphabates , then it will end the program 
    print("Invalid name")
    exit()
id = input("Enter ID :") #print ID
if not id.isdigit(): # if ID isn't consist of digits , then it will end the program 
    print("Invalid ID")
    exit()
stu=student(name,id) #it will send the name and id to the class: class student
for i in range(3) :
    grade=int(input("Enter grade:")) # print grade
    if not grade.is_integer(): #if grade isn't consist of integers , then it will end the program
        printf("Invalid grade")
        exit()
    stu.add_grade(grade) # send grade to the class , and enter the add_grade function

stu.display_info( )# display name,id,grades and the average