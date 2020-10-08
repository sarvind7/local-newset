import csv
import sys
import os


def read_county_to_newspaper_csv(file):
    """ Takes in a csv file with each row containing a county
    and newspaper and outputs a list of (county, newspaper) tuples."""
    newspaper_list = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            newspaper_list.append((row['counties'], row['localnewspapers']))
    return newspaper_list
