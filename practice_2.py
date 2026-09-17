n = input()

numbers = list(n)
original = numbers.copy()

numbers.reverse()

if numbers == original:
    print("YES")
else:
    print("NO")