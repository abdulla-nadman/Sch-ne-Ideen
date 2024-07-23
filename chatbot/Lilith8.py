import tkinter as tk
from tkinter import ttk

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Notebook Beispiel")

# Erstellen des Notebook-Widgets
notebook = ttk.Notebook(root)

# Erstellen von Registerkarten
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Hinzufuegen von Registerkarten zum Notebook
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')

# Platzieren von Widgets innerhalb der Registerkarten
label1 = ttk.Label(tab1, text="Inhalt von Tab 1")
label1.pack(padx=10, pady=10)

label2 = ttk.Label(tab2, text="Inhalt von Tab 2")
label2.pack(padx=10, pady=10)

# Packen des Notebook-Widgets
notebook.pack(fill='both', expand=True)

# Starten der GUI-Schleife
root.mainloop()

