import tkinter as tk
from tkinter import messagebox
import random
import copy


def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    for y in range(9):
        if board[y][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for y in range(start_row, start_row + 3):
        for x in range(start_col, start_col + 3):
            if board[y][x] == num:
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
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return (y, x)
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

        self.explanation_button = tk.Button(self.difficulty_frame, text="Anleitung", command=self.show_explanation)
        self.explanation_button.pack(side=tk.LEFT, padx=10, pady=10)


        self.frame = tk.Frame(self.root)

        for y in range(9):
            for x in range(9):
                entry = tk.Entry(self.frame, width=3, font=("Arial", 18), justify="center")
                entry.grid(row=y, column=x, padx=5, pady=5)
                self.entries[y][x] = entry

        self.solve_button = tk.Button(self.root, text="Lösung anzeigen", command=self.show_solution)
        self.check_button = tk.Button(self.root, text="Prüfen", command=self.check_solution)
        self.reset_button = tk.Button(self.root, text="Neues Spiel", command=self.reset_game)
        self.validate_button = tk.Button(self.root, text="Einzelne Zahl prüfen", command=self.validate_single)

    def show_explanation(self):
        explanation = (
            "Was ist Sudoku?\n\n"
            "Ziel des Spiels ist es, die leeren Zellen in einem 9x9-Gitter so zu füllen, dass jede Spalte, jede Reihe und jedes der neun 3x3-Untergitter die Zahlen 1 bis 9 genau einmal enthält.\n\n"
            "So spielt man:\n"
            "1. Wähle einen Schwierigkeitsgrad aus.\n"
            "2. Fülle die leeren Zellen mit Zahlen von 1 bis 9.\n"
            "3. Nutze die Buttons, um die Lösung zu prüfen oder dir die Lösung anzeigen zu lassen."
        )
        messagebox.showinfo("Spielerklärung", explanation)

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
        for y in range(9):
            for x in range(9):
                if self.board[y][x] != 0:
                    self.entries[y][x].delete(0, tk.END)
                    self.entries[y][x].insert(0, self.board[y][x])
                    self.entries[y][x].config(state="readonly")
                else:
                    self.entries[y][x].config(state="normal")
                    self.entries[y][x].delete(0, tk.END)


    def show_solution(self):
        for y in range(9):
            for x in range(9):
                self.entries[y][x].config(state="normal")
                self.entries[y][x].delete(0, tk.END)
                self.entries[y][x].insert(0, self.solution[y][x])
                self.entries[y][x].config(state="readonly")

    def check_solution(self):
        user_solution = []
        for y in range(9):
            row = []
            for x in range(9):
                value = self.entries[y][x].get()
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
        invalid_positions = []
        for y in range(9):
            for x in range(9):
                value = self.entries[y][x].get()
                if value.isdigit() and self.board[y][x] == 0:
                    if not is_valid(self.board, y, x, int(value)):
                         invalid_positions.append((y + 1, x + 1))

        if invalid_positions:
            message = "Die folgenden Positionen enthalten ungültige Zahlen:\n"
            message += "\n".join([f"({row}, {col})" for row, col in invalid_positions])
            messagebox.showerror("Sudoku", message)
        else:
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