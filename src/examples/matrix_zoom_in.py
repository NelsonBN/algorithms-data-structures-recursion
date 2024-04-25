
def print_matrix(matrix):
    for row in matrix:
        print(row)


def zoom_in(matrix, zoom): # Time complexity: O(n^2), Space complexity: O(n^2)
    if zoom <= 1:
        return matrix

    rows = len(matrix)
    if rows - 2 < 2:
        return matrix

    cols = len(matrix[0])
    if cols - 2 < 2:
        return matrix

    rows -= 1
    cols -= 1

    sub_matrix = [row[1:cols] for row in matrix[1:rows]]

    return zoom_in(sub_matrix, zoom - 1)



# Create a matrix 10x10
matrix = [[j+i*100 for j in range(1, 11)] for i in range(1, 11)]
print_matrix(matrix)

target_zoom = 4

print(f'Zooming in {target_zoom} times')

print_matrix(zoom_in(matrix, target_zoom))
