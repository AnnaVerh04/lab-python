import csv


path_to_annotation = "annotation1.csv"

def read_file(path):
    files = []
    with open(path, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter="/")
        for row in reader:
            files.append([row["full_path"], row["class"]])
    return files

class A:
    def __init__(self, files_class, path):
        self.file_class = files_class
        csv_f = read_file(path)
        self.annotation = []
        for i in csv_f:
            if self.file_class == i[1]:
                self.annotation.append(i)

    def __next__(self):
        if self.annotation:
            return self.annotation.pop()[0]
        else:
            return None

a = A("cat", path_to_annotation)

while True:
    next_val = next(a)
    print(next_val)
    if next_val == None:
        break
