def draw_stairs n 
    s = ""
    n.times do |i|
        if i + 1 == n 
            s << "I"
        else 
            s << "I\n " + " " * i
        end
    end
    return s
end
