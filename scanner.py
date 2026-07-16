import socket
import time
from concurrent.futures import ThreadPoolExecutor
print("=" * 45)
print("        PYTHON PORT SCANNER")
print("=" * 45)

# Ask the user for the target IP address
target = input("Enter the IP address to scan: ")

# Ask for the port range
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))
start_time = time.time()


print(f"\nScanning {target}...\n")
results = []

# Loop through each port in the range
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a timeout so the program doesn't wait too long
    sock.settimeout(0.2)

    # Try connecting to the port
    result = sock.connect_ex((target, port))

    # If result is 0, the port is open
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown Service"

        output = f"Port {port} ({service}) is OPEN"
        print(output)
        results.append(output)

    # Close the socket
    sock.close()

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))


print("\nScan Complete!")

with open("results.txt", "w") as file:
    for line in results:
        file.write(line + "\n")

print("Results saved to results.txt")
print(f"Open Ports Found: {len(results)}")

end_time = time.time()
print(f"scanning completed in {end_time - start_time:.2f} seconds")