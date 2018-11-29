def machtv3(basisgetal,macht):
    assert macht > 0
    vermenigvuldigingen = 0
    resultaat = 1
    while macht > 0:
        vermenigvuldigingen += 1
        if macht%2 == 0:
            basisgetal *= basisgetal
            macht /= 2
        else:
            resultaat *= basisgetal
            macht -= 1
    return resultaat,vermenigvuldigingen

my_macht = machtv3(4,7)
print( "4 ** 7 =", my_macht[0], "met", my_macht[1], "vermenigvuldigingen")