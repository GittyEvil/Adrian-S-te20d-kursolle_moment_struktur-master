ränta=1.03
konto=10000
for i in range(1,16):
    konto*=ränta

print(f"det du har efter {i} år är:{konto:.0f}kr")

