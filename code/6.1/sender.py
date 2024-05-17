from microbit import *
import radio # Importation du module radio
radio.config(group=1, power=7) # Attribution du module radio pour le gruope (ou le réseau n°1)
                               # Puissance d'émission maximale (1 mini - 7 maxi)
radio.on() # Activation du module radio
isStarted = False
angle = 0

def start():
    if button_a.is_pressed():
        if isStarted == False:
            isStarted == True

while True:
    if isStarted == False:
        start()
    gesture = accelerometer.current_gesture()
    if gesture == "left":
        radio.send("left")
    if gesture == "right":
        radio.send("right")
    if gesture == "up":
        radio.send("up")
    if gesture == "down":
        radio.send("down")
    if gesture == "shake":
        radio.send("shake")
    
