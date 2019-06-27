def duplicate_encode(word):
    encoded = ""
    for i in word:
        if word.lower().count(i.lower()) > 1:
            encoded += ")"
        else:
            encoded += "("

    return encoded