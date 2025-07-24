# Related to searching for the smallest number with more than n factors


from prime_generator import next_prime
from prime_nearest import index_prime
from prime_factorization import quick_factors


class FactorState():
    def __init__(self, factors, value=None, num_factors=None):
        self.factors = factors
        if value is None:
            self.value, self.num_factors = self.findValue()
        else:
            self.value = value
            self.num_factors = num_factors
    
    def findValue(self):
        factors = self.getFactors()
        prod = 1
        num_factors = 1
        for factor, exponent in factors.items():
            prod *= factor**exponent
            num_factors *= exponent+1
        return prod, num_factors

    def multBy(self, factor):
        factors = self.getFactors()
        factors[factor] = factors.get(factor, 0) + 1
        return FactorState(factors)
    
    def lastPrimeFactor(self):
        """
        As the name says, finds the last prime factor
        """
        factors = self.getFactors()
        return list(factors.keys())[-1]

    
    def getFactors(self):
        return self.factors.copy()
    
    def getValue(self):
        return self.value
    
    def numFactors(self):
        return self.num_factors

    def rank(self):
        return self.getValue() / self.numFactors()
    
    def __str__(self):
        return str(self.getFactors())


class StackFrontier():
    def __init__(self, f=None):
        """
        Frontier history stores the smallest number for each number of factors    
        """
        if f is None:
            f = []
        self.frontier = f
        self.snapshot()
    
    def snapshot(self):
        """
        Saves an image of the current best in the frontier    
        """
        history = {}
        for state in self.getFrontier():
            try:
                if state.getValue() > history[state.numFactors()]:
                    history[state.numFactors()] = state.getValue()
            except KeyError:
                history[state.numFactors()] = state.getValue()
        self.newHistory(history)
    
    def getHistory(self):
        return self.history
    
    def newHistory(self, h):
        self.history = h
    
    def getFrontier(self):
        return self.frontier[:]
    
    def updateFrontier(self, frontier):
        self.frontier = frontier
    
    def remove(self):
        return self.frontier.pop()
    
    def remove_from_root(self, root):
        to_del = []
        f = self.getFrontier()
        for i in range(len(f)):
            if not f[i].is_stable and f[i].get_unstable().num() == root:
                to_del.append(i)
        for d in reversed(to_del):
            del f[d]
    
    def add(self, state: FactorState):
        """
        Note: only adds stuff to the frontier if the thing being added
        is better than the stuff in the history    
        """
        h = self.getHistory()
        print("history:", str(h))
        if h.get(state.numFactors(), None) is not None:
            if state.getValue() < h[state.numFactors()]:
                h[state.numFactors()] = state.getValue()
            else:
                return
        else:
            h[state.numFactors()] = state.getValue()
        f = self.frontier
        f.append(state)
        f = list(reversed(sorted(f, key=lambda action: action.rank())))
        self.updateFrontier(f)
    
    def has_stuff(self):
        return bool(self.getFrontier())

    def __str__(self):
        return str([str(i) for i in self.getFrontier()])


def actions(state: FactorState, primes):
    """
    Given a state, finds the actions that can be performed
    """
    a = []
    # print("finding actions for state", state)
    factors = state.getFactors()
    for factor in factors.keys():
        # print("first factor", factor)
        # print("\taction is", state.multBy(factor))
        a.append(state.multBy(factor))
        # print("after appending:", [str(i) for i in a])
    next_factor = next_prime(primes[-1]+1, primes)
    a.append(state.multBy(next_factor))
    return next_factor, a


def searchMostFactors(n):
    """
    Searches for the smallest number with more than n factors
    """
    primes = [2]
    frontier = StackFrontier([FactorState({2: 1})])
    while frontier.has_stuff():
        state = frontier.remove()
        print("state being considered", state, "with factors:", state.numFactors())
        if state.numFactors() >= n:
            print(frontier)
            return state
        if state.lastPrimeFactor() == primes[-1]:
            prime, a = actions(state, primes)
            primes.append(prime)
        else:
            prime, a = actions(state, primes[:index_prime(state.lastPrimeFactor()+1, primes)])
        a = list(reversed(sorted(a, key=lambda action: action.rank())))
        print("\tactions for this state", [str(i) for i in a])
        print("this is the value of a", a)
        for act in a:
            print("\tadding", act, "to the frontier")
            frontier.add(act)
        print("values in the frontier", frontier)
    return None


# result = searchMostFactors(501)
# You did good, but these numbers aren't just any numbers...
# They have to be triangular...


