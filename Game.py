# classe Game projet rpg-game
# Creation devops
import os
import json
from random import *


class Game:
    file_path = 'game.json'
    partie = "Pas Commencer"
    score_fuite = 10
    contexte = {
        'mouvement': 'mouvement',
        'combat': 'combat'
    }
    equipe = {
        'guerrier': 'guerrier',
        'chasseur': 'chasseur',
        'magicien': 'magicien',
    }
    info = {
        'nom': '',
        'contexte': '',
        'butin': 0,
        'equipe': {
            'guerrier': 0,
            'chasseur': 0,
            'magicien': 0,
        },
    }

    def __init__(self) -> None:
        print("Jeu démarré")
        self.store_json(Game.info)
        self.start_game()

    # fonction config fini
    def config(self):
        data = self.load_json()
        self.nom = input("Quel est votre nom de joueur ? ")
        data['nom'] = self.nom
        self.store_json(data)

    # fonction start fini
    def start(self):
        data = self.load_json()
        data['contexte'] = Game.contexte['mouvement']
        data['butin'] = 40
        self.store_json(data)

    # fonction flee fini
    def flee(self):
        if(Game.info["context"] == "combat"):
            my_team = Game.info["equipe"]
            for i in my_team:
                if(randint(1, Game.score_fuite) == 1):
                    print("on as un mort ")
                    my_team.remove(i)
            Game.info["equipe"] = ",".join(my_team)
        # print(info["équipe"])

    # fonction status fini
    def status(self):
        data = self.load_json()
        if(Game.partie == "Perdu"):
            print("GAME OVER")
        else:
            print("Votre nom de joueur est : " + data["nom"] + ".")
            print("Votre butin est de  : " +
                  str(data["butin"]) + " pièces d'or.")
            print("Votre équipe est composée de  : " +
                  str(data["equipe"]) + ".")
            if(data["contexte"] == "combat"):
                print("Vous êtes dans le contexte : " +
                      data["contexte"] + " vous pouvez vous battre ou vous enfuir.")
            if(data["contexte"] == "mouvement"):
                print("Vous êtes dans le contexte : " +
                      data["contexte"] + " vous pouvez vous déplacer ou acheter des unitées.")

    def store_json(self, value: dict):
        if os.path.isfile(Game.file_path):
            data = self.load_json()
            data.update(value)
            self.create_json(data)
        else:
            self.create_json(Game.info)

    def load_json(self) -> dict:
        with open(Game.file_path, 'r+') as line:
            data = json.load(line)
        return data

    def create_json(self, data: dict):
        json_data = json.dumps(data)
        with open(Game.file_path, 'w') as line:
            line.write(json_data)

    def buy_unit(self):
        data = self.load_json()
        if(data["contexte"] == "mouvement"):
            print("\n\n++++ Zone d'achat ++++")
            print("\t++++ Tapez: ++++")
            print("\t1 - Pour 5 guerriers = 10 unit")
            print("\t2 - Pour 5 chasseurs = 20 unit")
            print("\t3 - Pour 5 magiciens = 30 unit")
            choix = int(input('Votre choix: '))
            if(choix == 1):
                if(data['butin'] >= 10):
                    data['butin'] -= 10
                    data['equipe']['guerrier'] += 5
                    print("Achat efféctué")
                    print(
                        f"Vous avez : {data['equipe']['guerrier']} guerriers")
                    print(f"Votre butin est de {data['butin']}")
                    self.store_json(data)
                else:
                    print("Votre butin est insuffisant")
            elif(choix == 2):
                if(data['butin'] >= 20):
                    data['butin'] -= 20
                    data['equipe']['chasseur'] += 5
                    print("Achat efféctué")
                    print(
                        f"Vous avez : {data['equipe']['chasseur']} chasseurs")
                    print(f"Votre butin est de {data['butin']}")
                    self.store_json(data)
                else:
                    print("Votre butin est insuffisant")
            elif(choix == 3):
                if(data['butin'] >= 30):
                    data['butin'] -= 30
                    data['equipe']['magicien'] += 5
                    print("Achat efféctué")
                    print(
                        f"Vous avez : {data['equipe']['magicien']} magiciens")
                    print(f"Votre butin est de {data['butin']}")
                    self.store_json(data)
                else:
                    print("Votre butin est insuffisant")
            else:
                print("Votre choix est invalide")
        else:
            print("Vous ne pouver pas faire d'achat en mode combat")

    def start_game(self):
        print("Liste des actions possibles : exit, config, status, flee, start, buy")
        action = input("Faite une action : ")
        while(action != "exit"):
            if(action == "config"):
                self.config()
            if(action == "flee"):
                self.flee()
            if(action == "status"):
                self.status()
            if(action == "start"):
                self.start()
            if(action == "buy"):
                self.buy_unit()
            action = input("Faite une action : ")


game = Game()
