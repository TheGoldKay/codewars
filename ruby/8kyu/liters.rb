def liters time 
    (time*0.5).floor # same as (time*0.5).to_i
end
# time.div(2) -> integer result, different from time.fdiv(2) floor result
# time.to_i / 2 -> integer division