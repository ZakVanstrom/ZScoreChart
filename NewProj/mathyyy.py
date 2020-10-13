import math

#
def doCalc(n):
    # a = 1/(2pi)
    a = 0.3989422804
    e = 2.71828182846
    exp = -(n ** 2) / 2
    b = e ** exp
    return a * b

def findCumToN(n):
    ans = 0
    val = n * 100
    if( val < 0):
        for x in range(0, -val):
            calc = doCalc(x / 10000)
            ans += calc / 10000
        ans = .5 - ans
    else:
        for x in range(0, val):
            calc = doCalc(x / 10000)
            ans += calc / 10000
        ans += .5
    return ans

nList = []
for x in range(-400, 400):
    val = findCumToN(x)
    nList.append(findCumToN(x))
    print(val)
