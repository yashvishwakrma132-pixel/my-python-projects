n = input("Enter a number: ")
length = len(n)
total = 0

for digit in n:
    total += int(digit) ** length

if total == int(n):
    print(f"{n} is an Armstrong number")
    # print("Armstrong number hai")
else:
    print(f"{n} is not an Armstrong number")
    # print("Armstrong number nahi hai")