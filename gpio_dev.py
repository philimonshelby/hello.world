from gpiozero import LED,Button
from time import sleep
from signal import pause

led = LED(18)
button = Button(2)
#while True:
 #     led.on()
  #    sleep(0.5)
   #   led.off()
    #  sleep(0.5)
button.when_pressed = led.on
button.when_released = led.off

pause()
