# User se number input le rahe hain
num = int(input("Enter a number: "))

# Original number ko print ke liye save kar lete hain
original_num = num

# Jab tak number 9 se bada hai (yaani single digit nahi hai), loop chalega
while num > 9:
    total = 0
    temp = num
    
    # Ye andar wala loop digits ko plus karega
    while temp > 0:
        digit = temp % 10
        total += digit
        temp = temp // 10
        
    # Total ko hi naya number bana denge agle round ke liye
    num = total

print(f"The single digit sum of {original_num} is {num}")