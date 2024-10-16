import math

def square_area_perimeter(length, length_error):
    area = length**2
    perimeter = 4 * length
    area_error = 2 * length * length_error
    perimeter_error = 4 * length_error
    return area, perimeter, area_error, perimeter_error

def circle_area_perimeter(radius, radius_error):
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    area_error = 2 * math.pi * radius * radius_error
    perimeter_error = 2 * math.pi * radius_error
    return area, perimeter, area_error, perimeter_error

def triangle_area_perimeter(side1, side2, base, height, side1_error, side2_error, base_error, height_error):
    area = 0.5 * base * height
    perimeter = side1 + side2 + base
    area_error = 0.5 * height * (base_error + height_error) + 0.5 * base * height_error
    perimeter_error = side1_error + side2_error + base_error
    return area, perimeter, area_error, perimeter_error

def trapezium_area_perimeter(side1, side2, side3, side4, height, side1_error, side2_error, side3_error, side4_error, height_error):
    area = 0.5 * (side1 + side3) * height
    perimeter = side1 + side2 + side3 + side4
    area_error = 0.5 * height * (side1_error + side3_error) + 0.5 * (side1 + side3) * height_error
    perimeter_error = side1_error + side2_error + side3_error + side4_error
    return area, perimeter, area_error, perimeter_error

length_sq = 45.09
length_error_sq = 0.01

radius_circ = 34.90
radius_error_circ = 0.05

side1_tri = 70.9
side2_tri = 89.07
base_tri = 76.07
height_tri = 100.07
side1_error_tri = 0.23
side2_error_tri = 0.07
base_error_tri = 0.04
height_error_tri = 0.05

side1_trap = 670.9
side2_trap = 849.07
side3_trap = 376.07
side4_trap = 716.07
height_trap = 231.07
side1_error_trap = 0.53
side2_error_trap = 0.27
side3_error_trap = 0.74
side4_error_trap = 0.14
height_error_trap = 0.25

area_sq, perimeter_sq, area_error_sq, perimeter_error_sq = square_area_perimeter(length_sq, length_error_sq)
area_circ, perimeter_circ, area_error_circ, perimeter_error_circ = circle_area_perimeter(radius_circ, radius_error_circ)
area_tri, perimeter_tri, area_error_tri, perimeter_error_tri = triangle_area_perimeter(side1_tri, side2_tri, base_tri, height_tri, side1_error_tri, side2_error_tri, base_error_tri, height_error_tri)
area_trap, perimeter_trap, area_error_trap, perimeter_error_trap = trapezium_area_perimeter(side1_trap, side2_trap, side3_trap, side4_trap, height_trap, side1_error_trap, side2_error_trap, side3_error_trap, side4_error_trap, height_error_trap)

print('Square:')
print('Area:', area_sq, 'cm^2 (±', area_error_sq, 'cm^2)')
print('Perimeter:', perimeter_sq, 'cm (±', perimeter_error_sq, 'cm)')
print('Circle:')
print('Area:', area_circ, 'cm^2 (±', area_error_circ, 'cm^2)')
print('Perimeter:', perimeter_circ, 'cm (±', perimeter_error_circ, 'cm)')
print('Triangle:')
print('Area:', area_tri, 'cm^2 (±', area_error_tri, 'cm^2)')
print('Perimeter:', perimeter_tri, 'cm (±', perimeter_error_tri, 'cm)')
print('Trapezium:')
print('Area:', area_trap, 'cm^2 (±', area_error_trap, 'cm^2)')
print('Perimeter:', perimeter_trap, 'cm (±', perimeter_error_trap, 'cm)')

