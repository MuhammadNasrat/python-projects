import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Text Editor")

        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(fill="both", expand=1)

        self.scrollbar = ttk.Scrollbar(self.text_area)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        self.menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=self.menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)
                self.root.title(f"Python Text Editor - {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                self.root.title(f"Python Text Editor - {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def exit_app(self):
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.geometry("800x600")
    root.mainloop()
