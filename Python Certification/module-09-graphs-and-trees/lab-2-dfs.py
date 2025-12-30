
def print_matrix(matrix):
    for row in matrix:
        print(row)

def dfs(matrix, start_node):
    n = len(matrix)
    reachable = [False]*n
    stack = [start_node]
    visited = []
    print_matrix(matrix)
    limit = 10
    while stack and limit:
        print("-"*20)
        print(f"stack: {stack}\nvisited: {visited}")
        current_node = stack.pop()
        if current_node in visited:
            continue
        visited.append(current_node)
        for i,is_neighbor in enumerate(matrix[current_node]):
            if is_neighbor:                
                stack.append(i)
                print(f"node: {current_node}, neighbor: {i}")
        limit -= 1
    return list(visited)

test1 = ([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)
test2 = ([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3)
test3 = ([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3)
test4 = ([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0)

check1 = [1, 2, 3, 0]
check2 = [3, 2, 1, 0]
check3 = [3, 2]
check4 = [0, 1]

print("\n========Tests=======")
print(f"Test1: {dfs(*test1)==check1}\n\n")
print(f"Test2: {dfs(*test2)==check2}\n\n")
print(f"Test3: {dfs(*test3)==check3}\n\n")
print(f"Test4: {dfs(*test4)==check4}")
print("======================")