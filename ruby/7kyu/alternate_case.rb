class String
  def toJadenCase
    self.split(" ").map{|l| l.capitalize()}.join(" ")
  end
end

str = "this is just As test"

puts str.toJadenCase()
