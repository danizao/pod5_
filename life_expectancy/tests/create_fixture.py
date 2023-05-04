import pandas as pd
import sys
import os
from life_expectancy.utils.utils import load_data, save_data
from . import OUTPUT_DIR, FIXTURES_DIR

def create_fixture() -> None:
    data = load_data(OUTPUT_DIR, "pt_life_expectancy.csv")
    data_subset = data.iloc[:100]
    save_data(data_subset, "pt_life_expectancy_expected_teste.csv", FIXTURES_DIR)

if __name__ == '__main__': # pragma: no cover
    create_fixture()