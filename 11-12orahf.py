egyikszám = int(input("kérek egy számot 1-100: "))
másikszám = int(input("kérek egy számot 1-100: "))
if egyikszám < másikszám:
    print("ennyivel:", másikszám-egyikszám)
elif egyikszám > másikszám:
    print("az első szám nagyobb")
    print("ennyivel:", egyikszám-másikszám)
else:
    print("megegyezik")
