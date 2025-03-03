# Import the tkinter module for GUI creation
import tkinter as tk
# Import file dialong, messagebox and font for file operations, message display and font selection
from tkinter import filedialog, messagebox, font
# Import ttk for using the combobox widget
from tkinter import ttk

# Main window setup

# Create a main Tkinter window
win = tk.Tk()
# set the title of the window
win.title("Text Editor")
# Set the background color of the main window
win.config(bg="#BAEDE6")

# Function to Open a file
def open_file():
    # Open file dialog and allow the user to select a text file
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    # If a file is selected, read the content of the file and insert it into the text area
    if file:
        # Open the file in read mode
        with open(file, "r") as f:
            text_area.delete(1.0, tk.END)   # Clear the existing content in the text area
            text_area.insert(tk.END, f.read())  # Insert the content of the file into the text area

# Function to Save a file
def save_file():
    # Open file dialog and allow the user to select a location to save the file
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    # If the user selects a location, save the content of the text area into the file
    if file:
        # Open the file in write mode
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))  # Save the content of the text area into the file

# Function to Exit the program
def program_exit():
    # Quit the main event loop and close the program
    win.quit()

# Function to enable/disable Word Wrap
def word_wrap():
    # Get the current wrap setting of the text box
    current_value = text_area.cget("wrap")
    # If word wrap is currently off
    if current_value == "none":
        # Enable word wrap
        text_area.config(wrap="word")
    else:
        # Disable word wrap
        text_area.config(wrap="none")

# Function to change font style
def change_font():
    
    # Open a new window to choose font style and size
    def apply_font():
        # Get the selected font style
        selected_font = font_combobox.get()
        # Get the selected font size
        selected_size = size_combobox.get()
        # Apply the selected font style and size to the text area
        text_area.config(font=(selected_font, selected_size))
        # Close the font selection window
        font_win.destroy()

    # Create a new top-level window for font selection
    font_win = tk.Toplevel(win)
    # Set the title of the font window
    font_win.title("Choose Font")

    # Define the vailabe fonts and sizes
    fonts = ["Arial", "Helvetica", "Times New Roman", "Courier", "Verdana", "Georgia", "Palatino", "Garamond", "Bookman", "Comic Sans MS"]
    sizes = [str(i) for i in range(8, 31)]  # Font sizes from 8 to 30

    # Create a label and combobox for font selection
    tk.Label(font_win, text="Select Font: ").pack() # Label for font selection
    font_combobox = ttk.Combobox(font_win, values=fonts)    # Dropdown for font selection
    font_combobox.set("Arial")  # Default font set to Arial
    font_combobox.pack()

    tk.Label(font_win, text="Select Size: ").pack()  # Label for size selection
    size_combobox = ttk.Combobox(font_win, values=sizes)    # Dropdown for size selection
    size_combobox.set("11")  # Default size set to 11
    size_combobox.pack()

    # Create an Apply button to apply the selected font style and size
    tk.Button(font_win, text="Apply", command=apply_font).pack()


# Create a Text widget (or the Text area) for typing text
text_area = tk.Text(win, wrap="word", font=("Arial", 11), undo=True, bg= "#BAEDE6", fg="black")
# Pack the Text widget to the window
text_area.pack(expand=True, fill=tk.BOTH)

# Create a Menu Bar
menu_bar = tk.Menu(win) # Create a menu bar for the window

# Create a File Menu (for opening, saving, and exiting the program)

# Create a file menu with no tearoff feature
file_menu = tk.Menu(menu_bar, tearoff=0)
# Add a New command to clear the text area
file_menu.add_command(label="New", command=lambda: text_area.delete(1.0, tk.END))
# Add an Open command to open a file
file_menu.add_command(label="Open", command=open_file)
# Add a Save command to save the content of the text area into a file
file_menu.add_command(label="Save", command=save_file)
# Add a separator line between menu items
file_menu.add_separator()
# Add an Exit command to close the program
file_menu.add_command(label="Exit", command = program_exit)
# Add the file menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an Edit Menu (for toggling word wrap)

# Create an Edit Menu with no tearoff feature
edit_menu = tk.Menu(menu_bar, tearoff=0)
# Add a Word Wrap command to enable/disable word wrap
edit_menu.add_command(label="Word Wrap", command=word_wrap)
# Add the Edit menu to the menu bar
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create a Format Menu (for customizaion of text)

# Create a Format Menu with no tearoff feature
format_menu = tk.Menu(menu_bar, tearoff=0)
# Add a Font command to change the font style and size
format_menu.add_command(label="Font", command=change_font)
# Add the Format menu to the menu bar
menu_bar.add_cascade(label="Format", menu=format_menu)

# Attach the Menu to the window
win.config(menu=menu_bar)   # Set the menu bar for the window

# Start the Tkinter event loop
win.mainloop()

