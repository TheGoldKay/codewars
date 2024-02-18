def hotpo n, count=0
    if n == 1
        count
    else
        hotpo n.even? ? n / 2 : 3 * n + 1, count + 1
    end
end