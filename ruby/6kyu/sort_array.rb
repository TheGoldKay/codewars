def sort_array arr
  odds = []
  index = []
  arr.each_with_index {|num, i|
    if num%2 == 1 then 
      odds.push(num)
      index.push(i)
    end 
  }
  odds.sort!
  odds.each_with_index {|num, i| 
    arr[index[i]] = num 
  }
  arr
end 

print sort_array [5, 8, 6, 3, 4]
puts
print sort_array [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
puts
  
