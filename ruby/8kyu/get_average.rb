def get_average(marks)
    marks.reduce(0, &:+).div(marks.length)
end