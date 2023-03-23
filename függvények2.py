#lower()
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
#A lower()metódus egy olyan karakterláncot ad vissza, amelyben minden karakter kisbetű.
#A szimbólumokat és számokat figyelmen kívül hagyja.

#upper()
txt = "Hello my friends"
x = txt.upper()
print(x)
#A upper()metódus egy olyan karakterláncot ad vissza, amelyben minden karakter nagybetűs.
#A szimbólumokat és számokat figyelmen kívül hagyja.

#capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
#A capitalize()metódus egy karakterláncot ad vissza, ahol az első karakter nagybetű, a többi pedig kisbetű.

#endswith()
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
#A endswith()metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel végződik, ellenkező esetben False-t.

#find()
const ages = [3, 10, 18, 20];
function checkAge(age) {
  return age > 18;
}
function myFunction() {
  document.getElementById("demo").innerHTML = ages.find(checkAge);
}
#A find()metódus az első teszten átmenő elem értékét adja vissza.
#A find()metódus minden tömbelemhez végrehajt egy függvényt.
#A find()metódus akkor tér vissza undefined, ha nem található elemek.
#A find()metódus nem hajtja végre a függvényt üres elemek esetén.
#A find()metódus nem változtatja meg az eredeti tömböt.

#isalnum()
txt = "Company12"
x = txt.isalnum()
print(x)
#A isalnum()metódus igaz értéket ad vissza, ha az összes karakter alfanumerikus, azaz ábécé betűi (az) és számok (0-9).
#Példa olyan karakterekre, amelyek nem alfanumerikusak: (szóköz)!#%&? stb.

#isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x)
#A isalpha()metódus igaz értéket ad vissza, ha az összes karakter ábécé betűje (az).
#Példa olyan karakterekre, amelyek nem ábécé betűi: (szóköz)!#%&? stb.

#islower()
txt = "hello world!"
x = txt.islower()
print(x)
#A islower()metódus igaz értéket ad vissza, ha minden karakter kisbetűvel van írva, ellenkező esetben False-t.
#A számok, szimbólumok és szóközök nincsenek bejelölve, csak az ábécé karakterei.

#join()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
#A join()metódus az összes elemet iterálhatóvá teszi, és egyetlen karakterláncba egyesíti.
#Elválasztóként egy karakterláncot kell megadni.

#replace()
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#A replace()metódus lecserél egy megadott kifejezést egy másik megadott kifejezésre.

#rfind()
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
#A rfind()metódus megkeresi a megadott érték utolsó előfordulását.
#A rfind()metódus -1-et ad vissza, ha az érték nem található.
#A rfind()módszer majdnem megegyezik a rindex() módszerrel. Lásd alább a példát.

#rstrip()
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
#A rstrip()metódus eltávolítja a záró karaktereket (a karakterlánc végén lévő karaktereket), a szóköz az alapértelmezett eltávolítandó karakter.

#startswith()
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
#A startswith()metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel kezdődik, ellenkező esetben False-t.

#strip()
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#A strip()metódus eltávolítja a kezdő (szóköz az elején) és a záró (szóköz a végén) karaktereket (a szóköz az eltávolítandó alapértelmezett kezdő karakter).

#swapcase()
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
#A swapcase()metódus egy karakterláncot ad vissza, ahol az összes nagybetű kisbetű, és fordítva.

#title()
txt = "Welcome to my world"
x = txt.title()
print(x)
#A title()metódus egy karakterláncot ad vissza, ahol minden szó első karaktere nagybetű. Mint egy fejléc vagy egy cím.
#Ha a szó számot vagy szimbólumot tartalmaz, az utána lévő első betű nagybetűvé alakul.

# center()
txt = "banana"
x = txt.center(20)
print(x)
#A center()metódus középre igazítja a karakterláncot, és egy megadott karaktert használ (a szóköz az alapértelmezett) kitöltési karakterként.