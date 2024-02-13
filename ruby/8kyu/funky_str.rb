class String
    def value 
        self.split("").map(&:ord).sum 
    end
end

def solution(a, b)
  a.value > b.value ? "#{b}#{a}#{b}" : "#{a}#{b}#{a}"
end
#a, b = ARGV
puts solution *ARGV