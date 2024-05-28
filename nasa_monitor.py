import requests
import time

API_KEY = 'your_api_key_here'  # Replace with your actual API key
ENDPOINT = 'https://api.nasa.gov/planetary/apod'
PARAMS = {'api_key': API_KEY}

def monitor_apod():
    while True:
        response = requests.get(ENDPOINT, params=PARAMS)
        if response.status_code == 200:
            print("API is working. Response time: {} ms".format(response.elapsed.total_seconds() * 1000))
        else:
            print("Error: Status code {}".format(response.status_code))
        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    monitor_apod()
