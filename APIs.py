
import json
import requests
import 

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) 
# you have the option of selecting which artist's song you want to pick
# response.json() just calls the response file which is in a json format
print(json.dumps(response.json(), indent=2)) #changes the formatting to make is human friendly

#can also print all the songs by weezer by looking at the data and calling it through a specific path
o = response.json() #make sure to understand this very well!!!!
for result in o["results"]:
    print(result["trackName"])
