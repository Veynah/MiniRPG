
import pygame as pg
import pytmx
import os


class Renderer(object):
    """
    This object renders tile maps (tmx) from Tiled.
    """

    def __init__(self, filename):
        tm = pytmx.load_pygame('tiled/data/tmx/village.tmx', invert_y=True)
        self.size = tm.width * tm.tilewidth, tm.height * tm.tileheight
        self.tmx_data = tm

    def render(self, surface):

        tw = self.tmx_data.tilewidth
        th = self.tmx_data.tileheight
        gt = self.tmx_data.get_tile_image_by_gid

        if self.tmx_data.background_color:
            surface.fill(self.tmx_data.background_color)

        for layer in self.tmx_data.visible_layers:

            # Render image layers first.
            if isinstance(layer, pytmx.TiledImageLayer):
                # Load image from the source property
                image_path = os.path.join('tiled/data/tmx', layer.source)
                image = pg.image.load('tiled/data/tmx/village.tmx').convert_alpha()
                if image:
                    surface.blit(image, (0, 0))

            # Render tile layers.
            elif isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = gt(gid)
                    if tile:
                        surface.blit(tile, (x * tw, y * th))

            # Handle object groups if needed.
            elif isinstance(layer, pytmx.TiledObjectGroup):
                pass

    def make_map(self):
        temp_surface = pg.Surface(self.size)
        self.render(temp_surface)
        return temp_surface
