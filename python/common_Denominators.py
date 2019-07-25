def gcd(a, b):

    while b:
        a, b = b, a%b
    return a

def convertFracts(lst):

    if len(lst) == 0 or len(lst) == 1:
        return lst

    else:
        denoms =list([y for x,y in lst])
        lcm = denoms[0]
        for i in denoms[1:]:
            lcm = lcm*i//gcd(lcm, i)
        return [[int((x*(lcm//y))),int(lcm)] for x,y in lst]