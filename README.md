# NetworkTrafficAnalyzer
A Python-based tool for analyzing network traffic data and generating insightful visualizations.

# Key Features:
* Reads and processes PCAP CSV files.

* Extracts key network traffic information, including IP addresses, protocols, and packet counts.

* Calculates top destination/source IPs and protocol usage.

* Generates bar graphs to visualize traffic patterns.

* Produces interactive HTML reports with embedded graphs for easy dissemination.

# Project Structure:
* network_traffic_analyzer.py: The main Python script for analyzing network traffic data.

* template.html: HTML template used for generating the final report.

* output_YYYYMMDDHHMMSS.html: The generated HTML report with embedded graphs.

# Report Contents:
* File name and analysis date.

* Total number of packets in the file.

* Top 5 Destination IPs with percentages.

* Destination IP Graph.

* Top 5 Source IPs with percentages.

* Source IP Graph.

* Top 5 Protocols with percentages.

* Protocol Graph.

# Dependencies:
* Language: Python

* Libraries: pandas, matplotlib, jinja2, os, datetime, webbrowser
