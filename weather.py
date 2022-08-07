import requests
from bs4 import BeautifulSoup

url = requests.get('https://weather.com/en-IN/weather/today/l/d884bf8e15624162758659a71e31e084981e92c367a7bfa15c345c9b92d688c4')
web_content = BeautifulSoup(url.text, 'lxml')

current_temp = web_content.find('span', class_ = 'CurrentConditions--tempValue--3a50n').text
weather = web_content.find('div', class_ = 'CurrentConditions--phraseValue--2Z18W').text
day_temp = web_content.find('div', class_ = 'CurrentConditions--tempHiLoValue--3SUHy').text

print(f"Current temperature: {current_temp} | Weather: {weather} | Days's range: {day_temp}")