from CALC101 import*

P=str(input('enter op:'))
a=int(input('enter a:'))
b=int(input('enter b:'))

if P=='*':
    mal(a,b)   
elif P=='+':
    add(a,b)
elif P=='-':
    minus(a,b)
elif P=='/':
    div(a,b)
else:
    print("Syntax Error!!")          
    
        