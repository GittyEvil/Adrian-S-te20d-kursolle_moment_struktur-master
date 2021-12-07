månadslön=int(input("Vad är din månadslön?"))
årslön=månadslön*12

värnskatt=0.05
statskatt=0.20
kommunalskatt=0.2136
landstingsskatt=0.1148
if månadslön < 19247:
    print(f"du betalar inte skatt men din månadslön är: {månadslön}")
elif  månadslön > 19247:

    print(f"din månadslön:{månadslön}kr årslön:{årslön}kr")

    kskatt=månadslön*kommunalskatt
    print(f"Kommunalskatt={kskatt:.0f}kr")

    lskatt=månadslön*landstingsskatt
    print(f"landstingsskatt={lskatt:.0f}kr")

    eskatt=månadslön-lskatt-kskatt
    print(f"Kvar efter skatt={eskatt:.0f}kr")

if årslön > 468700:
    sskatt=månadslön*statskatt
    print(f"Statlig skatt={sskatt:.0f}kr")

if årslön > 675700:
    vskatt=månadslön*värnskatt
    print(f"Värnskatt={vskatt:.0f}kr")
