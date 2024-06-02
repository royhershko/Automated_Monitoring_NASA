import requests
import time
from prometheus_client import start_http_server, Summary, Counter

API_KEY = 'your_api_key_here'  # Replace with your actual API key
ENDPOINT = 'https://api.nasa.gov/planetary/apod'
PARAMS = {'api_key': API_KEY}

# Define Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
ERROR_COUNT = Counter('error_count', 'Total number of errors')

# Define the Monitoring Function
@REQUEST_TIME.time()
def monitor_apod():
    while True:
        response = requests.get(ENDPOINT, params=PARAMS)
        if response.status_code == 200:
            print("API is working. Response time: {} ms".format(response.elapsed.total_seconds() * 1000))
        elif response.status_code == 403:
            print("Error: Status code 403 - Forbidden. Check your API key and permissions.")
            ERROR_COUNT.inc()
        else:
            print("Error: Status code {}".format(response.status_code))
            ERROR_COUNT.inc()
        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    # Start up the server to expose the metrics
    start_http_server(8000)
    monitor_apod()

