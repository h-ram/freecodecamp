def hanoi_solver(n_disks):
    rod_1 = list(range(n_disks, 0, -1))
    rod_2 = []
    rod_3 = []
    moves = [f"{rod_1} {rod_2} {rod_3}"]
    
    stack = [(n_disks, rod_1, rod_3, rod_2, False)]
    
    while stack:
        n, source, destination, helper, processed = stack.pop()
        
        if n == 1:
            disk = source.pop()
            destination.append(disk)
            moves.append(f"{rod_1} {rod_2} {rod_3}")
        elif not processed:
            stack.append((n - 1, helper, destination, source, False))
            stack.append((1, source, destination, helper, True))
            stack.append((n - 1, source, helper, destination, False))
    
    return "\n".join(moves)


test1 = 2
test2 = 3
test3 = 4
test4 = 5

check1 = "[2, 1] [] []\n[2] [1] []\n[] [1] [2]\n[] [] [2, 1]"
check2 = "[3, 2, 1] [] []\n[3, 2] [] [1]\n[3] [2] [1]\n[3] [2, 1] []\n[] [2, 1] [3]\n[1] [2] [3]\n[1] [] [3, 2]\n[] [] [3, 2, 1]"
check3 = "[4, 3, 2, 1] [] []\n[4, 3, 2] [1] []\n[4, 3] [1] [2]\n[4, 3] [] [2, 1]\n[4] [3] [2, 1]\n[4, 1] [3] [2]\n[4, 1] [3, 2] []\n[4] [3, 2, 1] []\n[] [3, 2, 1] [4]\n[] [3, 2] [4, 1]\n[2] [3] [4, 1]\n[2, 1] [3] [4]\n[2, 1] [] [4, 3]\n[2] [1] [4, 3]\n[] [1] [4, 3, 2]\n[] [] [4, 3, 2, 1]"
check4 = "[5, 4, 3, 2, 1] [] []\n[5, 4, 3, 2] [] [1]\n[5, 4, 3] [2] [1]\n[5, 4, 3] [2, 1] []\n[5, 4] [2, 1] [3]\n[5, 4, 1] [2] [3]\n[5, 4, 1] [] [3, 2]\n[5, 4] [] [3, 2, 1]\n[5] [4] [3, 2, 1]\n[5] [4, 1] [3, 2]\n[5, 2] [4, 1] [3]\n[5, 2, 1] [4] [3]\n[5, 2, 1] [4, 3] []\n[5, 2] [4, 3] [1]\n[5] [4, 3, 2] [1]\n[5] [4, 3, 2, 1] []\n[] [4, 3, 2, 1] [5]\n[1] [4, 3, 2] [5]\n[1] [4, 3] [5, 2]\n[] [4, 3] [5, 2, 1]\n[3] [4] [5, 2, 1]\n[3] [4, 1] [5, 2]\n[3, 2] [4, 1] [5]\n[3, 2, 1] [4] [5]\n[3, 2, 1] [] [5, 4]\n[3, 2] [] [5, 4, 1]\n[3] [2] [5, 4, 1]\n[3] [2, 1] [5, 4]\n[] [2, 1] [5, 4, 3]\n[1] [2] [5, 4, 3]\n[1] [] [5, 4, 3, 2]\n[] [] [5, 4, 3, 2, 1]"


print("\n=====Tests=====")
print(f"Test1: {hanoi_solver(test1) == check1}")
print(f"Test2: {hanoi_solver(test2) == check2}")
print(f"Test3: {hanoi_solver(test3) == check3}")
print(f"Test4: {hanoi_solver(test4) == check4}")
print("===============")
