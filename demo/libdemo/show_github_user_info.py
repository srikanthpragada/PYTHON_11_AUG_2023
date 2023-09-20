
import requests

resp = requests.get("https://api.github.com/users/gvanrossum")
if resp.status_code != 200:
    print('Sorry! Could not details!')
    exit()

details = resp.json()
print('Name    : ', details['name'])
print('Company : ', details['company'])
print('Location: ', details['location'])
