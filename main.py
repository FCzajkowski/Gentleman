import tkinter as tk
from tkinter import filedialog, messagebox
import re
import webbrowser
font_list = ["Consolas", "Courier", "Helvetica",
             "Times New Roman",
             "Georgia",
             "Lucida Console", "Verdana",
             "System"]
x = 0
y = 0
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal++")
        self.root.geometry("1200x800")

        # Main text area
        self.text_area = tk.Text(self.root, wrap='word', undo=True)
        self.text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.text_area.bind('<KeyPress>', self.on_key_press)
        self.text_area.bind('<Return>', self.on_return_key)
        self.text_area.bind('<KeyRelease>', self.highlight_keywords)

        # Menu bar
        self.menu_bar = tk.Menu(self.root, font=(font_list[x], 15))  # Set larger font size for the menu bar
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="   File   ", menu=self.file_menu)
        self.file_menu.add_command(label="   New   ", command=self.new_file)
        self.file_menu.add_command(label="   Open   ", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="   Save   ", command=self.save_file)
        self.file_menu.add_command(label="   Save As   ", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="   Exit   ", command=self.exit_editor)

        # Appearance menu
        self.appearance_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="   View   ", menu=self.appearance_menu)
        self.appearance_menu.add_command(label="   Change Font   ", command=self.change_font)
        self.appearance_menu.add_command(label="   Change Theme   ", command=self.change_theme)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="   Help   ", menu=self.help_menu)
        self.help_menu.add_command(label="   Go to Repository (Github)   ", command=self.about)
        self.current_file = None

        # Set application icon (logo)
        self.set_icon()
        self.change_theme()
        self.text_area.config(font=(font_list[x], 15))
        # Define the tag for highlighting keywords
        self.text_area.tag_configure("keyword1", foreground="dark orange")
        self.text_area.tag_configure("keyword2", foreground="hot pink")
        self.text_area.tag_configure("keyword3", foreground="medium orchid")
        self.text_area.tag_configure("keyword4", foreground="sky blue")
        self.text_area.tag_configure("keyword5", foreground="green2")
        self.text_area.tag_configure("keyword6", foreground="brown1")
    def about(self):
        webbrowser.open("https://github.com/FCzajkowski")
    def change_theme(self):
        current_bg = self.text_area.cget("background")
        current_fg = self.text_area.cget("foreground")
        global y
        y += 1
        if y == 1:
            new_bg = "white"
            new_fg = "#16161d"
        else:
            new_bg = "#16161d"
            new_fg = "#EEE"
            y = 0

        self.text_area.config(background=new_bg, foreground=new_fg)
    def set_icon(self):
        try:
            self.root.iconbitmap("logo.png")  # Replace "logo.ico" with your PNG file
        except tk.TclError:
            print("Icon file 'logo.png' not found.")

    # Your existing methods (new_file, open_file, save_file, etc.) remain unchanged



    def new_file(self):
        if self.text_area.get("1.0", tk.END) != "\n":
            if messagebox.askyesno("Save File", "Do you want to save the current file?"):
                self.save_as_file()
        self.text_area.delete("1.0", tk.END)
        self.current_file = None
        self.root.title("Untitled - terminal++")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, content)
            self.current_file = file_path
            self.root.title(f"{file_path} - terminal++")

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                 filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
            self.current_file = file_path
            self.root.title(f"{file_path} - terminal++")

    def change_font(self):
        global x
        x = (x + 1) % len(font_list)
        self.text_area.config(font=(font_list[x], 15))
        print(f"Font changed to {font_list[x]}")

    def on_key_press(self, event):
        current_index = self.text_area.index(tk.INSERT)
        next_char = self.text_area.get(current_index)
        if event.char == '"' and next_char != '"':
            self.text_area.insert(tk.INSERT, '"')
            self.text_area.mark_set(tk.INSERT, f"{tk.INSERT}-1c")
        elif event.char == '(' and next_char != ')':
            self.text_area.insert(tk.INSERT, ')')
            self.text_area.mark_set(tk.INSERT, f"{tk.INSERT}-1c")
        elif event.char == "'" and next_char != "'":
            self.text_area.insert(tk.INSERT, "'")
            self.text_area.mark_set(tk.INSERT, f"{tk.INSERT}-1c")
        elif event.char == '[' and next_char != ']':
            self.text_area.insert(tk.INSERT, "]")
            self.text_area.mark_set(tk.INSERT, f"{tk.INSERT}-1c")
        elif event.char == '{' and next_char != '}':
            self.text_area.insert(tk.INSERT, "}")
            self.text_area.mark_set(tk.INSERT, f"{tk.INSERT}-1c")

    def on_return_key(self, event):
        current_index = self.text_area.index(tk.INSERT)
        line_start = self.text_area.index(f"{current_index} linestart")
        line_end = self.text_area.index(f"{current_index} lineend")
        line_content = self.text_area.get(line_start, line_end)

        indentation = ""
        for char in line_content:
            if char.isspace():
                indentation += char
            else:
                break

        if line_content.strip().endswith(':'):
            self.text_area.insert(current_index, f"\n{indentation}\t")
            self.text_area.mark_set(tk.INSERT, f"{float(current_index) + 1} lineend")
        else:
            self.text_area.insert(current_index, f"\n{indentation}")

        return "break"  # Prevent default newline behavior

    def highlight_keywords(self, event=None):
        self.text_area.tag_remove("keyword1", "1.0", tk.END)
        self.text_area.tag_remove("keyword2", "1.0", tk.END)
        self.text_area.tag_remove("keyword3", "1.0", tk.END)
        self.text_area.tag_remove("keyword4", "1.0", tk.END)
        self.text_area.tag_remove("keyword5", "1.0", tk.END)
        self.text_area.tag_remove("keyword6", "1.0", tk.END)

        keywords1 = ["import", "if", "else", "elif", "for", "while", "try", "except", "finally", "with", "as", "pass",
                     "break", "continue", "yield", "nonlocal", "from", "raise"]
        keywords2 = ["def", "class", "return", "lambda", "global"]
        keywords3 = ["if", "else", "for", "while", "range"]
        keywords4 = ["str", "int", "float", "complex", "bool", "bytes", "bytearray", "memoryview", "NoneType", "list",
                     "dict", "tuple", "self", "print", "printf", "println", ]
        keywords5 = ['True', 'False', 'None', '__init__']
        keywords6 = ["index", "insert", "mro", "pop", "copy", "append", "clear", "count", "extend", "remove", "reverse",
                     "sort"]

        pattern1 = r'\b(' + '|'.join(keywords1) + r')\b'
        pattern2 = r'\b(' + '|'.join(keywords2) + r')\b'
        pattern3 = r'\b(' + '|'.join(keywords3) + r')\b'
        pattern4 = r'\b(' + '|'.join(keywords4) + r')\b'
        pattern5 = r'\b(' + '|'.join(keywords5) + r')\b'
        pattern6 = r'\b(' + '|'.join(keywords6) + r')\b'
        text = self.text_area.get("1.0", tk.END)

        for match in re.finditer(pattern1, text):
            start = self.text_area.index(f"1.0+{match.start()}c")
            end = self.text_area.index(f"1.0+{match.end()}c")
            self.text_area.tag_add("keyword1", start, end)

        for match in re.finditer(pattern2, text):
            start = self.text_area.index(f"1.0+{match.start()}c")
            end = self.text_area.index(f"1.0+{match.end()}c")
            self.text_area.tag_add("keyword2", start, end)

        for match in re.finditer(pattern3, text):
            start = self.text_area.index(f"1.0+{match.start()}c")
            end = self.text_area.index(f"1.0+{match.end()}c")
            self.text_area.tag_add("keyword3", start, end)

        for match in re.finditer(pattern4, text):
            start = self.text_area.index(f"1.0+{match.start()}c")
            end = self.text_area.index(f"1.0+{match.end()}c")
            self.text_area.tag_add("keyword4", start, end)

        for match in re.finditer(pattern5, text):
            start = self.text_area.index(f"1.0+{match.start()}c")
            end = self.text_area.index(f"1.0+{match.end()}c")
            self.text_area.tag_add("keyword5", start, end)

        for match in re.finditer(pattern6, text):
            start = self.text_area.index(f"1.0+{match.start()}c")
            end = self.text_area.index(f"1.0+{match.end()}c")
            self.text_area.tag_add("keyword6", start, end)

    def exit_editor(self):
        if self.text_area.get("1.0", tk.END) != "\n":
            if messagebox.askyesno("Save File", "Do you want to save the current file?"):
                self.save_as_file()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
