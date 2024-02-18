def letter(item)
    if item.ord >= "A".ord && item.ord <= "Z".ord 
        return "uppercase"
    elsif item.ord >= "a".ord && item.ord <= "z".ord 
        return "lowercase"
    else
        return "not letter"
    end
end

def same_case(a, b)
    a_case, b_case = letter(a), letter(b)
    if a_case == "not letter" || b_case == "not letter"
        return -1
    elsif a_case == b_case 
        return 1
    else
        return 0
    end
end
