# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.defense = 5
        self.attack_power = 10
        self.level = 1
        self.experience = 0

    def sword_attack(self, enemy):
        damage = self.attack_power
        enemy.take_damage(damage)

    def magic_bolt(self, enemy):
        if self.mana >= 20:
            damage = self.attack_power * 1.5
            enemy.take_damage(damage)
            self.mana -= 20
        else:
            print("Not enough mana to cast the spell.")

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        if self.health <= 0:
            return True
        return False

    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack_power += 5
        self.mana += 10
        self.defense += 2
        self.experience = 0


# Main game loop
player_name = input("Enter name for Player: ")
player = Player(player_name)
