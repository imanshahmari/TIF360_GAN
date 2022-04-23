import os
import shutil
src_images_dir = "data/export/images"
src_labels_dir = "data/export/labels"
dst_dir = "data/export/images/results"

os.chdir(src_labels_dir)

def read_text_file(file_path):
    with open(file_path,'r') as f:
        x=[]
        for line in f:
            line = line.strip()
            line = line.split(" ")
            if line[0] == "1":
                x.append(file_path)
                x.append(line[1:len(line)])
        return x
lista=[]
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{file}"
        y = read_text_file(file_path)
        lista.append(y)

res = list(filter(None, lista))


os.chdir("../")
os.chdir("images")
print(os.getcwd())


for listan in res:
    label_file_name = listan[0]
    label_file_name = label_file_name[0:len(label_file_name)-4]
    for file in os.listdir():
        image_file_name = file[0:len(file)-4]
        if image_file_name == label_file_name:
            shutil.copy(file,"results")