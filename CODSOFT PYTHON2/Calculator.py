import tkinter as tk

def click(event):
    global expression
    expression += event.widget.cget("text")
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Initialize Tkinter
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

expression = ""
equation = tk.StringVar()

# Result Display
result_frame = tk.Frame(root, bg="lightblue")
result_frame.pack(expand=True, fill="both")
result_entry = tk.Entry(result_frame, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4, bg="powder blue", justify='right')
result_entry.pack(expand=True, fill="both")

# Buttons
button_frame = tk.Frame(root, bg="grey")
button_frame.pack(expand=True, fill="both")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

i = 0
for b in buttons:
    button = tk.Button(button_frame, text=b, font=('arial', 18, 'bold'), bd=8, relief='ridge', bg="white")
    button.grid(row=i//4, column=i%4, sticky="nsew")
    button.bind("<Button-1>", click)
    i += 1

# Clear and Delete Buttons
clear_frame = tk.Frame(root, bg="lightgreen")
clear_frame.pack(expand=True, fill="both")

clear_button = tk.Button(clear_frame, text="Clear", font=('arial', 18, 'bold'), bd=8, relief='ridge', bg="red", command=clear)
clear_button.pack(side="left", expand=True, fill="both")

delete_button = tk.Button(clear_frame, text="Delete", font=('arial', 18, 'bold'), bd=8, relief='ridge', bg="orange", command=delete)
delete_button.pack(side="left", expand=True, fill="both")

equal_button = tk.Button(clear_frame, text="=", font=('arial', 18, 'bold'), bd=8, relief='ridge', bg="yellow", command=equal)
equal_button.pack(side="left", expand=True, fill="both")

# Grid configuration for button_frame
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
    button_frame.grid_rowconfigure(i, weight=1)

# Start the GUI
root.mainloop()
