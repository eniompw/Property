"""
Property Search Script
This script searches for properties for sale in the UK using the Zoopla UK API via RapidAPI.
"""

import requests

# API configuration
API_URL = "https://zoopla-uk.p.rapidapi.com/properties/search-sale"
API_KEY = "YOUR_RAPIDAPI_KEY_HERE" # Replace with your actual RapidAPI key

# Fetch property listings for South Kensington
response = requests.get(
    API_URL,
    headers={"x-rapidapi-key": API_KEY},
    params={"query": "South Kensington"}
).json()

# Extract first property from results
first_property = response['data']['listings']['regular'][0]

# Display property information
print(first_property.keys())
print(first_property['address'])
