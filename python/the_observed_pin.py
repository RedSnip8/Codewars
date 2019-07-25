import itertools

'''
Can you help us to find all those variations? It would be nice to have a function, that
returns a list of all variations for an observed PIN with a length of 1 to 8 digits.
We could name the function get_pins. But please note that all PINs, the observed one and also the results,
 must be strings, because of potentially leading '0's. We already prepared some test cases for you.

[1][2][3]
[4][5][6]
[7][8][9]
[*][0][>]

'''


def get_pins(observed):
    '''TODO: This is your job, detective!'''
    number_perms = {
        '1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'], '8': ['5', '7', '8', '9', '0'], '9': ['6', '8', '9'], '0': ['0', '8']
    }

    options = []
    final_permuations = []

    for i in observed:
        options.append(number_perms[i])

    for i in list(itertools.product(*options)):
        final_permuations.append(''.join(i))

    return final_permuations


expectations = [('8', ['5', '7', '8', '9', '0']),
                ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398", "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359", "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"])]

for tup in expectations:
    get_pins(tup[0])
