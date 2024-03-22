from microbit import * 
pin0.set_analog_period(20) # Modulation en largeur d'impulsion de période de 20ms 
pin1.set_analog_period(20) # Sur la broche de commande n°0


def servo(angle): # Création d'une fonction "servo" permettant la génération du signal
     # à partir de la valeur calculée de la variable angle
    pin0.write_analog(angle) # Sur la broche de commande n°0
    pin1.write_analog(180-angle) # Sur la broche de commande n°1
    
while True:
    pot = pin2.read_analog() # Capture de la valeur délivrée par le potentiomètre rotatif
    print('pot = ', pot,) # Afficher cette valeur (dans la gamme allant de 0 à 1023 ) 
    print((pot,)) # Afficher le graphique de la valeur de la variable angle
    angle = (pot / 1023) * 180 # Normalisation de cette valeur sur la plage 0 à 180
    print('angle = ', angle, 'Deg') # Affichage de cette valeur angle en degrés
    print('angle1 = ', 180-angle, 'Deg')
    servo(angle) # appel de la fonction "servo"
    sleep(20) # Pause de 20ms entre la prise d'échantillon, pour soulager 
              # la liaison série, lors des transferts d'informations.
