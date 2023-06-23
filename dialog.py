import pygame

class DialogBox:
    X_POSITION = 300
    Y_POSITION = 500

    def __init__(self):
        self.box = pygame.image.load('dialog/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (750, 125))
        self.dialogues = []
        self.dialogue_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("dialog/dialog_font.ttf", 18)
        self.reading = False
        self.display_options = False
        self.dialogue_colors = [(0, 0, 0), (255, 0, 0)]  # Noir et rouge
        self.used_dialogues = set()

    def execute(self, dialogues=[]):
        if self.reading:
            self.next_dialogue()
        else:
            self.reading = True
            self.dialogue_index = 0
            self.dialogues = [dialogue for dialogue in dialogues if dialogue not in self.used_dialogues]

    def terminate(self):
        self.reading = False
        self.dialogue_index = 0
        self.letter_index = 0
        self.dialogues = []

    def render(self, screen):
        if self.reading and self.dialogues and self.dialogue_index < len(self.dialogues):
            self.letter_index += 1

            if self.letter_index >= len(self.dialogues[self.dialogue_index]):
                self.letter_index = len(self.dialogues[self.dialogue_index])

            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))

            # Récupérer le dialogue actuel et sa couleur associée
            current_dialogue = self.dialogues[self.dialogue_index]
            dialogue_color = self.dialogue_colors[self.dialogue_index % len(self.dialogue_colors)]

            # Diviser le dialogue en lignes distinctes
            lines = current_dialogue.splitlines()

            # Position verticale initiale
            y_position = self.Y_POSITION + 15

            # Rendre chaque ligne du dialogue avec la couleur correspondante
            for line in lines:
                text = self.font.render(line[0:self.letter_index], False, dialogue_color)
                screen.blit(text, (self.X_POSITION + 50, y_position))
                y_position += self.font.get_height() + 5

    def next_dialogue(self):
        if self.dialogue_index < len(self.dialogues):
            self.used_dialogues.add(self.dialogues[self.dialogue_index])
        self.dialogue_index += 1
        self.letter_index = 0

        if self.dialogue_index >= len(self.dialogues):
            # Fermer le dialogue.
            self.reading = False
