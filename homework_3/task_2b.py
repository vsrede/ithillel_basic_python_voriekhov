digit = int(input())
digit_sum = digit % 10
digit //= 10
digit_sum += digit % 10
digit //= 10
digit_sum += digit % 10
print(digit_sum)
