from microbit import *
pin0.set_analog_period(20) # 

def servo(angle): # Création d'une fonction "sevo" permettant la génération du signal
    pin0.write_analog(angle)

while True:
    pot = pin2.read_analog() 
    print('pot = ', pot,)
    print((pot,))
    angle = (pot / 1023) * 180
    print('angle = ', angle, 'Deg')
    servo(angle) # appel de la fonction servo
    sleep(20) # Pause de 200ms entre la prise d'échantillon, pour soulager 
              # la liaison série, lors des transferts d'informations.