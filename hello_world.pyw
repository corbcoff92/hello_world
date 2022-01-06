import tkinter as tk

# Create & Configure main window
window = tk.Tk()
window.title('Hello')
window.columnconfigure(0, minsize=225, weight=1)
window.rowconfigure(0, minsize=100, weight=1)
window.rowconfigure(1, minsize=100, weight=1)

# Create 'Hello World' label and add it to the main window
label = tk.Label(master=window, text='Hello World!', font=('Times', 25))
label.grid(column=0, row=0)

# Create 'Exit' button and add it to the main window
button = tk.Button(master=window, text='Exit', width=10, pady=10, command=window.destroy)
button.grid(column=0, row=1, pady=25)

# Run main loop of main window
window.mainloop()