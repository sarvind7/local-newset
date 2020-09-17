import csv
import sys
import os


def readFile(file):
    countylist = []
    newspaperlist = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            countylist.append(row['counties'])
            newspaperlist.append(row['localnewspapers'])
    totallist = (countylist,newspaperlist)
    return totallist
