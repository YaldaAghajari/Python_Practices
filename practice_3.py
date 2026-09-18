while True:
    n = int(input())

    if 3 <= n <= 10:
        break
    else:
        print("n باید بین 3 و 10 باشد.")

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")