def pass_or_fail harmony
    arr = []
    harmony.map!{|item| item.split(" ")}
    (0..3).each do |first|
        ((first+1)..3).each do |second|
            pairs = []
            harmony.each do |notes|
                if notes[first] == notes[second]
                    pairs.push([notes[first], notes[second]])
                end
            end
            arr.push(pairs) if pairs.length != 0
        end
    end
    arr
end

def show arr
    print arr 
    print "\t"
    puts 
end

h = [
    'do re mi fa' ,
    'mi fa sol do' ,
    'fa ti fa ti' ,
    'fa do fa mi' , 
    ]

show pass_or_fail h