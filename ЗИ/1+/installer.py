from sys import *
import hashlib
from subprocess import *
import os

def get_CPU():
    if platform == 'win32':
        uuid_id = check_output("wmic csproduct get UUID", shell=True).decode()
    elif platform == 'linux':
        uuid_id = check_output("dmidecode -s system-uuid").decode()
    elif platform == "darwin":
        uuid_id = str(check_output("system_profiler SPHardwareDataType | grep UUID")).decode()
    return hashlib.sha256(uuid_id.encode('utf-8')).hexdigest()

def check_CPU(given):
    real_key = license_key()
    if real_key != get_CPU():
        return False
    else:
        return True

def to_license_key(checksum):
    with open("certificate.key", "w") as lic_file:
        lic_file.write(checksum)
    
def license_key():
    with open("certificate.key", 'r') as file:
        return file.readline()
    
if __name__ == "__main__":
    to_license_key(get_CPU())
    print(license_key())
