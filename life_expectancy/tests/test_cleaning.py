"""Tests for the cleaning module"""
import pandas as pd
import pytest
import os

from pathlib import Path

from life_expectancy.cleaning import clean_data, extract_numeric_values_from_column
from life_expectancy.loaders import TypeStrategy, TSVStrategy, JSONStrategy
from life_expectancy.enums import Country

def test_clean_data_TSV(eu_life_expectancy_raw,
                        pt_life_expectancy_expected,
                        region: str = Country.PT,
                        type_strategy: TypeStrategy = TSVStrategy()) -> None:
    """Run the `clean_data` function and compare the output to the expected output"""

    actual = clean_data(eu_life_expectancy_raw,
                        region = region,
                        type_strategy = type_strategy)
    expected = pt_life_expectancy_expected
    pd.testing.assert_frame_equal(
        actual, expected
    )

def test_clean_data_JSON(eurostat_life_expect,
                         pt_life_expectancy_expected,
                         region: str = Country.PT,
                         type_strategy: TypeStrategy = JSONStrategy()) -> None:
    """Run the `clean_data` function and compare the output to the expected output"""

    actual = clean_data(eurostat_life_expect,
                        region = region,
                        type_strategy=type_strategy).reset_index(drop=True)
    expected = pt_life_expectancy_expected.reset_index(drop=True)
    pd.testing.assert_frame_equal(
        actual, expected, check_index_type=False
    )

def test_extract_numeric_values_from_column(numeric, numeric_expected) -> None:
    """Run the `clean_data` function and compare the output to the expected output"""
    actual = extract_numeric_values_from_column(numeric, "value")#.reset_index(drop=True)
    pd.testing.assert_frame_equal(actual, numeric_expected)
