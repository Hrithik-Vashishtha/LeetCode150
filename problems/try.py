def sumOfSquareDigits(n):
    count = 0
    while n:
        rem = n % 10
        count += rem ** 2
        n //= 10
    return count


def isHappy(n):
    visited = set()
    while n:
        if n == 1:
            return True
        if n in visited or n ** 2 < 10:
            return False
        visited.add(n)
        n = sumOfSquareDigits(n)

n = 19
print(isHappy(n))