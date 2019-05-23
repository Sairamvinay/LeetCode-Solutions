'''
[1,2,3]
find min(moves) which is just adding 1 to any of the n-1 elements of array to get an
array such that all elements are equal in this array
i.e
pick 0,1 to get [2,3,3]
pick 0,1 to get [3,4,3]
pick 0,2 to get [4,4,4]
'''


def move(L):

 
    move = 0
    S = sum(L)
    m = min(L)
    while (sum(L) - (min(L) * len(L))) != 0:
        move += 1
        M = L.index(max(L))
        for i in range(len(L)):
            if i != M:
                L[i] += 1

            else:
                pass

        #print L

    return (S - (m * len(L)))

print move([10,11,8,9,7])
