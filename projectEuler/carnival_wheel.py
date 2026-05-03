

def main():
    n = input()
    
    for i in range(int(n)):
        try:
            l, a, b = [int(k) for k in input("blah\n").split(" ")]
        except Exception as e:
            print(e)

        if b % l == 0:
            return 0
        
        print("here")
        
        m = a
        explored = [m]
        spins = 1
        while True:
            # print("spin", spins)
            val = (a + b * spins) % l
            # print("this is val:", val)
            if val in explored:
                break
            else:
                explored.append(val)
            if val > m:
                m = val
            spins += 1
        print(m)
    
    return "here why"


main()
