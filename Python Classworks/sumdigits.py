def sum_digits(num):
    num = str(num)
    total = 0
    for ch in num:
        total = total + int(ch)
    return total

n = 12345
print(sum_digits(n))

n = 9767
print(sum_digits(n))