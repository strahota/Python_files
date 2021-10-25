items = [int(element) for element in input().split(", ")]
entry_point = int(input())
type_of_item = input()
sum_left = 0
sum_right = 0
value_of_entry_point = items[entry_point]
left_side = items[:entry_point]
right_side = items[entry_point + 1:]
for item in left_side:
    if type_of_item == "cheap":
        if item < value_of_entry_point:
            sum_left += item
    elif type_of_item == "expensive":
        if item >= value_of_entry_point:
            sum_left += item
for item in right_side:
    if type_of_item == "cheap":
        if item < value_of_entry_point:
            sum_right += item
    elif type_of_item == "expensive":
        if item >= value_of_entry_point:
            sum_right += item
if sum_left >= sum_right:
    print(f"Left - {sum_left}")
else:
    print(f"Right - {sum_right}")
