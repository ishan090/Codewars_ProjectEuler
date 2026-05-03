
from prime_checker import prime_check
from prime_generator import gen_indefinite, next_prime
from problem51 import bin_search

conflicts = {}

def actions(p_set, primes, prime_gen, fixed=0):
    """Given a prime set, returns the possible actions
    assumes all values of the p_set to be congruent modulo 3 (expect 3 itself)"""
    # print("here's the p_set", p_set)
    options = []
    if p_set[0] % 3 == 0:
        mod3 = p_set[1] % 3
    else:
        mod3 = p_set[0] % 3
    # print("initial pset", p_set)
    for i in range(fixed, len(p_set)):
        # print("prime is:", i, p_set[i])
        p_index = bin_search(p_set[i], primes)[1]
        
        p_index += 1
        if p_index >= len(primes) - 1:
            primes.append(next(prime_gen))
        found = False
        while primes[p_index] not in p_set[i+1:]:
            # print("trying", primes[p_index])
            if conflicts.get(primes[p_index], 0) == 0:
                conflicts[primes[p_index]] = [] 
            if (primes[p_index] % 3 == 0 or primes[p_index] % 3 == mod3) and primes[p_index] not in [2, 5] and not any([bin_search(x, conflicts[primes[p_index]])[0] for x in p_set[:i]+p_set[i+1:]]):
                # print("soething here:", i, p_set[i])
                for x in p_set[:i] + p_set[i+1:]:
                    # print("None or What?", conflicts.get(primes[p_index], None))
                    if check_concs(x, primes[p_index]):
                        # print("inside")
                        val = primes[p_index]
                        # print("found val:", val)
                        found = True
                        break
                    # confs_x = conflicts[primes[p_index]]
                    # bin_index = bin_search(x, confs_x)[1]
                    # conflicts[primes[p_index]] = confs_x[:bin_index] + [x] + confs_x[bin_index+1:]
                if found:
                    break
            
            p_index += 1
            if p_index >= len(primes) - 1:
                primes.append(next(prime_gen))
        if not found:
            continue
        # print("out")
        # print(i, p_set, "WHSFHH")
        new = p_set[:]
        new[i] = val
        options.append((i, new))
    
    return options, primes, prime_gen



# p = gen_indefinite()
# next(p)
# ps = [next(p) for i in range(10)]

# print(actions([3, 7, 13], ps, p))


def check_concs(n, m):
    global conflicts
    if conflicts.get(n, []) == []:
        conflicts[n] = []
    bin_res = bin_search(n, conflicts[n])
    if bin_res[0]:
        return False
    # Otherwise, if the current move is thought to be undocumented
    res = prime_check(int(str(n)+str(m)))[0] and prime_check(int(str(m)+str(n)))[0]
    if not res:
        conflicts[n].insert(bin_res[1], m)
        return False
    return True


def new_status(i, links):
    i = str(i)
    return [j for j in links if i not in j] 


def check_all(p_set):
    out = []
    global conflicts
    for i in range(len(p_set)-1):
        for j in range(i+1, len(p_set)):
            # print("yoy", i, j, conflicts.get(p_set[j], []))
            # print("conflict", conflicts)
            there, esti = bin_search(p_set[i], conflicts.get(p_set[j], []))
            if not there:
                if not check_concs(p_set[i], p_set[j]):
                    # print("-> these guys no work", i, j, p_set[i], p_set[j])
                    out += [str(i)+str(j)]
                    # print("before:", conflicts)
                    if p_set[j] not in conflicts:
                        conflicts[p_set[j]] = []
                    if p_set[i] not in conflicts:
                        conflicts[p_set[i]] = []
                    conflicts[p_set[j]].insert(esti, p_set[i])
                    conflicts[p_set[i]].insert(bin_search(p_set[j], conflicts.get(p_set[i], []))[1], p_set[j])                    
                    # print(conflicts)
            else:
                out += [str(i)+str(j)]
    return out


