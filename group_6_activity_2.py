""" 
Activity 2
Group 6
Students: Shaikha Alhajri, Fatma ALsuwaidi, Fatma Almadani, Iliazya Alattar, Noha Abou Karnib 
"""

import turtle

# Initialize turtle
turta = turtle.Turtle()
size = 30

# ------------------------------ setting each number (10 = A) as a color ----------------------------- #
# Function to get color based on character input
# Accepts a character and returns the corresponding color name.
# Returns None if the character is not in the dictionary.
def get_color(char):
    color_row = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray'
    }
    return color_row.get(char, None)

# Function to draw a square filled with a specified color
# Takes a color and a turtle as input
def draw_square(color, turta):
    turta.fillcolor(color)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(size)
        turta.right(90)
    turta.end_fill()

# ----------------------------- color in number and moving ----------------------------- #

# Uses the turtle instance to fill the square
def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(size)
        turta.right(90)
    turta.end_fill()
    draw_pixel(color_string)

# Retrieves the color from the character and draws it using turtle
def draw_pixel(color_string):
    color = get_color(color_string)
    if color is None:
        return
    draw_color_pixel(color, turta)

# Moves the turtle forward after each pixel and adjusts position for the next row
def draw_line_from_string(color_string, turta):
    for char in color_string: #for each character in the string
        color = get_color(char)
        if color is None:
            return False
        draw_pixel(char)
        turta.penup()
        turta.forward(size)
        turta.pendown()
    turta.penup()
    turta.backward(size * len(color_string))  # Move back to the start of the row
    turta.right(90)
    turta.forward(size)  # Move down to the next row
    turta.left(90)
    turta.pendown()
    return True
# Function to draw a line of pixels from a string of color characters

# ---------------------------- red and black grid ---------------------------- #
# Function to draw a red and black checkerboard grid
# Uses turtle to draw alternating colored squares on a 20x20 grid
def draw_grid(turta):
    start_y = 300  
    for row in range(20):
        for col in range(20):
            x = col * size - 300  
            y = start_y - row * size  
            color = 'black' if (row + col) % 2 == 0 else 'red'
            turta.penup()
            turta.goto(x, y)
            turta.pendown()
            draw_square(color, turta)

# ------------------------------ draw from file ------------------------------ #
# Function to draw a line of pixels from a string of numbers
# Function to read and draw shapes from a file
# Reads lines from a file, processes each line as a string of color codes
def draw_from_file(turta):
    # Prompt the user to enter the file name
    file_name = input("Enter the path of the file that you want to read its content: ")

    try:
        # Open the file and read its content
        with open(file_name, 'r') as file:
            print(f"Reading from {file_name}...")

            # Start drawing each line from the file
            for line in file:
                line = line.strip()  # Remove extra spaces or newlines
                if line:  # If the line is not empty
                    result = draw_line_from_string(line, turta)
                    if not result:  # If an invalid character is found, stop drawing
                        print(f"Invalid color in line: {line}")
                        break

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# ----------------------------- draw from string ----------------------------- #
# Function to draw a square pixel of a specified color
# Prompts the user for a string of color codes and draws accordingly
def draw_shape_from_string():
    while True:
        user_input = input("Enter a color string (or press Enter to quit): ")
        if user_input == "":
            break
        if not draw_line_from_string(user_input, turta):
            break

# ---------------------------- ask the user --------------------------- #
# Main function to select the type of grid to draw
# Offers options to draw a red/black grid, color from string, or draw from a file
def main():
    pick = input("Which type of grid would you like 1-Red&Black 2-ColorFromString 3-DrawFromFile: ")
    if pick == '1':
        draw_grid(turta)
    elif pick == '2':
        # Position turtle at the starting point (optional)
        turta.penup()
        turta.goto(-(size*10), (size*10))  # Move to top-left of the screen
        turta.pendown()
        draw_shape_from_string()
    elif pick == '3':
        # Position turtle at the starting point (optional)
        turta.penup()
        turta.goto(-(size*10), (size*10))  # Move to top-left of the screen
        turta.pendown()
        draw_from_file(turta)
    else:
        print("Invalid choice. Please choose 1, 2 or 3")
    turtle.Screen().exitonclick()

# ------------------------------ main execution ------------------------------ #
# Entry point of the script, sets turtle speed and starts the main function
if __name__ == "__main__":
    turta.speed(10)
    main()