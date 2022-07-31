def descending_order n
  n.to_s.chars.sort.join.reverse.to_i
end

puts descending_order 123

