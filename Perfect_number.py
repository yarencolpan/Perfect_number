a = int(input("Enter the number:"))
i = 1
Total = 0
while i < a:
    if a % i == 0:
        Total += i
    i += 1
if Total == a:
    print("Perfect number")
else:
    print("Not a perfect number")
