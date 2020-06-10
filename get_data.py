# get_data.py

import requests
import json
from statistics import mean

print("REQUESTING SOME DATA FROM THE INTERNET...")


#request a product

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
#print(response.status_code)
#print(response.text)

response_data = json.loads(response.text)
print(response_data["name"])


#requesting products

request_url2 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response2 = requests.get(request_url2)
response_data2 = json.loads(response2.text)
for r in response_data2:
    print("Name: ",r["name"] + "   " + "ID: ", r["id"])

#requesting the gradebook

request_url3 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response3 = requests.get(request_url3)
response_data3 = json.loads(response3.text)
grades = []

#students = response_data3["students"]      #version 1 (works)
#for r in students:                     
#    grades.append(r["finalGrade"])

grades = [s["finalGrade"] for s in response_data3["students"]]

print("Max: ",max(grades))
print("Min: ", min(grades))
print("Average: ", mean(grades))

