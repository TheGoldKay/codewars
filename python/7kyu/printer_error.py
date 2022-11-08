def printer_error(s):
  count = 0
  for c in s:
    ascii = ord(c)
    if not (97 <= ascii <= 109):
      count += 1
  return f"{str(count)}/{len(s)}"


s="aaabbbbhaijjjm"
ans=printer_error(s)
assert ans == "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
ans=printer_error(s)
assert ans == "8/22"