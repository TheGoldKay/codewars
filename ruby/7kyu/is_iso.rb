def is_isogram string
  s = string.downcase
  s.each_char{|c|
    if s.count(c) > 1 then 
      return false 
    end 
  }
  return true
end
