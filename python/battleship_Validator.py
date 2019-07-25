def find_four():


def find_threes():


def find_twos():


def find_ones():


def validate_battlefield(battleField):

    # Flatten the battle field to a single array
    flat_field = [cell for row in battleField for cell in row]

    if len(flat_field) != 20:
        return False

    # set flat list to be the index of all occupied cells
    flat_index = [i for i,x in enumerate(flat_field) if x == 1]

    # loop through list of indexes comparing each cell to its neighbor with
    # special cases for corners [0,9,90,99] and each side sets. the
    # add each found pairs to a set.


    for cell in flat_index:
        if cell == 0:
            if







battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


print(validate_battlefield(battleField))