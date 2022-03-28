travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, country_visits, cities_names):
    x = travel_log.append({})
    length = len(travel_log) - 1
    travel_log[length]["country"] = country_name
    travel_log[length]["visits"] = country_visits
    travel_log[length]["cities"] = cities_names 



# Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
