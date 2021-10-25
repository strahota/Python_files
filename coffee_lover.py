coffee_list = input().split()

number_of_commands = int(input())

for each_command in range(number_of_commands):
    command = input().split()
    action = command[0]
    if action == 'Include':
        coffee = command[1]
        coffee_list.append(coffee)
    elif action == 'Remove':
        first_last = command[1]
        number_coffee = int(command[2])
        if number_coffee < len(coffee_list):
            if first_last == 'first':
                coffee_list = coffee_list[number_coffee:]
            else:
                coffee_list = coffee_list[:-number_coffee]
    elif action == 'Prefer':
        index1 = int(command[1])
        index2 = int(command[2])
        if 0 <= index1 < len(coffee_list) and 0 <= index2 < len(coffee_list):
            coffee_list[index1], coffee_list[index2] = coffee_list[index2], coffee_list[index1]
    elif action == 'Reverse':
        coffee_list.reverse()

print('Coffee:')
print(*coffee_list)
