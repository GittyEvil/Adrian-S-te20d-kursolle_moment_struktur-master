from time import localtime



x=localtime().tm_hour

if x < 8:
    print("Skoldagen har inte börjat än.")
elif x < 17:
    print("Skolan pågår fortfarande.")
else: 
    print("Skolan är slut stick hem.")

    
    
