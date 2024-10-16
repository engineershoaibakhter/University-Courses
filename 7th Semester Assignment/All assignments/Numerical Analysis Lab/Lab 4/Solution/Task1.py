import sympy as sp
x = sp.symbols('x')
user_input = input("Enter the equation: ")
expression = sp.sympify(user_input)
derivative = sp.diff(expression, x)
print('Darevative: ',derivative)
fun = sp.lambdify(x, expression, 'numpy')
differential = sp.lambdify(x, derivative, 'numpy')

def newton_raphson_method(x0):
    prev_x = float('inf')
    while x0 != prev_x:
        prev_x = x0
        x0 = x0 - (fun(x0) / differential(x0))
    print(f'approx root: {x0:.5f}')

initial_guess = float(input("Enter the initial guess: "))
newton_raphson_method(initial_guess)
