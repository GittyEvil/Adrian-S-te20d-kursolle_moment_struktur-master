from time import localtime



x=localtime().tm_hour

if x < 8:
    print("Skoldagen har inte börjat än.")
elif x < 17:
    print("Skolan pågår fortfarande.")
else: 
    print("Skolan är slut stick hem.")

    
#pseudo kod

#importerar local time.
    #sätter variabeln för localtime till x
    
#Frågar användaren om x är mindre än 8.
    #Om klockan är mindre än 8 skriv då ut
        #Skoldagen har inte börjat än.

#Om det inte stämmer frågar användaren då om x är mindre än 17.
    #Om klockan är mindre än 17 skriv då ut.
        #Skoldagen pågår fortfarande.

#Annars så skriver du ut.
    #Skolan är slut stick hem.