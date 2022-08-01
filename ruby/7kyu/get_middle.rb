def get_middle(s)
  puts s
  ln = s.length
  if ln%2 == 0 then 
    ln = ln / 2
    return s[ln-1] + s[ln]
  end 
  return s[ln/2]
end
