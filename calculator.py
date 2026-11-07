import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.expression = ""

        # Display Screen
        self.display = tk.Entry(
            root, 
            font=("Arial", 24), 
            bg="#181825", 
            fg="#cdd6f4", 
            bd=0, 
            justify="right", 
            insertbackground="#cdd6f4"
        )
        self.display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=15)

        # Button Layout
        buttons = [
            ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("±", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
        ]

        # Frame for buttons
        btn_frame = tk.Frame(root, bg="#1e1e2e")
        btn_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configure Grid
        for i in range(6):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)

        # Create Buttons
        for text, row, col in buttons:
            self.create_button(btn_frame, text, row, col)

        # Keyboard Bindings
        self.root.bind("<Key>", self.handle_keypress)

    def create_button(self, frame, text, row, col):
        bg_color = "#313244"
        fg_color = "#cdd6f4"

        if text in ["/", "*", "-", "+", "="]:
            bg_color = "#fab387"
            fg_color = "#11111b"
        elif text in ["C", "⌫", "%", "±"]:
            bg_color = "#45475a"

        btn = tk.Button(
            frame, 
            text=text, 
            font=("Arial", 14, "bold"), 
            bg=bg_color, 
            fg=fg_color,
            activebackground="#585b70",
            activeforeground="#ffffff",
            bd=0,
            command=lambda: self.on_button_click(text)
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.evaluate()
            return
        elif char == "±":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
        else:
            self.expression += str(char)

        self.update_display(self.expression)

    def evaluate(self):
        try:
            # Replace visual symbols with valid Python operators
            formatted_expr = self.expression.replace("%", "/100")
            result = str(eval(formatted_expr))
            self.update_display(result)
            self.expression = result
        except ZeroDivisionError:
            self.update_display("Error: Division by 0")
            self.expression = ""
        except Exception:
            self.update_display("Error")
            self.expression = ""

    def update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)

    def handle_keypress(self, event):
        key = event.char
        if key in "0123456789.+-*/%":
            self.on_button_click(key)
        elif event.keysym == "Return":
            self.on_button_click("=")
        elif event.keysym == "BackSpace":
            self.on_button_click("⌫")
        elif event.keysym == "Escape":
            self.on_button_click("C")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
