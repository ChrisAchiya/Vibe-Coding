import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas

def calculate_grade():
    try:
        name = name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a student's name.")
            return
        
        marks = []
        for i in range(3):
            mark_str = mark_entries[i].get().strip()
            if not mark_str:
                messagebox.showerror("Error", f"Please enter mark for subject {i+1}.")
                return
            mark = float(mark_str)
            marks.append(mark)
        
        average = sum(marks) / 3
        
        if average >= 75:
            grade = 'A'
        elif average >= 60:
            grade = 'B'
        elif average >= 40:
            grade = 'C'
        else:
            grade = 'Fail'
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "------------------------------\n")
        result_text.insert(tk.END, f"Name : {name}\n")
        result_text.insert(tk.END, f"Average: {average:.1f}\n")
        result_text.insert(tk.END, f"Grade : {grade}\n")
        result_text.insert(tk.END, "------------------------------\n")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for marks.")

def clear_fields():
    name_entry.delete(0, tk.END)
    for entry in mark_entries:
        entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# Create main window
root = tk.Tk()
root.title("Student Grade Calculator")

# Create gradient background
def create_gradient(canvas, width, height, color1, color2):
    """Create a vertical gradient from color1 to color2"""
    for i in range(height):
        # Calculate color for this line
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)
        color = f'#{r:04x}{g:04x}{b:04x}'
        canvas.create_line(0, i, width, i, fill=color)

canvas = Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Bind resize event to redraw gradient
def on_resize(event):
    canvas.delete("all")
    create_gradient(canvas, event.width, event.height, "#667eea", "#764ba2")

root.bind("<Configure>", on_resize)

# Create a frame for the content with transparent background
content_frame = tk.Frame(root)
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Name input
tk.Label(content_frame, text="Student Name:", fg='#ffffff', font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(content_frame, bg='#ffffff', fg='#2e4057', font=('Arial', 10))
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Marks inputs
mark_entries = []
for i in range(3):
    tk.Label(content_frame, text=f"Mark for Subject {i+1}:", fg='#ffffff', font=('Arial', 10, 'bold')).grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(content_frame, bg='#ffffff', fg='#2e4057', font=('Arial', 10))
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    mark_entries.append(entry)

# Buttons
calculate_button = tk.Button(content_frame, text="Calculate Grade", command=calculate_grade, bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'), relief='raised', bd=3)
calculate_button.grid(row=4, column=0, padx=10, pady=10)

clear_button = tk.Button(content_frame, text="Clear", command=clear_fields, bg='#f44336', fg='white', font=('Arial', 10, 'bold'), relief='raised', bd=3)
clear_button.grid(row=4, column=1, padx=10, pady=10)

# Result display
tk.Label(content_frame, text="Result:", fg='#ffffff', font=('Arial', 10, 'bold')).grid(row=5, column=0, padx=10, pady=5, sticky="ne")
result_text = tk.Text(content_frame, height=6, width=30, bg='#ffffff', fg='#2e4057', font=('Arial', 10), relief='sunken', bd=2)
result_text.grid(row=5, column=1, padx=10, pady=5)

# Run the GUI
root.mainloop()