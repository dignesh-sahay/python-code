# # import csv 

# # #with open('D:\python\Book1.csv' , mode = 'r')as file:
# # file = "D:\python\Book1.csv"
# # csvfile = csv.DictReader(file)
# # for lines in csvfile:
# #     print(lines)

# # import pandas
# # file = pandas.read_csv('D:\python\Book1.csv')
# # print(file)

# # print("hello")

# # with open( "D:\python\doc.txt" , mode = 'r' ) as file:
# #     newfile = file.read()
# #     line = sorted(newfile)
# #     line.reverse()
# #     print(line)

# marks = []

# f1 = int(input( "enter the marks " ))
# marks.append(f1)
# f2 = int(input( "enter the marks " ))
# marks.append(f2)
# f3 = int(input( "enter the marks " ))
# marks.append(f3)

# marks.sort()

# print(marks) 

def extract_unique_ips(log_file_path):
    unique_ips = set()  # Use a set to store unique IPs

    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                # Extract the IP address (assumes the IP is the first part of the line)
                ip = line.split()[0]
                unique_ips.add(ip)
    except FileNotFoundError:
        print(f"Error: File not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return unique_ips

# Example usage
log_file_path = 'access.log'  # Replace with the path to your access log file
unique_ips = extract_unique_ips(log_file_path)

# Print unique IPs
for ip in unique_ips:
    print(ip)