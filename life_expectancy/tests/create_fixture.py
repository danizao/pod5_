import pandas as pd
from pathlib import Path
import numpy as np
from loaders import load_data, save_data
from _cleaning import clean_data


# BASE_DIR = Path(__file__).parent.parent / "data"
# FIXTURES_DIR = Path(__file__).parent / "fixtures"
# print(BASE_DIR)
# print(FIXTURES_DIR)

def create_fixture() -> None:
    data = load_data("eu_life_expectancy_raw.tsv")
    data = clean_data(data, region="PT")
    sample_df = data.sample(n=100)
    save_data(sample_df, "pt_life_expectancy_expected.csv")

if __name__ == '__main__': # pragma: no cover
    create_fixture()