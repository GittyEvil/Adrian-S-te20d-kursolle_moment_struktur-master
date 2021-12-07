from time import localtime



x=localtime(10)

if localtime > 16:
    print("Skoldagen är slut, stick hem.")
elif localtime < 17:
    print("SKolan pågår fortfarande.")
    
