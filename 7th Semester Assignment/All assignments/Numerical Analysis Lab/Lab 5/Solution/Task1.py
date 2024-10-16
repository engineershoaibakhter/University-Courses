def calculate_u(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def display_forward_difference_table(x, y, n):
    for i in range(n):
        print(x[i], end="\t")
        for j in range(n - i):
            print(y[i][j], end="\t")
        print("")

def interpolate(x, y, n, value):
    sum = y[0][0]
    u = (value - x[0]) / (x[1] - x[0])
    for i in range(1, n):
        sum = sum + (calculate_u(u, i) * y[0][i]) / factorial(i)
    return round(sum, 6)

n = int(input("Enter the number of data points: "))
x = []
y = []

for i in range(n):
    x_val = float(input(f"Enter x[{i}]: "))
    y_val = float(input(f"Enter y[{i}]: "))
    x.append(x_val)
    y.append([0] * n)
    y[i][0] = y_val

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

print("\nForward Difference Table:")
display_forward_difference_table(x, y,n)

value = float(input("\nEnter the value to interpolate at: "))
result = interpolate(x, y, n, value)
print(f"\nInterpolated value at {value} is approximately {result}")
