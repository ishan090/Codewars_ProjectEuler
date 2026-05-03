
# Relates to prime pair sets of which concatenations of all possible
# pairs in any order result in primes as well.

# The lowest sum for a set of 4 primes of this property is:
# 3, 7, 109, 673 -> 792
# The objective is to find a least sum prime set of length 5

# IMPORTS
from copy import deepcopy
from prime_generator import gen_indefinite
from prime_checker import prime_check
from binary_search import inside, closest


class AllPrimes():
    def __init__(self, n=10, exclude=2):
        """
        Essentially a list of primes which can generate further primes as needed
        """
        self.prime_gen = gen_indefinite()
        self.p_s = [1] + [next(self.prime_gen) for i in range(n)]
        if exclude is not None:
            self.p_s.pop(exclude)
        # print("these are the primes:", self.p_s)
    
    def val(self, index):
        while index >= len(self.p_s):
            self.p_s.append(next(self.prime_gen))
        return self.p_s[index]
    
    def snip(self, a, b):
        return [self.val(i) for i in range(a, b)]
    
    def getVals(self, indicies):
        return [self.val(i) for i in indicies]


class PrimeSet():
    def __init__(self, inds=None, size=None):
        """
        A Prime Set which may or may not conform to the concerned property
        """
        assert not (inds is None and size is None), "Inputs inds and size can't both be none"
        if inds is None:
            self.indicies = [i for i in range(1, size+1)]
        else:
            self.indicies = inds.copy()
        self.primes = prime_stack.getVals(self.indicies)
        self.rem = self.primes[-1] % 3
    
    def getIndicies(self):
        return self.indicies.copy()
    
    def getPrimes(self):
        return self.primes.copy()

    def val(self):
        return sum(self.primes)

    def baseActions(self):
        """
        assumes self has only two elements which aren't yet compatible
        """
        second = self.unsolActions()
        inds = self.getIndicies()
        first = inds[0] + 1
        while first < inds[1]:
            if prime_stack.val(first) % 3 == self.rem:
                return [(0, first)] + second
            first += 1
        return second
            
    
    def unsolActions(self, inds=None):
        """
        Actions for a prime set whose final index is the only one malaligned
        """
        out = []

        if inds is None:
            inds = self.getIndicies()
        ind = len(inds) - 1
        x = inds[-1] + 1
        vals = sorted([dp_tables[self.rem-1].val(elem) for elem in inds[:ind]], key=lambda y: (y[1], y[0]), reverse=True)
        
        if x < vals[0][1]:
            current = set(vals[0][0])
            for val in vals[1:]:
                current = current.intersection(val[0])
            largest_invalid = vals[0][1]

            # print("cleanupA complete, here's vals:", vals)
            target = vals[0][1]

            # found, invalid = False, False
            current = [valid for valid in current if x <= valid]
            
            found = False
            for valid in current:
                if prime_stack.val(valid) % 3 == self.rem:
                    found = True
                    out.append((ind, valid))
                    return out
        while True:
            if prime_stack.val(x) % 3 == self.rem:
                out.append((ind, x))
                break
            x += 1
        return out
    

    def solActions(self):
        inds = self.getIndicies() + [self.getIndicies()[-1] + 1]
        return self.unsolActions() + self.unsolActions(inds=inds)
    
    def actions(self, sol=False):
        print("inside actions")
        if sol:
            acts = self.solActions()
        elif len(self) == 2:
            acts = self.baseActions()
        else:
            acts = self.unsolActions()
        print("\tthese are the actions:", acts)
        return acts
    

    def old2_actions(self, sol=False):
        """
        Updated algo for determining the actions given a state
        """
        out = []
        # Logic - go through each index. Determine the next index that's compatible
        # with all the previous indicies.
        inds = self.getIndicies() + [self.getIndicies()[-1] + 1] if sol else []

        for ind in range(len(inds)):
            
            last = False
            if ind >= len(self.indicies) - 1:
                last = True

            x = inds[ind] + 1
            if not last:
                limit = inds[ind + 1]
            # print("starting x and limit:", x, limit)
            if ind == 0:
                # print("first element")
                while x < limit:
                    if prime_stack.val(x) % 3 == self.rem:
                    # print("hay espacio")
                        out.append((ind, x))
                        break
                    x += 1
                continue

            if ind == 1:
                vals = [dp_tables[self.rem-1].val(inds[0])]
            else:
                vals = sorted([dp_tables[self.rem-1].val(elem) for elem in inds[:ind]], key=lambda y: (y[1], y[0]), reverse=True)

            
            current = set(vals[0][0])
            for val in vals[1:]:
                current = current.intersection(val[0])
            largest_invalid = vals[0][1]

            # print("cleanupA complete, here's vals:", vals)
            target = vals[0][1]

            # found, invalid = False, False
            if not last:
                current = [valid for valid in current if x <= valid < limit] 
            else:
                current = [valid for valid in current if x <= valid]
            
            found = False
            for valid in current:
                if prime_stack.val(valid) % 3 == self.rem:
                    found = True
                    out.append((ind, valid))
                    break
            
            # print("finished looking through valids")
            if found:
                # print("invalid or found")
                continue
            x = target + 1
            while (last) or (not last and x < limit):
                if prime_stack.val(x) % 3 == self.rem:
                    out.append((ind, x))
                    break
                x += 1
        
        print("actions of", str(self), "are:", out)
        print([dp_tables[self.rem-1].invalidMarker(i) for i in self.getIndicies()])

        return out

    def actions_old(self):
        out = []
        inds = self.getIndicies() + [self.indicies[-1] * 2]
        print("this is inds", inds)
        for ind in range(len(inds)-1):
            print("ROUND", ind)
            x = inds[ind] + 1
            valid = False
            for i in inds[:ind]:
                print("x is:", x)
                valids = dp_tables[self.rem-1].validsFor(i)
                partA, partB, valid = True, True, False
                if not valids:
                    partA = False
                while x < inds[ind+1]:
                    print("loopin")
                    if prime_stack.val(x) % 3 == self.rem:
                        valid = True
                        break
                    x += 1
                    if partA:
                        print("partA")
                        best = lin_closest(valids, x)
                        if best >= len(valids):
                            partA = False
                            x = valids[-1] + 1
                        elif valids[best] > x:
                            x = valids[best]
                    elif partB:
                        print("partB")
                        nextValid = dp_tables[self.rem-1].invalidMarker(i) + 1
                        if nextValid >= x:
                            x = nextValid
                        partB = False
                if not valid:
                    break
            if not valid:
                continue
            out.append((ind, x))

        # last = self.getIndicies()[-1] + 1
        # while prime_stack.val(last) % 3 != self.rem:
        #     last += 1
        # out.append((len(self) - 1, last))
        print("actions of", str(self), "are:", out)
        return out
    
    def result(self, action):
        """performs the action on the object and returns a new object"""
        try:
            inds = self.getIndicies()
            inds[action[0]] = action[1]
        except IndexError:
            inds.append(action[1])
        return PrimeSet(inds)
    
    def isPSET(self):
        """
        Checks if the prime set follows the `property`
        """
        result = True
        for i in range(len(self)):
            x = self.getIndicies()
            z = x.pop(i)
            val = prime_stack.val(z)
            for y in x:
                other = prime_stack.val(y)
                e = dp_tables[self.rem-1].evaluate(z, y)
                if e is None:
                    a = prime_check(int( str(val) + str(other) ))[0]
                    b = prime_check(int( str(other) + str(val) ))[0]
                    if not (a and b):
                        dp_tables[self.rem-1].incompat(z, y)
                        dp_tables[self.rem-1].incompat(y, z)
                        result = False
                    else:
                        dp_tables[self.rem-1].entry(z, y)
                        dp_tables[self.rem-1].entry(y, z)
                elif not e:
                    result = False
        return result
    
    def elabPSET(self):
        for i in range(len(self)):
            x = self.getPrimes()
            val = x.pop(i)
            for other in x:
                p = int( str(val) + str(other) )
                q = int( str(other) + str(val) )
                a = prime_check(p)[0]
                b = prime_check(q)[0]
                print(f"{p} : {a}")
                print(f"{q} : {b}")
    
    @classmethod
    def single_match(self, val, other):
        a = prime_check(int( str(val) + str(other) ))[0]
        b = prime_check(int( str(other) + str(val) ))[0]
        return (a and b)
    
    def __len__(self):
        return len(self.indicies)
    
    def __eq__(self, other):
        return self.getIndicies() == other.getIndicies()
    
    def __str__(self):
        return str(self.indicies) + " : " + str(self.primes)
    
    def __repr__(self):
        return str(self.indicies) + " : " + str(self.primes) + " : (" + str(self.val()) + ")"
    

