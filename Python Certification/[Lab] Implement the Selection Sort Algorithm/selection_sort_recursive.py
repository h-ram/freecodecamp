
def selection_sort(numbers):
    # print(numbers)
    if len(numbers) <=1:
        return numbers
    # finding the smallest number and its index
    smallest = numbers[0]
    smallest_i = 0
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            smallest_i = i

    # swapping with first unsorted
    numbers[smallest_i] = numbers[0]
    numbers[0] = smallest
            
    return [smallest] + selection_sort(numbers[1:])



test1 = [33, 1, 89, 2, 67, 245]
test2 = [5, 16, 99, 12, 567, 23, 15, 72, 3]
test3 = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
test4 = [87, 11, 23, 18, 18, 23, 11, 56, 87, 56]

check1 = [1, 2, 33, 67, 89, 245]
check2 = [3, 5, 12, 15, 16, 23, 72, 99, 567]
check3 = [1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643]

print(f"Test1: {selection_sort(test1)==check1}")
print(f"Test2: {selection_sort(test2)==check2}")
print(f"Test3: {selection_sort(test3)==check3}")