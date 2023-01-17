import json

with open ('precipitation.json') as file: # Load json file
    precipitation = json.load(file)

seattle_precipitation = [station for station in precipitation if station['station'] == 'GHCND:US1WAKG0038'] # Filter for only Seattle stations

list_of_months = [0,0,0,0,0,0,0,0,0,0,0,0] # Initialize a list to store total precipitation per month
for measurement in seattle_precipitation: # Iterate through the measurements
    date = measurement['date']
    split_date = date.split('-') # First split the date and then extract the month
    month = int(split_date[1])
    precipitation = measurement['value'] # Get the value for precipitation 
    list_of_months[month-1] += precipitation # Update the total precipitation of that month
    # Adjust to the indexing, so subtract 1 so January is index 0
print(list_of_months)

output_data = {
    "Seattle": {
        "station": 'GHCND:US1WAKG0038',
        "state": 'Washington state',
        "total_monthly_precipitation": list_of_months
    }
}

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output_data, file, indent = 4)