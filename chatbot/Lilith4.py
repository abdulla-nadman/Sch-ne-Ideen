import tkinter as tk
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
            button = tk.Button(root, text=f"Button {i+1}")
            button.pack(pady=5)
            added_buttons.append(button)

# Erstelle eine Instanz des Tkinter-Fensters
root = tk.Tk()
root.title("Machine Learning und GUI Demo")
root.geometry("700x700")

added_buttons = []  # Liste zur Verfolgung der hinzugefuegten Buttons

main_button = tk.Button(root, text="Weitere Buttons anzeigen", command=add_buttons)
main_button.pack(pady=10)

# Label fuer Genauigkeit
accuracy_label = tk.Label(root, text="")
accuracy_label.pack(pady=20)

# Button zum Trainieren des Modells und Anzeigen der Genauigkeit
train_button = tk.Button(root, text="Modell trainieren und Genauigkeit anzeigen", command=train_model_and_display_accuracy)
train_button.pack(pady=10)

root.mainloop()
