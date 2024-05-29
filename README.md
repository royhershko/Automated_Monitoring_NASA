i# Automated_Monitoring_NASA
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

## 1.Setup

1. **Install Python 3**:
   If Python 3 is not already installed on your machine, you can download and install it from [python.org](https://www.python.org/downloads/).

2. **Install the `python3-venv` Package**:
   On Debian/Ubuntu systems, run the following commands to install the `python3-venv` package:

```bash
   sudo apt update
   sudo apt install python3-venv
```

## 2.Setup the API Key (NASA)

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

## 3.**Running the Script**:
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
        * docker network create monitoring-network
   * Create Prometheus Configuration File
        * Create a (prometheus.yml) file
   * Start Prometheus Container
        * Run the Prometheus container with the configuration file:
           - docker run -d --name=prometheus --network=monitoring-network -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
   * Start Grafana Container
        * Run the Grafana container:
           - docker run -d --name=grafana --network=monitoring-network -p 3000:3000 grafana/grafana

  
## 5. **Modify the Monitoring Script to Expose Metrics**:
   * Install Prometheus Client Library =(prometheus_client)
   * Update the Script to Expose Metrics
   * Activate your virtual environment

    - pip install prometheus_client


## 6. **Configure Grafana**
   * Access Grafana
        * http://localhost:3000
        * user & pass = 'admin' (need to change the pass).
   * Add Prometheus Data Source
        * URL: http://localhost:9090
        * Click Save & Test.
   * Create a Dashboard
        * Dashboard [NAME] = 'My_Dashboard' =(Example)
   * Customize the Dashboard

## 7. **Create Alerting Rules in Prometheus**
   * Create Alerting Rules File
     - Create a file named (alert_rules.yml)
   * Update Prometheus Configuration
     - Update your (prometheus.yml) configuration file to include the alerting rules
   * Restart Prometheus
     - sudo systemctl restart prometheus
  
## 8. **Set Up Alertmanager**
   * Install Alertmanager
     - Download and install Alertmanager from the Prometheus website.
   * Create Alertmanager Configuration File
     - Create a file named (alertmanager.yml)
   * Start Alertmanager
     * Run Alertmanager with the configuration file:
         - ./alertmanager --config.file=alertmanager.yml

## 9. **Configure Grafana to Send Alerts**
      * Configure Notification Channels in Grafana
      * Create Alert Rules in Grafana
      * Alert Group - Alert > 'My_Alert'
  
## 10. **Simulate Service Downtime**

          * Service Downtime
          * Modify /etc/hosts:

        * 127.0.0.1 api.nasa.gov


## 11.Verify errors in Prometheus and Grafana.
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
   





