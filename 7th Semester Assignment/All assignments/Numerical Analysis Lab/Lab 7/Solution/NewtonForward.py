import math

def main():
    x = [0.0] * 20
    y = [[0.0] * 20 for _ in range(20)]
    sum_value = 0.0
    index = 0
    flag = 0
    sign = 1
    
    # Read the number of data points
    n = int(input("Enter the number of data points: "))
    
    # Read the actual data for x and y
    print("Enter data:")
    for i in range(n):
        x[i] = float(input(f"x[{i}] = "))
        y[i][0] = float(input(f"y[{i}] = "))
    
    # Read the calculation point
    xp = float(input("Enter the value of x where you want to calculate the derivative: "))
    
    # Check if the given point (xp) is a valid point in the x data
    for i in range(n):
        if abs(xp - x[i]) < 0.0001:
            index = i
            flag = 1
            break
    
    # If the flag is still 0, (xp) is not in the list of x data
    if flag == 0:
        print("Invalid calculation point. Exiting program...")
        exit(0)
    
    # Generate the Forward Difference Table
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
    
    # Calculate the finite difference (step size)
    h = x[1] - x[0]
    
    # Apply formula to calculate the sum of terms for derivatives
    for i in range(1, n - index):
        term = (y[index][i] ** i) / i
        sum_value += sign * term
        sign = -sign
    
    # Divide by h to get the first derivative
    first_derivative = sum_value / h
    
    # Display the final result
    print(f"The first derivative at x = {xp:.2f} is {first_derivative:.2f}")

if __name__ == "__main__":
    main()
