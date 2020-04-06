cars = ['bmw m3', 'audi rs4', 'mercedes amg', 'porsche 911']
# cars is not a list, just a link to list ['bmw', 'audi', ..]
# all list variables are in real links

newcars = cars  # newcars is a link for cars list;
# modifying original variable will cause modifying a new (link)

# now newcars and cars are links to the same list


cars[2] = 'SLR McLaren'

print(newcars)
