# Write your solution here
def row_sums(matrix: list) -> None:
    for row in matrix:
        row.append(sum(row))


if __name__ == '__main__':
    matrix = [[1, 2], [3, 4]]
    row_sums(matrix)
    
    print(matrix)
