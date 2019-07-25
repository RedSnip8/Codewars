def to_nato(words)

  nato = {
    'A' => 'Alfa', 'B' => 'Bravo', 'C' => 'Charlie', 'D' => 'Delta', 'E' =>'Echo', 'F' =>'Foxtrot',
    'G' => 'Golf', 'H' => 'Hotel', 'I' => 'India', 'J' => 'Juliett', 'K' => 'Kilo', 'L' => 'Lima', 'M' => 'Mike',
    'N' => 'November', 'O' => 'Oscar', 'P' => 'Papa', 'Q' => 'Quebec', 'R' => 'Romeo', 'S' => 'Sierra', 'T' => 'Tango',
    'U' => 'Uniform', 'V' => 'Victor', 'W' => 'Whiskey', 'X' => 'Xray', 'Y' => 'Yankee', 'Z' => 'Zulu'
  }

nato_words = ''

words.delete!(' ')
words.upcase!


words.split('').each { |letter| !letter.match(/[^A-Za-z]/)? (nato_words << ' ' + nato[letter]) : (nato_words << ' ' + letter)  }

nato_words.strip!
end

puts(to_nato('If you can read'))