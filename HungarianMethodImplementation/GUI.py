import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from HungarianMethod import hungarian_method
import numpy as np

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

        solve_button = ttk.Button(self.root, text="Solve (Minimum)", command=self.solve_minimum)
        solve_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

        max_button = ttk.Button(self.root, text="Solve (Maximum)", command=self.solve_maximum)
        max_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

    def create_grid(self):
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())

        cost_matrix_label = ttk.Label(self.root, text="Cost Matrix:")
        cost_matrix_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")

        for i in range(rows):
            self.cost_matrix_entries.append([])
            for j in range(cols):
                self.cost_matrix_entries[i].append(ttk.Entry(self.root))
                self.cost_matrix_entries[i][j].grid(row=i+5, column=j, padx=10, pady=10)

    def solve_minimum(self):
        self.solve(False)

    def solve_maximum(self):
        self.solve(True)

    def solve(self, is_maximum):
        try:
            cost_matrix = self.get_cost_matrix()
            positions = hungarian_method(cost_matrix.copy(), is_maximum)
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
