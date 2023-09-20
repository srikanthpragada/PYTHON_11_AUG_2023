import requests

resp = requests.get("https://restcountries.com/v3.1/all")

countries = resp.json()  # list of dict

for country in countries:
    print(f"{country['name']['common']:50}  {country['area']:10}")

