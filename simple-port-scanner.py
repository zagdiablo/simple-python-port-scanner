import socket
import sys
import threading


def scanTarget(target_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target_ip, port))
    socket.setdefaulttimeout(1)
    if result == 0:
        print(f"port {port} is open.")
    s.close()


def main():

    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print(
            f"invalid amount of argument, requires 1 argument but {len(sys.argv)-1} was given.")
        print("Usage: python3 simple-port-scanner.py <ip>")
        print("Example: python3 simple-port-scanner.py 192.168.0.1")
        exit()

    threads = []
    try:
        for port in range(1000):
            threads.append(threading.Thread(
                target=scanTarget, args=(target, port)))

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("Exiting...")
    except socket.gaierror:
        print("Host name could not be resolved.")
    except socket.error:
        print("Cannot connect to target.")
        exit()


if __name__ == "__main__":
    main()
