# 4 uzd
import requests

x = requests.get('https://restcountries.com/v3.1/all')

print(x.text)