import requests



print("Testing")

url = "https://catfact.ninja/fact"
response = requests.get(url)

# Test
print("Code", response.status_code)
print()

# Raw
print("Raw")
print(response.text)
print()

#Formatted
print("Formatted Output")
data = response.json()

print("Cat Fact:", data.get("fact"))
print("Length:", data.get("length"))