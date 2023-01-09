név=input("adja meg a nevét: ")
kor=int(input("adja meg az életkorát: " ))
if kor<1:
    print("a kora alapján" ,név ,"csecsemő")
elif kor<6:
    print("a kora alapján" ,név ,"kisgyerek")
elif kor<12:
    print("a kora alapján" ,név ,"gyerek")
elif kor<16:
    print("a kora alapján" ,név ,"serdülö")
elif kor<25:
    print("a kora alapján" ,név ,"ifjú")
elif kor<65:
    print("a kora alapján" ,név ,"felnőtt")
elif kor>=65:
    print("a kora alapján" ,név ,"nyugdijas")