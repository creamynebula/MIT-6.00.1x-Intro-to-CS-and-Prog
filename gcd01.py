def gcdIter(a, b):
    guess = a if a < b else b
    while guess > 1:
        if (a%guess == 0) and (b%guess == 0):
            return guess
        else:
            guess -= 1
    return guess

print(gcdIter(6,12))
print(gcdIter(9,12))

def gcdRecur(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else
        return gcdRecur(b, a%b)