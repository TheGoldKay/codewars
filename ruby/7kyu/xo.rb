def XO str
  s = str.downcase # str.downcase! update in place
  s.count('x') == s.count('o')
end 
