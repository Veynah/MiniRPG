import pytmx
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self, tmx_file, player, screen):
        self.player = player
        self.screen = screen
        self.tmx_data = load_pygame(tmx_file)

    def render(self):
        # Loop through all layers in the tmx_data
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        self.screen.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))
            elif isinstance(layer, pytmx.TiledImageLayer):
                image = layer.image
                if image:
                    self.screen.blit(image, (0, 0))  # Assuming image layers should be drawn starting from (0,0)




    def player_has_reached_end_of_level(self): #ce sera la transition des niveaux
        # Add your condition for the player reaching the end of the level
        # This is a placeholder and will need to be replaced
        pass
