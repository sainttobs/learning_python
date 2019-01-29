# using return values in a function


def exponent(num,n):
    exp = num ** n
    return exp


sum = exponent(4, 3)  # 64
print(sum)