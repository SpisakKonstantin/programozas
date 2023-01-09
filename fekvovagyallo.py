szélesség=int(input("adja meg a téglalap szélességét: "))
magasság=int(input("adja meg a téglalap magasságát: "))
terület = magasság*szélesség
if magasság>szélesség:
    print("ez egy álló téglalap. Területe: ",terület )
elif szélesség>magasság:
     print("ez egy fekvő téglalap. Területe: ",terület )
elif szélesség==magasság:
     print("ez egy négyzet. Területe: ",terület )
