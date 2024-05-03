from microbit import * 
pin0.set_analog_period(20) # Pouce
pin1.set_analog_period(20) # Index
pin8.set_analog_period(20) #  Majeur
pin12.set_analog_period(20) # Annulaire
pin16.set_analog_period(20) # Auriculaire
pin2.set_analog_period(20) # Poignet
angle = 0
# anglePoignet = 0

def servo(angle): # Création d'une fonction "servo" permettant la génération du signal
    # à partir de la valeur calculée de la variable angle
    print("angle", angle)
    # print("anglePoignet", anglePoignet)
    pin2.write_analog(angle) # Sur la broche de commande n°2
    pin0.write_analog(angle) # Sur la broche de commande n°0
    pin1.write_analog(180-angle) # Sur la broche de commande n°1
    pin8.write_analog(180-angle) # Sur la broche de commande n°8
    pin12.write_analog(180-angle) # Sur la broche de commande n°12
    pin16.write_analog(180-angle) # Sur la broche de commande n°16

    
while True: # Boucle infinie
    while button_a.is_pressed(): # Tant que le bouton a est pressé
        angle += 1 # Incrementé 1 à angle
        if angle >= 170: # Si angle depasse 170 définir angle à 170
            angle = 170          
        servo(angle) # Faire bouger le servomoteur selon l'angle
        sleep(20) # Pause de 20ms
    while button_b.is_pressed():  # Tant que le bouton b est pressé
        angle -= 1 # Décrementé 1 à angle
        if angle <= 0: # Si angle est en dessous de 0 définir angle à 0
            angle = 0
        servo(angle) # Faire bouger le servomoteur selon l'angle
        sleep(20) # Pause de 20ms
