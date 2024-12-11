#№1#
def find_max_min_sum_rows(matrix):
    max_sum = float('-inf')
    min_sum = float('inf')
    max_row = None
    min_row = None
    for row in matrix:
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum = row_sum
            max_row = row
        if row_sum < min_sum:
            min_sum = row_sum
            min_row = row
    return max_row, max_sum, min_row, min_sum
matrix = [[4, 9, 7], [1, 3, 8], [5, 6, 2]]
max_row, max_sum, min_row, min_sum = find_max_min_sum_rows(matrix)
print(max_row, max_sum)
print(min_row, min_sum)
#№2#
def replace_min_values(matrix): 
    new_matrix = []
    for row in matrix: 
        min_value = min(row)
        new_row = [0 if value % 2 == 0 else 1 for value in row]
        new_matrix.append(new_row)
    return new_matrix
matrix = [[4, 9, 7], [1, 3, 8], [5, 6, 2]]
new_matrix = replace_min_values(matrix)
for row in new_matrix: 
    print(row)