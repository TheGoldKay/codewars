def find_next_square(sq)
  root = sq**0.5
  if root * root == sq then 
    (root+1)**2
  else 
    -1 
  end 
end

