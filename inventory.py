import pygame

class Inventory:
    def __init__(self):
        self.items = {}
        self.health = 100
        self.level = 1
        self.money = 0
        
        self.type = "Inventory"
        self.position = (0,0)

    def add_item(self, item):
        self.items[item.type] = self.items.get(item.type, 0) + 1

    def remove_item(self, item):
        if item.type in self.items and self.items[item.type] > 0:
            self.items[item.type] -= 1

    def get_item_count(self, item_type):
        return sum(1 for item in self.items if item.type == item_type)

    def get_health(self):
        return self.health

    def decrease_health(self, decrease_amount):
        self.health -= decrease_amount
        if self.health < 0:
            self.health = 0

    def get_level(self):
        return self.level

    def increase_level(self):
        self.level += 1

    def get_money(self):
        return self.money

    def decrease_money(self, amount):
        self.money -= amount
        if self.money < 0:
            self.money = 0

    def increase_money(self, amount):
        self.money += amount

