# %% Simplex

import numpy as np

def SimplexMin(function_koefs, restriction_koefs, free_koefs):
    
    # Create simplex matrix
    
    matrix = np.hstack((restriction_koefs, free_koefs))
    matrix = np.vstack((matrix, np.append(function_koefs, 0)))
    
    print('Matrix:')
    print(matrix)
    
    base_variables, non_base_variables = defines_variables(matrix)
    
    # Check if all values in function_koefs are negative
    while(last_row_negative(matrix) == False):
    
        # Specifying pivot column
        pivot_col_index = get_pivot_col_min(matrix)
        pivot_col = matrix[:, pivot_col_index]
        
        # Specifying pivot row
        last_col = matrix[:, -1]
        matrix = np.column_stack((matrix, last_col/pivot_col))
        
        # Check ih new col has all values negative
        if(last_col_positive(matrix) == True):
            print('Matrix after dividing:')
            print(matrix)
        
            pivot_row_index = get_pivot_row(matrix)
            # pivot_row = matrix[pivot_row_index, :]
            
            # Specifying pivot
            pivot = matrix[pivot_row_index, pivot_col_index]
            print('pivot: ', pivot)
            
            # Check if all values in function_koefs are negative
            if(last_row_negative(matrix) == False):
                # Updating matrix
                matrix = updating_matrix(pivot, pivot_row_index, pivot_col_index, matrix, base_variables, non_base_variables)
                print('updated matrix: ')
                print(matrix)
    
    result = results(matrix, non_base_variables, base_variables)
    
    return result

def SimplexMax(function_koefs, restriction_koefs, free_koefs):
    
    # Create simplex matrix
    
    matrix = np.hstack((restriction_koefs, free_koefs))
    matrix = np.vstack((matrix, np.append(function_koefs, 0)))
    
    print('Matrix:')
    print(matrix)
    
    base_variables, non_base_variables = defines_variables(matrix)
    
    # Check if all values in function_koefs are negative
    while(last_row_positive(matrix) == False):
    
        # Specifying pivot column
        pivot_col_index = get_pivot_col_max(matrix)
        pivot_col = matrix[:, pivot_col_index]
        
        # Specifying pivot row
        last_col = matrix[:, -1]
        matrix = np.column_stack((matrix, last_col/pivot_col))
        
        # Check ih new col has all values negative
        if(last_col_positive(matrix) == True):
            print('Matrix after dividing:')
            print(matrix)
        
            pivot_row_index = get_pivot_row(matrix)
            # pivot_row = matrix[pivot_row_index, :]
            
            # Specifying pivot
            pivot = matrix[pivot_row_index, pivot_col_index]
            print('pivot: ', pivot)
            
            # Updating matrix
            matrix = updating_matrix(pivot, pivot_row_index, pivot_col_index, matrix, base_variables, non_base_variables)
            print('updated matrix: ')
            print(matrix)
    
    result = results(matrix, non_base_variables, base_variables)
    
    return result

def results(matrix, non_base_variables, base_variables):
    
    f = matrix[-1, -1]
    
    last_col = []
    for el in matrix[:, -1]:
        last_col.append(el)
    last_col.pop()
    
    for row, i in zip(base_variables, last_col):
        print(f"{row} = {i}")
    
    for col in non_base_variables:
        print(f"{col} = 0")
    
    print('Value of f:',f)
    
    return

