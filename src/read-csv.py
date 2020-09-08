import csv
countylist = []
newspaperlist = []
def readFile(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            countylist.append(row['counties'])
            newspaperlist.append(row['localnewspapers'])
    totallist = (countylist, newspaperlist)
    return totallist
