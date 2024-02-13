def monkey_count n
    Array.new(n){|i| i+1} # same as (1..n).to_a
end
n = 10
puts (monkey_count n) == (1..n).to_a