import csv
import sys
import os


def read_in_counties_newspapers(file):
    """ A function that takes in a file of counties and the
    corresponding local newspaper. Then, stores the counties in
    a list, and the local newspapers in another list and stores
    the two lists in a tuple."""
    county_list = []
    newspaper_list = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            county_list.append(row['counties'])
            newspaper_list.append(row['localnewspapers'])
        return (county_list, newspaper_list)
