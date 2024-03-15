from microbit import * 
pin0.set_analog_period(20) # M... en d' de période de 20ms 
                            # Sur la broche de commande n°0


def servo(angle): # Création d'une fonction "sevo" permettant la génération du signal
    pin0.write_analog(angle) # à partir de la valeur calculée de la variable angle
                                # Sur la broche de commande n°0

while True:
    pot = pin2.read_analog() # 
    print('pot = ', pot,) # Afficher cette valeur (dans la gamme allant de ... à ... ) 
    print((pot,)) # Afficher le graphique de la valeur de la variable angle
    angle = (pot / 1023) * 180 # Normalisation de cette valeur sur la plage ... à ...
    print('angle = ', angle, 'Deg') # Affichage de cette valeur 
    servo(angle) # appel de la fonction servo
    sleep(20) # Pause de 200ms entre la prise d'échantillon, pour soulager 
              # la liaison série, lors des transferts d'informations.

