def F(n):
    if n > 10000:
        return "Value is too high"
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    waysToPay = []
    for coin in range(len(coins)):
        if n > coins[coin]:
            maxCoin = coin

    for coin in range(maxCoin + 2):
        waysToPay.append([])
        for way in range(n + 1):
            waysToPay[coin].append(1)

    for coin in range(1, maxCoin + 2):
        for way in range(len(waysToPay[coin])):
            if way >= coins[coin]:
                waysToPay[coin][way] = waysToPay[coin - 1][way] + waysToPay[coin][way - coins[coin]]
            elif way < coins[coin]:
                waysToPay[coin][way] = waysToPay[coin - 1][way]

    return waysToPay[-1][-1]

print(F(18))
print(F(26))
print(F(5403))
print(F(20000))
