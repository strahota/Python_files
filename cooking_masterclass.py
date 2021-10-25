import math

budget = float(input())
count_students = int(input())
package_of_flour = float(input())
one_egg_price = float(input())
one_apron_price = float(input())

count = 0
free_packeges = 0

for price in range(1, count_students + 1):
    count += 1
    if count % 5 == 0:
        free_packeges += 1
total_price = one_apron_price * (math.ceil(count_students * 1.20)) + (
            one_egg_price * 10 * count_students) + package_of_flour * (count_students - free_packeges)

if budget >= total_price:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    money_needed = total_price - budget
    print(f"{money_needed:.2f}$ more needed.")
