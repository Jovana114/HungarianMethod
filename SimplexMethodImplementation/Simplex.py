import numpy as np
from SetUp import defines_variables, last_row_negative, get_pivot_col_min, last_col_positive, get_pivot_row
from SetUp import updating_matrix, last_row_positive, get_pivot_col_max, results

def Simplex(function_koefs, restriction_koefs, free_koefs, maximize=False):
    
    # Create simplex matrix
    matrix = np.hstack((restriction_koefs, free_koefs))
    matrix = np.vstack((matrix, np.append(function_koefs, 0)))
    
    if maximize:
        base_variables, non_base_variables = defines_variables(matrix)
        
        # Check if all values in function_koefs are positive
        while(last_row_positive(matrix) == False):
    
            # Specifying pivot column
            pivot_col_index = get_pivot_col_max(matrix)
            pivot_col = matrix[:, pivot_col_index]
        
            # Specifying pivot row
            last_col = matrix[:, -1]
            matrix = np.column_stack((matrix, last_col/pivot_col))
        
            # Check if the new column has all values positive
            if(last_col_positive(matrix) == True):
                print('Matrix after dividing:')
                print(matrix)
        
            pivot_row_index = get_pivot_row(matrix)
            pivot = matrix[pivot_row_index, pivot_col_index]
            print('pivot: ', pivot)
            
            # Updating matrix
            matrix = updating_matrix(pivot, pivot_row_index, pivot_col_index, matrix, base_variables, non_base_variables)
            print('updated matrix: ')
            print(matrix)
    
    else:
        base_variables, non_base_variables = defines_variables(matrix)
        
        # Check if all values in function_koefs are negative
        while(last_row_negative(matrix) == False):
    
            # Specifying pivot column
            pivot_col_index = get_pivot_col_min(matrix)
            pivot_col = matrix[:, pivot_col_index]
        
            # Specifying pivot row
            last_col = matrix[:, -1]
            matrix = np.column_stack((matrix, last_col/pivot_col))
        
            # Check if the new column has all values negative
            if(last_col_positive(matrix) == True):
                print('Matrix after dividing:')
                print(matrix)
        
            pivot_row_index = get_pivot_row(matrix)
            pivot = matrix[pivot_row_index, pivot_col_index]
            print('pivot: ', pivot)
            
            # Updating matrix
            matrix = updating_matrix(pivot, pivot_row_index, pivot_col_index, matrix, base_variables, non_base_variables)
            print('updated matrix: ')
            print(matrix)
    
    result = results(matrix, non_base_variables, base_variables)
    
    return result
