from src.read_csv import readFile
def test_answer():
    assert readFile('test/test_data/county_to_newspaper_test1.csv') == "Los Angeles","https://www.latimes.com/"