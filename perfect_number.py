# User se number input le rahe hain
num = int(input("Enter a number: "))

# Factors ka total store karne ke liye variable
total = 0

# 1 se lekar uss number ke pehle tak loop chalayenge
for i in range(1, num):
    # Agar number i se poora divide ho jata hai, toh wo factor hai
    if num % i == 0:
        total += i  # Factor ko total mein plus kar do

# Ab check karenge ki total original number ke barabar hai ya nahi
if total == num:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")