class Frontier():
    def __init__(self, target=5):
        self.frontier = {}
        self.keys = []
        self.target = 5
    
    def initPSETs(self, size):
        rem1 = []
        rem2 = []
        x = 1
        while len(rem1) < size or len(rem2) < size:
            v = prime_stack.val(x)
            if v % 3 == 0 or v % 3 == 1:
                rem1.append(x)
            if v % 3 == 0 or v % 3 == 2:
                rem2.append(x)
            x += 1
        
        # print("rems decided:", rem1, rem2)
        self.new(PrimeSet(inds=rem1))
        self.new(PrimeSet(inds=rem2))
        # print("frontier:", self)

        
    
    def remove(self):
        # print("before removing:", self.keys, self.frontier)
        out = self.frontier[self.keys[0]].pop(0)
        if not self.frontier[self.keys[0]]:
            del self.frontier[self.keys[0]]
            del self.keys[0]
        # print("after:", self.keys, self.frontier)
        return out
        
    
    def __len__(self):
        return sum([len(self.frontier[k]) for k in self.frontier])
    
    def get(self, val, default):
        return self.frontier.get(val, default)
    
    def new(self, elem):
        """
        adds elem to the frontier (which belongs to the PrimeSet class)
        """
        # print("trying to add", elem)
        # print("before adding:", len(self.keys))
        d = self.target - len(elem)
        v = prime_stack.val(elem.getIndicies()[-1])
        s = int(elem.val() + (d) * v + (d) * (20 + (d-1)*10) / 2)
        if len(self.get(s, [])) == 0:
            # print("dict cell", s, "is empty:", self.get(s, []), self.frontier.get(s, []))
            self.frontier[s] = [elem]
            self.newKey(s)
            return
            # print("not empty")
        elif elem in self.frontier[s]:
            return
        index = closest([len(el) for el in self.frontier[s]], len(elem))
        p = self.frontier[s]
        p = p[:index] + [elem] + p[index:]
        self.frontier[s] = p
        # print("came till here!")
        # self.newKey(s)
        
        # print("after adding:", len(self.keys))
    
    def newKey(self, s):
        if not len(self.keys):
            # print("in here")
            self.keys.append(s)
        else:
            cl = closest(self.keys, s)
            self.keys = self.keys[:cl] + [s] + self.keys[cl:]
    
    def __str__(self):
        return str(self.frontier)
    
    def within(self, x):
        s = x.val()
        return x in self.frontier.get(s, [])


