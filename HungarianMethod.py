# %% Hungarian method

import numpy as np

def min_ha(cost_matrix):
    
    # Subtraction of the minimum
    
    for row in range(cost_matrix.shape[0]):
        cost_matrix[row, :] -= np.min(cost_matrix[row, :])
    
    for col in range(cost_matrix.shape[1]):
        if 0 not in cost_matrix[:,col]:
            cost_matrix[:, col] -= np.min(cost_matrix[:, col])
    
    sum_of_crossed_rows_and_cols = 0
    while sum_of_crossed_rows_and_cols < cost_matrix.shape[0]:
        
        # Determination of independent zeros 
        # Marking all rows without independent zeros
        positions_of_zeros, marked_rows_without_independent_zeros = get_independent_zeros(cost_matrix)
        print('positions_of_zeros:', positions_of_zeros)
        print('marked_rows_without_independent_zeros: ',marked_rows_without_independent_zeros)
 
        # Crossing out all columns with zeros in marked rows
        crossed_columns_with_zeros_in_marked_rows = []
        for i in range(cost_matrix.shape[0]):
            if i in marked_rows_without_independent_zeros:
                crossed_columns_with_zeros_in_marked_rows.extend(np.where(cost_matrix[i,:] == 0)[0])
        
    
        crossed_columns_with_zeros_in_marked_rows = np.unique(crossed_columns_with_zeros_in_marked_rows)
        print('crossed_columns_with_zeros_in_marked_rows', crossed_columns_with_zeros_in_marked_rows)
        
        # Marking all rows with independent zeros from crossed out columns
        
        marked_rows_with_ind_zeros_from_cr_col = []
        temp_help = []
        for i in range(cost_matrix.shape[1]):
            if i in crossed_columns_with_zeros_in_marked_rows:
                temp_help.extend(np.where(cost_matrix[:, i] == 0)[0])
        
        marked_rows_with_ind_zeros_from_cr_col = remove_mismatched(temp_help, positions_of_zeros, crossed_columns_with_zeros_in_marked_rows)
        print('marked_rows_with_ind_zeros_from_cr_col', marked_rows_with_ind_zeros_from_cr_col)
        
        # Crossing out all unmarked rows
        
        crossed_rows = []
        for i in range(cost_matrix.shape[0]):
            if i not in marked_rows_without_independent_zeros and i not in marked_rows_with_ind_zeros_from_cr_col:
                crossed_rows.append(i)
        
        crossed_rows = np.unique(crossed_rows)
        print('crossed_rows', crossed_rows)
        
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
            
            # Subtract min-uncrossed value of the all uncrossed elements
            
            for i in range(cost_matrix.shape[0]):
                if i not in crossed_rows:
                    for j in range(cost_matrix.shape[1]):
                        if j not in crossed_columns_with_zeros_in_marked_rows:
                            cost_matrix[i][j] -= min_uncrossed_element
            
    print('cost_matrix', cost_matrix)
    result, nvm = get_independent_zeros(cost_matrix)
    return result

def max_ha(cost_matrix_1):
    
    cost_matrix = (-1) * cost_matrix_1
    print(cost_matrix)
    
    # Subtraction of the minimum
    
    for row in range(cost_matrix.shape[0]):
        cost_matrix[row, :] -= np.min(cost_matrix[row, :])
    
    for col in range(cost_matrix.shape[1]):
        if 0 not in cost_matrix[:,col]:
            cost_matrix[:, col] -= np.min(cost_matrix[:, col])
    
    sum_of_crossed_rows_and_cols = 0
    while sum_of_crossed_rows_and_cols < cost_matrix.shape[0]:
        
        # Determination of independent zeros 
        # Marking all rows without independent zeros
        positions_of_zeros, marked_rows_without_independent_zeros = get_independent_zeros(cost_matrix)
        print('positions_of_zeros:', positions_of_zeros)
        print('marked_rows_without_independent_zeros: ',marked_rows_without_independent_zeros)
 
        # Crossing out all columns with zeros in marked rows
        crossed_columns_with_zeros_in_marked_rows = []
        for i in range(cost_matrix.shape[0]):
            if i in marked_rows_without_independent_zeros:
                crossed_columns_with_zeros_in_marked_rows.extend(np.where(cost_matrix[i,:] == 0)[0])
        
    
        crossed_columns_with_zeros_in_marked_rows = np.unique(crossed_columns_with_zeros_in_marked_rows)
        print('crossed_columns_with_zeros_in_marked_rows', crossed_columns_with_zeros_in_marked_rows)
        
        # Marking all rows with independent zeros from crossed out columns
        
        marked_rows_with_ind_zeros_from_cr_col = []
        temp_help = []
        for i in range(cost_matrix.shape[1]):
            if i in crossed_columns_with_zeros_in_marked_rows:
                temp_help.extend(np.where(cost_matrix[:, i] == 0)[0])
        
        marked_rows_with_ind_zeros_from_cr_col = remove_mismatched(temp_help, positions_of_zeros, crossed_columns_with_zeros_in_marked_rows)
        print('marked_rows_with_ind_zeros_from_cr_col', marked_rows_with_ind_zeros_from_cr_col)
        
        # Crossing out all unmarked rows
        
        crossed_rows = []
        for i in range(cost_matrix.shape[0]):
            if i not in marked_rows_without_independent_zeros and i not in marked_rows_with_ind_zeros_from_cr_col:
                crossed_rows.append(i)
        
        crossed_rows = np.unique(crossed_rows)
        print('crossed_rows', crossed_rows)
        
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
            
            # Subtract min-uncrossed value of the all uncrossed elements
            
            for i in range(cost_matrix.shape[0]):
                if i not in crossed_rows:
                    for j in range(cost_matrix.shape[1]):
                        if j not in crossed_columns_with_zeros_in_marked_rows:
                            cost_matrix[i][j] -= min_uncrossed_element
            
    print('cost_matrix', cost_matrix)
    result, nvm = get_independent_zeros(cost_matrix)
    print(result)
    return result

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

