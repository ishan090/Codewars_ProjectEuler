
# Coins of different denominations can be summed in different ways to produce
# a particular resulting value.

# Demoninations for this particular problem include: {1, 2, 5, 10, 20, 50, 100, 200}
# And the objective is to calculate the number of unique sums that equal 200


class CoinCombination():
    def __init__(self, coins_dict, denominations):
        self.coins = coins_dict
        self.denominations = denominations
    
    def sumVal(self):
        coins = self.coins
        total = 0
        for i in coins:
            total += i * coins[i]
        return total
    
    def fillCoin(self, denom, limit):
        """
        Given the sum of the sequence at hand, finds the num of coins of a certain
        denomination that can be filled and outputs it 
        """
        assert limit > self.sumVal(), "There must atleast be some space to fill in the coin"
        return (limit - self.sumVal()) % denom
    


def coin_sum(limit, denoms):
    """ 
    Assumptions:
    The denoms are in descending order of magnitude
    That the last denominator is 1, which means, it's not necessary
    to compute the possibilities for the last one.
    """
    if len(denoms) == 1:
        # print("found a possibility")
        return 1
    next_denom = denoms[0]
    # print("Denom under consideration:", next_denom)
    denoms = denoms[1:]
    num_mults = limit // next_denom
    # print(f"{next_denom} times {num_mults} is the largest value: {num_mults * next_denom}")
    poss = 0
    for i in range(num_mults+1):
        # print("Exploring under", next_denom, "=", i)
        new_limit = limit - i*next_denom
        # print("new limit is", new_limit)

        # print("\t\tposs increased")
        poss += coin_sum(new_limit, denoms)
    return poss


if __name__== "__main__":
    print(coin_sum(200, [200, 100, 50, 20, 10, 5, 2, 1]))
