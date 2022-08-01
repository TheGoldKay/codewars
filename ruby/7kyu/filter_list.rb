def filter_list l
  l.select{|elem| elem.instance_of? Integer}
end
