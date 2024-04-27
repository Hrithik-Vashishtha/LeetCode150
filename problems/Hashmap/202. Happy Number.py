def sum_of_square_digits(num):
    count = 0
    while num:
        mod = num % 10
        count += mod ** 2
        num //= 10
    return count

def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_square_digits(n)

    return n == 1

n = 19
print(isHappy(n))