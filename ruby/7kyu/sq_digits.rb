def square_digits num
  out = ""
  while num > 0
    d = num % 10
    out.insert(0, (d**2).to_s)
    num = num / 10
  end 
  puts num
  out
end

puts square_digits 3212

