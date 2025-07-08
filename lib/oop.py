class Room:
    def __init__(self, number, max_guests):
        self.room_number = number
        self.max_occupancy = max_guests

class HardRoom:    

    # method for creating a new room with set number and maximum number of guests
    def __init__(self,number,max_guests):
        self.number = number
        self.max_guests = max_guests
        self.guests = []
        
    # method for checking in a guest
    def checkIn(self, guest):
        if (len(self.guests) < self.max_guests):
            self.guests.append(guest)
        else:
            print("Room is already full.")
            
    # method for checking out a guest
    def checkOut(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)
        else:
            print(f"{guest} is not a guest in this room.")

# base class person
class Person:
    
    # init person object with its name
    def __init__(self, name):
        self.name = name
        
    # print out the name of the person
    def printInfo(self):
        print(f"I am {self.name}.")
        

# derived class student
class Student(Person):
    
    # init student object as a person, then add other attributes
    def __init__(self,name,university,program):
        Person.__init__(self,name)
        self.university = university
        self.program = program
        self.creditpoints = None
        
    # print out the name, university and program of the student
    def printInfo(self):
        Person.printInfo(self)
        print(f"I am a student at {self.university}. "
              f"I study {self.program}.")
        
    # set the number of credit points
    def setCreditPoints(self,points):
        self.creditpoints = points
        
    # get the number of credit points
    def getCreditPoints(self):
        return self.creditpoints
        
# subclasses for bachelor and master students
class BachelorStudent(Student):
    
    # init a bachelor student as student, add school
    def __init__(self,name,university,program,school):
        Student.__init__(self,name,university,program)
        self.school = school
    
    # print out the student information, plus the school
    def printInfo(self):
        Student.printInfo(self)
        print(f"I went to school in {self.school}.")
        
class MasterStudent(Student):
    
    # init a master student as a student, add bachelor's degree
    def __init__(self,name,university,program,bdegree):
        Student.__init__(self,name,university,program)
        self.bdegree = bdegree
                
    # print out the student information, plus the bachelor's degree
    def printInfo(self):
        Student.printInfo(self)
        print(f"I have a Bachelor's degree in {self.bdegree}.")
        
# derived class Teacher
class Lecturer(Person):
    
    # init lecturer as a person, add university and department info
    def __init__(self,name,university,department):
        Person.__init__(self,name)
        self.university = university
        self.department = department
    
    # print out lecturer information
    def printInfo(self):
        Person.printInfo(self)
        print(f"I am a lecturer at {self.university}, {self.department}.")
