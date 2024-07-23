import tkinter as tk
from tkinter import Canvas, Scrollbar
from tkinter.ttk import Notebook

def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int(event.delta/120), "units")

root = tk.Tk()
root.title("Lilith")

notebook = Notebook(root)
notebook.pack(fill="both", expand=True)

# Erstelle Tab 1
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Tab 1")

# Fuege ein Canvas und eine Scrollbar zu Tab 1 hinzu
canvas = Canvas(tab1)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(tab1, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Fuege ein Frame zu Canvas hinzu
inner_frame = tk.Frame(canvas)
inner_frame_id = canvas.create_window((0, 0), window=inner_frame, anchor="center")

# Fuege Widgets zum inneren Frame hinzu
buttons = []
for i in range(114):
    button = tk.Button(inner_frame, text=f"Button {i+1}")
    buttons.append(button)

# Berechne die Mitte des Canvas und passe die Position des inneren Frames entsprechend an
def center_inner_frame(event):
    canvas.update_idletasks()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    frame_width = sum(button.winfo_reqwidth() for button in buttons)
    frame_height = sum(button.winfo_reqheight() for button in buttons)

    x_offset = (canvas_width - frame_width) // 2
    y_offset = (canvas_height - frame_height) // 2

    canvas.coords(inner_frame_id, x_offset, y_offset)

inner_frame.bind("<Configure>", center_inner_frame)

# Platzieren Sie die Buttons im inneren Frame
for button in buttons:
    button.pack(pady=5, padx=5)

# Erstelle Tab 2
tab2 = tk.Frame(notebook)
notebook.add(tab2, text="Tab 2")

root.mainloop()



