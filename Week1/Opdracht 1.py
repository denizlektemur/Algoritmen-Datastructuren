# Naam: Deniz Lektemur
# Studentnummer: 1722313
# Klas: V2C
# Docent: Frits Dannenberg

def mymax(a):
    assert len(a) > 0
    max_number = a[0]
    for i in a:
        assert type(i) == int or type(i) == float
        if i > max_number:
            max_number = i
    print(max_number)

try:
    mymax([1,2,3,45,2.5,6,784,8])
except:
    print("value type error or invalid length")

try:
    mymax([])
except:
    print("value type error or invalid length")

try:
    mymax([1,2,3,45,2.5,6,784,'8'])
except:
    print("value type error or invalid length")
