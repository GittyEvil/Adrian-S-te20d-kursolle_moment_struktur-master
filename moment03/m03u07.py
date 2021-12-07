#Fråga användaren efter ett heltal.
#Fråga användaren efter ytterligare ett heltal.
#Multiplicera de två heltalen.
#Om de två heltalen är lika stora
#Skriv ut sidornas längd och vad "kvadratens area är"
#Annars
#Skriv ut sidornas längd och vad "rektangelns area är"


tal1=input(int("Säg ett tal."))
tal2=input(int("Säg ett tal till."))
x=tal1*tal2

if tal1==tal2:
    print(f"Kvadratens area är {x} och sidornas längd är {tal1} och {tal2}.")
else:
    print(f"Rektangels area är {x} och sidornas läng är då {tal1} och {tal2}.")
