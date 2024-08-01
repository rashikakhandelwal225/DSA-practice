from collections import Counter
def checkIfExist(arr):
    hashmap = Counter(arr)

    for key in hashmap:
        if key == 0 and hashmap[key] > 1:
            return True
        elif key != 0 and key * 2 in hashmap:
            return True
    return False

arr =[-2,0,10,-19,4,6,-8]
print(checkIfExist(arr))