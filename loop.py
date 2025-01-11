# num = int(input("enter number "))

# for i in range(1, 11):
#     print(f"{i} = {num}, {i*num}")

def filter_name(word, path):
    #file_path = "D:\python\\access.log"
    # name = "ubuntu"
    with open (path, mode = 'r' ) as file:
        for line in file:
            if word in line:
                print(line.strip())
    return line

word = "ubuntu"
path = "D:\python\\access.log"

r = filter_name(word, path)
print(r)

