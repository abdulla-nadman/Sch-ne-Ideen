from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from tkinter import Canvas, Scrollbar
import tkinter as tk

# Daten laden
iris = load_iris()
X, y = iris.data, iris.target

# Daten aufteilen in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell initialisieren und trainieren
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Vorhersagen treffen
predictions = model.predict(X_test)

# Genauigkeit berechnen
accuracy = accuracy_score(y_test, predictions)
print("Genauigkeit:", accuracy)

# Erstelle eine Instanz des Tkinter-Fensters
root = tk.Tk()
root.title("Machine Learning und GUI Demo")
root.geometry("800x600")  # Neue Groesse des Fensters (Breite x Hoehe)

# Setze den Titel des Fensters
root.title("Mein erstes Fenster")

# Setze die Groesse des Fensters
root.geometry("400x300")

# Fuege Widgets oder Elemente zum Fenster hinzu, z.B. Label, Button, etc.
label = tk.Label(root, text="Hallo, Welt!")
label.pack(pady=20)

button = tk.Button(root, text="Klick mich!")
button.pack()

# Starte die Tkinter-Schleife, damit das Fenster angezeigt wird und auf Ereignisse reagieren kann
def add_buttons():
    for i in range(10):
        button = tk.Button(root, text=f"Button {i+1}")
        button.pack(pady=5)

root.title("Button Demo")

main_button = tk.Button(root, text="Weitere Buttons anzeigen", command=add_buttons)
main_button.pack(pady=10)


def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int(event.delta/120), "units")

    # Erstelle eine Canvas
canvas = Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Erstelle einen Scrollbar
scrollbar = Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Verbinde die Scrollbar mit der Canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Fuege ein Frame der Canvas hinzu
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Setze das Ereignis fuer das Mausrad
canvas.bind("<MouseWheel>", on_mouse_wheel)


root.mainloop()
