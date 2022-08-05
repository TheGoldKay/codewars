def sum_two_smallest_numbers numbers
  numbers.sort!
  numbers[0..1].sum
end 

arr = [19, 5, 42, 2, 77]
puts sum_two_smallest_numbers arr
