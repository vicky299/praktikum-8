buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}


def sortByValue():
    sortedByValueBuah= sorted(buah.items(),reverse=True, key = lambda t:t[0])
    print (sortedByValueBuah)
