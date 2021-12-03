class Customer:

    def __init__(self,name,balance=0):
        self.name=name
        self._balance=balance

    def __str__(self):
        return "Klient\'{}\'. Balanc: {}rub.".format(self.name,self.balance) 
    @property
    def balance(self):
        return self._balance

    def record_payment(self,amount_paid):
        assert amount_paid>0
        self._balance+=amount_paid
        
    def record_call(self,call_type,minutes):

        
       if call_type=='G':
             self._balance-=minutes*5
       elif call_type=='M':
             self._balance-=minutes*1
if __name__=='__main__':
    
    ivan=Customer('Ivan Petrov')
    elena=Customer('Elena Mironova',100)
    ivan.record_call('G',20)
    ivan.record_call('M',5)
    elena.record_call('M',10)

    ivan.record_payment(155)

    print(ivan)
    print(elena)    
