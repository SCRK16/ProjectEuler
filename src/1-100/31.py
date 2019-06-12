def coin_sum(target, used, coins):
    current = sum(used)
    if current == target:
        return 1
    elif current > target:
        return 0
    ways = 0
    for coin in coins:
        if len(used) == 0 or coin >= used[-1]:
            used.append(coin)
            ways += coin_sum(target, used, coins)
            used.pop()
    return ways

coins = [1, 2, 5, 10, 20, 50, 100, 200]
used = []
target = 200

result = coin_sum(target, used, coins)

print(result)
