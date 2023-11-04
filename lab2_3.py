import csv
import os
import shutil
import random

start_path = "dataset"
end_path = "my_dataset2"
file_name = "annotation.csv"

def write_file(file_name, data):
    with open(file_name, "w") as f:
        writer = csv.writer(f, delimiter="/")
        for row in data:
            writer.writerow(row)

data = [["full_path", "path", "class"]]

random_names = []

dirs = os.listdir(start_path)
for dir in dirs:
    path = os.path.join(start_path, dir)
    files = os.listdir(path)
    if not os.path.isdir(os.path.join(end_path, "dataset")):
        os.mkdir(os.path.join(end_path, "dataset"))

    for file in files:

        random_file_name = random.randint(0, 10000)
        while random_file_name in random_names:
            random_file_name = random.randint(0, 10000)

        random_names.append(random_file_name)

        shutil.copyfile(os.path.join(start_path,dir,file),
                        os.path.join(end_path, "dataset", str(random_file_name)+".jpg"))

        data.append([os.path.abspath(os.path.join(end_path, "dataset", dir+"_"+file)),
                     os.path.join(end_path, "dataset", str(random_file_name)+".jpg"), dir])

write_file(os.path.join(end_path,file_name), data)


