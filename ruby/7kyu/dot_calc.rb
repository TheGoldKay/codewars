def dot_calculator equation
  arr = equation.split(" ")
  n1, n2, op = arr[0], arr[2], arr[1]
  n1 = n1.count('.')
  n2 = n2.count('.')
  res = case op
    when '+'
      n1 + n2
    when '-'
      n1 - n2
    when '*'
      n1 * n2
    when '//'
      (n1 / n2).to_i
  end
  res * '.'
end
