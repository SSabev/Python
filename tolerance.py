import math

array = range(10000)

array = [i+1 for i in array]

array_sum = math.pi*math.pi/6.00
print(array_sum)

tolerance = 0.01/100.0
print tolerance

result = 0.00

for i in array:
    result = result + 1.0/(i*i)
    temp = math.fabs((array_sum-result)/array_sum)
    if temp < tolerance:
        print 'Less than the tolerance. Solution found'
        print i
        break
