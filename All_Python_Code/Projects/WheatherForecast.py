import requests
import json
import win32com.client as wincl

speaker = wincl.Dispatch("SAPI.SpVoice")    # For Creating Instance of Text to Speech.

city = input('Enter the name of your city : ')

url = f'https://api.weatherapi.com/v1/current.json?key=1c7837ee3b00491a9dd122503230810&q={city}'

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)

op = f'The current wheather in {city} is {wdic["current"]["temp_c"]} degrees'

print(op)
speaker.Speak(op)