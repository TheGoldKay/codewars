def accum(s)
  i = 0
  out = ""
  s.each_char{ |c|
    ans = c.upcase
    ans += c.downcase * i
    i += 1
    out += ans + "-"
  }
  out.chomp("-")
end
