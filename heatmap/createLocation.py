import json
from itertools import groupby
from collections import Counter

data = []
with open('yelp_academic_dataset_business.json') as f:
    for line in f:
        data.append(json.loads(line))

categories = []
locations = {}
for d in data:
    categories_current = d.get('categories')
    lat = d.get('latitude')
    longt = d.get('longitude')
    coord = {'lat':lat,'longt':longt}
    for cur in categories_current:
        if cur not in categories:
            locations[cur] = []
        locations[cur].append(coord)
    categories.extend(categories_current)

for key,value in locations.iteritems():
    category = ''.join(key)
    category = category.replace(" ","-")
    category = category.replace("/","-")
    category = category.replace("\\","-")
    nfile = open('locations/'+category+'.csv', 'w+')
    print category
    for item in value:
        lat = item.get('lat');
        longt = item.get('longt');
        nfile.write(str(lat)+','+str(longt)+'\n');




