# Function to calculate 'u' as per the formula
def calculate_u(u, n):
    result = u
    for i in range(1, n):
        result *= (u + i)
    return result

# Function to compute the factorial of 'n'
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# User input: Number of data points
n = int(input("Enter the number of data points: "))

# Initialize lists to store data
x = []
y = []

# Input data points
for i in range(n):
    x_val = float(input(f"Enter x[{i}]: "))
    y_val = float(input(f"Enter y[{i}]: "))
    x.append(x_val)
    y.append([0] * n)  # Initialize difference table
    y[i][0] = y_val

# Calculate the backward difference table
for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

# Display the backward difference table
for i in range(n):
    for j in range(i + 1):
        print(y[i][j], end="\t")
    print()

# User input: Value to interpolate at
value = float(input("Enter the value to interpolate: "))

# Initialize 'u' and 'result'
result = y[n - 1][0]
u = (value - x[n - 1]) / (x[1] - x[0])

# Calculate the interpolated value using Newton's backward interpolation
for i in range(1, n):
    result += (calculate_u(u, i) * y[n - 1][i]) / factorial(i)

# Display the interpolated value
print(f"\nThe interpolated value at year {value} is approximately {result}")
