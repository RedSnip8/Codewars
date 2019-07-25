def zero(y= None):
    x = 0
    return x if y == None else eval(y)

def one(y = None):
    x = 1
    return x if y == None else eval(y)

def two(y = None):
    x = 2
    return x if y == None else eval(y)

def three(y = None):
    x = 3
    return x if y == None else eval(y)

def four(y = None):
    x = 4
    return x if y == None else eval(y)

def five(y = None):
    x = 5
    return x if y == None else eval(y)

def six(y = None):
    x = 6
    return x if y == None else eval(y)

def seven(y = None):
    x = 7
    return x if y == None else eval(y)

def eight(y = None):
    x = 8
    return x if y == None else eval(y)

def nine(y = None):
    x = 9
    return x if y == None else eval(y)


def plus(num):
    return 'x + ' + str(num)

def minus(num):
    return 'x - ' + str(num)

def times(num):
    print("in times")
    return  'x *  ' + str(num)

def divided_by(num):
    return 'x // ' + str(num) if num != 0 else '0'