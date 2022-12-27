import csv

with open("prime.csv",newline="") as csvfile:
    rows = csv.reader(csvfile)
    with open("primetable.csv",mode="w",newline='') as target:
        for row in rows:
            writer = csv.writer(target)
            writer.writerow([row[1]])
