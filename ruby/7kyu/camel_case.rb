def to_camel_case str
  s = str.split '-'
  if str.include? '-' then 
    s = str.split '-'
  else 
    s = str.split '_'
  end 
  news = s[0]
  s[1..-1].each {|word|
    word[0] = word[0].upcase
    news += word
  }
  news 
end

puts to_camel_case "The-Stealth-Warrior"