import time

# initialisation de l'heure actuelle
heure_actuelle = (8, 52, 30)
# initialisation de l'heure de l'alarme
heure_alarme = (8, 52, 45)


def afficher_heure():
    # affichage de l'heure actuelle en format hh:mm:ss
    print(f"{heure_actuelle[0]:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d}")


def regler_heure(nouvelle_heure):
    # mise à jour de l'heure actuelle
    global heure_actuelle
    heure_actuelle = nouvelle_heure


def regler_alarme(nouvelle_alarme):
    # mise à jour de l'heure de l'alarme
    global heure_alarme
    heure_alarme = nouvelle_alarme


while True:

    # affichage de l'heure actuelle toutes les secondes
    afficher_heure()
    time.sleep(1)

    # incrémentation de la seconde
    heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)

    # si la seconde est égale à 60, incrémentation de la minute
    if heure_actuelle[2] == 60:
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)

    # si la minute est égale à 60, incrémentation de l'heure
    if heure_actuelle[1] == 60:
        heure_actuelle = (heure_actuelle[0] + 1, 0, 0)

    # si l'heure actuelle est égale à l'heure de l'alarme, affichage d'un message
    if heure_actuelle == heure_alarme:
        print("Alarme !")
