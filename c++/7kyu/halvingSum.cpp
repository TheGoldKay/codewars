unsigned halving_sum(unsigned n) {
    int half = n / 2;
    unsigned sum = n;
    while (half){
      sum += half;
      half = half / 2;
    }
    return sum;
}
