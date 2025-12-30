
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]
    sublist1 = [num for num in numbers if num < pivot]
    sublist2 = [num for num in numbers if num == pivot]
    sublist3 = [num for num in numbers if num > pivot]

    return quick_sort(sublist1) + sublist2  + quick_sort(sublist3)

test1 = [20, 3, 14, 1, 5]
test2 = [83, 4, 24, 2]
test3 = [4, 42, 16, 23, 15, 8]
test4 = [87, 11, 23, 18, 18, 23, 11, 56, 87, 56]

check1 = [1, 3, 5, 14, 20]
check2 = [2, 4, 24, 83]
check3 = [4, 8 , 15, 16, 23, 42]
check4 = [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]

print(f"Test1: {quick_sort(test1)==check1}")
print(f"Test2: {quick_sort(test2)==check2}")
print(f"Test3: {quick_sort(test3)==check3}")
print(f"Test4: {quick_sort(test4)==check4}")
