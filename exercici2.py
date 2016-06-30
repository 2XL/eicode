import sys

def main():
    try:
        f = open(sys.argv[1], 'r')
    except:
        print "No es pot obrir el fitxer"
        exit()

    try:
        n = int(f.readline())
    except:
        print "No es pot llegir el numero"
        exit()

    period = n

    initial = 1
    maturing = 0
    mature = 0
    total = 0
    idx = 0
    while period > idx:
        maturing = initial
        initial = mature
        mature = mature + maturing
        # print "{} min => {}".format(idx, total)
        idx+=1
    total = initial + maturing
    print total
    print ""
    f.close()


if __name__ == "__main__":
    main()


# print quadrat
