// Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10^n.


int countNumbersWithUniqueDigits(int n){
    if (n < 2) {
        return 1 + 9 * n;
    }
    int ndigits = 9;
    int increm = ndigits;
    int x = n;
    int res = 10;
    while (x > 1) {
        increm *= ndigits;
        res += increm;
        ndigits -= 1;
        x -= 1;
    }
    return res;
}
