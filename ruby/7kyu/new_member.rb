def open_or_senior(data)
  pos = []
  data.each{|d|
    if d[0] >= 55 and d[1] > 7 then 
      pos.append("Senior")
    else 
      pos.append("Open")
    end 
  }
  pos
end
