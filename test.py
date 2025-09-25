import tkinter as tk
root = tk.Tk()
num = 1
root.title("test_box")

fram = tk.Frame(root)

fram.grid(row=5, column=5)

entry = tk.Entry(fram, text="enter text")
e_button = tk.Button(fram)
e_button.grid(row= 7, column=7)
entry.grid(row=6, column=6)
root.mainloop()

