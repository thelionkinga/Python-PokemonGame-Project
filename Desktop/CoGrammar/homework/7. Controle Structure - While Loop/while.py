# Declare a variable to store the total sum of numbers
total = 0

# Request user to enter a number
number = int(input("Please enter a number (type -1 to stop):"))

# Continue the loop until the user enters -1
while number != -1:
    # Add the entered number to the total sum
    total += number

    # Request the user to enter another number
    number = int(input("Please enter a number: "))

    # Check if the user entered -1, and if so, print the total sum
    if number == -1:
        print(f"The sum of the entered numbers is: {total}.")