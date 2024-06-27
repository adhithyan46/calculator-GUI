
![Screenshot (1)](https://github.com/adhithyan46/calculator-GUI/assets/171124070/2c5fc1e2-179c-41dd-b4e4-d58c81bb2ee5)

This code creates a simple calculator application using Tkinter, a Python library for building graphical user interfaces. The calculator can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. Here's a detailed description of the code:

**Importing Tkinter Library:**

The tkinter library is imported as tk to create the GUI elements.

**Defining the Button Click Function:**

A function clk(value) is defined to handle button clicks.
It retrieves the current text from the entry widget, appends the clicked button's value, and updates the entry widget with the new text.

**Defining the Clear Function:**

A function clr() is defined to clear the entry widget.

**Defining the Equals Function:**

A function eqls() is defined to evaluate the expression in the entry widget.
It tries to evaluate the expression using eval() and displays the result. If there's an error, it displays "ERROR".

**Setting Up the Main Window:**

The main window (root) is created with the title 'calculator'.

**Creating the Entry Widget:**

A Text widget (entry) is created to display the input and result, with specific width, height, and font.
It is placed in the grid layout at the top, spanning 4 columns.

**Creating the Buttons:**

A list of button configurations (buttons) is created, where each tuple contains the button text, row, and column position.
A loop iterates through the button configurations to create and place each button on the grid.
If the button text is "C", a red button is created to clear the entry widget when clicked.
If the button text is "=", a green button is created to evaluate the expression when clicked.
For all other buttons, a grey button is created to append the button text to the entry widget when clicked.

**Running the Main Loop:**

The root.mainloop() method is called to start the Tkinter event loop, making the window and its contents interactive.
