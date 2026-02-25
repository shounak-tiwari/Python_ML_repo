import csv
with open("data.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name","akash"])
    writer.writerow(["role","trainer"])
    writer.writerow(["add.","indoremp"])
    print("done")