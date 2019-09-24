from GameLibrary.LibraryObjects.Terrain.Terrain import Terrain


class Grass(Terrain):
    def __init__(self, status, background_color):
        Terrain.__init__(self, "Grass", status, '.', self.generate_text_color(status), background_color)

    def generate_text_color(self, status):
        if status == 'Alive':
            return 0, 255, 0
        elif status == 'Burned':
            return 163, 181, 109
