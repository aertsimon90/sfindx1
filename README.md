# SfindX1 - Random Network Scanner (Educational Use Only)

## ⚠️ Disclaimer: Usage Policy ⚠️

**This tool is provided strictly for educational purposes, learning about network programming, and conducting authorized security auditing on networks and systems you own or have explicit permission to test.**

* **DO NOT** use this tool to scan public, unknown, or third-party networks. Unauthorized scanning of computer networks is illegal and unethical.
* The author and contributors assume **no liability** and are not responsible for any misuse or damage caused by this program.
* **You are solely responsible** for ensuring your actions comply with all local, state, and international laws.

## 🌟 Overview

SfindX1 (Server Finder eXperiment 1) is a simple, multi-threaded Python script designed to randomly scan IP addresses and specified ports to check for open TCP connections.

It is primarily a learning exercise demonstrating:
1.  Basic **Socket Programming** in Python.
2.  The use of **Threading** to handle concurrent network I/O operations.
3.  The concept of a network **Port Scanner** (used ethically by security professionals to check for vulnerabilities on their own systems).

## 🚀 Features

* **Multi-threaded Scanning:** Uses Python's `threading` module for parallel scanning, improving performance.
* **Random IP Generation:** Randomly generates standard IPv4 addresses for theoretical scanning (strictly for educational simulation).
* **Live Output:** Displays the current count of found server-like endpoints.
* **Automatic Saving:** Continuously saves found IP:Port combinations to a specified file.

## 🛠️ Requirements

* Python 3.x
* Standard Python libraries (`random`, `threading`, `socket`, `time`, `os`)

## 💡 How It Works (Educational)

The script operates in a continuous loop:

1.  **Random Target:** It generates a random IP address (`0.0.0.0` to `255.255.255.255`) and selects a random port from the user-provided list.
2.  **Connection Attempt:** It attempts to establish a simple TCP connection (`socket.connect`) to the generated IP:Port.
3.  **Timeout:** A short timeout (0.8 seconds) is set to quickly skip unresponsive targets.
4.  **Success:** If a connection is successful, the IP:Port combination is saved to the global list (`ss`).
5.  **Multi-threading:** The `sfthread` and `botfind` functions manage multiple threads, allowing many connection attempts to happen simultaneously.

## ⚙️ Usage (For Authorized Networks Only)

### 1. Run the Script

```bash
python3 your_script_name.py
````

### 2\. Menu Input

The script will prompt you for three values:

| Prompt | Description | Example |
| :--- | :--- | :--- |
| **Enter Bot Count** | The number of concurrent threads/workers to use. (More threads = faster scanning, but higher resource usage). | `44` |
| **Enter Ports** | A list of ports to scan, separated by a slash (`/`) or a space. | `80/443/22` |
| **Enter File Name** | The name of the file where found endpoints will be saved. | `found_servers.txt` |

-----

### Developed by aertsimon90

*Code licensed for personal and educational use.*
