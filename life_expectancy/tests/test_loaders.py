"""Tests for the loaders module"""
import pandas as pd 
from life_expectancy.loaders import save_data, load_data
from pytest import MonkeyPatch
from pathlib import Path

# BASE_DIR = Path(__file__).parent.parent / "data"
FIXTURES_DIR = Path(__file__).parent / "fixtures"
# print(BASE_DIR)

def test_load_data() -> None:

    """testing if the load_data is called with the necessary arguments"""
    input = "pt_life_expectancy_expected_test.csv"
    print("here I am")
    expected = pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv")
    print("Now, here")
    actual = load_data(input)
    print("and again here")
    pd.testing.assert_frame_equal(actual, expected)

if __name__ == '__main__':
    test_load_data()

# def test_save_data(monkeypatch: MonkeyPatch) -> None:

#     """testing if the save_data is called with the necessary arguments"""

#     pass


