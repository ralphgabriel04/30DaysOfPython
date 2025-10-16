import math

def calculate_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i]-point2[i])**2
    return math.sqrt(distance)
        
point1 = [1,2,3]
point2 = [4,5,6]
distance = calculate_distance(point1, point2)
print(distance)

    