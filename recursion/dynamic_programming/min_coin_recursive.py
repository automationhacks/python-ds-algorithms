import time

"""
Given a return amount, figure out the min no of coins that can be expelled
from the vending machine to make up the required change
"""

COINS = [25, 10, 5, 1]


def find_min_coins(coin_values, change):
    min_coins = change

    if change in coin_values:
        return 1
    else:
        remaining_coins = [coin for coin in coin_values if coin <= change]
        for coin in remaining_coins:
            # 1 means, we are using a coin every time we recurse
            num_coins = 1 + find_min_coins(coin_values, change - coin)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


def test_min_coin():
    start = time.time()
    result = find_min_coins(COINS, 63)
    assert result == 6
    end = time.time()
    time_elapsed = end - start
    print('Total time taken: {}'.format(time_elapsed))

