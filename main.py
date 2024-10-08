import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import re
import webbrowser
import json  # Import JSON module for settings

# List of fonts and colors
font_list = [
    'System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial CE', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Courier', 'Courier New CE', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Text', 'Sitka Subheading', 'Sitka Heading', 'Sitka Display', 'Sitka Banner', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Times New Roman CE', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight', 'HoloLens MDL2 Assets', 'Arial Unicode MS', '@Arial Unicode MS', 'Century', 'Leelawadee', 'Microsoft Uighur', 'Wingdings 2', 'Wingdings 3', 'Tempus Sans ITC', 'Pristina', 'Papyrus', 'Mistral', 'Lucida Handwriting', 'Kristen ITC', 'Juice ITC', 'French Script MT', 'Freestyle Script', 'Bradley Hand ITC', 'Arial Narrow', 'Book Antiqua', 'Garamond', 'Monotype Corsiva', 'Century Gothic', 'Algerian', 'Baskerville Old Face', 'Bauhaus 93', 'Bell MT', 'Berlin Sans FB', 'Bernard MT Condensed', 'Bodoni MT Poster Compressed', 'Britannic Bold', 'Broadway', 'Brush Script MT', 'Californian FB', 'Centaur', 'Chiller', 'Colonna MT', 'Cooper Black', 'Footlight MT Light', 'Harlow Solid Italic', 'Harrington', 'High Tower Text', 'Jokerman', 'Kunstler Script', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Magneto', 'Matura MT Script Capitals', 'Modern No. 20', 'Niagara Engraved', 'Niagara Solid', 'Old English Text MT', 'Onyx', 'Parchment', 'Playbill', 'Poor Richard', 'Ravie', 'Informal Roman', 'Showcard Gothic', 'Snap ITC', 'Stencil', 'Viner Hand ITC', 'Vivaldi', 'Vladimir Script', 'Wide Latin', 'Tw Cen MT', 'Tw Cen MT Condensed', 'Script MT Bold', 'Rockwell Extra Bold', 'Rockwell Condensed', 'Rockwell', 'Rage Italic', 'Perpetua Titling MT', 'Perpetua', 'Palace Script MT', 'OCR A Extended', 'Maiandra GD', 'Lucida Sans Typewriter', 'Lucida Sans', 'Imprint MT Shadow', 'Haettenschweiler', 'Goudy Stout', 'Goudy Old Style', 'Gloucester MT Extra Condensed', 'Gill Sans Ultra Bold Condensed', 'Gill Sans Ultra Bold', 'Gill Sans MT Condensed', 'Gill Sans MT', 'Gill Sans MT Ext Condensed Bold', 'Gigi', 'Franklin Gothic Medium Cond', 'Franklin Gothic Heavy', 'Franklin Gothic Demi Cond', 'Franklin Gothic Demi', 'Franklin Gothic Book', 'Forte', 'Felix Titling', 'Eras Medium ITC', 'Eras Light ITC', 'Eras Demi ITC', 'Eras Bold ITC', 'Engravers MT', 'Elephant', 'Edwardian Script ITC', 'Curlz MT', 'Copperplate Gothic Light', 'Copperplate Gothic Bold', 'Century Schoolbook', 'Castellar', 'Calisto MT', 'Bookman Old Style', 'Bodoni MT Condensed', 'Bodoni MT Black', 'Bodoni MT', 'Blackadder ITC', 'Arial Rounded MT Bold', 'Agency FB', 'Berlin Sans FB Demi', 'Tw Cen MT Condensed Extra Bold', 'MT Extra', 'MS Outlook', 'Bookshelf Symbol 7', 'MS Reference Sans Serif', 'MS Reference Specialty'
]
default_color_list = ["dark orange", "hot pink", "medium orchid", "Sky Blue", "DeepSkyBlue3", "brown1"]

x = 0
y = 0

# Running Value
run: bool = True
error_mess: str = ""

