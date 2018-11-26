def machtv3(basisgetal,macht):
    assert macht > 0

    resultaat = 1
    while macht > 0:
        if macht%2 == 0:
            basisgetal *= basisgetal
            macht /= 2
        else:
            resultaat *= a
            macht -= 1
    return resultaat

print(machtv3(2,10))