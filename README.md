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
```

3. **Running the Script**:
   Running the Script
To run the monitoring script, execute the following command in the terminal:

```bash
python3 nasa_monitor.py
```

4. **Set Up Prometheus and Grafana Using Docker**:
   * Create a Docker Network
   * Create Prometheus Configuration File
   * Start Prometheus Container
   * Start Grafana Container
  
5. **Modify the Monitoring Script to Expose Metrics**:
   * Install Prometheus Client Library
   * Update the Script to Expose Metrics

6. **Configure Grafana**
   * Access Grafana
   * Add Prometheus Data Source
   * Create a Dashboard
   * Customize the Dashboard

7. **Create Alerting Rules in Prometheus**
   * Create Alerting Rules File
   * Update Prometheus Configuration
   * Restart Prometheus
  
8. **Set Up Alertmanager**
   * Install Alertmanager
   * Create Alertmanager Configuration File
   * Start Alertmanager

9. **Configure Grafana to Send Alerts**
    * Configure Notification Channels in Grafana
    * Create Alert Rules in Grafana
    * 
   





