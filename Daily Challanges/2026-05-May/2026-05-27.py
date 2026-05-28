import math
def get_pizzas_to_order(hours_worked):
    slices = 0
    for hours in hours_worked:
        slices += max(2, math.ceil(hours/3))
    return math.ceil(slices / 8)

print(get_pizzas_to_order([8, 8, 8]))
print(get_pizzas_to_order([10, 9, 8, 2, 2, 6, 10]))
print(get_pizzas_to_order([1, 2, 3, 4, 5]))
print(get_pizzas_to_order([8, 8, 8, 8, 8, 8, 8, 8]))
print(get_pizzas_to_order([9, 9, 6]))
print(get_pizzas_to_order([9, 9, 6]))