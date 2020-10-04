import csv
import sys
import os


def read_county_to_newspaper_csv(file):
    """ Takes in a csv file with each row containing a county
    and newspaper and outputs a list of (county, newspaper) tuples."""
    county_list = []
    newspaper_list = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            county_list.append(row['counties'])
            newspaper_list.append(row['localnewspapers'])
    county_tuple = tuple(county_list)
    newspaper_tuple = tuple(newspaper_list)
    return [county_tuple, newspaper_tuple]
