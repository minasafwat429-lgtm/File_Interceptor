# Network Packet Manipulation Tool (Educational Purpose Only)

[![License: Educational Use Only](https://img.shields.io/badge/License-Educational%20Use%20Only-red.svg)](LICENSE)

## ⚠️ IMPORTANT WARNING
**THIS TOOL IS FOR EDUCATIONAL AND AUTHORIZED SECURITY TESTING ONLY**

Unauthorized interception, modification, or redirection of network traffic is **ILLEGAL** in most countries and can result in:
- Criminal charges
- Imprisonment
- Heavy fines
- Civil lawsuits

## 📋 Description
This tool demonstrates how network packets can be intercepted and manipulated using:
- `netfilterqueue` - Linux Netfilter queue integration
- `scapy` - Packet manipulation library
- iptables - Packet redirection

The script specifically intercepts HTTP traffic and replaces `.exe` file downloads with a redirect to a malicious file (demonstration only).

## 🎯 Educational Use Cases
- Understanding MITM (Man-in-the-Middle) attacks
- Learning network security concepts
- Authorized penetration testing (with written permission)
- CTF (Capture The Flag) competitions
- Security research in isolated lab environments

## 🔧 Requirements
- Linux operating system (Kali Linux, Ubuntu, etc.)
- Python 3.6+
- Root/Administrator privileges
- Network interface in monitor/promiscuous mode (for ARP spoofing)

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# Install Python dependencies
pip install -r requirements.txt

# Make script executable
chmod +x script.py
```
## Usage
Step 1: Enable IP forwarding
```
sudo echo 1 > /proc/sys/net/ipv4/ip_forward
```
Step 2: Set iptables rules
```
# Forward all traffic to NFQUEUE
sudo iptables -I FORWARD -j NFQUEUE --queue-num 1

# OR for local traffic only
sudo iptables -I INPUT -j NFQUEUE --queue-num 1
sudo iptables -I OUTPUT -j NFQUEUE --queue-num 1
```
Step 3: Run the script
```
sudo python3 script.py
```
Step 4: Clean up (CTRL+C then run)
```
sudo iptables --flush
```


