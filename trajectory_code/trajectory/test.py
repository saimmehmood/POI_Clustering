import imp 

cal = imp.load_source('calculation', '../distance/calculation.py')

result = cal.distanceLatLong(43.73254, -79.30589, 43.73241, -79.30583)

print(result)