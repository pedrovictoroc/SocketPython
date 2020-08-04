# https://www.geeksforgeeks.org/socket-programming-python/

import socket # For socket 
import sys  # Catch argvs
  
try:
    # Initialize connection
    # AF_INET refers to the address family ipv4
    # SOCK_STREAM means connection oriented TCP protocol 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except socket.error as err: 
    print("socket creation failed with error %s" %(err)) 

# default port for socket 
port = 80

'''
# Construir CLI para facilitar manuseio de porta
if('-port' in sys.argv):
    portPosition = sys.argv.index('-port')
    shouldUpdatePort = isinstance(int(sys.argv[portPosition+1]),int)
    print(shouldUpdatePort)
    if(shouldUpdatePort):
        print(sys.argv[portPosition+1])
'''

try: 
    host_ip = socket.gethostbyname('www.google.com') 
except socket.gaierror: 
  
    # this means could not resolve the host 
    print("there was an error resolving the host")
    sys.exit() 
  
# connecting to the server 
s.connect((host_ip, port)) 
  
print("the socket has successfully connected to google {}".format(port))