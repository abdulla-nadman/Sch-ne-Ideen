import random #Siehe Zeile 16
import tkinter as tk

class Lilith:
    def __init__(self):
        self.name = "Lilith"
        self.status = "in Bearbeitung"

    def introduce(self):
        greeting = f"Hallo, ich bin {self.name}, deine persoenliche KI."
        status_info = f"Derzeit befinde ich mich noch {self.status}."
        return greeting, status_info

    def respond_to_user(self, user_input):
        responses = ["Ich verstehe.", "Interessant!", "Vielen Dank fuer die Information."]
        return random.choice(responses)



# Erstelle eine Instanz des Tkinter-Fensters
root = tk.Tk()
root.title("Machine Learning und GUI Demo")
root.geometry("800x600")  # Neue Groesse des Fensters (Breite x Hoehe)

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fenstergroesse
WIDTH, HEIGHT = 500, 500


# Erstelle eine Canvas
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



# Fuege ein Frame der Canvas hinzu
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Instanziierung von Lilith
lilith = Lilith()

# Starte die Tkinter-Schleife, damit das Fenster angezeigt wird und auf Ereignisse reagieren kann
def add_buttons():
    for i in range(10):
        button = tk.Button(frame, text=f"Button {i+1}")
        button.pack(pady=5)

root.title("Button Demo")

main_button = tk.Button(root, text="Weitere Buttons anzeigen", command=add_buttons)
main_button.pack(pady=10)

# Setze das Ereignis fuer das Mausrad
def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int(event.delta/120), "units")

canvas.bind("<MouseWheel>", on_mouse_wheel)

root.mainloop()
















#Ab hier nur noch Notizen

# Initialisierung von Pygame
pygame.init()

# Erstellen des Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lilith Chat")


# Hauptprogrammschleife
running = True
while running:
    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hintergrund zeichnen
    screen.fill(WHITE)

    # Text anzeigen
    font = pygame.font.Font(None, 24)
    greeting, status_info = lilith.introduce()
    
    greeting_text = font.render(greeting, True, BLACK)
    greeting_rect = greeting_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
    screen.blit(greeting_text, greeting_rect)
    
    status_text = font.render(status_info, True, BLACK)
    status_rect = status_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
    screen.blit(status_text, status_rect)

    # Bildschirm aktualisieren
    pygame.display.flip()

# Pygame beenden
pygame.quit()
