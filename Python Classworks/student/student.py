class Student:
    
    count  = 0
    
    def __init__(self, name, idnum, year):
        """Create objects"""
        self._name = name
        self._idnum = idnum
        self._year = year
        self.__class__.count += 1
    def getCount(self):
        return self.__class__.count
    def getName(self):
        return self._name
    def getIdnum(self):
        return self._idnum
    def getYear(self):
        return self._year
    def setYear(self, year):
        if year < 0:
            print("Error: Year must be +ve.")
        else:
            self._year = year
    
        