# %% gui

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HungarianAlgorithmApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hungarian Algorithm")
        self.cost_matrix_entries = []
        self.setup_gui()
        self.root.mainloop()

    def setup_gui(self):
        
        rows_label = ttk.Label(self.root, text="Enter number of workers (rows):")
        rows_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.rows_entry = ttk.Entry(self.root)
        self.rows_entry.grid(row=0, column=1, padx=10, pady=10)

        cols_label = ttk.Label(self.root, text="Enter number of jobs (jobs):")
        cols_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.cols_entry = ttk.Entry(self.root)
        self.cols_entry.grid(row=1, column=1, padx=10, pady=10)
 
    
        solve_button = ttk.Button(self.root, text="Solve", command=self.create_grid)
        solve_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)


    def create_grid(self):
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())
    
        cost_matrix_label = ttk.Label(self.root, text="Cost Matrix:")
        cost_matrix_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")
    
        for i in range(rows):
            self.cost_matrix_entries.append([])
            for j in range(cols):
                self.cost_matrix_entries[i].append(ttk.Entry(self.root))
                self.cost_matrix_entries[i][j].grid(row=i+4, column=j, padx=10, pady=10)
    
        solve_button = ttk.Button(self.root, text="Find Minimum", command=self.minimum)
        solve_button.grid(row=i+5, column=0, padx=10, pady=10, ipadx=10, ipady=10)
    
        solve_button = ttk.Button(self.root, text="Find Maximum", command=self.maximum)
        solve_button.grid(row=i+5, column=cols-1, padx=10, pady=10, ipadx=10, ipady=10)


    def minimum(self):
        try:
            cost_matrix = self.get_cost_matrix()
            positions = min_ha(cost_matrix.copy())
            result_window = tk.Toplevel(self.root)
            result_window.title("Result")
            result_window.geometry("400x400")

            result_label = tk.Label(result_window, text="Result:")
            result_label.pack()
            
            font = ('Arial', 18)
            
            print(positions)
            for worker, job in positions:
                print(f"Worker {worker} is assigned to Job {job}")
                result_ass = tk.Label(result_window, text=f"Worker {worker} is assigned to Job {job}")
                result_ass.pack()
            
            total_cost = 0
            for worker, job in positions:
                total_cost += cost_matrix[worker][job]
            cost_label_n = tk.Label(result_window, text="Total Cost: " + str(total_cost))
            cost_label_n.pack()
            
            result = np.zeros((cost_matrix.shape[0], cost_matrix.shape[1]))
            for i in range(len(positions)):
            	result[positions[i][0], positions[i][1]] = cost_matrix[positions[i][0], positions[i][1]]

            result_matrix = tk.Label(result_window, text=result, font=font)
            result_matrix.pack() 

        except ValueError as error:
            messagebox.showerror("Error", error)
    

        except ValueError as error:
            messagebox.showerror("Error", error)
    
    def maximum(self):
        try:
            cost_matrix = self.get_cost_matrix()
            positions = max_ha(cost_matrix.copy())
            result_window = tk.Toplevel(self.root)
            result_window.title("Result")
            result_window.geometry("400x400")

            result_label = tk.Label(result_window, text="Result:")
            result_label.pack()
            
            font = ('Arial', 18)
            
            print(positions)
            for worker, job in positions:
                print(f"Worker {worker} is assigned to Job {job}")
                result_ass = tk.Label(result_window, text=f"Worker {worker} is assigned to Job {job}")
                result_ass.pack()
            
            total_cost = 0
            for worker, job in positions:
                total_cost += cost_matrix[worker][job]
            cost_label_n = tk.Label(result_window, text="Total Cost: " + str(total_cost))
            cost_label_n.pack()
            
            result = np.zeros((cost_matrix.shape[0], cost_matrix.shape[1]))
            for i in range(len(positions)):
            	result[positions[i][0], positions[i][1]] = cost_matrix[positions[i][0], positions[i][1]]

            
            result_matrix = tk.Label(result_window, text=result, font=font)
            result_matrix.pack() 

        except ValueError as error:
            messagebox.showerror("Error", error)
    
    def get_cost_matrix(self):
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())
        cost_matrix = [[int(self.cost_matrix_entries[i][j].get()) for j in range(cols)] for i in range(rows)]
        return np.array(cost_matrix)

# %% main

def main():
    HungarianAlgorithmApp()

if __name__ == '__main__':
	main()

