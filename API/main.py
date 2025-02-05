import requests
import json
name = input("Please write your name: ")
x= requests.get(f"https://api.genderize.io?name={name}")
data = x.json()
gender = data["gender"]
probability = data["probability"]
print(f"The probabilty of {name} being {gender} is {probability} ")