"""Tests for the loaders module"""
import os
from pathlib import Path
from unittest.mock import patch

import pandas as pd 

from life_expectancy.loaders import save_data, load_data


BASE_DIR = Path(__file__).parent.parent / "data"
FIXTURES_DIR = Path(__file__).parent / "fixtures"
# print(BASE_DIR)


@patch("life_expectancy.loaders.pd.read_csv")
def test_load_data(mock_read_csv, eu_life_expectancy_expected) -> None:

    """testing if the load_data is called with the necessary arguments"""
    mock_read_csv.return_value = eu_life_expectancy_expected
    input = "pt_life_expectancy_expected_test.csv"
    actual = load_data(input)
    mock_read_csv.assert_called_once_with(BASE_DIR / input, delimiter="\t")
    pd.testing.assert_frame_equal(actual, eu_life_expectancy_expected)


def test_save_data(capfd) -> None:

    """testing if the save_data is called with the necessary arguments"""
    # Create a sample DataFrame for testing
    input = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    df = pd.DataFrame(input)

    # mock_.side_effect = print("Data was saved")
    
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

    out, _ = capfd.readouterr()
    assert out == f"{expected_file_path}\n"

    # Clean up - remove the created file
    os.remove(expected_file_path)
