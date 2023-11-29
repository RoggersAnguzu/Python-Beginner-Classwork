class Car:
    count = 0
    def __init__(self, make, model, color, year):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self.__class__.count += 1
        
    def setColor(self, color):
        self._color = color

    def getMake(self):
        return self._make
    
    def getModel(self):
        return self._model
    
    def getColor(self):
        return self._color
    
    def getYear(self):
        return self._year
    
    def getCount(self):
        return self.__class__.count
    
    def __str__(self):
        return "Make: " + self._make + \
            "\nModel: " + self._model + \
                "\nColor: " + self._color + \
                    "\nYear: " + str(self._year)
        
    
   