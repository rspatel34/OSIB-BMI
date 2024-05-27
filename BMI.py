#CODE BY PATEL RUDRA SHAILESHBHAI
#OASIS INFOBYTE PYTHON PROGRAMMING INTERNSHIP

print("Welcome to the BMI Calculator!")

weight = float(input("Enter your weight in kilograms: "))   #user input for weight in kgs
height = float(input("Enter your height in meters: "))         #user input for height in kgs

bmi = weight / (height ** 2)  #bmi formula

print(f"Your BMI is: {bmi:.2f}")

#if,elif,else concepts for decision making
if bmi < 18.5:
    category = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    category = "Normal"
elif bmi >= 25 and bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI Category: {category}") #giving output 
