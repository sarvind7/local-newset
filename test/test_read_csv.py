from src.read_csv import read_county_to_newspaper_csv
def test_csv_with_one_county():
    assert read_county_to_newspaper_csv('test/test_data/county_to_newspaper_test1.csv') == [("Los Angeles","https://www.latimes.com/")]


def test_csv_with_two_counties():
    assert read_county_to_newspaper_csv('test/test_data/county_to_newspaper_test2.csv') == [("Los Angeles", "https://www.latimes.com/"),
                                                                                            ("San Diego", "https://www.sandiegouniontribune.com/")]

