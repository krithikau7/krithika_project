balance = 5000

print("Welcome to ATM")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your account balance is:", balance)

elif choice == 2:
    deposit = int(input("Enter amount to deposit: "))
    balance = balance + deposit
    print("Amount deposited successfully")
    print("Updated balance:", balance)

elif choice == 3:
    withdraw = int(input("Enter amount to withdraw: "))

    if withdraw <= balance and withdraw > 0:
        balance = balance - withdraw
        print("Please collect your cash")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance or invalid amount")

elif choice == 4:
    print("Thank you for using ATM")

else:
    print("Invalid choice")

print("See you!")


a = [1,2,3]
for i in a:
    print(a)

print("jai balaiyya")