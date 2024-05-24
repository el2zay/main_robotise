from microbit import *
import radio # Importation du module radio
radio.config(group=4, power=7) # Attribution du module radio pour le gruope (ou le réseau n°1)
                               # Puissance d'émission maximale (1 mini - 7 maxi)
radio.on() # Activation du module radio
isStarted = False
angle = 0    

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "left":
        print("left")
        radio.send("left")
    if gesture == "right":
        print("right")
        radio.send("right")
    if gesture == "up":
        print("up")
        print("up")
        radio.send("up")
        print("up")
    if gesture == "down":
        print("down")
        radio.send("down")
    
