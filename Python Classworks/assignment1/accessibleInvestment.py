from investment import Investment

class AccessibleInvestment(Investment):
    
    def __init__(self, principal, interest):
        Investment.__init__(self, principal, interest)
        
        
    def withdraw(self, amount):
        return Investment.getPrincipal(self) - amount
        
    
    
