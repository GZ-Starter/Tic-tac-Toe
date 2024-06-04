import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title(" ")
        self.current_player = "X"
        self.size = 3  # Default size of the board
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        # Create a frame for the title with a different background color
        title_frame = tk.Frame(self.root, bg="lightblue", padx=10, pady=10)
        title_frame.pack(side="top", fill="x")

        # Create a label for the title inside the title frame
        title_label = tk.Label(title_frame, text="Tic Tac Toe", font=("Arial", 14, "bold"), bg="lightblue")
        title_label.pack()

        # Create a frame for the content with a different background color
        content_frame = tk.Frame(self.root, bg="white", padx=5, pady=5)
        content_frame.pack(side="top", fill="both", expand=True)

        # Create buttons for the game board inside the content frame
        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(content_frame, text="", font=("Arial", 35), width=3, height=1,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col, padx=1, pady=1)
                button.bind("<Enter>", lambda event, btn=button: btn.config(bg="lightgray"))
                button.bind("<Leave>", lambda event, btn=button: btn.config(bg="SystemButtonFace"))
                self.buttons[row][col] = button

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu", menu=game_menu)
        game_menu.add_command(label="Reset", command=self.reset_game)
        game_menu.add_command(label="Set Board Size", command=self.show_size_window)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.root.quit)

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
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg=self.get_player_color(self.current_player))
            if self.check_winner():
                self.end_game(f"Player {self.current_player} wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def get_player_color(self, player):
        return "blue" if player == "X" else "red"

    def check_winner(self):
        for row in range(self.size):
            if all(self.board[row][col] == self.current_player for col in range(self.size)):
                return True
        for col in range(self.size):
            if all(self.board[row][col] == self.current_player for row in range(self.size)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == self.current_player for i in range(self.size)):
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
