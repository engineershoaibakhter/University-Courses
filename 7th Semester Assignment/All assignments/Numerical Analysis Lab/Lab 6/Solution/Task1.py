def calculate_product_term(i, value, x):
    product = 1
    for j in range(i):
        product *= (value - x[j])
    return product

def calculate_divided_difference_table(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i-1] - y[j+1][i-1]) / (x[j] - x[i+j]))
    return y

def apply_newton_formula(value, x, y, n):
    result = y[0][0]
    for i in range(1, n):
        result += (calculate_product_term(i, value, x) * y[0][i])
    return result

def display_divided_difference_table(y, n):
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t", end=" ")
        print("")

n = int(input("Enter the number of inputs: "))
x = []
y = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    x_val = float(input(f"Enter x[{i}]: "))
    y_val = float(input(f"Enter y[{i}]: "))
    x.append(x_val)
    y[i][0] = y_val

y = calculate_divided_difference_table(x, y, n)

print("\nDivided Difference Table:")
display_divided_difference_table(y, n)

value = float(input("\nEnter the value to interpolate: "))

interpolated_value = apply_newton_formula(value, x, y, n)
print("\nInterpolated value at", value, "is approximately", round(interpolated_value, 4))
