class Person:
    
    def __init__(self, first, last):
        self._first = first
        self._last = last
        
    def get_first(self):
        return self._first
    
    def get_last(self):
        return self._last
    

# Inheritance
class Student(Person):
    
    def __init__(self, first, last, stunum):
        Person.__init__(self, first, last)
        self._stunum = stunum
    
    def get_stunum(self):
        return self._stunum

