import socket

def banner(ip,port):
    try:
        s = socket.socket()
        s.connect((ip,int(port)))
        banner = str(s.recv(1024)).strip('b').strip('\r\n')
        print(banner)
        print(type(banner))
    except ConnectionRefusedError:
        print("Connection refused by the server")
    except TimeoutError:
        print("server time out")
    except ValueError:
        print("put valid IP address and port")

def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip,port)

main()