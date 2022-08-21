def over_the_road(address, n)
  if address%2 != 0 then 
    odd_pos = (address + 1) / 2
    2 * n - (odd_pos - 1) * 2
  else 
    even_pos = address / 2
    (2 * n - 1) - (even_pos - 1) * 2
  end 
end
