import  pygame



class Dialogbox

    def __init__(self):
        self.box = pygame.image.load("../dialog/dialog_box.png")

    
    def render (self,screen):
        screen.blit(self.box,(0,0))

        

