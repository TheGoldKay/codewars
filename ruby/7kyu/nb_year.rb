def nb_year p0, percent, aug, p
  y = 0
  actual = p0
  percent *= 0.01
  while actual < p do 
    actual += (actual * percent).floor + aug
    y += 1
  end 
  y 
end 
