from microbit import * 
pin0.set_analog_period(20) # Modulation en largeur d'impulsion de période de 20ms 
pin1.set_analog_period(20) # Sur la broche de commande n°0
angle = 0

def servo(angle): # Création d'une fonction "servo" permettant la génération du signal
     # à partir de la valeur calculée de la variable angle
    pin0.write_analog(angle) # Sur la broche de commande n°0
    pin1.write_analog(180-angle) # Sur la broche de commande n°1
    
while True: # Boucle infinie
    while button_a.is_pressed(): # Tant que le bouton a est pressé
        angle += 1 # Incrementé 1 à angle
        if angle >= 180: # Si angle depasse 180 définir angle à 180
            angle = 180  
        servo(angle) # Faire bouger le servomoteur selon l'angle
        sleep(10) # Pause de 10ms
    while button_b.is_pressed():  # Tant que le bouton b est pressé
        angle -= 1 # Décrementé 1 à angle
        if angle <= 0: # Si angle est en dessous de 0 définir angle à 0
            angle = 0
        servo(angle) # Faire bouger le servomoteur selon l'angle
        sleep(10) # Pause de 10ms
