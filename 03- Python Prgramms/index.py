#########################Assignment In The Class##################################### 
#1 BMI Calculation

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))


bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")


########################################################################################

#2 Volume of a Cylinder Calculation
radius = int(input("Enter the radius of the cylinder in meters: "))
height = int(input("Enter the height of the cylinder in meters: "))

# Volume formula: V = π * r^2 * h
volume = 22/7* (radius ** 2) * height

print(f"The volume of the cylinder is: {volume:.2f} cubic meters")

##################################Assignment After The Class###############################
#3 Age Calculation

# Input: current year and birth year
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print(f"You are {age} years old.")

########################################################################################

#4 Area of a Rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width


print(f"The area of the rectangle is: {area} square units.")

########################################################################################
#4 Area of a Circle

radius = float(input("Enter the radius of the circle: "))

area = 22/7 * (radius ** 2)

print(f"The area of the circle is: {area} square units.")

########################################################################################
#5 Surface Area of a Cube

side = float(input("Enter the length of one side of the cube: "))

surface_area = 6 * (side ** 2)

print(f"The surface area of the cube is: {surface_area} square units.")

########################################################################################
#6 Temperature Conversion

temp = float(input("Enter the temperature Fahrenheit: "))


celsius = (temp - 32) * 5/9

print(f"Temperature in Celsius is: {celsius}")


temp = float(input("Enter the temperature in Celsius: "))



fahrenheit = (temp * 9/5) + 32
print(f"{temp}°C is {fahrenheit}°F.")

########################################################################################
#7 Convert Seconds into Minutes and Seconds

total_seconds = int(input("Enter the number of seconds: "))

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")

########################################################################################
#8 Percentage Calculation


total_marks = float(input("Enter the total marks: "))
obtained_marks = float(input("Enter the obtained marks: "))

percentage = (obtained_marks / total_marks) * 100

print(f"The percentage is: {percentage}%")

