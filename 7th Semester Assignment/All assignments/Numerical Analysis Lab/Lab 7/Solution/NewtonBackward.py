import math

def main():
    x = [0.0] * 20
    y = [[0.0] * 20 for _ in range(20)]
    sum_value = 0.0
    index = 0
    flag = 0
    n = int(input("Enter the number of data points: "))
    print("Enter data:")
    for i in range(n):
        x[i] = float(input(f"x[{i}] = "))
        y[i][0] = float(input(f"y[{i}] = "))
    xp = float(input("Enter the value of x where you want to calculate the derivative: "))
    for i in range(n):
        if abs(xp - x[i]) < 0.0001:
            index = i
            flag = 1
            break
    if flag == 0:
        print("Invalid calculation point. Exiting the program...")
        exit(0)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1]
    h = x[1] - x[0]
    for i in range(1, index + 1):
        term = (y[index][i] ** i) / i
        sum_value += term
    first_derivative = sum_value / h
    print(f"The first derivative at x = {xp:.2f} is {first_derivative:.2f}")
if __name__ == "__main__":
    main()
