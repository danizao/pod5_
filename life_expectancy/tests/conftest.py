"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR


@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    print(OUTPUT_DIR)
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv", index_col=0)


@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load the raw input of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", delimiter="\t")

@pytest.fixture(scope="session")
def eurostat_life_expect() -> pd.DataFrame:
    """Fixture to load the raw input of the cleaning script"""
    return pd.read_json(FIXTURES_DIR / "eurostat_life_expect.json")

@pytest.fixture()
def eu_life_expectancy_expected() -> pd.DataFrame:
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv")


@pytest.fixture(scope="session")
def numeric() -> pd.DataFrame:
    """
    Fixture to load the numeric input of the cleaning script
    """
    return pd.read_csv(FIXTURES_DIR / "numeric.csv")


@pytest.fixture(scope="session")
def numeric_expected() -> pd.DataFrame:
    """
    Fixture to load the expected output of the cleaning script
    """
    return pd.read_csv(FIXTURES_DIR / "numeric_expected.csv")

@pytest.fixture(scope="session")
def all_actual_countries() -> list:
    """
    Fixture to create a list of all countries
    """
    return ['AT', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DK', 'EE', 'EL', 'ES',
            'FI', 'FR', 'HR', 'HU', 'IS', 'IT', 'LI', 'LT', 'LU', 'LV',
            'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'SE', 'SI', 'SK', 'DE',
            'AL', 'IE', 'ME', 'MK', 'RS', 'AM', 'AZ', 'GE', 'TR', 'UA',
            'BY', 'UK', 'XK', 'FX', 'MD', 'SM', 'RU']