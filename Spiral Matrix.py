# Task: Given an m x n matrix, return all elements of the matric in spiral order
# Input Example: [[1,2,3], [4,5,6], [7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Online example of the task: https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

def matrix_builder(matrix_size:int):
    """
    Make the matrix for the spiral processing
    :param matrix_size: which size the matrix should have, i.e. a 3 would make a 3x3 matrix with 9 cells
    :return: the matrix as an array of arrays
    """
    return_matrix = []

    i = 0
    for rows in range(matrix_size):
        matrix_row = []

        for cols in range(matrix_size):
            matrix_row.append(i+1)
            i+=1
        return_matrix.append(matrix_row)
    return return_matrix


def spiral_matrix(input_matrix, return_array = None):
    #print(f"Starting Matrix: {input_matrix}, Return Array: {return_array}")
    if return_array is None:
        return_array = []

    #get the first row
    for cells in input_matrix[0]:
        return_array.append(cells)
        print(return_array)
    input_matrix.pop(0)

    #go down (last column, but does not contain the content of the first row, was removed in previous step)
    for rows in input_matrix:
        return_array.append(rows.pop())
        print(return_array)


    #go left at bottom (bottom row, once again without the content from the last row)
    bottom_row = input_matrix.pop()
    for cell in reversed(bottom_row):
        return_array.append(cell)
        print(return_array)


    # go right if done, else go up (if only 1 list with 2 elements remain get those, else go up on the leftmost column and then recursion)
    if len(input_matrix) == 1 and len(input_matrix[0]) == 2:
        for cell in input_matrix[0]:
            return_array.append(cell)
            print(return_array)
        input_matrix.pop()
        print(f"Final Return Array: {return_array}")
        print("-------")
        return return_array
    else:
        for rows in reversed(input_matrix):
            return_array.append(rows.pop(0))
            print(return_array)
        spiral_matrix(input_matrix, return_array)





if __name__ == "__main__":
    spiral_matrix(matrix_builder(5))
    #print(matrix_builder(5))
