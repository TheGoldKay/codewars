def elevator(left, right, call)
    (right - call).abs <= (left - call).abs ? "right": "left"
end