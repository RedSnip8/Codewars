def to_nato(words):
    nato = [
         'Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu'
    ]

    words = words.replace(' ', '')
    words = words.lower()

    nato_words = ''

    for letter in words:
        if nato_words == '' and (ord(letter)-97) >= 0:
            nato_words = nato[ord(letter)-97]

        elif nato_words == '' and (ord(letter)-97) <= 0:
            nato_words = letter

        elif (ord(letter)-97) >= 0:
            nato_words = nato_words + ' ' + nato[ord(letter)-97]
        else:
            nato_words = nato_words + ' ' + letter

    return nato_words