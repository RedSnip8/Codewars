def squared_factors(x):
    factors = []
    for i in range(1, (round(x**(1/2))+1)):
        if x % i == 0 and x/i != i:
            other_factor = x/i
            factors.append(i**2)
            factors.append(other_factor**2)
        elif x/i == i:
            factors.append(i**2)
    return factors

def is_square_sum(x, square_number = False):
    if x == 1:
        square_number = True
        return square_number
    else:
        if x**(1/2) == round(x**(1/2)):
            square_number = True
            return square_number
        return square_number


def list_squared(m, n):
    square_divsor_sum = []

    for i in range(m, n+1):
        summed_factors = int(sum(squared_factors(i)))
        if is_square_sum(summed_factors) == True:
            square_divsor_sum.append([i, summed_factors])
    return(square_divsor_sum)

    1 month ago