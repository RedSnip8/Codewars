def is_square(x)
  is_square = false

  if x < 0
    is_square = false

  elsif x == 0
    is_square = true

  else
    square_root = x ** (0.5)
    square_root = square_root.round

    if x / square_root == square_root
      is_square = true

    else
      is_square = false

    end
  end
  is_square
end

puts is_square 4