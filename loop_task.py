#Question 1: Multiplication Table
#Ask the user to enter a number, then print its multiplication table from 1 to 10.
number= int(input("Enter a number: "))
for i in range (1,11):
    print(f"{number}*{i}= {number*i}")

#Question 2: Count Even Numbers
#Write a program that prints all even numbers from 1 to 30.
#At the end, print how many even numbers were found.
counter= 0
for number in range (1,31):
    if number %2 == 0:
        print (number)
        counter= counter+1

#Level 2 — Medium

#Question 3: Password Attempts
#Write a program that asks the user to enter a password.
#The correct password is:"python123"
#The user has only 3 attempts.
#If the password is correct, print:Access granted
#If the user fails after 3 attempts, print:Account locked
correct_password= "python123"
attempts = 3
while attempts >0:
    password = input("Enter password: ")
    if password == correct_password:
        print ("Access granted")
        break
    else:
        attempts-=1
        if attempts >0:
            print (f" wrong password. You have {attempts}attempt(s) left")
        else:
            print ("Account locked")
#Question 4: Calculate Average Marks
#Ask the user how many marks they want to enter.
#Then ask them to enter the marks one by one.
#Finally, print the average mark.
num_marks= int(input("How many marks do you want to enter: "))
total= 0
for i in range (1, num_marks+1):
    mark = float(input(f"Enter mark {i}:"))
    total+=mark
average= total/ num_marks
print (f" Average:{average}")

#Level 3 — Hard

#Question 5: Number Guessing Game
#Create a number guessing game.
#Use this fixed secret number:
#secret_number = 7
#Ask the user to guess the number.
#The program should keep running until the user guesses correctly.
#Rules:
#● If the guess is too high, print:Too high
#● If the guess is too low, print:Too low
#● If the guess is correct, print:Correct!
secret_number = 7
while True:
    guess= int( input( "Guess the number: "))
    if guess > secret_number:
        print ("Too high")
    elif guess < secret_number:
        print ("Too low")
    else:
        print ("Correct")
        break


#Question 6: Simple ATM Menu
#Create a simple ATM program.
#Start with this balance: balance = 1000
#Show this menu repeatedly:
#1. Check balance
#2. Deposit money
#3. Withdraw money
#4. Exit
#Requirements:

#● If the user chooses 1, print the current balance.
#● If the user chooses 2, ask for an amount and add it to the balance.
#● If the user chooses 3, ask for an amount:
#○ If the amount is greater than the balance, print: Insufficient balance
#● Otherwise, subtract the amount from the balance.
#● If the user chooses 4, print: Thank you!
#Then stop the program.
balance = 1000
while True:
     print("1. Check balance")
     print("2. Deposit money")
     print("3. Withdraw money")
     print("4. Exit")
     choice = input("Choose an option (1-4): ")
     if choice == "1":
        print(balance)
    
     elif choice == "2":
        amount = float(input("Enter amount: "))
        balance+= amount
        print (balance)
     elif choice =="3":
         amount = float(input("Enter amount: "))
         if amount > balance:
             print("Insufficient balance")
         else:
             balance= balance - amount
             print (balance)
     elif choice=="4":
         print(" Thank you")
         break
     else:
         print ("Invalid choice")
         



