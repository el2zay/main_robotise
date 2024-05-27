from microbit import *
import radio # Importation du module radio
radio.config(group=4, power=7) # Attribution du module radio pour le groupe 4
                               # Puissance d'émission maximale (1 mini - 7 maxi)
radio.on() # Activation du module radio
angle = 0 # Variable angle sur 0

while True: # Boucle infinie
    gesture = accelerometer.current_gesture() # Détecteur de geste
    if gesture == "left": # Si la carte est vers la gauche
        radio.send("left") # On envoie left
    if gesture == "right": # Si la carte est vers la droite
        radio.send("right") # On envoie right
    if gesture == "up": # Si la carte est vers le haut
        radio.send("up") # On envoie up
    if gesture == "down": # Si la carte est vers le bas
        radio.send("down") # On envoie down
