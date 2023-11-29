from person import Person

class Student(Person):
    
    def __init__(self, first, last, stunum):
        Person.__init__(self, first, last)
        self._stunum = stunum
    
    def get_stunum(self):
        return self._stunum
    
    def __str__(self):
        return "First Name: " + self.get_first() + \
            "\nLast Name: " + self.get_last() + \
                "\nStudent Number: " + self.get_stunum()
