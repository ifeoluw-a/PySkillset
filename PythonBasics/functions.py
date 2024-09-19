# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def sub(a, b):
    return a - b

# Function to multiply two numbers (exponent)
def exp(a, b):
    return a * b

# Function to divide two numbers
def div(a, b):
    return a / b

# Dictionary to map operation names to their respective symbols
calc = dict(add='+', sub='-', exp='*', div='/')

# Print available operations
for i in calc.values():
    print(i)

# Get the first number from the user
a = int(input('Enter the first number: '))

# Main loop to handle calculations
while True:
    # Get the operation sign from the user
    sign = input('Enter a sign: ')
    
    # Get the second number from the user
    b = int(input('Enter the second number: '))
    
    # Perform the appropriate operation based on the sign entered
    if sign == '+':
        result = add(a, b)
        print(result)
    elif sign == '-':
        result = sub(a, b)
        print(result)
    elif sign == '*':
        result = exp(a, b)
        print(result)
    elif sign == '/':
        result = div(a, b)
        print(result)
    
    # If the user enters '=', display the final answer and break out of the loop
    elif sign == '=':
        print(f"The final answer is {result}")
        break

    # Ask if the user wants to continue further calculations
    cont = input('Do you want to continue? (yes/no): ')
    
    # Check if the user wants to continue
    should_continue = True
    while should_continue:
        if cont == 'yes':
            # Set the current result as the starting number for the next operation
            c = result
            print(c)
            
            # Get the next operation and number from the user
            sign = input('Enter a sign: ')
            b = int(input('Enter another number: '))
            
            # Perform the appropriate operation based on the sign entered
            if sign == '+':
                result = add(c, b)
                print(result)
            elif sign == '-':
                result = sub(c, b)
                print(result)
            elif sign == '*':
                result = exp(c, b)
                print(result)
            elif sign == '/':
                result = div(c, b)
                print(result)
            
            # If the user enters '=', display the final answer and break out of the loop
            elif sign == '=':
                print(f"The final answer is {result}")
            break
        
        # Exit the loop if the user does not want to continue
        else:
            break
