import requests

def local_crawler(location, keywords):
    # Set up the API request URL
    url = f'https://nominatim.openstreetmap.org/search.php?q={"+".join(keywords)}&format=json&addressdetails=1&limit=10&viewbox=&bounded=1&countrycodes='

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the results from the JSON response
        results = response.json()

        # Print out the name and address of each result
        for result in results:
            name = result.get('display_name', 'Unknown')
            address = ', '.join(filter(None, [result.get('address', {}).get('road'), result.get('address', {}).get('city'), result.get('address', {}).get('state')]))
            print(f'{name}: {address}\n')
    else:
        print(f'Request failed with status code {response.status_code}')

# Example usage
location = 'Mumbai, India' # City and state abbreviation
keywords = ['Hospital','Doctor','Mumbai']
local_crawler(location, keywords)


