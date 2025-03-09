class car:
    def __init__(self,auto,brand,model,year):
        self.auto=auto
        self.brand=brand
        self.model=model
        self.year=year
        
    def sales(self):
        print(self.auto," is a",self.brand)
        
    def exhibition(self):
        print(self.auto," is ",self.model," of the year",self.year)
        
A=car("SUV","Audi","RS7",2024)
 

if __name__=="__main__":
    A.sales()         
    A.exhibition() 
             