# Python Port Scanner

A multithreaded TCP Port Scanner built using Python. This project scans a target IP address over a specified range of ports and identifies open ports along with their associated services.

## Features

- Scan any IPv4 address
- Scan a custom range of ports
- Multithreaded scanning for faster performance
- Detect open TCP ports
- Identify common services (HTTP, SSH, FTP, etc.)
- Save scan results to `results.txt`
- Display scan completion time

## Technologies Used

- Python 3
- Socket Programming
- ThreadPoolExecutor
- Time Module

## Project Structure

```text
Python-Port-Scanner/
│── scanner.py
│── gui.py
│── README.md
│── .gitignore
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/ashikarao05/Python-Port-Scanner.git
```

2. Open the project folder

```bash
cd Python-Port-Scanner
```

3. Run the scanner

```bash
python scanner.py
```

## Example Output

```text
=============================================
        PYTHON PORT SCANNER
=============================================

Enter the IP address to scan: 127.0.0.1
Enter the starting port: 1
Enter the ending port: 1024

Scanning...

Port 135 (epmap) is OPEN
Port 445 (microsoft-ds) is OPEN

Scan Complete!

Open Ports Found: 2
Scanning completed in 1.25 seconds
```

## Disclaimer

This project is intended for educational purposes. Only scan systems that you own or have explicit permission to test.

## Author

Ashika A Rao