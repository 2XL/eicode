import sys
try:
    dictionary = {}
    f = open(sys.argv[1], 'r')
    words = int(f.readline())
    words_list = []
    while words > 0:
        words-=1
        words_list.append(f.readline().rstrip())
    print words_list

    rows, cols = f.readline().split(' ')
    sopa_rows = int(rows)
    sopa_cols = int(cols)
    print sopa_rows, sopa_cols
    w, h = sopa_rows, sopa_cols
    Matrix = [[0 for x in range(w)] for y in range(h)]

    item_row = 0
    while True:
        # Matrix[x][y]
        line = f.readline().strip()
        if line == "":
            break
        else:
            item_col = 0
            for item in line.split(' '):
                Matrix[item_row][item_col] = item
                item_col+=1
                # print item_col, item
        item_row += 1

    # print Matrix
    print ''.join(Matrix[1])

    candidateRowLeft = []
    candidateRowRight = []
    for x in range(0, sopa_rows):
        candidateRowRight.append(''.join(Matrix[x]))
        candidateRowLeft.append(''.join(reversed(Matrix[x])))
        for y in range(0, sopa_cols):



    candidateColDown = []
    candidateColUp = []


    candidateNE = []
    candidateNW = []
    candidateSE = []
    candidateSW = []

    megaList = [candidateRowLeft, candidateRowRight,
                candidateColUp, candidateColDown,
                candidateNE, candidateNW, candidateSE, candidateSW]

	# instead of loading these arrays... just shift and check...

    while True:
        print "while wordlist not empty"
        for lists in megaList:
            for line in lists:
                for word in words_list:
                    if word in line:
                        print "Found {} > {} > {} ".format(word, line.index(word), line)
                        # add word in found, remove from checking list

















    # try:
    #     while True:
    #         dictionary[int(f.readline())] = 1
    # except:
    #     # print "finish reading file"
    #     pass
    # finally:
    #     # sord keys
    #     # print "sort keys and get key by index"
    #     # print "keys: ", \
    #     print dictionary.keys()[k-1]
    #     print ""
except Exception as ex:
    print ex.message

finally:
    print "Dummy Solution "
