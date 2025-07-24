# A trucatable prime is such that when its digits are
# truncated in a left to right fashion or a right to left fashion,
# (but not both), the remainder continues to be a prime.

from prime_checker import prime_check


def truncate(num, left_to_right=True):
    if not left_to_right:
        return int(str(num)[:-1])
    return int(str(num)[1:])


def is_truncatable_prime(num, left_to_right=True):
    while len(str(num)) > 1:
        test = prime_check(num)
        if not test[0]:
            return test
        num = truncate(num, left_to_right)
    return True, True


class TrucatablePrime():
    def __init__(self, p, last_stable, first_unstable, is_stable):
        """
        p is ideally a prime.
        unstable is the value of the first unstable node
        which aims to become stable by yielding a stable
        through attaining more digits 
        """
        self.val = p
        self.last_stable = last_stable
        self.unstable = first_unstable
        self.is_stable = is_stable
    
    def set_stable(self, stable):
        self.last_stable = stable
    
    def stable(self):
        return self.is_stable

    def set_unstable(self, unstable):
        self.unstable = unstable
    
    def get_stable(self):
        return self.last_stable

    def get_unstable(self):
        return self.unstable
    
    def num(self):
        return self.val
    

class StackFrontier():
    def __init__(self, f):
        if not f:
            f = []
        self.frontier = f
    
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


    
    def add(self, val):
        f = self.frontier
        f.append(val)
        self.updateFrontier(f)
    
    def has_stuff(self):
        return bool(self.getFrontier())

    def __str__(self):
        return self.getFrontier()


def actions(state):
    """
    returns the possible actions given the current state
    """
    actions = [3, 7, 9, 1]
    if str(state).count(str(7)) == 2:
        del actions[actions.index(7)]
    return actions


def eval_action(state, action):
    """
    returns 3 possible values, [0, 1, 2]
    """
    if str(state)[-1] == action and len(str(state)) > 1:
        return 0
    elif action == 9 or action == 1:
        return 0
    elif int(str(state)[-1]) % 3 == action % 3 == 0:
        return 0
    else:
        return 1


def create_t_primes():
    t_primes = []
    frontier = StackFrontier([TrucatablePrime(i, i, None, True) for i in [2, 5, 3, 7]])
    while frontier.has_stuff():
        state = frontier.remove()
        # print("removed element", state.num())
        dead_end = True
        for action in actions(state.num()):
            # print("\taction", action)
            proposed = int(str(state.num()) + str(action))
            if prime_check(proposed)[0]:
                # print(proposed, "is a prime")
                evaluation = eval_action(state.num(), action)
                # print("evaluation was:", evaluation)
                dead_end = False
                new = TrucatablePrime(proposed, state.get_stable(), state.get_unstable(), is_stable=False)
                if evaluation == 1:
                    new.set_stable(new)
                    new.set_unstable(None)
                    new.is_stable = True
                    t_primes.append(new.num())
                elif state.stable():
                    new.set_stable(state)
                    new.set_unstable(new)
                    new.is_stable = False
                frontier.add(new)
                # print("added", new.num())
        if dead_end:
            if not state.get_unstable() is None:
                frontier.remove_from_root(state.get_unstable().num())
    return t_primes

