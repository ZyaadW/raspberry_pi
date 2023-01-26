import RPi.GPIO as GPIO # importeer rpi.gpio als gpio

import time # importeer tijd

 

in1 = 17 # variabele is gelijk aan pin 17

in2 = 18 # variabele is gelijk aan pin 18

in3 = 27 # variabele is gelijk aan pin 27

in4 = 22 # variabele is gelijk aan pin 22

 

buttonPin1 = 19 # drukknop pin1 is gelijk aan gpio 19

buttonPin2 = 20 # drukknop pin2 is gelijk aan gpio 20

step_sleep = 0.002 # varaibele gelijk aan 2 microseconden

stappen_teller = 4096 # 5.625*(1/64) per stap, 4096 stappen is 360°

richting = False # True voor wijzerins, False voor tegenwijzersin

stap_sequentie = [[1,0,0,1],

                 [1,0,0,0],

                 [1,1,0,0],

                 [0,1,0,0],

                 [0,1,1,0],

                 [0,0,1,0],

                 [0,0,1,1],

                 [0,0,0,1]] # stappen sequentie voor stappenmotor

 

GPIO.setmode( GPIO.BCM ) # bepaal de modus voor het bordje

GPIO.setup( in1, GPIO.OUT ) # gpio pin wordt een uitgang

GPIO.setup( in2, GPIO.OUT ) # gpio pin wordt een uitgang

GPIO.setup( in3, GPIO.OUT ) # gpio pin wordt een uitgang

GPIO.setup( in4, GPIO.OUT ) # gpio pin wordt een uitgang

 

GPIO.output( in1, GPIO.LOW ) # gpio pin wordt laag

GPIO.output( in2, GPIO.LOW ) # gpio pin wordt laag

GPIO.output( in3, GPIO.LOW ) # gpio pin wordt laag

GPIO.output( in4, GPIO.LOW ) # gpio pin wordt laag

 

 

motor_pinnen = [in1,in2,in3,in4] # alle pinnen worden door middel van een lijst in 1 variabele gestopt

motor_stappen_teller = 0  # variabele is gelijk aan nul

 

 

def cleanup(): # maak alle pinnen laag

    GPIO.output( in1, GPIO.LOW ) # gpio pin wordt laag

    GPIO.output( in2, GPIO.LOW ) # gpio pin wordt laag

    GPIO.output( in3, GPIO.LOW ) # gpio pin wordt laag

    GPIO.output( in4, GPIO.LOW ) # gpio pin wordt laag

    GPIO.cleanup() # maak alle gebruikte poorten schoon

 



try: # probeer dit

    i = 0 # variabele is gelijk aan 0

    for i in range(stappen_teller): # voor i in afstand van  alle stappen

        for pin in range(0, len(motor_pinnen)): # voor pin in de afstand tussen eerste pin tot de lengte van de pinnen

            GPIO.output( motor_pinnen[pin], stap_sequentie[motor_stappen_teller][pin])# de pinnen worden gedefineerd als uitgangen

        if richting==True and buttonPin1.value: # als de richting waar is en knop1 hoog

            motor_stappen_teller = (motor_stappen_teller - 1) % 8 # draai naar links

        elif richting==False and buttonPin2.value: # anders-als de richting vals is en knop2 hoog

            motor_stappen_teller = (motor_stappen_teller + 1) % 8 # draai naar rechts

        else: # anders

            print( "Er is een fout in het programma het moet True of False zijn." ) # print dit

            cleanup() # roep functie op

            exit( 1 ) # print dit cijfer en ga uit programma

        time.sleep( step_sleep ) # wacht volgens variabele

 

except KeyboardInterrupt: # behalve bij een toetsenbordonderbreking (control + c)

    cleanup() # roep functie op

    exit( 1 ) # print dit cijfer en ga uit programma

 

cleanup() # roep functie op

exit( 0 ) # print dit cijfer en ga uit programm