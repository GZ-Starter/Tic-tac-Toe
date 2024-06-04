import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.size = 3  # Default size of the board
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(self.root, text="", font=("Arial", 30), width=3, height=1,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                button.bind("<Enter>", lambda event, btn=button: btn.config(bg="lightgray"))
                button.bind("<Leave>", lambda event, btn=button: btn.config(bg="SystemButtonFace"))
                self.buttons[row][col] = button

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

       
        game_menu = tk.Menu(menubar, tearoff=0, font=("Arial", 12))
        menubar.add_cascade(label="Menu", menu=game_menu)

        theme_menu = tk.Menu(game_menu, tearoff=0)
        game_menu.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Default", command=self.set_default_theme)
        theme_menu.add_command(label="Dark", command=self.set_dark_theme)

        game_menu.add_command(label="Reset", command=self.reset_game)
        game_menu.add_command(label="Set Board Size", command=self.show_size_window)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.root.quit)

    def set_default_theme(self):
        self.root.configure(bg="white")
        self.root.option_add("*Background", "white")
        self.root.option_add("*Foreground", "black")

    def set_dark_theme(self):
        self.root.configure(bg="#2C2F33")
        self.root.option_add("*Background", "#2C2F33")
        self.root.option_add("*Foreground", "white")

    def reset_game(self):
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                self.buttons[row][col].config(text="")
        self.current_player = "X"

    def show_size_window(self):
        size_window = tk.Toplevel(self.root)
        size_window.title("Set Board Size")

        size_label = tk.Label(size_window, text=f"Current Size: {self.size}x{self.size}", font=("Arial", 10))
        size_label.pack(pady=10)

        def increase_size():
            if self.size < 10:
                self.size += 1
                size_label.config(text=f"Current Size: {self.size}x{self.size}")

        def decrease_size():
            if self.size > 3:
                self.size -= 1
                size_label.config(text=f"Current Size: {self.size}x{self.size}")

        plus_button = tk.Button(size_window, text="+", font=("Arial", 10), command=increase_size)
        plus_button.pack(side="right", padx=20, pady=20)

        minus_button = tk.Button(size_window, text="-", font=("Arial", 10), command=decrease_size)
        minus_button.pack(side="left", padx=20, pady=20)

        set_button = tk.Button(size_window, text="Set Size", font=("Arial", 10), command=lambda: self.set_board_size(size_window))
        set_button.pack(pady=20)

    def set_board_size(self, size_window):
        size_window.destroy()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.create_widgets()
        self.create_menu()

    def on_button_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner(self.current_player):
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg=self.get_player_color(self.current_player))
            if self.check_winner(self.current_player):
                self.end_game(f"Player {self.current_player} wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.root.after(500, self.ai_move)  # 500 ms delay before AI move

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        depth_limit = 3 if self.size <= 4 else 2  # Adjust depth limit for larger boards
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == "":
                    self.board[row][col] = "O"
                    score = self.minimax(self.board, 0, False, depth_limit)
                    self.board[row][col] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        if best_move:
            row, col = best_move
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", fg=self.get_player_color("O"))
            if self.check_winner("O"):
                self.end_game("Player O wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = "X"

    def minimax(self, board, depth, is_maximizing, depth_limit):
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if self.check_draw() or depth >= depth_limit:
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(self.size):
                for col in range(self.size):
                    if board[row][col] == "":
                        board[row][col] = "O"
                        score = self.minimax(board, depth + 1, False, depth_limit)
                        board[row][col] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(self.size):
                for col in range(self.size):
                    if board[row][col] == "":
                        board[row][col] = "X"
                        score = self.minimax(board, depth + 1, True, depth_limit)
                        board[row][col] = ""
                        best_score = min(score, best_score)
            return best_score

    def get_player_color(self, player):
        return "blue" if player == "X" else "red"

    def check_winner(self, player):
        # Check rows
        for row in range(self.size):
            if all(self.board[row][col] == player for col in range(self.size)):
                return True
        # Check columns
        for col in range(self.size):
            if all(self.board[row][col] == player for row in range(self.size)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def end_game(self, result):
        messagebox.showinfo("Game Over", result)
        self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
