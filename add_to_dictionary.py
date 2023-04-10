def add_to_dictionary(alist, item):
    #third requirement
        for pos in range(len(alist)):
            if alist[pos] == item:
                return True
            else:
                if alist[pos] > item:
                    alist.insert(pos,item)
        return alist
