import tkinter as tk
from tkinter import Canvas, Scrollbar
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def train_model_and_display_accuracy():
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
    accuracy_label.config(text=f"Genauigkeit: {accuracy}")

def add_buttons():
    if not added_buttons:
        for i in range(114):
            button = tk.Button(inner_frame, text=f"Button {i+1}")
            button.pack(pady=5)
            added_buttons.append(button)

# Erstelle eine Instanz des Tkinter-Fensters
root = tk.Tk()
root.title("Machine Learning und GUI Demo")

# Erstelle ein Canvas fuer Scrollbar
canvas = Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Fuege einen Rahmen zum Canvas hinzu
inner_frame = tk.Frame(canvas)
inner_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Fuege Scrollbar hinzu
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

# Konfiguriere das Canvas, um mit der Scrollbar zu arbeiten
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Fuege das innere Rahmen zum Canvas hinzu
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

added_buttons = []  # Liste zur Verfolgung der hinzugefuegten Buttons

main_button = tk.Button(inner_frame, text="WeitereButtons anzeigen", command=add_buttons)
main_button.pack(pady=10)

# Label fuer Genauigkeit
accuracy_label = tk.Label(inner_frame, text="")
accuracy_label.pack(pady=20)

# Button zum Trainieren des Modells und Anzeigen der Genauigkeit
train_button = tk.Button(inner_frame, text="Modell trainieren und Genauigkeit anzeigen", command=train_model_and_display_accuracy)
train_button.pack(pady=10)

root.mainloop()
