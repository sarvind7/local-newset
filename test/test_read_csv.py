from src.read_csv import read_in_counties_newspapers
def test_csv_with_one_county():
    assert read_in_counties_newspapers('test/test_data/county_to_newspaper_test1.csv') == (["Los Angeles"],
                                                                                           ["https://www.latimes.com/"])

def test_csv_with_two_counties():
    assert read_in_counties_newspapers('test/test_data/county_to_newspaper_test2.csv') == (["Los Angeles", "San Diego"],
                                                                                           ["https://www.latimes.com/", "https://www.sandiegouniontribune.com/"])

