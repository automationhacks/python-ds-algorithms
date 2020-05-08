COINS = [25, 21, 10, 5, 1]


def min_coins_dp(coin_values, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents

        potential_coins_to_use = [coin for coin in coin_values if coin <= cents]
        for potential_coin in potential_coins_to_use:

            balance = cents - potential_coin
            # Since each index is init with 0 in dp list
            min_coins_value = min_coins[balance] + 1

            if min_coins_value < coin_count:
                coin_count = min_coins_value

        print('cents={}, min_coins={}'.format(cents, coin_count))
        min_coins[cents] = coin_count
    return min_coins[change]


def test_min_coins_dp():
    change = 63
    dp = [0] * (change + 1)
    result = min_coins_dp(COINS, change, dp)
    assert result == 3
