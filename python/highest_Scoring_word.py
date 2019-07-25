def high(x):
    highest_word = ''
    highest_total = 0

    for word in x.split(' '):
        current_total = 0
        for letter in word:
          current_total += ord(letter)-96
        if current_total > highest_total:
            highest_total = current_total
            highest_word = word

    return highest_word