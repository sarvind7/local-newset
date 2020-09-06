import csv
countylist = []
newspaperlist = []

with open('[insert].csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        countylist.append(row['counties'])
        newspaperlist.append(row['localnewspapers'])

totallist = (countylist, newspaperlist)