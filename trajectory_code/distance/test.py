import calculation 
import math

result = calculation.distanceLatLong(43.7740662, -79.5051495, 43.760337, -79.478733)

test_calculateDestination = calculation.calculateDestination(43.73254, -79.30589, 45.0, 4.0)

print(test_calculateDestination)

test_calculateBearing = calculation.calculateBearing(43.73254, -79.30589, test_calculateDestination[0], test_calculateDestination[1])

#print(test_calculateBearing)
print(result)
