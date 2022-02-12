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
        'PlayerTeam': {
            'nom': None,
            'contexte': None,
            'butin': 0,
            'equipe': {
                'guerrier': {
                    'degat': 5,
                    'chance': 5,
                    'fuite': 3,
                    'prix': 10,
                    'nombre': 0
                },
                'chasseur': {
                    'degat': 2,
                    'chance': 10,
                    'fuite': 20,
                    'prix': 25,
                    'nombre': 0
                },
                'magicien': {
                    'degat': 4,
                    'chance': 20,
                    'fuite': 10,
                    'prix': 15,
                    'nombre': 0
                }
            },
        },
        'EnemyTeam': {
            'orc': {
                'degat': 5,
                'loot': 3,
                'nombre': 1
            },
            'goblin': {
                'degat': 3,
                'loot': 2,
                'nombre': 1
            },
            'zombie': {
                'degat': 2,
                'loot': 1,
                'nombre': 1
            },
        }
    }

    def __init__(self) -> None:
        print("Jeu démarré")
        self.store_json(Game.info)
        self.start_game()

    # fonction config fini
    def config(self):
        data = self.load_json()
        self.nom = input("Quel est votre nom de joueur ? ")
        data['PlayerTeam']['nom'] = self.nom
        self.store_json(data)

    # fonction start fini
    def start(self):
        data = self.load_json()
        data['PlayerTeam']['contexte'] = Game.contexte['mouvement']
        data['PlayerTeam']['butin'] = 40
        self.store_json(data)

    # fonction flee fini
    def flee(self):
        if(Game.info["contexte"] == "combat"):
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
            print(f"Votre nom de joueur est : " +
                  str(data['PlayerTeam']["nom"]) + ".")
            print("Votre butin est de  : " +
                  str(data['PlayerTeam']["butin"]) + " pièces d'or.")
            print("Votre équipe est composée de :")
            for i in data['PlayerTeam']['equipe']:
                print(str(data['PlayerTeam']['equipe'][i]['nombre'])+' '+ i +('', 's') [data['PlayerTeam']['equipe'][i]['nombre'] > 1])
            if(data['PlayerTeam']["contexte"] == "combat"):
                print("Vous êtes dans le contexte : " +
                      str(data['PlayerTeam']["contexte"]) + " vous pouvez vous battre ou vous enfuir.")
            if(data['PlayerTeam']["contexte"] == "mouvement"):
                print("Vous êtes dans le contexte : " +
                      str(data['PlayerTeam']["contexte"]) + " vous pouvez vous déplacer ou acheter des unitées.")

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
        return dict(data)

    def create_json(self, data: dict):
        json_data = json.dumps(data)
        with open(Game.file_path, 'w') as line:
            line.write(json_data)

    def buy_unit(self):
        data = self.load_json()
        if (data['PlayerTeam']["contexte"] == "mouvement"):
            print("\n\n++++ Zone d'achat ++++")
            print("++++ Tapez: ++++")
            print("\t1 - Pour 1 guerrier = 10 unit")
            print("\t2 - Pour 1 magicien = 15 unit")
            print("\t3 - Pour 1 chasseur = 25 unit")
            choix = int(input('Votre choix: '))
            if (choix == 1):
                if (data['PlayerTeam']['butin'] >= 10):
                    data['PlayerTeam']['butin'] -= 10
                    data['PlayerTeam']['equipe']['guerrier']['nombre'] += 1
                    print("Achat efféctué")
                    print(
                        f"Vous avez : {data['PlayerTeam']['equipe']['guerrier']['nombre']} guerriers")
                    print(f"Votre butin est de {data['PlayerTeam']['butin']}")
                    self.store_json(data)
                else:
                    print("Votre butin est insuffisant")
            elif (choix == 3):
                if (data['PlayerTeam']['butin'] >= 25):
                    data['PlayerTeam']['butin'] -= 25
                    data['PlayerTeam']['equipe']['chasseur']['nombre'] += 1
                    print("Achat efféctué")
                    print(
                        f"Vous avez : {data['PlayerTeam']['equipe']['chasseur']['nombre']} chasseurs")
                    print(f"Votre butin est de {data['PlayerTeam']['butin']}")
                    self.store_json(data)
                else:
                    print("Votre butin est insuffisant")
            elif (choix == 2):
                if (data['PlayerTeam']['butin'] >= 15):
                    data['PlayerTeam']['butin'] -= 15
                    data['PlayerTeam']['equipe']['magicien']['nombre'] += 1
                    print("Achat efféctué")
                    print(
                        f"Vous avez : {data['PlayerTeam']['equipe']['magicien']['nombre']} magiciens")
                    print(f"Votre butin est de {data['PlayerTeam']['butin']}")
                    self.store_json(data)
                else:
                    print("Votre butin est insuffisant")
            else:
                print("Votre choix est invalide")
        else:
            print("Vous ne pouver pas faire d'achat en mode combat")

    def start_game(self):
        print("Liste des actions possibles : exit, config, status, flee, start, buy, fight")
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
