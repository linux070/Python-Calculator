# `````` Building a Calculator program with python.````````
print("A Pythonista Calculator program")
from calc_logo import logo
# For Addition section ---
def add(n1, n2):
    return n1 + n2
# For Subtraction section ---
def subtract(n1, n2):
    return n1 - n2
# For Multiplication section ---
def multiply(n1, n2):
  return n1 * n2
# For Division section ---
def divide(n1, n2):
  return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number:\n"))
  for operators in operations:
    print(operators)
  calculation_end = True
  while calculation_end:
    operation_symbol = input("Pick an operation from the list above:\n")
    num2 = float(input("What's the next number:\n"))
    calculation_result = operations[operation_symbol]
    answer = round(calculation_result(num1, num2),2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.:") == "y":
      num1 = answer
    else:
      calculation_end = False
      calculator()
calculator() 

# linuxmode


# user_input = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.:")
#   user_input == "n":
#      calculation_end = False
#     


# operation_symbol = input("Pick another operation:\n")
# num3 = float(input("What's the next number:\n"))
# calculation_result = operations[operation_symbol]
# second_answer = round(calculation_result(first_answer, num3),2)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
  