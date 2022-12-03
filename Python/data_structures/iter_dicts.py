state_capitals = {'Washington': 'olympia',
                  'Oregon': 'salem', 'California': 'sacramento'}

# for state in state_capitals:
#     print(state)
for city in state_capitals.values():
    print(city)

for state in state_capitals:
    print(state_capitals[state], 'is the capital of', state)

for state, city in state_capitals.items():
    print(city, 'is the capital of', state)
