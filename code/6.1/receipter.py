from microbit import *
import radio # Importation du module radio

radio.config(group=4, power=7) # Attribution du module radio pour le gruope (ou le réseau n°1)
                               # Puissance d'émission maximale (1 mini - 7 maxi)

radio.on() # Activation du module radio
angle = 0
angleIndex = 0

pin0.set_analog_period(20) # Pouce
pin1.set_analog_period(20) # Index
pin8.set_analog_period(20) #  Majeur
pin12.set_analog_period(20) # Annulaire
pin16.set_analog_period(20) # Auriculaire
pin2.set_analog_period(20) # Poignet

def servoFingers(angle): # Création d'une fonction "servo" permettant la génération du signal
     # à partir de la valeur calculée de la variable angle
    pin0.write_analog(angle) # Sur la broche de commande n°0
    pin1.write_analog(180-angle) # Sur la broche de commande n°1
    pin8.write_analog(180-angle)
    pin12.write_analog(180-angle)
    pin16.write_analog(180-angle)

def servoIndex(angle):
    pin0.write_analog(0) # Sur la broche de commande n°0
    pin1.write_analog(180-angle) # Sur la broche de commande n°1
    pin8.write_analog(0)
    pin12.write_analog(0)
    pin16.write_analog(0)

def servoPoignet(angle):
    pin2.write_analog(angle)

while True:
    message = radio.receive() # Métode pour la réception d'une donnée
    if message == "stop":
       print("stop")
       display.show(Image.NO)
        
    if message == "up":
         angle += 1 # Incrementé 1 à angle
         if angle >= 170: # Si angle depasse 180 définir angle à 180
            angle = 170  
         servoFingers(angle) # Faire bouger le servomoteur selon l'angle
         sleep(20) # Pause de 20ms

    if message == "down":
        angle -= 1 # Décrementé 1 à angle
        if angle <= 0: # Si angle est en dessous de 0 définir angle à 0
            angle = 0
        servoFingers(angle) # Faire bouger le servomoteur selon l'angle
        sleep(20) # Pause de 20ms

    if message == "left":
         angle += 1 # Incrementé 1 à angle
         if angle >= 90: # Si angle depasse 170 définir angle à 170
            angle = 90   
         print(angle)
         servoPoignet(angle) # Faire bouger le servomoteur selon l'angle
         sleep(20) # Pause de 20ms

    if message == "right":
        angle -= 1 # Décrementé 1 à angle
        if angle <= 30: # Si angle est en dessous de 0 définir angle à 0
            angle = 30
        print(angle)
        servoPoignet(angle) # Faire bouger le servomoteur selon l'angle
        sleep(20) # Pause de 20ms

    if message == "shake":
        print("shake")
        print("angle de l'index", angleIndex)
        servoIndex(30)
        #angleIndex = 170
        #else:
            #print("angle de l'index", angleIndex)
            #servoIndex(0)
            #angleIndex = 0
