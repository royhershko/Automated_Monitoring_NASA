# Automated_Monitoring_NASA
set up automated monitoring and alerting for a simple web service.

# NASA API Monitor

This project monitors the NASA Astronomy Picture of the Day (APOD) API endpoint to ensure it is functioning correctly. It periodically makes HTTP requests to the API, checks the response status code, and logs the response time.

## Prerequisites
- Docker
- Prometheus
- Grafana
- Alertmanager
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
```

## Setup the API Key (NASA)

	1.	Sign Up for an API Key:
	   •	Visit the NASA API portal.
	   •	Sign up for an API key. This key will be used to authenticate your requests.
	2.	Choose an Endpoint to Monitor:
	    •	Decide which specific API endpoint you want to monitor.
	    •	For this Project, we take: Astronomy Picture of the Day (APOD): https://api.nasa.gov/planetary/apod
	3.	Set Up Monitoring:
	    •	Write a script (nasa_monitor.py) or use a monitoring tool to periodically make HTTP requests to the chosen endpoint.
     	 • Check the response status code and response time to ensure the API is functioning correctly.
	    •	Log the responses and any errors for further analysis.

## Set the environment variable before running the script:


  * export NASA_API_KEY=your_api_key_here

##  **Running the Script**:
   Running the Script
To run the monitoring script, execute the following command in the terminal:

```bash
python3 nasa_monitor.py
```

This script makes a request to the APOD endpoint every 60 seconds, checks if the response status code is 200 (indicating success), and prints the response time. 

	•	Handling API Key: To avoid hardcoding the API key in your script, you can use environment variables. 
      Set an environment variable for your API key and modify the script to read it



     
## 4. **Set Up Prometheus and Grafana Using Docker**:
   * Create a Docker Network
   * Create Prometheus Configuration File
   * Start Prometheus Container
   * Start Grafana Container
  
## 5. **Modify the Monitoring Script to Expose Metrics**:
   * Install Prometheus Client Library
   * Update the Script to Expose Metrics

## 6. **Configure Grafana**
   * Access Grafana
        * http://localhost:3000
        * user & pass = 'admin' (need to change the pass).
   * Add Prometheus Data Source
        * URL: http://localhost:9090
        * Click Save & Test.
   * Create a Dashboard
        * Dashboard [NAME] = 'NASA-SRE'
   * Customize the Dashboard

## 7. **Create Alerting Rules in Prometheus**
   * Create Alerting Rules File
   * Update Prometheus Configuration
   * Restart Prometheus
  
## 8. **Set Up Alertmanager**
   * Install Alertmanager
   * Create Alertmanager Configuration File
   * Start Alertmanager

## 9. **Configure Grafana to Send Alerts**
      * Configure Notification Channels in Grafana
      * Create Alert Rules in Grafana
      * Alert Group - 'Alert > DevOps'
  
## 10. **Simulate Service Downtime**

          * Service Downtime
          * Modify /etc/hosts:

        * 127.0.0.1 api.nasa.gov


## Verify errors in Prometheus and Grafana.
Restore /etc/hosts after testing:

   * 127.0.0.1 api.nasa.gov

     **Performance Degradation**
  1. Introduce delay in Python script:

```bash
* time.sleep(5)
``` 

  2. Verify response time metrics in Prometheus and Grafana.
  3. Remove delay after testing.
     
       **Increased Error Rates**
  1. Use an invalid API key in Python script:

```bash
API_KEY = 'invalid_api_key'
``` 
  2. Verify error rate metrics in Prometheus and Grafana.
  3. Restore valid API key after testing.

##        **Verification**
 * **Check Prometheus**: Verify metrics collection in the Prometheus web UI.
 * **Check Grafana**: Ensure panels are displaying metrics correctly.
 * **Check Alertmanager**: Verify alerts are triggered when thresholds are exceeded.
   





