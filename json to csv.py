import requests
import csv

# API endpoint URL
api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=5a9786006225b21617d966d212e93c04'

# Make API request
response = requests.get(api_url)
data = response.json()
dataarr=[]
for x in data['weather']:
    listing=[x['main'],x['id'],x['description']]
    dataarr.append(listing)
    print(dataarr)
