limit = int(input("Enter the limit: "))
total = 0

for i in range(1, limit + 1):
    print(i)
    total = total + i

print(f"The sum is {total}")
