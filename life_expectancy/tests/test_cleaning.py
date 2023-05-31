"""Tests for the cleaning module"""
import pandas as pd
import pytest
import os

from pathlib import Path

from life_expectancy.cleaning import clean_data, extract_numeric_values_from_column

def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected) -> None:
    """Run the `clean_data` function and compare the output to the expected output"""

    actual = clean_data(eu_life_expectancy_raw).reset_index(drop=True)
    expected = pt_life_expectancy_expected
    pd.testing.assert_frame_equal(
        actual, expected
    )

def test_extract_numeric_values_from_column(numeric, numeric_expected) -> None:
    """Run the `clean_data` function and compare the output to the expected output"""
    actual = extract_numeric_values_from_column(numeric, "value")#.reset_index(drop=True)
    pd.testing.assert_frame_equal(actual, numeric_expected)
