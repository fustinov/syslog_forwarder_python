import socket
import argparse

# Input parameters
parser = argparse.ArgumentParser(description='This is syslog forwarder written in Python')
parser.add_argument("-t", "--target", help="Destination server", type=str, required=True)
parser.add_argument("-p", "--port", help="Target port. Default - 514", type=int, required=False, default="514")
parser.add_argument("-l", "--listen", help="Interface to listen on. Default - all", default='0.0.0.0')
args = parser.parse_args()


def forward_syslog_message(message, dest_host, dest_port):
    # Create a UDP socket
    forward_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the syslog message to the destination host
    forward_sock.sendto(message, (dest_host, dest_port))

# Create a UDP socket to receive syslog messages
recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('{}'.format(args.listen), int(args.port))
recv_sock.bind(server_address)

# Receive and forward syslog messages
while True:
    data, address = recv_sock.recvfrom(4096)

    # Save the syslog message to a file
    #with open("syslog.txt", "w") as file:
    #    file.write(data.decode())

    # Forward the syslog message to the destination host
    forward_syslog_message(data, '{}'.format(args.target), int(args.port))

