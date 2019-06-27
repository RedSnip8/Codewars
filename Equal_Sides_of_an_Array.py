def find_even_index(arr):
    index = 0
    front = []
    back = arr[1::]
    not_solved = True

    while not_solved:

        if sum(front) == sum(back):
            not_solved = False
            return index

        elif len(back)<=0:
            return -1

        else:
            front.append(arr[index])
            index += 1
            del back[0]