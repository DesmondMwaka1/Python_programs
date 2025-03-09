from carGenModule import*

class cost:
    def __init__(self,irc):
        self.irc=irc
    def importDuties(self):
        #print(self.auto," has the following taxes:")
        import_duty=0.25*self.irc 
        print("import duty = ",import_duty)
        exercise_duty=0.16*(import_duty+self.irc)
        print("exercise duty = ",exercise_duty)
        port_taxes=0.10*(self.irc+import_duty+exercise_duty)  
        print("any other port taxes = ",port_taxes)
        
        total_import_taxes=self.irc+import_duty+exercise_duty+port_taxes
        print(" total import taxes = ",total_import_taxes)
        
    def any_otherTaxes(self):
        other_licences=0.15*self.irc
        print("any other taxes = ",other_licences)
        
class TotalCost(cost):
    
    def allCost(self):
        Y=self.importDuties()
        Z=self.any_otherTaxes()
        
        cosT=Y+Z
        print("Total amount required to import the car is : ",cosT)
        
            
        
A=car("Sportcar","Porche",911,2022)
A.sales()
A.exhibition()           
#A=cost(int(input("Enter current price of the car: ")))
A=TotalCost(int(input("Enter current price of the car: ")))
A.importDuties()   
A.any_otherTaxes()          

A.allCost()