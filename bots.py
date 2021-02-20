import urllib.request
import json
import subprocess
import sys
import os

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    print("[GAME] Trying to import wolfram")
    import wolframalpha
    print("proceed")
except:
    print("[EXCEPTION] wolframAlpha not installed")
    try:
        print("[GAME] Trying to install wolframalpha via pip")
        import pip
        install("wolframalpha")
        print("[GAME] WOLFRAM has been installed")
    except:
        print("Sorry this won't work :( ")

def TempCheck(city):
  api_endpoint=   "http://api.openweathermap.org/data/2.5/weather"
  # city= "Toronto"
  # city= input()
  apikey = "13f2f7b1cbc81591ae423a7844c4e569"
  
  try:
    url= api_endpoint + "?q=" + city + "&appid=" + apikey
    # print(url)
    with urllib.request.urlopen(url) as url_:
      data = json.loads(url_.read().decode())
  
  except:
    print("Sorry, couldn't get that for you.\nPlease check  the location name again.")
  
  else:
    temperature = data['main']['temp']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    weather= data['weather'][0]['description']
    
    reply = f"Temperature:{(temperature-273.15):.2f}\n"
    reply += f"Minimum Temperature:{(min_temp-273.15):.2f}\n"
    reply += f"Maximum Temperature:{(max_temp-273.15):.2f}\n"
    reply += weather.title()
    return (reply)

def WikiBot(src_qr):
  api_endpoint= "https://api.duckduckgo.com/"

  # src_qr = input().split()
  src_qr = src_qr.split()
  src_qr = "+".join(src_qr)

  try:
    url = api_endpoint + "?q=" + src_qr + "&format=json&pretty=1"
    with urllib.request.urlopen(url) as url_:
      data = json.loads(url_.read().decode())

  except:
    print("Sorry, couldn't get that for you.")

  else:
    wiki = data['Abstract']
    # print(wiki)
    return wiki


def Wolfram(question):  
  # question = input('Question: ') 

  app_id = 'WQ895X-6WWW76E68T'

  try:  
    client = wolframalpha.Client(app_id) 
    res = client.query(question)
    answer = next(res.results).text 
    # print(answer)
    return answer
  except:
    print("Sorry, couldn't get that for you.")

TempCheck("Jaipur")
