#Miguel Fernandez
#Module 9.2 Assignment
import requests

print("Make Connection")

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

#Make Connection
print("Status", response.status_code)
print()

#Raw
print("Raw")
print(response.text)
print()

#Formatted
print("Formatted")
data = response.json()

print("people in space:", data["number"])
print("\nPeople in space:")

for person in data["people"]:
    print(f"- {person['name']} on {person['craft']}")

