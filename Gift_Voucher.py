from scapy.all import *
import random


def get_voucher_code(client_id):

	# Server IP and port
	server_ip = "192.168.126.129" # Change it to your kali IP address
	server_port = 12431  # Replace with the discovered port (e.g., 12449)

	# Generate a random source port
	source_port = random.randint(10024, 65535)

	# Create a UDP packet
	packet = IP(dst=server_ip)/UDP(sport=source_port, dport=server_port)/Raw(load=client_id)

	# Send the packet and wait for a response
	response = sr1 (packet, timeout=3)

	# Check if a response was received
	if response:
		# Extract and print the gift voucher code from the response
		gift_voucher_code = response[Raw].load.decode()
		print(response.show())
	else:
		print("No response received. The server may be down or not responding.")

# Define client ID (use your UOW student number)
client_id = "8039276"  # Replace with your 7-digit UOW student number
get_voucher_code(client_id)
