#för att kunna avsluta lätt.
import sys

namn=input("Vad heter du?")
ålder=int(input("hur gammal är du?"))
program=input("Vilket program läser du? NA för natur och TE för teknik")


if program == "TE" or "te":
    val=input("Vilken inriktning vill du ha? finns TEINF, TEDES och TETEK.")

    if val == "TEINF" or "TEDES" or "TETEK":
        print(f"du heter {namn} och är {ålder}, går i {program} och har valt linjen {val}")

    else:
        print("koden har gått fel, avslutad")

    
    
    
    
if program == "NA" or "TE":
    val=input("du har valt Natur, vilken inriktning vill du gå på? de som finns att välja är:NANAS och NANAT.")

    if val== "NANAS" or "NANAT":
        print(f"Du heter {namn} är {ålder} och går i {program} och har då valt linjen {val}.")





        
        
