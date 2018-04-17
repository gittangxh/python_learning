points = [{'x':2, 'y':3}, {'x':4, 'y':1}]
#t according to the element whose key = 'y'
points.sort(key = lambda i:i['y'])

print(points)

#sort according to default condition
points.sort(key = lambda i:i['y'])
print(points)

#sort according to element whose key=='x'
points.sort(key = lambda x:x['x'])
print(points)
print(points[0]['x'])


