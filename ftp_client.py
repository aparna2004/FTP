import ftplib
import os

# Configuration for FTP client
HOSTNAME = "127.0.0.1"  # IP address of the FTP server
FTP_PORT = 2121  # Corrected port for FTP
USERNAME = "user"
PASSWORD = "pwd"
FILE_TO_UPLOAD = "dummy_file.txt"

# Ensure file exists or create it with dummy content
if not os.path.exists(FILE_TO_UPLOAD):
    print(f"Creating dummy file: {FILE_TO_UPLOAD}")
    with open(FILE_TO_UPLOAD, "w") as f:
        f.write("This is a dummy file for FTP transfer.\n")
else:
    print(f"Using existing file: {FILE_TO_UPLOAD}")

try:
    print(f"Connecting to FTP server at {HOSTNAME} on port {FTP_PORT}...")
    ftp_server = ftplib.FTP()
    ftp_server.connect(HOSTNAME, FTP_PORT)  # Connect to the FTP server at the right address and port
    ftp_server.login(USERNAME, PASSWORD)  # Corrected login method
    ftp_server.encoding = "utf-8"
    print(f"Connected to FTP server: {ftp_server.getwelcome()}")

    # Upload the file
    print(f"Uploading file: {FILE_TO_UPLOAD}...")
    with open(FILE_TO_UPLOAD, "rb") as file:
        ftp_server.storbinary(f"STOR {FILE_TO_UPLOAD}", file)

    # List files on the server
    print("Directory listing on the server:")
    ftp_server.dir()

    ftp_server.quit()
    print("FTP session closed.")

except Exception as e:
    print(f"An error occurred: {e}")
