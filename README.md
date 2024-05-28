# Automated_Monitoring_NASA
set up automated monitoring and alerting for a simple web service.

# NASA API Monitor

This project monitors the NASA Astronomy Picture of the Day (APOD) API endpoint to ensure it is functioning correctly. It periodically makes HTTP requests to the API, checks the response status code, and logs the response time.

## Prerequisites

- Python 3. Ensure you have Python 3 installed on your machine.
- A NASA API key. Sign up for an API key at [NASA API](https://api.nasa.gov/).

## Setup

1. **Install Python 3**:
   If Python 3 is not already installed on your machine, you can download and install it from [python.org](https://www.python.org/downloads/).

2. **Install the `python3-venv` Package**:
   On Debian/Ubuntu systems, run the following commands to install the `python3-venv` package:

   ```bash
   sudo apt update
   sudo apt install python3-venv

2. **Running the Script**:
   Running the Script
To run the monitoring script, execute the following command in the terminal:

  ```bash
python3 nasa_monitor.py

