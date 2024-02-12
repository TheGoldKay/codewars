def square_or_square_root arr 
    narr = []
    arr.each do |num|
        sqrt = Math.sqrt(num).to_i
        narr << (sqrt**2 == num ? sqrt : num**2)
    end
    narr
end
