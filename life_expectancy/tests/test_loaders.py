"""Tests for the loaders module"""
import pandas as pd 
from life_expectancy.loaders import save_data, load_data
from pytest import MonkeyPatch
from pathlib import Path
import os

# BASE_DIR = Path(__file__).parent.parent / "data"
FIXTURES_DIR = Path(__file__).parent / "fixtures"
# print(BASE_DIR)

def test_load_data() -> None:

    """testing if the load_data is called with the necessary arguments"""
    input = "pt_life_expectancy_expected_test.csv"
    expected = pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv")
    actual = load_data(input)
    pd.testing.assert_frame_equal(actual, expected)

def test_save_data() -> None:

    """testing if the save_data is called with the necessary arguments"""
    # Create a sample DataFrame for testing
    input = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    df = pd.DataFrame(input)
    
    # Define the expected file path and name
    file = "test_data.csv"
    expected_file_path = os.path.join(FIXTURES_DIR, file)
    
    # Call the function to save the data
    save_data(df, file)

    # Check if the file exists
    assert os.path.exists(expected_file_path)

    # check if the file content matches the DataFrame
    loaded_df = pd.read_csv(expected_file_path)
    assert df.equals(loaded_df)

    # Clean up - remove the created file
    os.remove(expected_file_path)
