##
# Funzioni utili liste
# @en Useful list functions
# - 
#   
# Gabriele Proietti Mattia - gabry.gabry@hotmail.it
# Università La Sapienza di Roma
# Facoltà di Ingegneria Informatica
# 2014/15
##

from random import randint

## Generates list of n random numbers
# @param n Number of elements
# @param minNum Min random number
# @param maxNum Max random number 
# @return List of random elements
def randomList(n = 10, minNum = 1, maxNum = 10) :
    'Return a list of n random numbers'
    l = []
    for i in range(n) :
        l.append(randint(minNum, maxNum))

    return l

## Generates list of n different random numbers
# @param n Number of elements
# @param minNum Min random number
# @param maxNum Max random number 
# @return List of random elements
def randomDiffList(n = 10, minNum = 1, maxNum = 10) :
    'Return a list of n different random numbers'
    l = []
    while len(l) < n :
        k = randint(minNum, maxNum)
        if k not in l :
            l.append(k)

    return l
    
