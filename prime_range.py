# Range ke liye user se input le rahe hain
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print(f"Prime numbers between {lower} and {upper} are:")

# Ek-ek karke saare numbers check karne ke liye loop
for num in range(lower, upper + 1):
    # Prime numbers humesha 1 se bade hote hain
    if num > 1:
        is_prime = True
        
        # Check karne ke liye ki number kisi aur se divide toh nahi ho raha
        for i in range(2, num):
            if num % i == 0:
                is_prime = False  # Agar divide ho gaya toh prime nahi hai
                break             # Loop se bahar niklo
        
        # Agar loop poora chal gaya aur is_prime True raha, toh print kar do
        if is_prime:
            print(num)