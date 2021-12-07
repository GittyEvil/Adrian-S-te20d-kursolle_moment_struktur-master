namn=input("vad heter du?")
ålder=input("Hur gammal är du?")
bokstav=namn(0)
ålder=ålder.strip(0)


print(f"du heter {namn}.och första bokstaven i ditt namn är {bokstav} ")

if ålder > 17:
    print("Du är myndig.")
