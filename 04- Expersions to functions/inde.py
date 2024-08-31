######################### Assignment In The Class #####################################

# 1. BMI Calculation
def calculate_bmi(height: float, weight: float):
    bmi= weight / (height ** 2)
    print(bmi)

calculate_bmi(2,2)


########################################################################################

# 2. Volume of a Cylinder Calculation
def calculate_cylinder_volume(radius: int, height: int):
    vlume= 22/7 * (radius ** 2) * height
    print(f"The volume of the cylinder is: {volume} cubic meters")


volume = calculate_cylinder_volume(3, 2)


################################## Assignment After The Class ###########################

# 3. Age Calculation
def calculate_age(current_year: int, birth_year: int):
    age= current_year - birth_year
    print(f"You are {age} years old.")

calculate_age(2024, 1994)



########################################################################################

# 4. Area of a Rectangle
def calculate_rectangle_area(length: float, width: float):
    area= length * width
    print(f"The area of the rectangle is: {area} square meters.")

calculate_rectangle_area(4, 3)
########################################################################################

# 5. Area of a Circle
def calculate_circle_area(radius: float):
    area= 22/7 * (radius ** 2)
    print(f"The area of the circle is: {area} square units.")


calculate_circle_area(34)


########################################################################################

# 6. Surface Area of a Cube
def calculate_cube_surface_area(side: float):
    surface_area= 6 * (side ** 2)
    print(f"The surface area of the cube is: {surface_area} square units.")


calculate_cube_surface_area(5)


########################################################################################

# 7. Temperature Conversion
def fahrenheit_to_celsius(fahrenheit: float):
    celsius= (fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius is: {celsius}")

def celsius_to_fahrenheit(celsius: float):
    fahrenheit= (celsius * 9/5) + 32
    print(f"{temp_c}°C is {fahrenheit}°F.")


celsius_to_fahrenheit(38)
fahrenheit_to_celsius(100)


########################################################################################

# 8. Convert Seconds into Minutes and Seconds
def convert_seconds(total_seconds: int):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")


convert_seconds(900)


########################################################################################

# 9. Percentage Calculation
def calculate_percentage(total_marks: float, obtained_marks: float):
    percentage= (obtained_marks / total_marks) * 100
    print(f"The percentage is: {percentage}%")


calculate_percentage(1120, 775)

