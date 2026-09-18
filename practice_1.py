n = int(input())

while True:
    
        numbers = [int(number) for number in input().split()]

        if len(numbers) == n:
            break
        else:
            print(f"عدد وارد کنید{n}")
            numbers = [int(number) for number in input().split()]


print(max(numbers))
 