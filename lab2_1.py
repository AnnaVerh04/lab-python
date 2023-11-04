import csv
import os


path_to_annotation = "annotation1.csv"
path_data = "dataset"

def write_file(file_name, data):
    with open(file_name, "w") as f:
        writer = csv.writer(f, delimiter="/")
        for row in data:
            writer.writerow(row)

data = [["full_path", "path", "class"]]

dirs = os.listdir(path_data)

for dir in dirs:
    path = os.path.join(path_data, dir)
    files = os.listdir(path)
    for file in files:
        data.append([os.path.abspath(os.path.join(path, file)),
                     os.path.join(path, file),
                     dir])

write_file(file_name=path_to_annotation, data= data)