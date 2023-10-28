import numpy as np
from SetUp import get_independent_zeros, remove_mismatched

def hungarian_method(cost_matrix, maximize=False):
    if maximize:
        cost_matrix = (-1) * cost_matrix

    # Subtraction of the minimum
    for row in range(cost_matrix.shape[0]):
        cost_matrix[row, :] -= np.min(cost_matrix[row, :])

    for col in range(cost_matrix.shape[1]):
        if 0 not in cost_matrix[:, col]:
            cost_matrix[:, col] -= np.min(cost_matrix[:, col])

    sum_of_crossed_rows_and_cols = 0
    while sum_of_crossed_rows_and_cols < cost_matrix.shape[0]:

        # Determination of independent zeros
        # Marking all rows without independent zeros
        positions_of_zeros, marked_rows_without_independent_zeros = get_independent_zeros(cost_matrix)

        # Crossing out all columns with zeros in marked rows
        crossed_columns_with_zeros_in_marked_rows = []
        for i in range(cost_matrix.shape[0]):
            if i in marked_rows_without_independent_zeros:
                crossed_columns_with_zeros_in_marked_rows.extend(np.where(cost_matrix[i, :] == 0)[0])

        crossed_columns_with_zeros_in_marked_rows = np.unique(crossed_columns_with_zeros_in_marked_rows)

        # Marking all rows with independent zeros from crossed out columns
        marked_rows_with_ind_zeros_from_cr_col = []
        temp_help = []
        for i in range(cost_matrix.shape[1]):
            if i in crossed_columns_with_zeros_in_marked_rows:
                temp_help.extend(np.where(cost_matrix[:, i] == 0)[0])

        marked_rows_with_ind_zeros_from_cr_col = remove_mismatched(temp_help, positions_of_zeros,
                                                                  crossed_columns_with_zeros_in_marked_rows)

        # Crossing out all unmarked rows
        crossed_rows = []
        for i in range(cost_matrix.shape[0]):
            if i not in marked_rows_without_independent_zeros and i not in marked_rows_with_ind_zeros_from_cr_col:
                crossed_rows.append(i)

        crossed_rows = np.unique(crossed_rows)
        sum_of_crossed_rows_and_cols = len(crossed_rows) + len(crossed_columns_with_zeros_in_marked_rows)

        if sum_of_crossed_rows_and_cols < cost_matrix.shape[0]:

            # Finding min-uncrossed element
            uncrossed_elements = []
            for i in range(cost_matrix.shape[0]):
                if i not in crossed_rows:
                    for j in range(cost_matrix.shape[1]):
                        if j not in crossed_columns_with_zeros_in_marked_rows:
                            uncrossed_elements.append(cost_matrix[i][j])

            min_uncrossed_element = min(uncrossed_elements)

            # Add min-uncrossed value to the elements at the intersections
            for i in range(cost_matrix.shape[0]):
                if i in crossed_rows:
                    for j in range(cost_matrix.shape[1]):
                        if j in crossed_columns_with_zeros_in_marked_rows:
                            cost_matrix[i][j] += min_uncrossed_element

            # Subtract min-uncrossed value of all uncrossed elements
            for i in range(cost_matrix.shape[0]):
                if i not in crossed_rows:
                    for j in range(cost_matrix.shape[1]):
                        if j not in crossed_columns_with_zeros_in_marked_rows:
                            cost_matrix[i][j] -= min_uncrossed_element

    result, nvm = get_independent_zeros(cost_matrix)
    return result