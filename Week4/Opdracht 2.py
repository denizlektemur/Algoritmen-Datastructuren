mydict = {}
i = 0.000001
a = 0.999999
while i < a:
    hashvalue = hash(i)
    if hashvalue in mydict:
        print(repr(i), "==", repr(mydict[hashvalue]), "==", repr(hashvalue))
    else:
        mydict[hashvalue] = i
    i += 0.000001
