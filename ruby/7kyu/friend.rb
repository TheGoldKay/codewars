def friend friends
  friends.select{|f| f.size == 4}
end 