def switch_variables(matrix, pivot_row_index, pivot_col_index, base_variables, non_base_variables):
    
    pivot_col_index = "x" + str(int(pivot_col_index) + 1)
    print('pivot_col', pivot_col_index)
    
    pivot_row_index = "x" + str(int(pivot_row_index) + len(non_base_variables) + 1)
    print('pivot_row', pivot_row_index)
    
    if pivot_col_index in base_variables:
        index_col = base_variables.index(pivot_col_index)
        index_row = non_base_variables.index(pivot_row_index)
        
        base_variables.remove(pivot_col_index)
        non_base_variables.remove(pivot_row_index)
        
        non_base_variables.insert(index_row, pivot_col_index)
        base_variables.insert(index_col, pivot_row_index)
    elif pivot_col_index in non_base_variables:
        index_col = non_base_variables.index(pivot_col_index)
        index_row = base_variables.index(pivot_row_index)
        
        non_base_variables.remove(pivot_col_index)
        base_variables.remove(pivot_row_index)
        
        base_variables.insert(index_row, pivot_col_index)
        non_base_variables.insert(index_col, pivot_row_index)

    print('new non_base_variables', non_base_variables)
    print('new base_variables', base_variables)
        
    return matrix

def defines_variables(matrix):
    base_variables = []
    non_base_variables = []
    
    for col in range(matrix.shape[1]):
        non_base_variables.append(col)
    
    non_base_variables = [f"x{i}" for i in range(1, len(non_base_variables))]
    
    print('non_base_variables', non_base_variables)
    
    for row in range(matrix.shape[0] - 1):
        base_variables.append(row)
    
    cont = len(non_base_variables) + 1
    base_variables = [f"x{i}" for i in range(cont, cont + len(base_variables))]
    
    print('base_variables', base_variables)
    
    return base_variables, non_base_variables

def last_col_positive(matrix):
    last_col = matrix[:,-1]
    if (np.any(last_col > 0)):
        return True
    return False

def last_row_negative(matrix):
    last_row = matrix[-1,:]
    if (np.all(last_row <= 0)):
        return True
    return False

def last_row_positive(matrix):
    last_row = matrix[-1,:]
    if (np.all(last_row > 0)):
        return True
    return False

def updating_matrix(pivot, pivot_row_index, pivot_col_index, matrix, base_variables, non_base_variables):
    matrix = matrix[:, :-1]
    
    matrix = switch_variables(matrix, pivot_row_index, pivot_col_index, base_variables, non_base_variables)
      
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            if row != pivot_row_index:
                if col != pivot_col_index:
                    matrix[row, col] = matrix[row, col] - (
                        matrix[pivot_row_index, col] * matrix[row, pivot_col_index] 
                        / pivot)
                
    
    matrix[pivot_row_index,:] = matrix[pivot_row_index,:] / pivot
    matrix[:, pivot_col_index] = -(matrix[:, pivot_col_index] / pivot)
    
    matrix[pivot_row_index, pivot_col_index] = 1/pivot
    
    return matrix

def get_pivot_row(matrix):
    last_col = matrix[:,-1]
    positive_values = last_col[last_col > 0]
    print('positive_values', positive_values)
    min_positive_element = np.min(positive_values)
    print('min_positive_element', min_positive_element)
    print(min_positive_element)
    
    # Get the indices of the minimum positive element
    indices = np.argwhere(last_col == min_positive_element)
    pivot_row, _ = indices[0]
    print('pivot_row', pivot_row)
    
    return pivot_row

def get_pivot_col_min(matrix):
    
    pivot_col = np.argmax(matrix[-1, :])
    
    return pivot_col

def get_pivot_col_max(matrix):
    
    # Get the indices of the minimum positive element
    pivot_col = np.argmin(matrix[-1, :])
    
    return pivot_col

# %% main

def main():

    #Example 1) - min
    function_koefs = np.array([2, -3])
    restriction_koefs = np.matrix([[1, 1], [1, -1]]) # <=
    free_koefs = np.array([[4], [6]])  
    
    SimplexMin(function_koefs, restriction_koefs, free_koefs)
    
    #Example 2) - max
    #function_koefs = np.array([-1, -1])
    #restriction_koefs = np.matrix([[-1, 0], [0, -1]]) # <=
    #free_koefs = np.array([[0], [0]])
    
    #SimplexMax(function_koefs, restriction_koefs, free_koefs)

if __name__ == '__main__':
	main()