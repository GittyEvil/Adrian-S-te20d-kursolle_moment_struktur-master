
radie = float(input("säg ett decimaltal:"))
pi= 3.14

def area(radie):
    area = radie*radie *pi
    return area
    

def omkrets(radie):
    omkretse = 2*radie*pi
    return omkretse

print(f"radien är :{radie}")
print(f"arean är :{area(radie)}")
print(f"omkretsen är :{omkrets(radie)} ")

area()
omkrets()
