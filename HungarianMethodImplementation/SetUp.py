import numpy as np

def get_independent_zeros(cost_matrix):
    cost_matrix_in_bool_for_positions_of_zeros = np.full((cost_matrix.shape[0], cost_matrix.shape[1]), False)
    help_matrix = cost_matrix.copy()

    while (np.sum(help_matrix == 0) != 0):
        column_with_min_number_of_zeros = find_col_with_min_zeros(help_matrix)
        independent_zero_row = get_row_of_zero_from_col_with_min_zeros(help_matrix, column_with_min_number_of_zeros)
        
        cost_matrix_in_bool_for_positions_of_zeros[independent_zero_row, column_with_min_number_of_zeros] = True
        
        help_matrix[independent_zero_row, :] = -1
        help_matrix[:, column_with_min_number_of_zeros] = -1
    
    # Recording possible answer positions by marked_zero
    positions_of_zeros = find_true_positions(cost_matrix_in_bool_for_positions_of_zeros)
    
    # Mark all rows without independent zeros
    marked_rows_without_independent_zeros = np.where(~np.any(cost_matrix_in_bool_for_positions_of_zeros, axis=1))[0]
    
    return positions_of_zeros, marked_rows_without_independent_zeros

def remove_mismatched(temp_help, ordered_pairs, crossed_columns_with_zeros_in_marked_rows):
    temp_help = [value for value in temp_help if any(value == pair[0] and pair[1] in crossed_columns_with_zeros_in_marked_rows for pair in ordered_pairs)]
    return temp_help

def find_true_positions(matrix):
    true_positions = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value:
                true_positions.append((i, j))
    return true_positions

def find_col_with_min_zeros(matrix):
    # Count the number of zeros in each column
    zero_counts = np.sum(matrix == 0, axis=0)
    
    min_value = np.min(zero_counts[zero_counts != 0])
    min_index = np.where(zero_counts == min_value)[0][0]
    
    return min_index

def get_row_of_zero_from_col_with_min_zeros(matrix, col):
    # Find the first zero in the specified column
    for i, row in enumerate(matrix):
        if row[col] == 0:
            return i
    return None
