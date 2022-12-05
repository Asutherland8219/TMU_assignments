def give_change(amount, coins):
        result = []
        return give_change_sort(amount, coins, result)


def give_change_sort(amount, coins, result):
        if amount == 0:
                return result
        while len(coins) > 0 and amount >= coins[0]:
                amount = amount - coins[0]
                result.append(coins[0])
        if len(coins) > 0:
                coins = coins[1:]
        else:
                return result
        return give_change_sort(amount, coins, result)