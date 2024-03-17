# Declare variables to store the total sum and count of numbers
total = 0
count = 0

# Request user to enter a number
number = int(input("Please enter a number (type -1 to stop): "))

# Continue the loop until the user enters -1
while number != -1:
    # Add the entered number to the total sum
    total += number

    # Increment the count of numbers entered
    count += 1

    # Request the user to enter another number
    number = int(input("Please enter a number (type -1 to stop): "))

# Check if any numbers were entered to avoid division by zero
if count > 0:
    # Calculate the average of the entered numbers
    average = total / count

    # Print both the sum and average
    print(f"The sum of the entered numbers is: {total}.")
    print(f"The average of the entered numbers is: {average}.")
else:
    print("No numbers were entered.")
