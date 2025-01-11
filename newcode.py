import re

# def extract_unique_ips(log_file_path):
#       unique_ips = set()
#       ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
#       with open ("D:\python\\access.log", mode = 'r' ) as file:
#            for line in file:
#                    ip = ip_pattern.search(line)
#                    if ip:
#                     unique_ips.add(ip.group(0))

#       return unique_ips


# log_file_path = "D:\python\\access.log"
# unique_ips = extract_unique_ips(log_file_path)

# print(unique_ips)

def extract_unique_ips(log_file_path):
    unique_ips = set()
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    
    with open ("D:\python\\access.log", mode = 'r' ) as file:
        for line in file:
            ip = ip_pattern.search(line)
            if line:
                unique_ips.add(ip.group(1))

    return unique_ips

unique_ips = extract_unique_ips("D:\python\\access.log")
log_file_path = "D:\python\\access.log"

print(unique_ips)

