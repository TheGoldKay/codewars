def is_square(x)
  x >= 0 and x.abs == (x.abs**0.5)**2
end

num = ARGV[0].to_i
puts is_square(num)
