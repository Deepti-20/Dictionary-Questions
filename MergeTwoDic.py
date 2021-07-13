d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}
d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}
d3={}

for key, value in d1.items():
    d3[key] = value
for key,value in d2.items():
    d3[key]=value
print(d3)
