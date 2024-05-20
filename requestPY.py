import requests

url = "https://fresh-berries-lick.loca.lt/api/resource/Project"

querystring = {"fields":["name","title"]}

headers = {"Authorization": ""}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)