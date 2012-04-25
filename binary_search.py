NOT_FOUND = "Key not found"

def binarys(array, num, minlen, maxlen):
    key = (minlen+maxlen)/2
    if num == array[key]:
        return key
    elif num<array[key]:
        return binarys(array, num, minlen, key-1)
    elif num>array[key]:
        return binarys(array, num, minlen+1, key)
    else:
        return NOT_FOUND


A = [1,2,3,10,100,1100, 9999, 112330]

result = binarys(A, 9999, 1, len(A))

print result
