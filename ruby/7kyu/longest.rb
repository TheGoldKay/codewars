def longest s1, s2
  (s1 + s2).chars.uniq.sort.join
end 

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

puts longest a, b
