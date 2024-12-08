from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Configuration for FTP server
FTP_PORT = 2121  # Default FTP port
FTP_USER = "user"
FTP_PASSWORD = "pwd"
FTP_DIRECTORY = "./ftp_storage"  # Directory to store files

def main():
    # Ensure the directory exists
    if not os.path.exists(FTP_DIRECTORY):
        print(f"Creating FTP directory: {FTP_DIRECTORY}")
        os.makedirs(FTP_DIRECTORY)
    else:
        print(f"Using existing FTP directory: {FTP_DIRECTORY}")
    
    # Set up authorizer
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    # Set up handler and attach authorizer
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib FTP server ready."

    # Create and start the server
    address = ('0.0.0.0', FTP_PORT)  # Bind to the specified IP and port
    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5

    print(f"FTP server running on port {FTP_PORT}...")
    server.serve_forever()

if __name__ == '__main__':
    main()
