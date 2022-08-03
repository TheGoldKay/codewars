$map = {"A" => "T", "T" => "A", "C" => "G", "G" => "C"} # global variable

def DNA_strand(dna)
	strip = ""
	dna.each_char{ |s|
		strip += $map[s] # to access it must use '$'
	}
	strip
end 

dna = "ATTGC"

puts DNA_strand(dna)
