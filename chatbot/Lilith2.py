# -*- coding: utf-8 -*-

import pygame
import random

class Lilith:
    def __init__(self):
        self.name = "Lilith"
        self.status = "in Bearbeitung"

    def introduce(self):
        return f"Hallo, ich bin {self.name}, deine persoenliche KI. Derzeit befinde ich mich noch {self.status}."

    def respond_to_user(self, user_input):
        responses = ["Ich verstehe.", "Interessant!", "Vielen Dank fuer die Information."]
        return random.choice(responses)

# Initialisierung von Pygame
pygame.init()

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fenstergr”áe
WIDTH, HEIGHT = 500, 500

# Erstellen des Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lilith Chat")

# Instanziierung von Lilith
lilith = Lilith()

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
    text = font.render(lilith.introduce(), True, BLACK)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text, text_rect)

    # Bildschirm aktualisieren
    pygame.display.flip()

# Pygame beenden
pygame.quit()


