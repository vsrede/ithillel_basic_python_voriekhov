digit = int(input())
digit_sum = 0
x, y = (divmod(digit, 10))
digit_sum += y
x, y = (divmod(x, 10))
digit_sum += y + x
print(digit_sum)


