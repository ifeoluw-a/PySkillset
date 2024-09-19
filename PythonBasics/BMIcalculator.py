# Get the user's name
name = input('name: ')

# Get the user's weight in kilograms and convert it to a float
weight = float(input('Enter your weight in kilogram: '))

# Get the user's height in meters and convert it to a float
height = float(input('Enter your height in meters: '))

# Calculate BMI using the formula: weight (kg) / (height (m) * height (m))
BMI = weight / (height * height)

# Print a greeting and the calculated BMI
print(f"Hello {name}, your BMI is: {BMI:.2f}")

# Determine the BMI category and provide feedback based on the BMI value
if BMI > 0:  # Check if BMI is positive
    if BMI < 18.5:
        print(f"{name}, you are underweight")
    elif BMI <= 24.9:
        print(f"{name}, you have a normal weight")
    elif BMI <= 29.9:
        print(f"{name}, you are overweight")
    elif BMI <= 34.9:
        print(f"{name}, you are obese")
    elif BMI <= 39.9:
        print(f"{name}, you are severely obese and you need help")
else:
    # Print an error message if the BMI is not positive
    print('Enter valid inputs')
