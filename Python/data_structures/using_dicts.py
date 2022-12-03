state_capitals = {'washington': 'olympia',
                  'oregon': 'salem', 'California': 'sacramento'}

# print(state_capitals['washington'])

state_capitals['washington'] = 'aberdeen'
state_capitals['Texas'] = 'Austin'
print(state_capitals)

del state_capitals['California']
print(state_capitals)

removed_capital = state_capitals.pop('oregon')
print(state_capitals)

print(removed_capital)
