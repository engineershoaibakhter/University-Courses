class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def lagrange_interpolation(data_points, x_value):
    result = 0.0
    for i in range(len(data_points)):
        term = data_points[i].y
        for j in range(len(data_points)):
            if j != i:
                term *= (x_value - data_points[j].x) / (data_points[i].x - data_points[j].x)
        result += term
    return result

if __name__ == "__main__":
    data_points = []
    n = int(input("Enter the number of known data points: "))
    for i in range(n):
        x = float(input(f"Enter x{i + 1}: "))
        y = float(input(f"Enter y{i + 1}: "))
        data_points.append(DataPoint(x, y))

    x_value = float(input("Enter the x value for interpolation: "))
    interpolated_value = lagrange_interpolation(data_points, x_value)
    print(f"Interpolated value at {x_value} is: {interpolated_value}")
