import pygame


class Level:
    def __init__(self, enemyCount = 0):

        self.data = []

        self.groundData = pygame.sprite.Group()
        self.buildingData = pygame.sprite.Group()
        self.enemyCount = enemyCount

    def add(self, data):
        self.data.append(data)

    def addGround(self, data):
        self.data.append(data)
        self.groundData.add(data)

    def addBuilding(self, data):
        self.data.append(data)
        self.buildingData.add(data)