def KeyWords_Loading_Error():
    global error_mess
    error_mess = f"Error ID: 1001: Failed Loading Up KeyWords"
    global run
    run = False

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("GentleMan")
        self.root.geometry("1400x800")

        self.text_area = tk.Text(self.root, wrap='word', undo=True)
        self.text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.text_area.bind('<KeyPress>', self.on_key_press)
        self.text_area.bind('<Return>', self.on_return_key)
        self.text_area.bind('<KeyRelease>', self.highlight_keywords)

        self.font_index = 0
        self.current_colors = default_color_list[:]  # Use default colors initially
        self.settings_file = "settings.json"

        # Load color settings from the settings file
        self.load_color_settings()

        self.bind_shortcuts()
        self.setup_menu()
        self.set_icon()
        self.change_theme()
        self.update_font()

        self.update_highlight_colors()

    def load_color_settings(self):
        """
        Load color settings from settings.json. If file does not exist, use default colors.
        """
        try:
            with open(self.settings_file, "r") as file:
                settings = json.load(file)
                self.current_colors = settings.get("highlight_colors", default_color_list)
        except (FileNotFoundError, json.JSONDecodeError):
            # If no settings file or invalid file, keep default colors and create a new settings file
            self.save_color_settings()

    def save_color_settings(self):
        """
        Save current highlight colors to settings.json.
        """
        settings = {"highlight_colors": self.current_colors}
        with open(self.settings_file, "w") as file:
            json.dump(settings, file, indent=4)
        print("Color settings saved to settings.json")

    def update_highlight_colors(self):
        """
        Assign colors to keyword tags for syntax highlighting.
        """
        self.text_area.tag_configure("keyword1", foreground=self.current_colors[0])
        self.text_area.tag_configure("keyword2", foreground=self.current_colors[1])
        self.text_area.tag_configure("keyword3", foreground=self.current_colors[2])
        self.text_area.tag_configure("keyword4", foreground=self.current_colors[3])
        self.text_area.tag_configure("keyword5", foreground=self.current_colors[4])
        self.text_area.tag_configure("keyword6", foreground=self.current_colors[5])

    def change_color(self, index):
        """
        Change the highlight color for the specified keyword set (index).
        """
        new_color = colorchooser.askcolor(title="Choose color")[1]
        if new_color:
            self.current_colors[index] = new_color
            self.update_highlight_colors()  # Update the highlighting with the new color
            self.save_color_settings()  # Save updated colors to settings.json
    def exit_editor(self, event=None):
        """This method exits the editor."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()
    def bind_shortcuts(self):
        self.root.bind('<Control-n>', self.new_file)
        self.root.bind('<Control-o>', self.open_file)
        self.root.bind('<Control-s>', self.save_file)
        self.root.bind('<Control-Shift-S>', self.save_as_file)
        self.root.bind('<Control-q>', self.exit_editor)
        self.root.bind('<Control-f>', self.change_font_menu)
        self.root.bind('<Control-t>', self.change_theme)
        self.root.bind('<Control-h>', self.about)

    def setup_menu(self):
        self.menu_bar = tk.Menu(self.root, font=("System", 15))
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="   File   ", menu=self.file_menu)
        self.file_menu.add_command(label="   New   ", command=self.new_file)
        self.file_menu.add_command(label="   Open   ", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="   Save   ", command=self.save_file)
        self.file_menu.add_command(label="   Save As   ", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="   Exit   ", command=self.exit_editor)

        self.appearance_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="   View   ", menu=self.appearance_menu)
        self.appearance_menu.add_command(label="   Change Theme   ", command=self.change_theme)

        self.font_menu = tk.Menu(self.appearance_menu, tearoff=0)
        self.appearance_menu.add_cascade(label="   Change Font   ", menu=self.font_menu)
        for font in font_list:
            self.font_menu.add_command(label=font, command=lambda f=font: self.change_font(f))

        self.colors_menu = tk.Menu(self.appearance_menu, tearoff=0)
        self.appearance_menu.add_cascade(label="   Change HotKeys Colors   ", menu=self.colors_menu)
        self.refresh_hotkeys_colors_menu()

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="   Help   ", menu=self.help_menu)
        self.help_menu.add_command(label="   Go to Repository (Github)   ", command=self.about)

    def refresh_hotkeys_colors_menu(self):
        """
        Refresh the 'Change HotKeys Colors' submenu to reflect current color settings.
        """
        self.colors_menu.delete(0, tk.END)  # Clear existing menu items
        for i, color in enumerate(self.current_colors):
            self.colors_menu.add_command(
                label=f"Keyword {i + 1} Color: {color}", 
                command=lambda i=i: self.change_color(i)
            )

    def update_font(self):
        font_name = font_list[self.font_index]
        self.text_area.config(font=(font_name, 12))

    def set_icon(self):
        try:
            self.root.iconbitmap("logo.png")
        except tk.TclError:
            print("Icon file 'logo.png' not found.")
    


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

    def change_font_menu(self):
        """This method is bound to Ctrl+F to open the font menu."""
        pass  # No operation needed since menu is already set up

    def change_font(self, font_name):
        try:
            self.text_area.config(font=(font_name, 12))
            print(f"Font changed to {font_name}")
        except Exception as e:
            self.show_error(f"Error changing font: {e}")
            self.text_area.config(font=("System", 12))  # Fallback to a default font

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
            new_fg = "#ccccff"
            y = 0

        self.text_area.config(background=new_bg, foreground=new_fg)

    def about(self):
        webbrowser.open("https://github.com/FCzajkowski")

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

        return "break"

    def highlight_keywords(self, event=None):
        self.text_area.tag_remove("keyword1", "1.0", tk.END)
        self.text_area.tag_remove("keyword2", "1.0", tk.END)
        self.text_area.tag_remove("keyword3", "1.0", tk.END)
        self.text_area.tag_remove("keyword4", "1.0", tk.END)
        self.text_area.tag_remove("keyword5", "1.0", tk.END)
        self.text_area.tag_remove("keyword6", "1.0", tk.END)

        keywords1 = ["try", "except", "finally", "raise", "assert",
                     "while", "break", "continue", "import",
                     "from", "as", "with", "pass", "del",
                     "global", "nonlocal", "yield", "async", "await"]
        keywords2 = ["def", "class", "return", "lambda", "yield",
                     "async", "await", "self", "__init__", "__str__",
                     "__repr__", "__call__", "__enter__", "__exit__"]
        keywords3 = ["if", "elif", "else", "for", "while",
                     "break", "continue", "in", "not in",
                     "is", "is not"]
        keywords4 = ["True", "False", "None", "and", "or",
                     "not", "is", "in", "is not", "not in"]
        keywords5 = ["str", "int", "float", "complex", "list",
                     "tuple", "dict", "set", "frozenset", "bool",
                     "bytes", "bytearray", "memoryview", "range",
                     "NoneType", "type", "object"]
        keywords6 = ["index", "insert", "mro", "pop", "copy", "append", "clear", "count", "extend", "remove", "reverse",
                     "sort", "print", "input", "len", "range", "sum",
                     "map", "filter", "sorted", "zip", "enumerate",
                     "min", "max", "open", "close", "read", "write",
                     "append", "extend", "insert", "remove", "pop",
                     "index", "count", "sort", "reverse", "join",
                     "split", "strip", "replace", "format"]

        pattern1 = r'\b(' + '|'.join(keywords1) + r')\b'
        pattern2 = r'\b(' + '|'.join(keywords2) + r')\b'
        pattern3 = r'\b(' + '|'.join(keywords3) + r')\b'
        pattern4 = r'\b(' + '|'.join(keywords4) + r')\b'
        pattern5 = r'\b(' + '|'.join(keywords5) + r')\b'
        pattern6 = r'\b(' + '|'.join(keywords6) + r')\b'
        text = self.text_area.get("1.0", tk.END).lower()

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

if __name__ == "__main__":
    if run:
        root = tk.Tk()
        app = TextEditor(root)
        root.mainloop()
    else:
        print(f"Program did not run successfully due to the following error: {error_mess}")
