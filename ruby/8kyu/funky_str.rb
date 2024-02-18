class String
    def val
        self.split("").count 
    end
end
 
def solution(a, b)
  a.val > b.val ? "#{b}#{a}#{b}" : "#{a}#{b}#{a}"
end
#a, b = ARGV
puts solution *ARGV