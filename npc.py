class NPC:
    def __init__(self, name, dialogue, player, equipment_stock=None, weapon_stock=None):
        self.name = name
        self.dialogue = dialogue
        self.player = player
        self.equipment_stock = equipment_stock
        self.weapon_stock = weapon_stock
        self.has_given_money = False

    def talk(self, response=None):
        if response is None:
            print(self.dialogue['default'])
        elif response in self.dialogue:
            print(self.dialogue[response])
            if self.name == "Maire" and response == 'oui' and not self.has_given_money:
                self.give_money()
        else:
            print("Je ne comprends pas.")

    def give_money(self):
        print("Voici de l'argent. Allez vous équiper chez le forgeron.")
        self.has_given_money = True
        self.player.gold += 100

    def sell_equipment(self, equipment_name):
        if self.equipment_stock and equipment_name in self.equipment_stock:
            if self.player.gold >= self.equipment_stock[equipment_name]:
                print(f"Voici votre {equipment_name}. Cela vous coûte {self.equipment_stock[equipment_name]} pièces d'or.")
                self.player.gold -= self.equipment_stock[equipment_name]
                del self.equipment_stock[equipment_name]
            else:
                print("Désolé, vous n'avez pas assez d'or.")
        else:
            print("Désolé, je n'ai pas de {equipment_name} en stock.")

    def sell_weapon_upgrade(self, weapon_name):
        if self.weapon_stock and weapon_name in self.weapon_stock:
            if self.player.gold >= self.weapon_stock[weapon_name]:
                print(f"Voici votre {weapon_name}. Cela vous coûte {self.weapon_stock[weapon_name]} pièces d'or.")
                self.player.gold -= self.weapon_stock[weapon_name]
                del self.weapon_stock[weapon_name]
            else:
                print("Désolé, vous n'avez pas assez d'or.")
        else:
            print("Désolé, je n'ai pas de {weapon_name} en stock.")
            

class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0  # Initial gold

player = Player("Joueur")

dialogue_maire = {
    'default': "La princesse a été kidnappée ! Voulez-vous la sauver ?",
    'oui': "Super ! Voici de l'argent. Allez vous équiper chez le forgeron.",
    'non': "Eh bien, allons tous à la taverne alors.",
}
maire = NPC("Maire", dialogue_maire, player)

dialogue_forgeron = {
    'default': "Que puis-je faire pour vous aujourd'hui ?",
}
equipment_stock = {
    "Armure de base": 50,
    "Bouclier de base": 50
}
weapon_stock = {
    "Amélioration d'épée": 75,
    "Amélioration de marteau": 75
}
forgeron = NPC("Forgeron", dialogue_forgeron, player, equipment_stock, weapon_stock)

dialogue_tavernier = {
    'default': "Salut, je suis le tavernier. Laissez-moi vous raconter ma vie...",
}
tavernier = NPC("Tavernier", dialogue_tavernier, player)

dialogue_guardien = {
    'default': "Attention, aventurier! La forêt est pleine de dangers et de pièges. Soyez vigilant et préparé. Bonne chance!",
}
guardien = NPC("Guardien", dialogue_guardien, player)
