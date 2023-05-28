# Tech Scenarios

### Scenario 1 - Random Number Generator

- To run the random number generator on macOS and Linux, you need to make sure you have python installed
- Check by opening the terminal and running `python --version`. Most UNIX systems come with python installed by default so it shouldn't be a problem but if it's not installed you can download on https://python.org/downloads/.
- in the terminal, navigate to the directory with the `random_num.py` and run the program using the following command: `python random_num.py`

- This will execute the script and random numbers between 1 and 10 will be generated and printed.


### Scenario 2

In order to monitor this ssl offloading server which proxies a huge number of requests, we can monitor the following metrics:

- **Memory Usage:** We need to make sure that the server has enough RAM that can handle the multiple connections. This way we can understand if there are any leaks or possibly excessive use of memory
- **CPU:** Monitoring CPU usage to ensure that the server has adequate processing power to handle the load.
- **Network Throughput:** There is need to ensure the server is capable of handling the SSL traffic. The 10Gbit/s NICs should not be overwhelmed and there shouldn't be any network congestion.
- **SSL Handshakes and Connections:** Monitoring the SSL handshakes and connections made per second is essential because it identifies the trends and potential issues that may affect the SSL offloading perfomance
- **SSL Certificate Expiry:** There should be timely certificate renewal to avoid interruptions due to expired certificates.
- **Error Rates:** Error rates should be monitored to identify any issues with the ssl offloading, proxying or other connections. 

To monitor all the mentioned metrics, we can use various tools and techniques. Here are examples:

- **System Logs:** logs can be reviewed regularly to identify anomalies, warning and errors related to SSL offloading and proxying.
- **Monitoring Software:** Monitoring software like Prometheus, Nagios or Zabbix can be used to collect and analyse the server metrics. These software have customised dashbaords and alerting features.
- **SSL tools:** Tools like OpenSSL can be used to check SSL certificate validity and configuration


##### Possible Challenges of monitoring this:

- processing 25000 requests per second requires effecient tools that provide almost real-time monitoring. The tools should also be able handle large data collection and analysis
- Having high request volumes means that a lot of data will be generated. Without enough storage, historical data retention will not be possible
- SSl offloading requires tools and solutions that can effectively handle sensitive data securely. This also means there is need to abide by a lot of compliance regulations.
- Monitoring such metrics for a high volume server means that there is need to ensure server perfomance is not affected. It can be an issue when there are limited resources to allow scaling of the servers



