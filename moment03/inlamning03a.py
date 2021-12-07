månadslön=int(input("Vad är din månadslön?"))
kommunalskatt=0.2136
landstingsskatt=0.1148
print(f"din månadslön:{månadslön}kr")


kskatt=månadslön*kommunalskatt
print(f"Kommunalskatt={kskatt}kr")

lskatt=månadslön*landstingsskatt
print(f"landstingsskatt={lskatt}kr")

eskatt=månadslön-lskatt-kskatt
print(f"Kvar efter skatt={eskatt}kr")

