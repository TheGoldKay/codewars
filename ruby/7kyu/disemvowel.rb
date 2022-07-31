str = "This website is for losers LOL!"

def disemvowel(str)
  vowels = "aAeEiIoOuU"
  news = ""
  str.each_char{ |c|
    if not vowels.include? c then 
      news += c
    end 
  }
  return news
end

puts disemvowel(str)
