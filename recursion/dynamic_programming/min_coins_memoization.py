import time

COINS = [25, 10, 5, 1]

"""
PROS:
- Faster than brute force recursive solution
- Cache avoids recursive calls for known results

CONS:
- Stores a list as long as the number
- Consumers lot of memory space.
"""


def find_min_coins_memoization(coin_values, change, known_results):
    min_coins = change

    if change in coin_values:
        return 1
    else:
        remaining_coins = [coin for coin in coin_values if coin <= change]
        for coin in remaining_coins:
            remaining_change = change - coin

            known_result = known_results[remaining_change]

            if known_result:
                num_coins = 1 + known_result
            else:
                num_coins = 1 + find_min_coins_memoization(
                    coin_values, remaining_change, known_results)
                known_results[remaining_change] = num_coins

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


def test_min_coins_with_memoization():
    start = time.time()

    change_for = 63
    known_results = [0] * change_for
    result = find_min_coins_memoization(COINS, change_for, known_results)
    assert result == 6

    end = time.time()
    time_elapsed = end - start
    print('Total time taken: {}'.format(time_elapsed))
