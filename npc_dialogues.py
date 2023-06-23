"""
npc_dialogues est un dictionnaire qui contient les dialogues des Non-Player Characters (NPC) du jeu.

Structure du dictionnaire:
    Clé (str): Nom du NPC.
    Valeur (list of str): Dialogues du NPC, chaque dialogue est une chaîne de caractères.

Exemple de clé et valeur:
    "Maire": ["MAIRE : Bonjour Chevalier Anakin ,\nque la Force soit avec toi !", ...],
    "Tavernier": ["Tavernier: Salutations, chevalier Anakin !\nUne bonne bière fraîche pour étancher votre soif ?", ...],
    "Forgeron": ["FORGERON: Bienvenue dans ma forge, Oh Chevalier \nAnakin, que puis-je faire pour vous?", ...],
    "Explorer": ["Chris: Anakin, devine quoi ? Des monstres m'ont \nattaqué et m'ont chassé de la forêt !", ...],
"""
npc_dialogues = {
            "Maire": ["MAIRE : Bonjour Chevalier Anakin ,\nque la Force soit avec toi !","ANAKIN : La Force m'accompagne !","MAIRE : Une sombre nouvelle m'est parvenue,\n La princesse Leia a été enlevée par l'impitoyable \n Seigneur Sith.","ANAKIN : Comment!!","MAIRE : Seul un chevalier aussi courageux que vous\npeut la sauver.","ANAKIN : Je ferai tout ce qui est en mon pouvoir\npour sauver la princesse Leia des griffes \ndu Seigneur Sith."
                      ,"MAIRE : Si vous acceptez cette quête,le village vous\nrécompensera avec de l'or pour acheter des armes.","ANAKIN :Je suis prêt à relever cette quête périlleuse.\nLa princesse Leia peut compter sur moi, et \nje ne laisserai pas l'obscurité triompher.","MAIRE : Mais si vous refusez, vous pouvez toujours\naller prendre une bonne bière fraîche\nchez le tavernier du coin.","ANAKIN : La bière fraîche du tavernier peut attendre. \nMon devoir envers la galaxie et mon sens \ndu devoir me guident vers cette quête cruciale","MAIRE: Bonne chance."],
            "Tavernier": ["Tavernier: Salutations, chevalier Anakin !\nUne bonne bière fraîche pour étancher votre soif ?",
                          "Anakin: Volontiers, tavernier.",
                          "Tavernier: Ah, quand j'étais jeune, j'ai vécu des\naventures aussi folles que les vôtres, Jedi.\nDes clients impatients, des verres renversés, \nc'était du vrai combat !",
                          "Anakin: Vraiment ?\nVous avez affronté de sacrés défis, tavernier.",
                          "Tavernier: Oh oui, j'ai même dû combattre un gang de\nmauvais payeurs.J'ai utilisé une attaque secrète\n : les cacahuètes volantes !","Anakin: Des cacahuètes volantes ?\nVous êtes un vrai héros, tavernier.",
                          "Tavernier: Héhé, la vie d'un tavernier est pleine de\nsurprises.Voici votre bière bien fraîche, servie\navec une mousse légère comme un sabre laser !",
                          "Anakin: Merci, tavernier. À votre santé !",
                          "Tavernier: À la vôtre, chevalier Anakin ! Si vous avez\nbesoin de conseils pour vaincre les ténèbres\nou la soif,revenez me voir.",
                          "Anakin: Je n'y manquerai pas.\nQue la Force soit avec vous, tavernier !",
                          "Tavernier: Et que la bière fraîche coule à flots,\ncher chevalier !"],
            "Forgeron": ["FORGERON: Bienvenue dans ma forge, Oh Chevalier \nAnakin, que puis-je faire pour vous?","ANAKIN : As-tu reçu les toutes dernières\narmes sur le marché galactique?","FORGERON : Bien sûr, j'ai justement été livré ce matin,\ntout droit sorti de l'atelier galactique !"],
            "Explorer": ["Chris: Anakin, devine quoi ? Des monstres m'ont \nattaqué et m'ont chassé de la forêt !"
                            ,"Anakin: Vraiment ? Ils ont pris tes affaires aussi ?"
                            ,"Chris: Ouais, tous ! Mes trucs, ma tente,\nmême mes figurines Ewok \nj'ai pu prendre que mon sac a dos !"
                            ,"Anakin: Pas les Ewoks ! On va les retrouver\n et récupérer tes affaires."
                            ,"Chris: Non, non, je te laisse faire ça.\nMoi, je t'attends ici, tranquille."
                            ,"Anakin: Écoute, Chris, je comprends tes craintes, \nmais je dois aussi sauver la princesse Leia.\nJe ne peux pas rester les bras croisés."
                            ,"Chris: La princesse Leia ? Vraiment ?\nBon, d'accord, vas-y, sauve le monde et retrouve\nmes affaires en même temps."
                            ,"Anakin: Merci, Chris. Je ferai de mon mieux.\nQue la Force soit avec moi, et que je retrouves\n tes affaires rapidement !"
                            ,"Chris: Bonne chance, Anakin.\nJ'attends ton retour triomphal !"]
        }