# Interacting with Googlemaps API to find driving time and distance between cities
#User to dynamically input start and end of destination

#pip install googlemaps

import googlemaps

#read API key from external file, without disclosing in Python script
API = open ("Google Maps Platform API key.txt", "r")
APIKey = API.read()

#Pass through API key
Maps = googlemaps.Client(key = APIKey)

# User inputs for start and end drive destination 
StartDestination = input ("Where will you start your drive?\n")
EndDestination = input ("Where will you end your drive?\n")

#Calculate distance using API 
Distance = Maps.directions(StartDestination, EndDestination)

#Format API output into relevant variables 
KMDistance = (Distance[0]['legs'][0]['distance']['text'])
HrsMinsDuration = (Distance[0]['legs'][0]['duration']['text'])

# Pass results into an easy to read text string
print("Your drive will cover a total distance of "+ KMDistance+", taking the total time of "+ HrsMinsDuration+ ".")

