def expression_matter(a,b,c)
    arr = []
    arr << a+b+c 
    arr << (a+b)*c
    arr << a*(b+c)  
    arr << a*b*c
    arr.max
end