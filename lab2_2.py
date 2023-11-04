import csv
import os
import shutil

start_path = "dataset"
end_path = "my_dataset"
file_name = "annotation.csv"

def write_file(file_name, data):
    with open(file_name, "w") as f:
        writer = csv.writer(f, delimiter="/")
        for row in data:
            writer.writerow(row)

data = [["full_path", "path", "class"]]

dirs = os.listdir(start_path)
for dir in dirs:
    path = os.path.join(start_path, dir)
    files = os.listdir(path)
    if not os.path.isdir(os.path.join(end_path, "dataset")):
        os.mkdir(os.path.join(end_path, "dataset"))

    for file in files:
        shutil.copyfile(os.path.join(start_path,dir,file),
                        os.path.join(end_path, "dataset", dir+"_"+file))
        data.append([os.path.abspath(os.path.join(end_path, "dataset", dir+"_"+file)),
                     os.path.join(end_path, "dataset", dir+"_"+file), dir])

write_file(os.path.join(end_path,file_name), data)