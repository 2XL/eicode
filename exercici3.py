import sys
try:
    dictionary = {}
    f = open(sys.argv[1], 'r')
    k = int(f.readline())
    try:
        while True:
            dictionary[int(f.readline())] = 1
    except:
        # print "finish reading file"
        pass
    finally:
        # sord keys
        # print "sort keys and get key by index"
        # print "keys: ", \
        # print dictionary.keys()[k-1]
        keys_list = dictionary.keys()
        keys_list.sort()  # # [k-1]
        print keys_list[k-1]
        print ""
    f.close()
except Exception as ex:
    print ex.message





