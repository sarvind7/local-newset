from src.read_csv import readFile
def test_csv_with_one_county():
    assert readFile('test/test_data/county_to_newspaper_test1.csv') == (["Los Angeles"],["https://www.latimes.com/"])

def test_csv_with_two_counties():
    assert readFile('test/test_data/county_to_newspaper_test2.csv') == (["Los Angeles", "San Diego"],["https://www.latimes.com/", "https://www.sandiegouniontribune.com/"])

def test_csv_with_three_counties():
    assert readFile('test/test_data/county_to_newspaper_test3.csv') == (["Los Angeles", "San Diego", "Orange"],["https://www.latimes.com/", "https://www.sandiegouniontribune.com/", "https://www.ocregister.com/"])