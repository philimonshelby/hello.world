import requests
url = 'https://maker.ifttt.com/trigger/philimon/json/with/key/i-s6kI9DTBA3ocCXGfnr6r3FqmnBwx-tBE6JEz34OVK'
r = requests.get(url)
print (r.status_code)