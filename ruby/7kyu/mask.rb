def maskify cc
  if cc.size <= 4 then 
    return cc 
  end 
  hide = ""
  (cc.size - 4).times do 
    hide += "#"
  end 
  return "#{hide}#{cc[cc.size - 4, cc.size]}"
end 

cc = "4556364607935616"
puts maskify cc
