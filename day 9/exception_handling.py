# Exception_handling: runtime error, the exception that occurs during the execution of the program.
# try block: consist the code that may raise an exception
# except block: consist the code that handles the exception
# error specific exception block can be created to handle specific exception, multiple error specific blocks can be created

abc = 10
try:
   a = int(input("Enter a number: "))
   print(a + 10)
except NameError:
   print("A is not defined")
except ValueError:
   print("Invalid input")
except:
   print("Something went wrong")


# implement exception handling 
# in calculator
# in program that converts a temperature from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32.
# in program that determines if a triangle is valid (sum of any two sides must be greater than the third side).
# in a program that checks if a number is between 1 and 100
# in grade calculation program
# in simple tip calculator