
def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0]*n for _ in range(n)] 

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
        print(matrix[node])
    return matrix


test1 = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}
test2 = {0: [1], 1: [0]}
test3 = {0: [], 1: [], 2: []}

check1 = [[0,1,1,0], [0,0,1,0], [1,0,0,1], [0,0,1,0]]
check2 = [[0,1], [1,0]]
check3 = [[0,0,0], [0,0,0], [0,0,0]]

print("\n=====Tests=====")
print(f"Test1: {adjacency_list_to_matrix(test1)==check1}\n")
print(f"Test2: {adjacency_list_to_matrix(test2)==check2}\n")
print(f"Test3: {adjacency_list_to_matrix(test3)==check3}")
print("===============")