import tkinter as tk
from tkinter import ttk
import sympy as sp

def calculator():
    def calculate():
        try:
            expression = entry.get()
            conclusion = sp.sympify(expression)
            conclusion_label.config(text="Conclusion: " + str(conclusion))
            history_listbox.insert(tk.END, expression + " = " + str(conclusion))
        except Exception as e:
            conclusion_label.config(text="unerwarteter Fehler!")

    def clean():
        entry.delete(0, tk.END)

    def undo():
        current_text = entry.get()
        entry.delete(len(current_text)-1, tk.END)

    def exit():
        for i in range(100, 0, -1):
            root.attributes("-alpha", i / 100)
            root.update_idletasks()
            root.after(10)
        root.quit()

    def opening_animation():
        for i in range(1, 101):
            root.attributes("-alpha", i / 100)
            root.update_idletasks()
            root.after(10)

    def cleared_history():
            history_listbox.delete(0, tk.END)

    root = tk.Tk()
    root.title("Rechner - von em41py")
    root.geometry("400x700")
    root.configure(bg="#2C3E50")
    root.attributes("-alpha", 0)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=8)
    style.configure("TLabel", font=("Arial", 14), background="#2C3E50", foreground="white")
    style.configure("TEntry", font=("Arial", 20), padding=10)

    entry = ttk.Entry(root, font=("Arial", 20), width=15, justify='right')
    entry.pack(pady=20)

    conclusion_label = ttk.Label(root, text="Ergebnis: ")
    conclusion_label.pack(pady=10)

    history_label = ttk.Label(root, text="Verlauf: ")
    history_label.pack(pady=10)

    history_listbox = tk.Listbox(root, height=6, width=35, font=("Arial", 10), selectmode=tk.SINGLE, bd=0, bg="#34495E", fg="white")
    history_listbox.pack(pady=10)

    history_listbox.config(selectbackground="#2980B9", selectforeground="white")

    button_frame = tk.Frame(root, bg="#2C3E50")
    button_frame.pack()

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("(", 4, 2), (")", 4, 3),
        ("C", 5, 0), ("CE", 5, 1), ("=", 5, 2), ("+", 5, 3),
        ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("log", 6, 3),
    ]

    for (text, row, col) in buttons:
        if text == "=":
            button = ttk.Button(button_frame, text=text, command=calculate)
        elif text == "C":
            button = ttk.Button(button_frame, text=text, command=clean)
        elif text == "CE":
            button = ttk.Button(button_frame, text=text, command=undo)
        else:
            button = ttk.Button(button_frame, text=text, command=lambda t=text: entry.insert(tk.END, t))
        
        button.grid(row=row, column=col, padx=5, pady=5)

    cleared_history_btn = ttk.Button(root, text="Verlauf löschen", command=cleared_history)
    cleared_history_btn.place(x=320, y=90)

    ttk.Button(root, text="beenden", command=exit).place(x=320, y=150)

    opening_animation()

    root.mainloop()

calculator()
