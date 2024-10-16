import math
def difference(list1):
    actual_sq = []
    measured_sq = []
    diffList = []
    for i in range(len(list1)):
        actual_sq.append("{:.3f}".format(math.sqrt(list1[i])))
        measured_sq.append("{:.3f}".format(list1[i] ** (1/2)))
        diff = "{:.3f}".format(float(actual_sq[i]) - float(measured_sq[i]))
        diffList.append(diff)

    return actual_sq, measured_sq, diffList

list1=[56.90, 100.45, 67.90, 25.67, 56.67]
actual_square_root, measured_square_root, differences = difference(list1)
print("Input Values:", list1)
print("Actual Square Roots:", actual_square_root)
print("Measured Square Roots:", measured_square_root)
print("Differences:", differences)