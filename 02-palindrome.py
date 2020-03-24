# a string tem de estar ordenada
def isIn(char, aStr):
    tamanho = len(aStr)
    if tamanho == 0:
        return False
    elif tamanho == 1:
        if char == aStr[0]:
            return True
        else:
            return False
    meio = tamanho // 2
    if aStr[meio] == char:
        return True
    else:
        if char < aStr[meio]:
            return isIn(char, aStr[0:meio])
        else:
            return isIn(char, aStr[(meio + 1):tamanho])

print(isIn('a','bola'))
print(isIn('a','LOL'))
print(isIn('a','how do you turn this on?'))
print(isIn('a','my last thoughts are of unbearable pain'))