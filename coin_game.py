def change(amount, coins):
    if len(coins) == 1 and coins[0] != amount:
        return 0
    if len(coins) == 1 and coins[0] == amount:
        return 1
    
    
    storing_combinations = [1] + [0] * amount
    for coin in coins:
        for combo in range(coin, amount+1):
            print(combo,coin)
            storing_combinations[combo] += storing_combinations[combo-coin]
            print(storing_combinations)
    return storing_combinations[amount]

amount = 4
coins =[1,2]
print(change(amount, coins))


