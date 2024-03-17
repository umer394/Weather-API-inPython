import requests
import json
import win32com.client as wincom
city=input("Enter the name of the city: \n")

url = f"https://api.weatherapi.com/v1/current.json?key=1af814325d7d48a3938213553240703&q={city}&aqi=yes"
r=requests.get(url)
#print(r.text)
#use json to convert r.text type string to dictionary
wdic=json.loads(r.text)
temp=wdic["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak(f"The current weather in {city} is {temp} degree")
print(f"The current weather in {city} is {temp} degree")