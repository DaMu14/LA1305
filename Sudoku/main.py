import tkinter as tk
from tkinter import messagebox
import random
import copy


def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True 
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
    
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    num_of_empty_cells = 0
    if difficulty == "easy":
        num_of_empty_cells = 30
    elif difficulty == "medium":
        num_of_empty_cells = 40
    elif difficulty == "hard":
        num_of_empty_cells = 50
    temp_board = copy.deepcopy(board)
    for _ in range(num_of_empty_cells):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while temp_board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        temp_board[row][col] = 0
    return temp_board

class SudokuUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.entries=[[None for _ in range(9)] for _ in range(9)]
        self.board = []
        self.solution=None
        self.create_widgets()

    def create_widgets(self):
        self.difficulty_frame = tk.Frame(self.root)
        self.difficulty_frame.pack()

        self.easy_button = tk.Button(self.difficulty_frame, text="Einfach", command=lambda: self.start_game("easy"))
        self.easy_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.medium_button = tk.Button(self.difficulty_frame, text="Mittel", command=lambda: self.start_game("medium"))
        self.medium_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.hard_button = tk.Button(self.difficulty_frame, text="Schwer", command=lambda: self.start_game("hard"))
        self.hard_button.pack(side=tk.LEFT, padx=10, pady=100)

        self.frame = tk.Frame(self.root)

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.frame, width=3, font=("Arial", 18), justify="center")
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j] = entry

        self.solve_button = tk.Button(self.root, text="Lösung anzeigen", command=self.show_solution)
        self.check_button = tk.Button(self.root, text="Prüfen", command=self.check_solution)
        self.reset_button = tk.Button(self.root, text="Neues Spiel", command=self.reset_game)
        self.validate_button = tk.Button(self.root, text="Einzelne Zahl prüfen", command=self.validate_single)

    def start_game(self, difficulty):
        self.difficulty_frame.pack_forget()
        self.frame.pack()
        self.solve_button.pack()
        self.check_button.pack()
        self.reset_button.pack()
        self.validate_button.pack()
        self.generate_sudoku(difficulty)

    def generate_sudoku(self, difficulty):
        self.board = generate_sudoku(difficulty)
        self.solution = copy.deepcopy(self.board)
        solve_sudoku(self.solution)
        self.update_board()
 
   
    def update_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, self.board[i][j])
                    self.entries[i][j].config(state="readonly")
                else:
                    self.entries[i][j].config(state="normal")
                    self.entries[i][j].delete(0, tk.END)


    def show_solution(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state="normal")
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, self.solution[i][j])
                self.entries[i][j].config(state="readonly")

    def check_solution(self):
        user_solution = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit():
                    row.append(int(value))
                else:
                    row.append(0)
            user_solution.append(row)
        if user_solution == self.solution:
            messagebox.showinfo("Sudoku", "Glückwunsch! Sie haben das Rätsel gelöst.")
        else:
            messagebox.showerror("Sudoku", "Die Lösung ist nicht korrekt.")

    def validate_single(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit() and self.board[i][j] == 0:
                    if not is_valid(self.board, i, j, int(value)):
                        messagebox.showerror("Sudoku", f"Die Zahl {value} an Position ({i + 1}, {j + 1}) ist ungültig.")
                        return
                    messagebox.showinfo("Sudoku", "Alle eingegebenen Zahlen sind korrekt.")

    def reset_game(self):
        self.frame.pack_forget()
        self.solve_button.pack_forget()
        self.check_button.pack_forget()
        self.reset_button.pack_forget()
        self.validate_button.pack_forget()
        self.difficulty_frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuUI(root)
    root.mainloop()
