# kérjünk be 2 számot (egész szám) utána irasuk ki a nagyobb számot.
első_szám=int(input("kérek egy egész számot: "))
második_szám=int(input("kérek még egy egész számot: "))
"""
if első_szám > második_szám:
    print('az első szám nagyobb',első_szám)
if második_szám>első_szám:
    print('a második szám nagyobb',második_szám)
"""
if első_szám>második_szám:
    print(első_szám)
elif második_szám>első_szám:
    print(második_szám)
else:
    print("az egyik szám megegyezik a másikal")