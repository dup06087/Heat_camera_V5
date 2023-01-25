from Cam_number import camera_num

### initial values
init_custom_cam_name = ["cam{}".format(i+1) for i in range(camera_num)]
print(init_custom_cam_name)

###changable values

file_path = "./cam_names.txt"
with open(file_path) as f:
    lines = f.read().splitlines()
    f.close()

while camera_num > len(lines):
    lines.append("")
# print(lines)

for i in range(len(lines)):
    if lines[i] == "":
        lines[i] = "cam{}".format(i+1)

Cam_names = lines
# print(Cam_names)

### logo
## inital
init_Logo_Location = "./0.jpg"

## changable
url_path = "./URL.txt"
with open(url_path) as f:
    line = f.read()
    if line != "":
        init_Logo_Location = line
        # print(line)
        f.close()

# print("logo : ", init_Logo_Location)