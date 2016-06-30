import sys

PRIME_INIT = 2200
PRIME_INIT_OFFSET = 19423


try:
    f = open(sys.argv[1], 'r')
except:
    print "No es pot obrir el fitxer"
    #exit()

try:
    n = int(f.readline())
except:
    print "No es pot llegir el numero"
    # exit()


# PRIME = n; # hasta n


p_init = []

p_init.append(2)
p_init.append(3)


pp = 2  # prime pointer
num = 5  # current cap

while pp < PRIME_INIT:  # index del primer
    i = 1
    while p_init[i] * p_init[i] <= num:
        if num % p_init[i] == 0:
            break
        i+=1

    if p_init[i] * p_init[i] > num:
        pp+=1
        p_init.append(num)
        # print num  # is prime
        if num > n:
            print p_init[-2]  # or write to file
            print ""
            exit(0)

    num+=2

# increments de 3 en tres del valor actual

# print pp  # valor actual, index actual
pp = PRIME_INIT_OFFSET
candidates = []
while pp < n:
    # lookup for more


    # each 30 items there might be 8 candidates

    # candidate1 = pp + 4
    # candidate2 = pp + 6
    # candidate3 = pp + 10
    # candidate4 = pp + 16
    # candidate5 = pp + 18
    # candidate6 = pp + 24
    # candidate7 = pp + 28
    # candidate8 = pp + 30

    candidates = [pp+4, pp+6, pp+10, pp+16, pp+18, pp+24, pp+28, pp+30]

    for item in candidates:
        isPrime = 1
        i = 3  # index of the first to check
        while p_init[i] * p_init[i] < item:
            # if item >= n:
            #     print p_init[-1]
            #     exit()
            if item % p_init[i] == 0:
                isPrime = 0
                break
            i+=1

        if isPrime:
            p_init.append(item)
            # print item

    # offset at each iteration

    pp+=30

idx = -1
while p_init[idx] > n:
    # print p_init[idx]
    if p_init[idx] <= n:
        break
    idx-=1

print p_init[idx]  # this is the result
print ""
f.close()



# python is too slow for this.





# ara si en el fitxer hiha un valor mes gran que la llista anterior, apr





# void paco4PrimeDynamicBlockForward


# xD



