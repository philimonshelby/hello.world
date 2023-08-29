import requests
from gpiozero import Button
from signal import pause

button = Button(18)
def get_url():
    url = 'https://maker.ifttt.com/trigger/philimon/json/with/key/i-s6kI9DTBA3ocCXGfnr6r3FqmnBwx-tBE6JEz34OVK'
    r = requests.get(url)
    print (r.status_code)
      

button.when_pressed = get_url

pause()