"""
this is the main.py to be called in life_expectancy project
"""
import argparse
from pathlib import Path
import pandas as pd

from life_expectancy.loaders import save_data, TSVStrategy, JSONStrategy
from life_expectancy.cleaning import clean_data
from life_expectancy.enums import Country

from life_expectancy.loaders import file_type

# Determines the absolute path of the directory we are working on
FILE_DIR = Path(__file__).parent

# Determines the relative path of the directory we are working on
data_dir = FILE_DIR / 'data'

def main(region: str = "PT",
        # type_strategy = None,
         file=None,
         location: str = data_dir) -> pd.DataFrame:
    """
    this is the main fuction to be called in life_expectancy project where we will use the loaders
    to load a file, clean it and then save the resulting dataframe in a csv file
    """
    region = Country[region]
    
    if file is None:
        #type_strategy = TSVStrategy()
        file = "eu_life_expectancy_raw.tsv"

    loader = file_type(country=region, file=file)
    dataframe = loader.load_type(file)
    df_cleaned = clean_data(dataframe, region = region, type_strategy = loader)
    save_data(df_cleaned, f"{region}_life_expectancy.csv", location)
    return df_cleaned


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean life expectancy data")
    parser.add_argument("--country", type=str, default="PT", help="Region code to clean data for")
    args = parser.parse_args()
    main(
        region = args.country,
        file = "eurostat_life_expect.json",
        #type_strategy=JSONStrategy(),
        location = data_dir
        )
