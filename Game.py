#classe Game projet rpg-game
#Creation devops
import os
from random import * 
info = {"nom": "Jean","contexte" : "mouvement", "butin" : 40, "équipe" : "guerrier,chasseur,magicien"}
partie = "Pas Commencer"
score_fuite=10

#fonction config fini
def config():
    
    nom = input("Quel est votre nom de joueur ? ")
    info["nom"] = nom
    #print("Votre nom de joueur est : " + info["nom"])

#fonction start fini
def start():
    print("La partie commence")
    info["contexte"] = "mouvement"
    info["butin"] = 40
    info["équipe"] = ""
    partie = "En cours"
    
    #print(info)

#fonction flee fini 
def flee():
    if(info["context"] == "combat"):
        my_team = info["équipe"].split(",")
        for i in my_team : 
            if(randint(1,score_fuite) == 1):
                print("on as un mort ")
                my_team.remove(i)
        info["équipe"] = ",".join(my_team)
    #print(info["équipe"])
  
#fonction status fini 
def status():
    if(partie == "Perdu"):
        print("GAME OVER")
    else:
        print("Votre nom de joueur est : " + info["nom"] + ".")
        print("Votre butin est de  : " + str(info["butin"]) + " pièces d'or.")
        print("Votre équipe est composée de  : " + info["équipe"] + ".")
        if(info["contexte"] == "combat"):
          print("Vous êtes dans le contexte : " + info["contexte"] + " vous pouvez vous battre ou vous enfuir.")
        if(info["contexte"] == "mouvement"):
          print("Vous êtes dans le contexte : " + info["contexte"] + " vous pouvez vous déplacer ou acheter des unitées.")
    
    
print("Liste des actions possibles : exit, config, status, flee, start")
action = input("Faite une action : ")
while(action != "exit"):
    if( action == "config"):
        config()
    if(action == "flee"):
        flee()
    if(action == "status"):
        status()
        
    if(action == "start"):
        start()
    
    
    action = input("Faite une action : ")