class DPTable():
    def __init__(self):
        self.connections = {}
    
    def val(self, elem):
        return deepcopy(self.connections.get(elem, [[], 0]))
    
    def compatible(self, elem, other):
        val = self.connections.get(elem, None)
        if val is None:
            return True
        if other in val[0] or other > val[1]:
            return True
        return False
    
    def entry(self, elem, valid):
        if elem not in self.connections:
            self.connections[elem] = [[valid], valid]
        else:
            valids = self.connections[elem][0]
            if valids:
                best = lin_closest(valids, valid)
                valids = valids[:best] + [valid] + valids[best:]
            else:
                valids = [valid]
            self.connections[elem][0] = valids
            if valid > self.invalidMarker(elem):
                self.connections[elem][1] = valid
    
    def isMatch(self, elem, match):
        return match in self.connections.get(elem, [[], 0])[0]
    
    def isInvalid(self, elem, ques):
        val = self.connections.get(elem, None)
        if val is None:
            return False
        if (not ques in val[0]) and ques < val[1]:
            return True
        return False
    
    def evaluate(self, elem, other):
        if self.isInvalid(elem, other):
            return False
        elif self.isMatch(elem, other):
            return True
        return None
    
    def invalidMarker(self, elem):
        """
        returns the last recorded invalid index for elem
        """
        val = self.connections.get(elem, None)
        if val is not None:
            return val[1]
        return 0
    
    def validsFor(self, elem):
        """
        returns the list of valid prime indicies for a specific index
        """
        return self.connections.get(elem, [[]])[0]
    
    def incompat(self, elem, invalid):
        """
        method to add an invalid entry into the dp_tables
        """
        if elem not in self.connections:
            self.connections[elem] = [[], invalid]
        elif self.invalidMarker(elem) < invalid:
            self.connections[elem][1] = invalid
    
    def show(self):
        print("~dp-table")
        for key, val in self.connections.items():
            print(key, prime_stack.val(key), val)

def lin_closest(elems, elem):
    """
    returns the index of the least greatest element in elems to elem
    """
    for i in range(len(elems)):
        if elems[i] > elem:
            return i
    return len(elems)



def main(n, till=1):
    """
    Finds the least sum prime pair set of size n
    """
    
    queue = Frontier()
    queue.initPSETs(2)
    print(queue)

    sols = []

    while len(queue):

        state = queue.remove()

        print("currently exploring:", repr(state), "frontier:", len(queue))
        print(queue)
        # print(state.getPrimes(), repr(state))
        # if state.getPrimes() == [3, 7, 109]:
        #     print("FOUND it, isPET?:", state.isPSET())
        #     exit()
        # print("frontier:", queue)
        # dp_tables.show()
        solved = False
        if state.isPSET():  # Solved?
            solved = True
            if len(state) == n:
                sols.append(state)
            if len(sols) >= till:
                return sols
        
        # otherwise append the next steps into the Frontier
        for act in state.actions(sol=solved):
            possible = state.result(act)
            if not queue.within(possible):
                queue.new(possible)
                print("ADDED", possible)
    
    return False





if __name__ == "__main__":
    # print(closest([], 1))

    prime_stack = AllPrimes()
    dp_tables = [DPTable(), DPTable()]

    # x = PrimeSet(inds=[1, 4, 7, 9])

    # f = Frontier()
    # for val in x.actions():
    #     val = x.result(val)
    #     f.new(val)
    
    # print(f)
    # print(x, x.isPSET())

    chicken = main(5)
    print(chicken)
    # chicken.elabPSET()
    
