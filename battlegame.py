# Setting characters
wizard = 'Wizard'
elf = 'Elf'
human = 'Human'

# Setting character HP
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Setting character damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

# Setting Dragon stats
dragon_hp = 300
dragon_damage = 50

# Character selection
while True:
    character = input(
        '1)   Wizard\n2)   Elf\n3)   Human\nChoose your Character: ')

    if character == '1':
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == '2':
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == '3':
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print('Unknown Character')

print('You have chosen character: ', character)
print('Health:', my_hp)
print('Damage:', my_damage)

# Battle with the dragon
while True:
    dragon_hp -= my_damage
    print(f'The {character} damaged the Dragon!')
    print(f'The Dragons current hp is{dragon_hp}')
    if dragon_hp <= 0:
        print('The Dragon has lost the battle')
        break
    my_hp -= dragon_damage
    print(f'The Dragon attacked {character} your hp is now {my_hp}')
    if my_hp <= 0:
        print('You have lost the battle')
        break