def check_2(p_set, fixie=False):
    if fixie:
        j = p_set[-1]
        for i in p_set[:-1]:
            if not check_concs(j, i):
                return False
    else:
        for i in range(len(p_set)-1):
            for j in range(i+1, len(p_set)):
                if not check_concs(p_set[i], p_set[j]):
                    return False
    return True

(231, [19, 31, 181])

def prime_sets(size, prev=None, many=False, prime=None, primes=None, r=False, till=0, rp=False, req=0):
    sols = []
    if prime is None:
        prime = gen_indefinite()
        primes = []
        init1, init2 = [], []
        while len(init1) < size or len(init2) < size:
            n = next(prime)
            primes.append(n)
            if n in [2, 5]:
                continue
            if n % 3 == 0:
                init1.append(n)
                init2.append(n)
            elif n % 3 == 1 and len(init1) < size:
                init1.append(n)
            elif len(init2) < size:
                init2.append(n)
        frontier = list(sorted([(sum(b), b) for b in [init1, init2]]))
        prev = []
    else:
        frontier = []
        if many:
            for f in prev:
                # print(f, "this is p")
                there, l = bin_search(f[-1], primes)
                if l >= len(primes) - 1:
                    primes.append(next(prime))
                init1 = f + [primes[l+1]]
                frontier.append((sum(init1), init1))
            frontier = list(sorted(frontier))
            prev = prev[0]
            # print("this is the length of prev:", len(prev))
            # exit()
        else:
            there, l = bin_search(prev[-1], primes)
            if l >= len(primes) - 1:
                primes.append(next(prime))
            init1 = prev + [primes[l+1]]
            frontier = [(sum(init1), init1)]

    # n = next(prime)
    # init1.append(n)
    # primes.append(n)
    # print("done with inits")
    # print("inits:", init1, init2)
    # frontier = [((sum(init1), init1))]
    # prime_status = {}
    current = frontier[0]
    print("here are the first vals:", frontier)

    loops = 0
    while len(frontier) and (len(sols) < req or (till > 0 and current[0] < till)):
        loops += 1
        
        current = frontier.pop(0)
        if loops % 1000 == 0:
            print("loop", loops, "looking at:", current, "sols:", len(sols), "len prev", len(prev))

        if check_2(current[1], True if len(prev) > 0 else False):
            sols.append(current)

        # print("choosing action~")
        acts, primes, prime = actions(current[1], primes, prime, fixed=len(prev))
        # print("chosen:", acts)

        for action in acts:
            key = (sum(action[1]), action[1])
            closest = bin_search(key, frontier)[1]
            # prime_status[tuple(action[1])] = new_status(action[0], prime_status[tuple(current[1])])

            if closest >= len(frontier) or frontier[closest] != key:
                frontier = frontier[:closest] + [key] + frontier[closest:]
                # print("oh~ added something", len(frontier))
        # print("frontier:", frontier)
    
    if r:
        return sols
    elif rp:
        # print("HEREERE")
        # print([sols, primes])
        return sols, primes
    # print(sols)
    with open("size2.txt", "w") as save_out:
            save_out.write(str(sols))
    # mod1, mod2 = None, None
    # for val, j in sols:
    #     if j[1] % 3 == 1:
    #         mod1 = j
    #         break
    # for val, j in sols:
    #     if j[1] % 3 == 2:
    #         print("AYAYEYEY")
    #         mod2 = j
    #         break
    # print(mod1, mod2)
    sizes = [3, 4, 5]
    blah = [500, 50, 1]
    for si in range(3):
        k = [g[1] for g in sols]
        if si < 2:
            sols, p_s = prime_sets(sizes[si], prev=k, many=True, prime=prime, primes=primes, rp=True, req=blah[si])
        else:
            sols = prime_sets(sizes[si], prev=k, many=True, prime=prime, primes=primes, r=True, req=1)
        with open("size"+str(sizes[si])+".txt", "w") as save_out:
            save_out.write(str(sols))



if __name__ == "__main__":
    # print("here")
    print(prime_sets(2, till=6000))



