def trapezoidal_rule_from_points(points):
    n = len(points)
    integral = points[0][1] + points[-1][1]  
    for i in range(1, n - 1):
        integral += 2 * points[i][1]  
    h = points[1][0] - points[0][0]  
    integral *= h / 2  
    return integral

given_points = [(-4, 0), (-3, 4), (-2, 5), (-1, 3), (0, 10),(1,11),(2,2)]
result = trapezoidal_rule_from_points(given_points)
print("Approximated integral value using given points:", result)
