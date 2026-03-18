class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
    def __str__(self):
        return " %s %s" % (self.firstname, self.lastname)

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject
    def getsubject(self):
        return  " %s %s, %s" %(self.firstname, self.lastname, self.subject)

class Teacher(Person):
    def __init__(self, firstname ,lastname, subject_taught):
        super().__init__(firstname,lastname)
        self.subject_taught = subject_taught
    def getsubtaught(self):
        return " %s %s ,%s" %(self.firstname, self.lastname, self.subject_taught)
    
