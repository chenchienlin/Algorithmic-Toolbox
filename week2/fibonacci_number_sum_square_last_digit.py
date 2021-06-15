def iter_fib_sum_square_last_digt(n):
    if n <= 1:
        return n
    a, b = 0, 1
    square_last_digit_sum = 0
    square_last_digit_sum += b
    for i in range(2, n+1):
        temp = b
        b = a + b
        a = temp
        
        b = b ** 2
        a = a ** 2
        
        b %= 10
        a %= 10
        
        square_last_digit_sum += b
    return square_last_digit_sum % 10