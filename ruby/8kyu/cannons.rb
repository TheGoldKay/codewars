def cannons_ready(gunners)
    gunners.each do |crew, answers|
        if answers == "nay"
            return "Shiver me timbers!"
        end
    end
    "Fire!"
end
cannons_ready2 = -> (gunners) { gunners.has_value?('nay') ? 'Shiver me timbers!' : 'Fire!'}
b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}
puts cannons_ready2.call(b)
