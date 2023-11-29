class Investment:
    def __init__(self, principal, interest):
        self._principal = principal
        self._interest = interest/100
    
    def value_after(self, n):
        return self._principal * (1 + self._interest) ** n 
    
    def getPrincipal(self):
        return self._prinicpal
    
    def __str__(self):
        return "Prinicpal - " + str(self._principal) + \
            " Interest rate - " + str(self._interest)
        
        
    