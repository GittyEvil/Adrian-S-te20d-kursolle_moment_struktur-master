penna=4
pennaantal=int(input("Hur många pennor vill du köpa?"))

totalkostnadpenna=penna*pennaantal

äpple=1
äppleantal=int(input("Hur många äpplen vill du köpa?"))
kgäpplen=19
äpplevikt=200
totalkostnadäpple=äppleantal*äpplevikt/1000*kgäpplen

print(f"Jag handlade {pennaantal} pennor för {totalkostnadpenna}och {äppleantal} för {totalkostnadäpple} vilket totalt blev {totalkostnadpenna+totalkostnadäpple}")

#I denna kod var jag tvungen att göra om ungefär allt för att det krävde inte bara variabler som jag satte in med fstring utan det krävde frågor för att få reda på kostnad av äpple etc.