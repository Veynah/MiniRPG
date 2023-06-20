import pygame


class DialogBox:

    X_POSITION = 300
    Y_POSITION = 500

    def __init__(self):
        self.box = pygame.image.load('dialog/dialog_box.png')
        self.box = pygame.transform.scale(self.box,(700,100))
        self.texts = [" Chevalier Anakin à l'aide !", "la princesse Rolande a été kidnappée !", " Voulez-vous la sauver ?"]
        self.text_index = 0
        self.font =pygame.font.Font("dialog/dialog_font.ttf",18)
        self.reading = True

    def render(self, screen):
        if self.reading:
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 80, self.Y_POSITION + 40))

    def next_text(self):
        self.text_index +=1

        if self.text_index >= len(self.texts):
            #fermer le dialogue.
            self.reading= False