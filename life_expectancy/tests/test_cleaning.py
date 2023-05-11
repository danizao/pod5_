"""Tests for the cleaning module"""
import pandas as pd
import pytest
import os

from pathlib import Path

from life_expectancy.cleaning import clean_data, extract_numeric_values_from_column

FILE_DIR = Path(__file__).parent
FIXTURES_DIR = FILE_DIR / "fixtures"

eu_life_expectancy_raw = pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", delimiter="\t")
pt_life_expectancy_expected = pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
numeric = pd.read_csv(os.path.join(FIXTURES_DIR, "numeric.csv"))

def test_clean_data() -> None:
    """Run the `clean_data` function and compare the output to the expected output"""

    actual = clean_data(eu_life_expectancy_raw).reset_index(drop=True)
    expected = pt_life_expectancy_expected
    pd.testing.assert_frame_equal(
        actual, expected
    )

def test_extract_numeric_values_from_column() -> None:
    """Run the `clean_data` function and compare the output to the expected output"""
    numeric = pd.read_csv(os.path.join(FIXTURES_DIR, "numeric.csv"))

    actual = extract_numeric_values_from_column(numeric, "value")#.reset_index(drop=True)
    expected = pd.read_csv(os.path.join(FIXTURES_DIR, "numeric_expected.csv"))
    pd.testing.assert_frame_equal(
        actual, expected
    )