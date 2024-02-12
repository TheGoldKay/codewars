def animals(heads, legs)
    chickens = 2 * heads - legs / 2
    cows = heads - chickens
    puts "heads = #{heads} legs = #{legs}"
    puts "chickens = #{chickens} cows = #{cows}"
    if heads <= 0 || legs <= 0 || chickens < 0 || cows < 0 || chickens.class == Float || chickens + cows == 0
      return "No solutions"
    else
      return [chickens, cows]
    end
end