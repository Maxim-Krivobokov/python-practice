import pprint

people = {}

people['Ford'] = {'Name': 'Ford Prefect', 'Gender': 'male',
                  'Occupation': 'researcher', 'Home planet': 'Betelgeuse Seven', 'age': 33}


people['Arthur'] = {'Name': 'Arthur Dent', 'Gender': 'male',
                    'Occupation': 'bomberman', 'Home planet': 'Mars', 'age': 38}

people['Xena'] = {'Name': 'Xena Warrior Princess', 'Gender': 'female',
                  'Occupation': 'amazon warrior', 'Home planet': 'Earth', 'age': 28}

people['T800'] = {'Name': 'Cyberdyne systems model T800', 'Gender': 'none',
                  'Occupation': 'cyborg-terminator', 'Home planet': 'Earth', 'age': 99}

pprint.pprint(people)

print(people['Xena']['Occupation'])
