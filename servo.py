from gpiozero import Servo # van importeer de nodige bibliotheek
myGPIO=17 # variabele is gelijk een gpio pin 17
servo = Servo(myGPIO) # variabele servo is gelijk aan myGpio

try: # probeer
    while True: # als waar
        waarde = float(input("wat is de waarde: ")) #  variabele is gelijk een je input
        if waarde > 0.0 and waarde < 180.0: # als de variabele
            getal = float(waarde/90-1) # variabele gelijk aan deze formule
       
            servo.value = getal # waarde van servo gelijk aan variabele
        else: # anders doe
            print("geef een getal tussen 0 en 180")  # print dit 
except KeyboardInterrupt: # behalve bij een toetsenbord onderbreking
        print("programma is gestopt") # print dit
except ValueError: # behalve bij een waarde fout
        print("foute datatype") # print dit