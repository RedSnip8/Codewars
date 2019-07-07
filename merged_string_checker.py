'''
At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 should be in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
'''


def in_order(word, fragment):
    indexes = [word.find(letter) for letter in fragment]
    return indexes == sorted(indexes)


def in_word(word, fragment):
    for letter in fragment:
        if letter not in word:
            return False
    return True


def is_merge(s, part1, part2):
    if len(part1 + part2) == len(s):
        if in_word(s, part1) and in_word(s, part2):
            if in_order(s, part1) and in_order(s, part2):
                return True

    return False


print(is_merge('codewars', 'code', 'wars'))
print(is_merge('codewars', 'cdw', 'oears'))
print(is_merge('codewars', 'cod', 'wars'))
