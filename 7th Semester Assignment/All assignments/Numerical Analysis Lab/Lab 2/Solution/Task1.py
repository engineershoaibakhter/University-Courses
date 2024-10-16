def absolute_error(actual,measured):
    return abs(actual-measured)

def realtive_error(actual,measured):
    return abs((absolute_error(actual,measured)/actual)*100)

actual_values = [11.0098, 167.902, 56.0567, 67.9860]
measured_values = [12.0001, 166.802, 55.0001, 69.0000]
absolute_errors=[]
realtive_errors=[]
for i in range(len(actual_values)):
    absolute_errors.append(absolute_error(actual_values[i],measured_values[i]))
    realtive_errors.append(absolute_error(actual_values[i],measured_values[i]))
print('Absolute Errors: ',absolute_errors)
print('Relative Errors: ',realtive_errors)
